#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Análise Financeira - 95STUDIO
Processa arquivo CSV de contas a pagar do sistema contábil
Data Base: 08/01/2026
"""

import csv
from datetime import datetime
from collections import defaultdict
from decimal import Decimal

# Configuração
CSV_FILE = '95STUDIOaccount.move.line_SANITIZED.csv'
DATA_BASE = datetime(2026, 1, 8)  # Excluir pagamentos até 07/01/2026 (já efetuados)

def parse_valor(valor_str):
    """Converte string de valor para Decimal"""
    if not valor_str or valor_str == 'FALSE':
        return Decimal('0')
    # Remove espaços e substitui vírgula por ponto
    valor_str = valor_str.strip().replace(',', '.')
    return Decimal(valor_str)

def parse_data(data_str):
    """Converte string de data para objeto datetime"""
    try:
        return datetime.strptime(data_str, '%Y-%m-%d')
    except:
        return None

def main():
    # Estruturas de dados
    titulos = []
    por_credor = defaultdict(Decimal)
    por_ano = defaultdict(Decimal)
    por_mes_2026 = defaultdict(Decimal)
    titulos_alta_prioridade = []

    # Leitura do CSV
    print(f"Processando arquivo: {CSV_FILE}")
    print("=" * 80)

    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            # Extrair campos
            data_vencimento_str = row.get('Data de Vencimento', '')
            parceiro = row.get('Parceiro', '').strip()
            credito_str = row.get('Crédito', '')
            debito_str = row.get('Débito', '')
            referencia = row.get('Referência', '').strip()

            # Parse de valores
            credito = parse_valor(credito_str)
            debito = parse_valor(debito_str)
            data_vencimento = parse_data(data_vencimento_str)

            # Filtrar: apenas créditos (passivos) com vencimento >= DATA_BASE
            if credito > 0 and data_vencimento and data_vencimento >= DATA_BASE:
                titulo = {
                    'vencimento': data_vencimento,
                    'parceiro': parceiro,
                    'valor': credito,
                    'referencia': referencia,
                    'ano': data_vencimento.year,
                    'mes': data_vencimento.month
                }

                titulos.append(titulo)
                por_credor[parceiro] += credito
                por_ano[data_vencimento.year] += credito

                if data_vencimento.year == 2026:
                    mes_ano = f"{data_vencimento.year}-{data_vencimento.month:02d}"
                    por_mes_2026[mes_ano] += credito

                # Títulos de alta prioridade (> R$ 5.000)
                if credito > 5000:
                    titulos_alta_prioridade.append(titulo)

    # Ordenar
    titulos.sort(key=lambda x: x['vencimento'])
    titulos_alta_prioridade.sort(key=lambda x: x['valor'], reverse=True)
    credores_ordenados = sorted(por_credor.items(), key=lambda x: x[1], reverse=True)

    # Calcular métricas
    total_geral = sum(por_credor.values())
    qtd_titulos = len(titulos)
    qtd_credores = len(por_credor)
    qtd_alta_prioridade = len(titulos_alta_prioridade)
    ticket_medio = total_geral / qtd_titulos if qtd_titulos > 0 else Decimal('0')
    maior_obrigacao = max(t['valor'] for t in titulos) if titulos else Decimal('0')

    # Total 2026
    total_2026 = sum(por_mes_2026.values())
    perc_2026 = (total_2026 / total_geral * 100) if total_geral > 0 else Decimal('0')

    # === SAÍDA DE RESULTADOS ===
    print("\n" + "=" * 80)
    print("RESUMO EXECUTIVO - 95STUDIO")
    print("=" * 80)
    print(f"Valor Total Geral a Pagar: R$ {total_geral:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Quantidade Total de Títulos: {qtd_titulos}")
    print(f"Títulos de Alta Prioridade (> R$ 5.000): {qtd_alta_prioridade}")
    print(f"Quantidade de Credores: {qtd_credores}")
    print(f"Ticket Médio por Título: R$ {ticket_medio:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Maior Obrigação Individual: R$ {maior_obrigacao:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

    # === RANKING DE CREDORES ===
    print("\n" + "=" * 80)
    print("RANKING DE CREDORES (TOP 15)")
    print("=" * 80)
    print(f"{'Credor':<50} {'Valor (R$)':>20} {'%':>8}")
    print("-" * 80)

    for i, (credor, valor) in enumerate(credores_ordenados[:15], 1):
        perc = (valor / total_geral * 100) if total_geral > 0 else 0
        valor_fmt = f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f"{i:2d}. {credor[:47]:<47} R$ {valor_fmt:>17} {perc:6.1f}%")

    # Soma dos outros
    if len(credores_ordenados) > 15:
        outros_valor = sum(v for _, v in credores_ordenados[15:])
        outros_qtd = len(credores_ordenados) - 15
        outros_perc = (outros_valor / total_geral * 100) if total_geral > 0 else 0
        outros_fmt = f"{outros_valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f"    OUTROS ({outros_qtd} fornecedores){' ':<28} R$ {outros_fmt:>17} {outros_perc:6.1f}%")

    print("-" * 80)
    total_fmt = f"{total_geral:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    print(f"{'TOTAL':<50} R$ {total_fmt:>17} 100.0%")

    # === TÍTULOS DE ALTA PRIORIDADE ===
    print("\n" + "=" * 80)
    print(f"TÍTULOS DE ALTA PRIORIDADE - TOP 20 (> R$ 5.000,00)")
    print("=" * 80)
    print(f"{'Vencimento':<15} {'Credor':<35} {'Valor (R$)':>15} {'Referência':<20}")
    print("-" * 80)

    for titulo in titulos_alta_prioridade[:20]:
        venc = titulo['vencimento'].strftime('%d/%m/%Y')
        credor = titulo['parceiro'][:32]
        valor_fmt = f"{titulo['valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        ref = titulo['referencia'][:17]
        print(f"{venc:<15} {credor:<35} R$ {valor_fmt:>12} {ref:<20}")

    if len(titulos_alta_prioridade) > 20:
        print(f"\n... e mais {len(titulos_alta_prioridade) - 20} títulos de alta prioridade")

    # === DISTRIBUIÇÃO MENSAL 2026 ===
    print("\n" + "=" * 80)
    print("CRONOGRAMA DE PAGAMENTOS - EXERCÍCIO 2026")
    print("=" * 80)
    print(f"{'Mês/Ano':<20} {'Valor (R$)':>20} {'% do Total':>12}")
    print("-" * 80)

    meses_nomes = {
        1: 'Janeiro/2026', 2: 'Fevereiro/2026', 3: 'Março/2026',
        4: 'Abril/2026', 5: 'Maio/2026', 6: 'Junho/2026',
        7: 'Julho/2026', 8: 'Agosto/2026', 9: 'Setembro/2026',
        10: 'Outubro/2026', 11: 'Novembro/2026', 12: 'Dezembro/2026'
    }

    for mes in range(1, 13):
        mes_ano = f"2026-{mes:02d}"
        valor = por_mes_2026.get(mes_ano, Decimal('0'))
        perc = (valor / total_geral * 100) if total_geral > 0 else Decimal('0')
        valor_fmt = f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f"{meses_nomes[mes]:<20} R$ {valor_fmt:>17} {perc:6.1f}%")

    print("-" * 80)
    total_2026_fmt = f"{total_2026:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    print(f"{'TOTAL 2026':<20} R$ {total_2026_fmt:>17} {perc_2026:6.1f}%")

    # === ANÁLISE 1º SEMESTRE 2026 ===
    print("\n" + "=" * 80)
    print("ANÁLISE DETALHADA - 1º SEMESTRE 2026")
    print("=" * 80)

    semestre_1 = sum(por_mes_2026.get(f"2026-{m:02d}", Decimal('0')) for m in range(1, 7))
    titulos_semestre = [t for t in titulos if t['ano'] == 2026 and t['mes'] <= 6]

    print(f"Total 1º Semestre: R$ {semestre_1:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Quantidade de Títulos: {len(titulos_semestre)}")
    print(f"Percentual do Total Geral: {(semestre_1/total_geral*100):,.1f}%".replace(',', 'X').replace('.', ',').replace('X', '.'))

    # === DISTRIBUIÇÃO POR ANO ===
    print("\n" + "=" * 80)
    print("DISTRIBUIÇÃO POR ANO")
    print("=" * 80)

    for ano in sorted(por_ano.keys()):
        valor = por_ano[ano]
        perc = (valor / total_geral * 100) if total_geral > 0 else Decimal('0')
        valor_fmt = f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f"{ano}: R$ {valor_fmt:>20} ({perc:5.1f}%)")

    print("\n" + "=" * 80)
    print("Processamento concluído com sucesso!")
    print("=" * 80)

    # Salvar métricas em arquivo
    with open('metrics_95studio.txt', 'w', encoding='utf-8') as f:
        f.write(f"TOTAL_GERAL={total_geral}\n")
        f.write(f"QTD_TITULOS={qtd_titulos}\n")
        f.write(f"QTD_ALTA_PRIORIDADE={qtd_alta_prioridade}\n")
        f.write(f"QTD_CREDORES={qtd_credores}\n")
        f.write(f"TICKET_MEDIO={ticket_medio}\n")
        f.write(f"MAIOR_OBRIGACAO={maior_obrigacao}\n")
        f.write(f"TOTAL_2026={total_2026}\n")
        f.write(f"PERC_2026={perc_2026}\n")

    print("\nMétricas salvas em: metrics_95studio.txt")

if __name__ == '__main__':
    main()
