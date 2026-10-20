# d064 Paper Patch Template
# 等 d064 结果到后，填入数字，发给 Paper Agent

## Scenario A: DR=0% for calibrated models (Qwen + Llama)

[Patch] d064 DocRED 998-doc beam 结果入稿

### appendix_beam_search.tex
1. Table beam-search: DocRED 行从 "(50)" 改为 "(998)"
   - Qwen beam-4 unc: ET=0, RV=0, DR=__%, CF=__%, E-F1=__, R-F1=__
   - Qwen beam-4 con: ET=0, RV=0, DR=__%, CF=__%, E-F1=__, R-F1=__
   - Llama beam-4 unc: ET=0, RV=0, DR=__%, CF=__%, E-F1=__, R-F1=__
   - Llama beam-4 con: ET=0, RV=0, DR=__%, CF=__%, E-F1=__, R-F1=__
   + 新增 Llama greedy unc/con 行（新 checkpoint baseline）

2. Table caption: "DocRED evaluated on matched 50-document subsets" → "DocRED evaluated on full 998-document dev set"

3. Discussion paragraph: 
   - 删除 "Clopper-Pearson 95% CI upper bound is 5.8%" 句子
   - 改为 "With DR=0 in 998 DocRED documents for both calibrated models, the zero-violation result generalizes beyond the SciERC schema to the larger DocRED ontology (96 relations)."

### section5_runtime.tex (beam results paragraph)
- "(SciERC 551 docs; DocRED 50-doc subset)" → "(SciERC 551 docs; DocRED 998 docs)"
- 更新具体 DR/CF 数字

### abstract.tex
- 如果 998-doc 也 DR=0%，可以强化：加 "across both datasets" 或类似

### section1_introduction_draft.tex
- C3: 更新 beam deployment config 描述

---

## Scenario B: DR near-zero but not exactly 0%

同上但：
- 报告实际 DR 数字（不 claim "eliminates"）
- CI 仍远优于 50-doc (upper bound ~0.5% vs 5.8%)
- §7 加限定词："near-eliminates DR on DocRED"

## Scenario C: DR notably higher

- 保留 50-doc 数据作为主表
- 998-doc 作为补充讨论
- 分析原因（parse failure rate, schema complexity）
