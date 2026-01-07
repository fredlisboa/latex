#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para processar CSV do 96STUDIO e gerar análise de contas a pagar
Baseado na coluna "Data de Vencimento"
"""

import csv
import sys
from datetime import datetime
from collections import defaultdict
from decimal import Decimal

def parse_decimal(value):
    """Converte string com vírgula em Decimal"""
    if not value or value == "FALSE" or value.strip() == "":
        return Decimal("0")
    return Decimal(value.replace(",", "."))

def parse_date(date_str):
    """Converte string de data em objeto datetime"""
    if not date_str or date_str == "FALSE" or date_str.strip() == "":
        return None
    try:
        date_str = date_str.strip()
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None

def main():
    input_file = "96STUDIOaccount.move.line_SANITIZED.csv"

    # Data base para análise (08/01/2026)
    data_base = datetime(2026, 1, 8)

    # Estruturas para armazenar dados
    contas_pagar = []
    total_geral = Decimal("0")
    credores = defaultdict(Decimal)
    meses = defaultdict(Decimal)
    meses_qtd = defaultdict(int)
    titulos_alta_prioridade = []

    print(f"Processando arquivo: {input_file}")
    print(f"Data base: {data_base.strftime('%d/%m/%Y')}")
    print("-" * 80)

    with open(input_file, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f, delimiter=';')

        # Pular cabeçalho
        next(reader)

        for row in reader:
            if len(row) < 15:
                continue

            # Índices das colunas:
            # 4: Parceiro
            # 5: Referência
            # 10: Débito
            # 11: Crédito
            # 14: Data de Vencimento

            # Verificar se é conta a pagar (Crédito > 0)
            credito = parse_decimal(row[11])

            if credito <= 0:
                continue

            # Obter data de vencimento
            data_vencimento = parse_date(row[14])

            if not data_vencimento:
                continue

            # Filtrar apenas vencimentos >= data base
            if data_vencimento < data_base:
                continue

            parceiro = row[4].strip() if row[4] else 'SEM PARCEIRO'
            if not parceiro:
                parceiro = 'SEM PARCEIRO'

            referencia = row[5].strip() if len(row) > 5 else ''

            # Adicionar à lista
            contas_pagar.append({
                'vencimento': data_vencimento,
                'parceiro': parceiro,
                'valor': credito,
                'referencia': referencia
            })

            total_geral += credito
            credores[parceiro] += credito

            # Agregar por mês
            mes_ano = data_vencimento.strftime("%Y-%m")
            meses[mes_ano] += credito
            meses_qtd[mes_ano] += 1

            # Títulos de alta prioridade (> 5000)
            if credito > 5000:
                titulos_alta_prioridade.append({
                    'vencimento': data_vencimento,
                    'parceiro': parceiro,
                    'valor': credito,
                    'referencia': referencia
                })

    # Ordenar contas a pagar por valor decrescente
    contas_pagar.sort(key=lambda x: x['valor'], reverse=True)
    titulos_alta_prioridade.sort(key=lambda x: x['valor'], reverse=True)

    # Imprimir estatísticas
    print(f"\n{'='*80}")
    print(f"RESUMO GERAL")
    print(f"{'='*80}")
    print(f"Total de títulos: {len(contas_pagar)}")
    print(f"Valor total a pagar: R$ {total_geral:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Títulos de alta prioridade (> R$ 5.000): {len(titulos_alta_prioridade)}")
    print(f"Quantidade de credores: {len(credores)}")

    if contas_pagar:
        ticket_medio = total_geral / len(contas_pagar)
        print(f"Ticket médio: R$ {ticket_medio:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Maior obrigação: R$ {contas_pagar[0]['valor']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    # Top credores
    print(f"\n{'='*80}")
    print(f"TOP 15 CREDORES")
    print(f"{'='*80}")
    credores_ordenados = sorted(credores.items(), key=lambda x: x[1], reverse=True)
    for i, (credor, valor) in enumerate(credores_ordenados[:15], 1):
        percentual = (valor / total_geral * 100) if total_geral > 0 else 0
        print(f"{i:2d}. {credor[:50]:50s} R$ {valor:>15,.2f} ({percentual:5.1f}%)".replace(",", "X").replace(".", ",").replace("X", "."))

    # Distribuição mensal
    print(f"\n{'='*80}")
    print(f"DISTRIBUIÇÃO MENSAL - 2026")
    print(f"{'='*80}")
    meses_ordenados = sorted([(k, v) for k, v in meses.items() if k.startswith('2026')])
    total_2026 = Decimal("0")
    for mes_ano, valor in meses_ordenados:
        qtd = meses_qtd[mes_ano]
        percentual = (valor / total_geral * 100) if total_geral > 0 else 0
        mes_nome = datetime.strptime(mes_ano, "%Y-%m").strftime("%B/%Y").capitalize()
        print(f"{mes_nome:20s} {qtd:3d} títulos  R$ {valor:>15,.2f} ({percentual:5.1f}%)".replace(",", "X").replace(".", ",").replace("X", "."))
        total_2026 += valor

    percentual_2026 = (total_2026 / total_geral * 100) if total_geral > 0 else 0
    print(f"{'-'*80}")
    print(f"{'TOTAL 2026':20s}           R$ {total_2026:>15,.2f} ({percentual_2026:5.1f}%)".replace(",", "X").replace(".", ",").replace("X", "."))

    # Top 20 títulos de alta prioridade
    print(f"\n{'='*80}")
    print(f"TOP 20 TÍTULOS DE ALTA PRIORIDADE (> R$ 5.000)")
    print(f"{'='*80}")
    for i, titulo in enumerate(titulos_alta_prioridade[:20], 1):
        venc = titulo['vencimento'].strftime("%d/%m/%Y")
        print(f"{i:2d}. {venc} {titulo['parceiro'][:35]:35s} R$ {titulo['valor']:>12,.2f} {titulo['referencia'][:20]}".replace(",", "X").replace(".", ",").replace("X", "."))

    # Análise do 1º semestre 2026
    print(f"\n{'='*80}")
    print(f"ANÁLISE DETALHADA - 1º SEMESTRE 2026")
    print(f"{'='*80}")

    semestre1_meses = ['2026-01', '2026-02', '2026-03', '2026-04', '2026-05', '2026-06']
    total_sem1 = Decimal("0")
    qtd_sem1 = 0

    for mes in semestre1_meses:
        if mes in meses:
            total_sem1 += meses[mes]
            qtd_sem1 += meses_qtd[mes]

    print(f"Total 1º semestre: R$ {total_sem1:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Quantidade de títulos: {qtd_sem1}")
    percentual_sem1 = (total_sem1 / total_geral * 100) if total_geral > 0 else 0
    print(f"Percentual do total: {percentual_sem1:.1f}%")

    # Análise Bancário vs Operacional (1º semestre)
    print(f"\n{'='*80}")
    print(f"COMPOSIÇÃO: BANCÁRIO VS OPERACIONAL (1º SEMESTRE 2026)")
    print(f"{'='*80}")

    for mes in semestre1_meses:
        if mes not in meses:
            continue

        bancario = Decimal("0")
        operacional = Decimal("0")

        for conta in contas_pagar:
            if conta['vencimento'].strftime("%Y-%m") == mes:
                if 'SANTANDER' in conta['parceiro'].upper() or 'BANCO' in conta['parceiro'].upper():
                    bancario += conta['valor']
                else:
                    operacional += conta['valor']

        total_mes = meses[mes]
        perc_bancario = (bancario / total_mes * 100) if total_mes > 0 else 0
        mes_nome = datetime.strptime(mes, "%Y-%m").strftime("%B").capitalize()

        print(f"{mes_nome:10s} Bancário: R$ {bancario:>12,.2f} | Operacional: R$ {operacional:>12,.2f} | Total: R$ {total_mes:>12,.2f} ({perc_bancario:5.1f}% banc.)".replace(",", "X").replace(".", ",").replace("X", "."))

    print(f"\n{'='*80}")
    print(f"Processamento concluído!")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
