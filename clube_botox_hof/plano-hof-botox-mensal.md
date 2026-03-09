# Estudo de Taxas — Clube da Beleza

## 1. Contexto

Este estudo calcula o **preço parcelado** dos planos do Clube da Beleza, partindo do **preço à vista** de cada tratamento e embutindo a taxa da maquininha de cartão. Inclui também a análise do **custo de antecipação de recebíveis** e sua viabilidade para o fluxo de caixa. A abordagem é **conservadora**: utiliza-se a **maior taxa cobrada entre todas as bandeiras** em cada modalidade.

---

## 2. Taxas da Maquininha — Maior Taxa por Bandeira

| Modalidade | Mastercard | Visa | Elo | 4ª Bandeira | **Maior Taxa (referência)** |
|---|---|---|---|---|---|
| Débito | 0,79% | 0,79% | 0,99% | — | **0,99%** |
| Crédito à vista | 1,65% | 1,65% | 1,73% | 2,99% | **2,99%** |
| 2× a 6× | 1,99% | 1,99% | 1,99% | 2,99% | **2,99%** |
| 7× a 12× | 2,23% | 2,52% | 2,23% | 3,00% | **3,00%** |

> **Taxa MDR de referência para 12×: 3,00% sobre o valor total da transação.**

### Taxa de Antecipação de Recebíveis

| Opção | Taxa ao mês | Prazo médio (exemplo) | Taxa no período (exemplo) |
|---|---|---|---|
| Depósito hoje | **3,36%** | 22,17 dias | 2,48% |
| Depósito próximo dia útil | 3,33% | 21,17 dias | 2,35% |

> **Taxa de antecipação de referência (conservadora): 3,36% ao mês.**
>
> A taxa é aplicada proporcionalmente ao número de dias antecipados de cada parcela.

---

## 3. Planos — Preço à Vista (Valor-Base)

Estes são os valores que a clínica **precisa receber líquido** para que o tratamento seja viável:

| Plano | Inclui | Bônus | **Preço à Vista** |
|---|---|---|---|
| **Plano 1** | 2 botox anuais | Peeling | **R$ 2.160,00** |
| **Plano 2** | 3 botox anuais | Microagulhamento c/ vitaminas | **R$ 3.180,00** |
| **Plano 3** | 2 botox + 1 bioestimulador de colágeno + 2 ml preenchimento | Microagulhamento c/ vitaminas **ou** 1 sessão Red Touch | **R$ 7.080,00** |

---

## 4. Cálculo do Preço Parcelado (12×) — Somente MDR

### Lógica

O cliente que parcela em 12× gera um custo de **3,00%** na maquininha. Para que a clínica receba o preço à vista líquido, o valor cobrado no cartão precisa ser maior:

```
Valor Parcelado = Preço à Vista ÷ (1 − taxa_MDR)
Valor Parcelado = Preço à Vista ÷ 0,97
```

### Resultado

| Plano | Preço à Vista | Valor Parcelado (exato) | Parcela Exata (÷12) | **Parcela Arredondada** | **Total Parcelado** | Líquido (−3%) | Diferença vs. à Vista |
|---|---|---|---|---|---|---|---|
| **Plano 1** | R$ 2.160,00 | R$ 2.226,80 | R$ 185,57 | **R$ 186,00** | R$ 2.232,00 | R$ 2.165,04 | +R$ 5,04 |
| **Plano 2** | R$ 3.180,00 | R$ 3.278,35 | R$ 273,20 | **R$ 274,00** | R$ 3.288,00 | R$ 3.189,36 | +R$ 9,36 |
| **Plano 3** | R$ 7.080,00 | R$ 7.298,97 | R$ 608,25 | **R$ 609,00** | R$ 7.308,00 | R$ 7.088,76 | +R$ 8,76 |

---

## 5. Tabela de Preços Comerciais — À Vista vs. Parcelado (Somente MDR)

| Plano | **À Vista** | **Parcelado 12×** | Diferença para o cliente |
|---|---|---|---|
| **Plano 1** | R$ 2.160,00 | 12× R$ 190,00 (= R$ 2.280,00) | +R$ 120,00 (+5,6%) |
| **Plano 2** | R$ 3.180,00 | 12× R$ 275,00 (= R$ 3.300,00) | +R$ 120,00 (+3,8%) |
| **Plano 3** | R$ 7.080,00 | 12× R$ 610,00 (= R$ 7.320,00) | +R$ 240,00 (+3,4%) |

