# Relatório Financeiro - 95STUDIO DENTAL

## Resumo da Atualização

Este documento apresenta a análise financeira do arquivo **95STUDIOaccount.move.line_SANITIZED.csv** com data base de **08/01/2026**.

## Arquivos Gerados

1. **process_95studio_csv.py** - Script Python de análise dos dados CSV
2. **metrics_95studio.txt** - Métricas consolidadas para referência
3. **relatorio_financeiro_atualizado.tex** - Relatório LaTeX atualizado
4. **relatorio_financeiro_atualizado.pdf** - Relatório PDF final (14 páginas)

## Indicadores Principais - 95STUDIO

| Métrica | Valor |
|---------|-------|
| **Valor Total Geral a Pagar** | R$ 738.915,20 |
| **Quantidade Total de Títulos** | 210 títulos |
| **Títulos de Alta Prioridade (> R$ 5.000)** | 92 títulos (43,8%) |
| **Quantidade de Credores** | 26 fornecedores |
| **Ticket Médio por Título** | R$ 3.518,64 |
| **Maior Obrigação Individual** | R$ 11.292,42 |

## Principais Credores

| Posição | Credor | Valor (R$) | % do Total |
|---------|--------|------------|------------|
| 1º | SANTANDER BRASIL | R$ 509.312,73 | 68,9% |
| 2º | UNIMED GOIÂNIA | R$ 64.800,00 | 8,8% |
| 3º | SIMPLES NACIONAL | R$ 62.400,00 | 8,4% |
| 4º | SIMONE HELENA DOS SANTOS | R$ 24.000,00 | 3,2% |
| 5º | VICTALAB F MANIPULACAO LTDA | R$ 16.263,64 | 2,2% |

## Distribuição Temporal

### Exercício 2026
- **Total 2026**: R$ 332.015,14 (44,9% do total)
- **1º Semestre 2026**: R$ 192.996,16 (26,1% do total)
- **108 títulos** no primeiro semestre

### Distribuição Mensal - 2026

| Mês | Valor (R$) | % do Total |
|-----|------------|------------|
| Janeiro | 36.636,98 | 5,0% |
| Fevereiro | 43.833,56 | 5,9% |
| Março | 37.122,87 | 5,0% |
| Abril | 27.983,92 | 3,8% |
| Maio | 24.459,43 | 3,3% |
| Junho | 22.959,40 | 3,1% |
| Julho | 22.959,38 | 3,1% |
| Agosto | 23.059,60 | 3,1% |
| Setembro | 22.750,00 | 3,1% |
| Outubro | 22.750,00 | 3,1% |
| Novembro | 22.750,00 | 3,1% |
| Dezembro | 24.750,00 | 3,3% |

### Distribuição por Ano

| Ano | Valor (R$) | % do Total |
|-----|------------|------------|
| 2026 | 332.015,14 | 44,9% |
| 2027 | 93.000,00 | 12,6% |
| 2028 | 87.600,00 | 11,9% |
| 2029 | 87.600,00 | 11,9% |
| 2030 | 87.600,00 | 11,9% |
| 2031 | 51.100,06 | 6,9% |

## Análise Crítica

### Pontos de Atenção

1. **Concentração Bancária**: 68,9% das obrigações concentradas no Santander Brasil (financiamentos de longo prazo)

2. **Novas Obrigações Estruturais**:
   - UNIMED GOIÂNIA (plano de saúde): R$ 64.800,00/ano
   - SIMPLES NACIONAL (tributos): R$ 62.400,00/ano
   - Folha de pagamento: R$ 24.000,00/ano

3. **Distribuição Equilibrada em 2026**: Média mensal de R$ 27.7 mil, com pico em fevereiro (R$ 43,8 mil)

4. **Obrigações de Longo Prazo**: 55,1% das obrigações estendem-se até 2031

### Composição 1º Semestre 2026

- **Obrigações Bancárias**: R$ 60.658,09 (31,4%)
- **Obrigações Operacionais**: R$ 132.338,07 (68,6%)
  - Fornecedores
  - Plano de saúde
  - Tributos
  - Folha de pagamento
  - Serviços contábeis

## Recomendações

1. **Provisão Mensal**: Estabelecer reserva de ~R$ 13,8k/mês para obrigações recorrentes
2. **Reserva de Liquidez**: Manter mínimo de R$ 50k para oscilações
3. **Renegociação Bancária**: Avaliar 156 títulos de longo prazo (2027-2031)
4. **Planejamento Tributário**: Otimização do SIMPLES NACIONAL
5. **Dashboard Financeiro**: Sistema de acompanhamento automático

## Como Usar

### Executar Análise
```bash
python3 process_95studio_csv.py
```

### Compilar Relatório
```bash
pdflatex relatorio_financeiro_atualizado.tex
pdflatex relatorio_financeiro_atualizado.tex  # Segunda compilação para referências
```

## Estrutura do Relatório PDF

1. **Capa** - Informações gerais
2. **Resumo Executivo** - Indicadores principais
3. **Detalhamento por Credor** - Ranking completo
4. **Títulos de Alta Prioridade** - Valores > R$ 5.000
5. **Cronograma 2026** - Distribuição mensal + gráfico
6. **Análise 1º Semestre** - Detalhamento Jan-Jun 2026
7. **Conclusões e Recomendações** - Estratégias financeiras

## Dados Técnicos

- **Empresa**: 95STUDIO DENTAL
- **CNPJ**: 46.125.234/0001-66
- **Data Base**: 08/01/2026
- **Arquivo Fonte**: 95STUDIOaccount.move.line_SANITIZED.csv
- **Total de Registros Processados**: 210 títulos
- **Período de Cobertura**: 2026-2031
- **Total de Páginas do Relatório**: 14

---

**Documento gerado em**: 07/01/2026
**Processamento**: Python 3 + LaTeX + pgfplots
