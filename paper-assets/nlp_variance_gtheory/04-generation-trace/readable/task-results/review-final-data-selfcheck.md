# review final data selfcheck

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_final_data_selfcheck_20260524T042716_result.json`
- **Structured JSON:** [`25dad83f0322f028d7ee.json`](../../sessions/25/25dad83f0322f028d7ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕，编译报告如下：

---

## 提交前自查报告

**1. Abstract 数字：PASS**
- G≥0.80 → experiments.tex §4.5 ✓
- 178 items → §4.5 "recommended 3-prompt × 3-seed design" ✓
- 1,602 evals → 178×9=1,602 ✓
- 3.1× → 552/178=3.10 ✓
- 552 items → Table 4 single-cond n_{G≥.80}=552 ✓
- 36% → Table 3 HellaSwag mod.×item=36.0% ✓
- 3B–72B → §4.6 Qwen2.5 3B/7B/72B ✓
- 2.3M → Table 1 total records=2,304,000 ✓

**2. Table 2 加总：PASS**
- 37.9+30.2+25.0+2.8+1.6+0.9+0.6+0.5+0.3 = 99.8%，"all others <0.1" 补足 0.2%

**3. Table 3 加总：PASS（全部 5 列）**
- MMLU: 37.9+30.2+2.8+0.9+1.6+25.0+1.6 = **100.0** ✓
- ARC: 37.9+33.7+3.1+1.4+8.0+15.4+0.5 = **100.0** ✓
- HellaSwag: 34.3+36.0+5.4+2.1+0.2+21.4+0.6 = **100.0** ✓
- GSM8K: 16.9+14.6+10.7+5.4+8.5+39.9+4.0 = **100.0** ✓
- MATH: 24.0+17.3+8.5+0.8+1.7+43.9+3.8 = **100.0** ✓

**4. Table 4 公式验证：PASS**
- Multi-facet: R=σ²_rel/σ²_p=13.675 → G(55)=55/68.675=0.801≈0.80 ✓; G(200)=0.936 ✓; total=55×1296=71,280 ✓
- Single-cond: R=137.84 → G(552)=552/689.84=0.800 ✓; G(200)=0.592 ✓; total=552 ✓
- Budget ratio: 552/55=10.04≈10.0× ✓
- IRT+multi: 116×1296=150,336 ✓

**5. §4.6 Llama-70B：PASS**
- item_id: 源 74.5106% → 论文 74.5% ✓
- G_item: 源 0.956639 → 论文 0.957 ✓
- Qwen-72B item_id: 源 83.2482% → 论文 83.2% ✓
- 差值: 83.25−74.51=8.74pp → 论文 8.7pp ✓

**6. Limitations partial-credit：PASS**
- Binary G: 源 0.862852 → 论文 0.86 ✓
- Partial G: 源 0.767985 → 论文 0.77 ✓
- 8/8 models G_partial < G_binary ✓; mean ΔG = −0.135 ✓

**7. Figure 源数据：5/5 存在**（论文引用 5 个 figure，非 6 个）
- fig0_teaser_dstudy.pdf ✓
- fig1_cross_benchmark.pdf ✓
- fig2_design_diagram.pdf ✓
- budget_sensitivity_band.pdf ✓
- fig4_difficulty_scatter.pdf ✓

**8. LaTeX 编译：PASS**
- Undefined citations: 0
- 页数: 17 页总计，主文 8 页（conclusion 结束于第 8 页），符合 EMNLP 限制
- Overfull hbox >30pt: 1 处（appendix 第 286–287 行，82pt）——仅在附录，不影响主文

---

**自查无问题。**

---