### Margem Líquida (Sem Antecipação)

| Plano | Total Parcelado | Líquido (−3% MDR) | vs. Preço à Vista |
|---|---|---|---|
| **Plano 1** | R$ 2.280,00 | R$ 2.211,60 | **+R$ 51,60** |
| **Plano 2** | R$ 3.300,00 | R$ 3.201,00 | **+R$ 21,00** |
| **Plano 3** | R$ 7.320,00 | R$ 7.100,40 | **+R$ 20,40** |

> **Sem antecipação**, todos os planos geram margem positiva. A clínica recebe parcelado (31 dias a cada parcela) ao longo de 12 meses.

---

## 6. Custo da Antecipação Total (12 parcelas)

### Como funciona

Sem antecipação, a clínica recebe cada parcela líquida (após MDR) a cada ~31 dias. Se optar por **antecipar todos os recebíveis**, a operadora cobra **3,36% ao mês**, proporcional ao número de dias antecipados de cada parcela.

### Fórmula

```
Parcela líquida (após MDR) = Parcela × (1 − 0,03) = Parcela × 0,97

Custo de antecipação da parcela nº N = Parcela_líquida × 3,36% × (31 × N ÷ 30)

Custo total de antecipação = soma do custo de todas as 12 parcelas
```

### Detalhamento — Plano 1 (12× R$ 190,00)

| Parcela nº | Dias até recebimento | Parcela líquida | Custo antecipação | Recebe hoje |
|---|---|---|---|---|
| 1 | 31 | R$ 184,30 | R$ 6,40 | R$ 177,90 |
| 2 | 62 | R$ 184,30 | R$ 12,80 | R$ 171,50 |
| 3 | 93 | R$ 184,30 | R$ 19,20 | R$ 165,10 |
| 4 | 124 | R$ 184,30 | R$ 25,59 | R$ 158,71 |
| 5 | 155 | R$ 184,30 | R$ 31,99 | R$ 152,31 |
| 6 | 186 | R$ 184,30 | R$ 38,39 | R$ 145,91 |
| 7 | 217 | R$ 184,30 | R$ 44,79 | R$ 139,51 |
| 8 | 248 | R$ 184,30 | R$ 51,19 | R$ 133,11 |
| 9 | 279 | R$ 184,30 | R$ 57,59 | R$ 126,71 |
| 10 | 310 | R$ 184,30 | R$ 63,99 | R$ 120,31 |
| 11 | 341 | R$ 184,30 | R$ 70,39 | R$ 113,91 |
| 12 | 372 | R$ 184,30 | R$ 76,79 | R$ 107,51 |
| **TOTAL** | | **R$ 2.211,60** | **R$ 499,11** | **R$ 1.712,49** |

### Resumo dos 3 Planos — Antecipação Total

| Plano | Bruto (12×) | Líquido MDR (−3%) | Custo Antecipação | **Líquido Final** | **vs. Preço à Vista** | **Perda %** |
|---|---|---|---|---|---|---|
| **Plano 1** | R$ 2.280,00 | R$ 2.211,60 | −R$ 499,11 | **R$ 1.712,49** | **−R$ 447,51** | −20,7% |
| **Plano 2** | R$ 3.300,00 | R$ 3.201,00 | −R$ 722,27 | **R$ 2.478,73** | **−R$ 701,27** | −22,1% |
| **Plano 3** | R$ 7.320,00 | R$ 7.100,40 | −R$ 1.602,64 | **R$ 5.497,76** | **−R$ 1.582,24** | −22,3% |

> ⚠️ **A antecipação total de 12 parcelas é INVIÁVEL.** O custo combinado (MDR + antecipação) consome de **20,7% a 22,3%** do preço à vista — um prejuízo severo que inviabiliza a operação.

---

## 7. Quanto custaria repassar a antecipação total ao cliente?

Se a clínica quisesse antecipar **todas** as parcelas e ainda receber o preço à vista líquido, a parcela precisaria ser:

```
Taxa efetiva combinada = 1 − [0,97 × (1 − 22,57%)] = 1 − 0,7511 = 24,89%

Parcela necessária = (Preço à Vista ÷ 0,7511) ÷ 12
```

| Plano | Preço à Vista | Total necessário | **Parcela 12×** | Acréscimo vs. à vista |
|---|---|---|---|---|
| **Plano 1** | R$ 2.160,00 | R$ 2.876,21 | **R$ 240,00** | +33,2% |
| **Plano 2** | R$ 3.180,00 | R$ 4.234,02 | **R$ 353,00** | +33,1% |
| **Plano 3** | R$ 7.080,00 | R$ 9.426,35 | **R$ 786,00** | +33,1% |

