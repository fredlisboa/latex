#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para processar CSV de contas a pagar e gerar métricas para relatório LaTeX
"""

import csv
from datetime import datetime
from collections import defaultdict
import locale

# Configurar locale para formatação brasileira
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    pass

def parse_date(date_str):
    """Converte string de data para datetime"""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except:
        return None

def parse_value(value_str):
    """Converte string de valor para float (formato brasileiro)"""
    if not value_str or value_str == 'False' or not value_str.strip():
        return 0.0
    try:
        # Formato brasileiro: vírgula é decimal, ponto é milhar
        # Ex: 1.234,56 -> 1234.56
        value_str = value_str.strip()
        # Remove pontos (separador de milhar)
        value_str = value_str.replace('.', '')
        # Substitui vírgula por ponto (decimal)
        value_str = value_str.replace(',', '.')
        return float(value_str)
    except Exception as e:
        print(f"Erro ao processar valor '{value_str}': {e}")
        return 0.0

def format_currency(value):
    """Formata valor como moeda brasileira"""
    return f"{value:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')

# Data base do relatório (pagamentos de 07/01/2026 já foram efetuados)
BASE_DATE = datetime(2026, 1, 8)

# Processar CSV
fornecedores = defaultdict(float)
contas_contabeis = defaultdict(float)
pagamentos_mensais = defaultdict(float)
titulos_altos = []
total_geral = 0.0
qtd_titulos = 0

print("Processando CSV...")

with open('/home/fredlisboa/latex/STUDIO DENTAL account.move.line_SANITIZED.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';')

    for row in reader:
        data_str = row.get('Data', '')
        data = parse_date(data_str)

        # Filtrar apenas datas >= 08/01/2026 (07/01 já foi pago)
        if not data or data < BASE_DATE:
            continue

        parceiro = row.get('Parceiro', 'SEM PARCEIRO').strip()
        if not parceiro:
            parceiro = 'SEM PARCEIRO'

        conta = row.get('Conta', 'SEM CONTA').strip()
        if not conta:
            conta = 'SEM CONTA'

        # Processar valores de crédito (passivos)
        credito = parse_value(row.get('Crédito', ''))

        if credito > 0:
            fornecedores[parceiro] += credito
            contas_contabeis[conta] += credito

            # Agrupar por mês/ano
            mes_ano = f"{data.year}-{data.month:02d}"
            pagamentos_mensais[mes_ano] += credito

            total_geral += credito
            qtd_titulos += 1

            # Identificar títulos acima de R$ 5.000,00
            if credito > 5000.0:
                titulos_altos.append({
                    'data': data.strftime('%d/%m/%Y'),
                    'parceiro': parceiro,
                    'valor': credito,
                    'referencia': row.get('Referência', ''),
                    'conta': conta
                })

# Ordenar fornecedores por valor (decrescente)
fornecedores_sorted = sorted(fornecedores.items(), key=lambda x: x[1], reverse=True)
contas_sorted = sorted(contas_contabeis.items(), key=lambda x: x[1], reverse=True)
titulos_altos_sorted = sorted(titulos_altos, key=lambda x: x['valor'], reverse=True)

# Preparar dados mensais para 2026
meses_2026 = []
for mes in range(1, 13):
    mes_ano = f"2026-{mes:02d}"
    valor = pagamentos_mensais.get(mes_ano, 0.0)
    meses_2026.append((mes, valor))

print(f"\n=== RESUMO ===")
print(f"Total Geral: R$ {format_currency(total_geral)}")
print(f"Quantidade de Títulos: {qtd_titulos}")
print(f"Títulos acima de R$ 5.000: {len(titulos_altos_sorted)}")
print(f"Fornecedores Únicos: {len(fornecedores)}")

# Salvar resultados em arquivo para usar no LaTeX
with open('/home/fredlisboa/latex/metrics.txt', 'w', encoding='utf-8') as f:
    f.write(f"TOTAL_GERAL={format_currency(total_geral)}\n")
    f.write(f"QTD_TITULOS={qtd_titulos}\n")
    f.write(f"QTD_TITULOS_ALTOS={len(titulos_altos_sorted)}\n")
    f.write(f"QTD_FORNECEDORES={len(fornecedores)}\n\n")

    f.write("=== TOP 15 FORNECEDORES ===\n")
    for i, (fornecedor, valor) in enumerate(fornecedores_sorted[:15], 1):
        f.write(f"{i}. {fornecedor}: R$ {format_currency(valor)}\n")

    f.write("\n=== CONTAS CONTÁBEIS ===\n")
    for i, (conta, valor) in enumerate(contas_sorted[:10], 1):
        f.write(f"{i}. {conta}: R$ {format_currency(valor)}\n")

    f.write("\n=== TÍTULOS ACIMA DE R$ 5.000 ===\n")
    for i, titulo in enumerate(titulos_altos_sorted, 1):
        f.write(f"{i}. {titulo['data']} | {titulo['parceiro']} | R$ {format_currency(titulo['valor'])} | {titulo['referencia']}\n")

    f.write("\n=== PAGAMENTOS MENSAIS 2026 ===\n")
    meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    for mes, valor in meses_2026:
        f.write(f"{meses_nomes[mes-1]}/2026: R$ {format_currency(valor)}\n")

# Gerar dados para tabelas LaTeX
with open('/home/fredlisboa/latex/latex_data.txt', 'w', encoding='utf-8') as f:
    # Top Fornecedores para tabela
    f.write("% TOP FORNECEDORES\n")
    for fornecedor, valor in fornecedores_sorted[:15]:
        fornecedor_clean = fornecedor.replace('&', '\\&').replace('_', '\\_')
        destaque = "\\textcolor{accentColor}{\\textbf{" if valor > 5000 else ""
        destaque_end = "}}" if valor > 5000 else ""
        f.write(f"{fornecedor_clean} & {destaque}{format_currency(valor)}{destaque_end} \\\\\n")

    f.write("\n% TÍTULOS ALTOS\n")
    for titulo in titulos_altos_sorted[:20]:
        parceiro_clean = titulo['parceiro'].replace('&', '\\&').replace('_', '\\_')
        ref_clean = titulo['referencia'].replace('&', '\\&').replace('_', '\\_')
        f.write(f"{titulo['data']} & {parceiro_clean} & \\textcolor{{accentColor}}{{\\textbf{{{format_currency(titulo['valor'])}}}}} & {ref_clean} \\\\\n")

    f.write("\n% DADOS PARA GRÁFICO\n")
    for mes, valor in meses_2026:
        f.write(f"({mes}, {valor/1000:.1f})\n")

print("\n✓ Arquivos gerados: metrics.txt e latex_data.txt")
