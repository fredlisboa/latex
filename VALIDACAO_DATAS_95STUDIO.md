# Validação de Datas - Análise 95STUDIO

## Data da Análise: 07/01/2026

## Verificação de Consistência de Dados

### Comparação entre Cenários de Data Base

| Critério | Incluindo 07/01/2026 | Excluindo 07/01/2026 (Atual) |
|----------|---------------------|-------------------------------|
| **Data Base** | >= 07/01/2026 | >= 08/01/2026 |
| **Total a Pagar** | R$ 798.785,36 | R$ 738.915,20 |
| **Quantidade de Títulos** | 222 | 210 |
| **Diferença** | - | **-R$ 59.870,16** (-12 títulos) |

### Títulos com Vencimento em 07/01/2026 (Já Pagos)

Estes valores **NÃO** constam no relatório atual:

| Parceiro | Valor (R$) | Referência |
|----------|------------|------------|
| COLABORADORES STUDIO DENTAL | R$ 2.700,00 | BILL/2026/0074 |
| VICTALAB F MANIPULACAO LTDA | R$ 1.743,48 | BILL/2026/0060 |
| GABRIELLA MACHADO COSTA LISBOA | R$ 5.000,00 | BILL/2026/0042 |
| EDUARDO BORGES NUNES | R$ 5.000,00 | BILL/2026/0041 |
| MATHEUS MAGALHÃES | R$ 1.500,00 | BILL/2026/0040 |
| SIMONE HELENA DOS SANTOS | R$ 5.445,22 | Diversos |
| VICTALAB F MANIPULACAO LTDA | R$ 2.240,67 | Diversos |
| Outros fornecedores | R$ ~36.240,79 | Diversos |

**TOTAL PAGO EM 07/01/2026**: **R$ 59.870,16**

## Validação do Relatório Atual

### ✅ Confirmações

1. **Data Base Correta**: 08/01/2026
2. **Exclusão de Pagamentos**: Valores com vencimento em 07/01/2026 corretamente excluídos
3. **Total Validado**: R$ 738.915,20 (210 títulos)
4. **Nota Explicativa**: Presente na capa do relatório

### 📋 Texto da Nota no Relatório

> *"Nota: Pagamentos com vencimento em 07/01/2026 já foram efetuados e não constam neste relatório."*

### 🎯 Métricas do Relatório Atual (Data Base: 08/01/2026)

| Métrica | Valor |
|---------|-------|
| Valor Total Geral a Pagar | R$ 738.915,20 |
| Quantidade Total de Títulos | 210 |
| Títulos de Alta Prioridade | 92 (> R$ 5.000) |
| Quantidade de Credores | 26 |
| Ticket Médio | R$ 3.518,64 |
| Maior Obrigação | R$ 11.292,42 |

## Distribuição Temporal Validada

### Exercício 2026

| Período | Valor | % do Total | Títulos |
|---------|-------|------------|---------|
| Janeiro/2026 | R$ 36.636,98 | 5,0% | 28 |
| Fevereiro/2026 | R$ 43.833,56 | 5,9% | 25 |
| Março/2026 | R$ 37.122,87 | 5,0% | 22 |
| **1º Trimestre** | **R$ 117.593,41** | **15,9%** | **75** |
| **2026 Completo** | **R$ 332.015,14** | **44,9%** | **-** |

### Distribuição Plurianual (2026-2031)

| Ano | Valor | % do Total |
|-----|-------|------------|
| 2026 | R$ 332.015,14 | 44,9% |
| 2027 | R$ 93.000,00 | 12,6% |
| 2028 | R$ 87.600,00 | 11,9% |
| 2029 | R$ 87.600,00 | 11,9% |
| 2030 | R$ 87.600,00 | 11,9% |
| 2031 | R$ 51.100,06 | 6,9% |
| **TOTAL** | **R$ 738.915,20** | **100,0%** |

## Principais Credores Validados

| Posição | Credor | Valor | % |
|---------|--------|-------|---|
| 1º | SANTANDER BRASIL | R$ 509.312,73 | 68,9% |
| 2º | UNIMED GOIÂNIA | R$ 64.800,00 | 8,8% |
| 3º | SIMPLES NACIONAL | R$ 62.400,00 | 8,4% |
| 4º | SIMONE HELENA DOS SANTOS | R$ 24.000,00 | 3,2% |
| 5º | VICTALAB F MANIPULACAO | R$ 16.263,64 | 2,2% |
| **Top 5** | **Subtotal** | **R$ 676.776,37** | **91,5%** |

## Análise de Criticidade - Janeiro 2026

### Títulos com Vencimento em Janeiro/2026

- **Total Janeiro**: R$ 36.636,98 (28 títulos)
- **Títulos > R$ 5.000**: 1 título (R$ 11.292,42 - Santander)
- **Média por Título**: R$ 1.308,46

### Primeira Quinzena (08/01 a 15/01/2026)

Verificando os vencimentos mais próximos:

```
26/01/2026 - SANTANDER BRASIL - R$ 11.292,42 (Título de maior valor em janeiro)
```

## Conclusão da Validação

### ✅ Status: VALIDADO

O relatório está **CORRETO** e reflete com precisão:

1. ✅ Exclusão dos pagamentos de 07/01/2026 (R$ 59.870,16)
2. ✅ Data base 08/01/2026 corretamente aplicada
3. ✅ Total de R$ 738.915,20 validado
4. ✅ 210 títulos processados
5. ✅ Nota explicativa presente
6. ✅ Distribuição temporal consistente

### 📊 Arquivos de Referência

- **CSV Original**: `95STUDIOaccount.move.line_SANITIZED.csv` (31.935 linhas)
- **Script de Análise**: `process_95studio_csv.py`
- **Métricas**: `metrics_95studio.txt`
- **Relatório LaTeX**: `relatorio_financeiro_atualizado.tex`
- **Relatório PDF**: `relatorio_financeiro_atualizado.pdf` (14 páginas)

### 🔍 Auditoria

- **Data da Extração**: 07/01/2026
- **Data Base do Relatório**: 08/01/2026
- **Pagamentos Excluídos**: 07/01/2026 (já efetuados)
- **Período de Cobertura**: 08/01/2026 a 09/07/2031
- **Última Compilação**: 07/01/2026 17:46

---

**Documento de Validação**
**Data**: 07/01/2026
**Validado por**: Sistema Automatizado de Análise Financeira
**Status**: ✅ APROVADO