> Repassar o custo integral ao cliente elevaria as parcelas em ~33% — comercialmente inaceitável para um programa de assinatura de estética.

---

## 8. Cenários de Antecipação Parcial

A solução prática é **antecipar apenas parte das parcelas**, equilibrando fluxo de caixa e custo financeiro.

### Cenário A — Antecipar somente as 3 primeiras parcelas

Recebe as parcelas 1-3 imediatamente; parcelas 4-12 chegam normalmente (31 dias cada).

| Plano | Recebe agora (parcelas 1-3) | Custo antecipação | Líquido agora | Recebe depois (parcelas 4-12) | **Total líquido** | **vs. à Vista** |
|---|---|---|---|---|---|---|
| **Plano 1** | R$ 552,90 | −R$ 38,39 | R$ 514,51 | R$ 1.658,70 | **R$ 2.173,21** | **+R$ 13,21** |
| **Plano 2** | R$ 800,25 | −R$ 55,57 | R$ 744,68 | R$ 2.400,75 | **R$ 3.145,43** | **−R$ 34,57** |
| **Plano 3** | R$ 1.775,10 | −R$ 123,26 | R$ 1.651,84 | R$ 5.325,30 | **R$ 6.977,14** | **−R$ 102,86** |

> ✅ **Cenário viável.** O Plano 1 mantém margem positiva. Os Planos 2 e 3 têm prejuízo de apenas 1,1% a 1,5% — absorvível ou compensável com ajuste mínimo na parcela.

### Cenário B — Antecipar as 6 primeiras parcelas

Recebe as parcelas 1-6 imediatamente; parcelas 7-12 chegam normalmente.

| Plano | Recebe agora (parcelas 1-6) | Custo antecipação | Líquido agora | Recebe depois (parcelas 7-12) | **Total líquido** | **vs. à Vista** |
|---|---|---|---|---|---|---|
| **Plano 1** | R$ 1.105,80 | −R$ 134,36 | R$ 971,44 | R$ 1.105,80 | **R$ 2.077,24** | **−R$ 82,76** |
| **Plano 2** | R$ 1.600,50 | −R$ 194,46 | R$ 1.406,04 | R$ 1.600,50 | **R$ 3.006,54** | **−R$ 173,46** |
| **Plano 3** | R$ 3.550,20 | −R$ 431,30 | R$ 3.118,90 | R$ 3.550,20 | **R$ 6.669,10** | **−R$ 410,90** |

> ⚠️ **Cenário caro.** O prejuízo fica entre 3,8% e 5,8% do preço à vista — significativo, mas pode ser parcialmente compensado se a parcela comercial absorver esse custo.

### Cenário C — Antecipação automática (receber tudo em D+1)

Este é o cenário onde a clínica ativa a antecipação automática para todas as vendas parceladas, recebendo no próximo dia útil (taxa de 3,33% ao mês).

| Plano | Bruto (12×) | Líquido MDR (−3%) | Custo antecipação (D+1) | **Líquido Final** | **vs. à Vista** | **Perda %** |
|---|---|---|---|---|---|---|
| **Plano 1** | R$ 2.280,00 | R$ 2.211,60 | −R$ 493,88 | **R$ 1.717,72** | **−R$ 442,28** | −20,5% |
| **Plano 2** | R$ 3.300,00 | R$ 3.201,00 | −R$ 714,72 | **R$ 2.486,28** | **−R$ 693,72** | −21,8% |
| **Plano 3** | R$ 7.320,00 | R$ 7.100,40 | −R$ 1.585,90 | **R$ 5.514,50** | **−R$ 1.565,50** | −22,1% |

> A diferença entre D+0 (3,36%) e D+1 (3,33%) é insignificante — economia de apenas ~R$ 5 a R$ 17 por plano. Não altera a conclusão de inviabilidade da antecipação total.

---

## 9. Comparativo Consolidado — Todos os Cenários

### Plano 1 (à vista R$ 2.160 / parcelado 12× R$ 190)

| Cenário | Líquido Total | vs. à Vista | Viabilidade |
|---|---|---|---|
| Sem antecipação | R$ 2.211,60 | **+R$ 51,60** | ✅ Ideal |
| Antecipa 3 parcelas | R$ 2.173,21 | **+R$ 13,21** | ✅ Viável |
| Antecipa 6 parcelas | R$ 2.077,24 | **−R$ 82,76** | ⚠️ Marginal |
| Antecipa tudo (D+0) | R$ 1.712,49 | **−R$ 447,51** | ❌ Inviável |
| Antecipa tudo (D+1) | R$ 1.717,72 | **−R$ 442,28** | ❌ Inviável |

### Plano 2 (à vista R$ 3.180 / parcelado 12× R$ 275)

| Cenário | Líquido Total | vs. à Vista | Viabilidade |
|---|---|---|---|
| Sem antecipação | R$ 3.201,00 | **+R$ 21,00** | ✅ Ideal |
| Antecipa 3 parcelas | R$ 3.145,43 | **−R$ 34,57** | ✅ Viável (−1,1%) |
| Antecipa 6 parcelas | R$ 3.006,54 | **−R$ 173,46** | ⚠️ Marginal (−5,5%) |
| Antecipa tudo (D+0) | R$ 2.478,73 | **−R$ 701,27** | ❌ Inviável |
| Antecipa tudo (D+1) | R$ 2.486,28 | **−R$ 693,72** | ❌ Inviável |

### Plano 3 (à vista R$ 7.080 / parcelado 12× R$ 610)

| Cenário | Líquido Total | vs. à Vista | Viabilidade |
|---|---|---|---|
| Sem antecipação | R$ 7.100,40 | **+R$ 20,40** | ✅ Ideal |
| Antecipa 3 parcelas | R$ 6.977,14 | **−R$ 102,86** | ✅ Viável (−1,5%) |
| Antecipa 6 parcelas | R$ 6.669,10 | **−R$ 410,90** | ⚠️ Marginal (−5,8%) |
| Antecipa tudo (D+0) | R$ 5.497,76 | **−R$ 1.582,24** | ❌ Inviável |
| Antecipa tudo (D+1) | R$ 5.514,50 | **−R$ 1.565,50** | ❌ Inviável |

---

## 10. Ganho Extra em Outras Modalidades de Pagamento

Se o valor cobrado for o **parcelado** (já com taxa embutida) e o cliente optar por pagar de forma mais barata para a clínica:

| Modalidade | Taxa Real | Plano 1 (R$ 2.280) | Plano 2 (R$ 3.300) | Plano 3 (R$ 7.320) |
|---|---|---|---|---|
| Pix / Débito | 0,99% | Líquido R$ 2.257,43 → **sobra R$ 97,43** | Líquido R$ 3.267,33 → **sobra R$ 87,33** | Líquido R$ 7.247,53 → **sobra R$ 167,53** |
| Crédito à vista | 2,99% | Líquido R$ 2.211,83 → **sobra R$ 51,83** | Líquido R$ 3.201,33 → **sobra R$ 21,33** | Líquido R$ 7.101,13 → **sobra R$ 21,13** |
| 12× (pior caso) | 3,00% | Líquido R$ 2.211,60 → **sobra R$ 51,60** | Líquido R$ 3.201,00 → **sobra R$ 21,00** | Líquido R$ 7.100,40 → **sobra R$ 20,40** |

> **Oportunidade comercial**: oferecer o preço à vista como "desconto" para pagamento via Pix — o cliente economiza de 3,4% a 5,6%, a clínica não perde nada.

---

## 11. Recomendação Final

### Tabela de Preços

| | **Preço à Vista / Pix** | **Preço Parcelado 12×** |
|---|---|---|
| **Plano 1** | R$ 2.160,00 | 12× **R$ 190,00** |
| **Plano 2** | R$ 3.180,00 | 12× **R$ 275,00** |
| **Plano 3** | R$ 7.080,00 | 12× **R$ 610,00** |

### Estratégia de Antecipação

1. **Não ativar antecipação automática.** O custo de ~22% sobre os recebíveis é destrutivo para a margem.
2. **Se precisar de fôlego no caixa**, antecipar no máximo as **3 primeiras parcelas** de cada venda — o custo é controlável (1,1% a 1,5% de perda sobre o preço à vista) e a clínica recebe um aporte imediato sem comprometer a rentabilidade do plano.
3. **Priorizar pagamento à vista / Pix** na abordagem comercial: a clínica elimina 100% do custo financeiro e recebe imediatamente. O "desconto" de 3-5% para Pix é custeado pela margem que já estava embutida no parcelado.
4. **Reservar a antecipação de 6+ parcelas** apenas para situações emergenciais de caixa, com consciência de que o custo é relevante (3,8% a 5,8%).