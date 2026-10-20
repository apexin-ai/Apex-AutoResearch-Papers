# paper final data audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-data-audit_20260523T191628_result.json`
- **Structured JSON:** [`8c668956d1f34d4bb4d3.json`](../../sessions/8c/8c668956d1f34d4bb4d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集和比对完成。编制审计报告。

## 数据自查报告

### ✅ 已核对一致

**Abstract（全部数字）**
- `d=0.74–1.05` ← tost_equivalence: hapax |d|=0.735 (heteroscedasticity table), entropy_mean |d|=1.054 → 0.74–1.05 ✓
- `d<0.10` ← entropy_max d=0.062, tail_decay d=0.087 → 均<0.10 ✓
- `d=0.46` ← entropy_std d=0.4571 → 0.46 ✓
- `≥8×` ← 0.735/0.087=8.4× ✓
- `F1=0.694` ← 8gen_logo binary f1_observed=0.6944 → 0.694 ✓
- `F1=0.830` ← cross_model binary_f1=0.8296 → 0.830 ✓
- `F1=0.762` ← 8gen_logo 3class f1_observed=0.762 ✓
- `F1=0.905` ← plan012_qwen06b macro_f1_3class=0.9052 → 0.905 ✓

**Table 1（8 generators + averages，逐行核对）**
- 所有 8 个 generator 的 Binary F1、95% CI、3-class F1 与 `8gen_logo_unfiltered.json` 完全一致 ✓
- Average: Bin=0.694, 3class=0.762 ✓
- LOFO (family-level)=0.686 ← `8gen_lofo_family.json` avg binary_f1=0.6865 → 0.686 ✓
- SD=0.028, IQR=[0.692, 0.714] ← 从 per-generator binary F1 计算验证 ✓

**Table 2（7 baselines，逐行核对）**
- 全部 7 个 method 的 3-class F1、Binary F1 与 `8gen_table3_v7_unified.json` 完全一致 ✓
- ms/text: 9.7, 22.8 ← `efficiency_comparison.json` ✓

**Results §5.1**
- N=37,058 ✓, CI [0.688, 0.700] ✓, 0.694±0.010 SE ✓
- 0.633 (Mistral-7B) ✓, 0.724 (Pythia-2.8B) ✓
- Cross-model binary F1=0.830, CI [.818, .841] ← cross_model_logo ✓
- Length-matched F1=0.724 vs 0.770 ← `8gen_length_confound.json` ✓
- Independent-seed F1=0.680 ← `independent_seed_results.json` avg=0.6803 → 0.680 ✓
- QLoRA +11.6pp: 0.905−0.789=0.116 ✓（0.789 = 6-gen LOGO XGBoost, appendix_classifier 验证）

**Results §5.2**
- Silhouette=0.660, p=0.030 ← appendix_ddr_validation 一致 ✓
- ρ: hapax -0.64, TTR -0.62, entropy_mean -0.60 ← `8gen_pooled_rho.json` ✓
- F1=0.773 (10-fold) ← `8gen_feature_ablation.json` full=0.7727 → 0.773 ✓
- Surface-only=0.688, reference-only=0.713 ← 同上 ✓
- ~2.4× lower cost ← efficiency speedup_ratio=2.35 → ~2.4× ✓

**Discussion**
- Depth-2 error rate=48.4% ← `comprehensive_error_analysis.json` depth_2 rate=0.4842 ✓
- ≤29.2% for gen-3 ← depth_3 rate=0.2917 → 29.2% ✓
- QLoRA F1=0.89–0.91 ← qlora_olmo-instruct 3class=0.888, qlora_qwen-instruct 3class=0.907 → 0.89–0.91 ✓
- Cross-domain F1=0.74–0.75 ← appendix_domain: 0.739–0.754 → 0.74–0.75 ✓

**Conclusion**
- F1=0.694–0.762 ✓, F1=0.830 ✓, QLoRA=0.89–0.91 ✓

**Limitations**
- Instruct LOGO binary F1=0.487 ← appendix_instruct line 50 内部一致
- QLoRA=0.89–0.91 ✓
- 5-class F1≈0.50 ← finer_ordinal GBT_5class=0.501 ✓

**Appendix tables（抽查）**
- LOFO 8-gen 全部 7 行 ← `8gen_lofo_results.json` 逐项验证 ✓
- Instruct table（OLMo/Qwen/Llama base vs instruct）← `instruct_analysis_summary.json` 逐项验证 ✓
- Instruct QLoRA table ← 4 个 qlora JSON 逐项验证 ✓
- Variance decomposition table η² values ← appendix 内部一致 ✓
- DDR validation epsilon sweep table d values ← tost_equivalence + heteroscedasticity table 一致 ✓
- Length confound: F1=0.724, 0.770, random=0.767, Δ=0.046 ← `8gen_length_confound.json` ✓

---

### ⚠️ 发现的不一致

**1. Discussion η²_gen 标注错误（discussion.tex:8）**

论文写：`η²_depth=0.34–0.37 for location vs η²_gen<0.009 (>48×)`

实际：
- η²_depth=0.34–0.37（location, 正确）来自 variance decomposition table
- `>48×` 的比较对象是 **shape η²_depth<0.007**（0.341/0.007=48.7×），NOT η²_gen
- η²_gen 在 variance decomposition table 中范围 0.001–0.024，不是 <0.009
- η²_gen ≤ 0.009 是来自 **cross-model appendix** 的不同 ANOVA（正确引用在 results.tex:22）
- Appendix 自身正确描述了这个比较（line 31: "34-37% location vs <1% shape"）

→ **建议修正**: 将 discussion.tex 中 `$\eta^2_{\text{gen}}{<}0.009$` 改为 `$\eta^2_{\text{depth}}{<}0.01$ for shape features`，或拆分为两个独立声明。

**2. Cross-ref spread 0.013 vs 源数据 0.012（results.tex:101）**

论文写：`F1 spread of only 0.013`
源数据：avg_macro_f1 across 3 refs = 0.8034, 0.8072, 0.8158 → range = 0.0124 → 0.012

→ **建议修正**: 改为 `0.012` 或保留 `0.013` 并标注为 ceiling rounding。影响很小。

**3. Same-family "up to 1.3 pp"（results.tex:101）**

论文写：`same-family proximity may inflate Pythia F1 by up to 1.3 pp`
源数据 (`review_p2f_cross_ref_bias.json`)：
- Pythia-1B: same-family vs cross-family delta = 0.0086 → 0.9pp
- Pythia-2.8B: max cross-ref delta = 0.0114 → 1.1pp

1.3pp 与 spread 0.013 是同一个数的不同表述（0.0124→0.013/1.3pp），但源数据实际为 0.0124=1.24pp，非 1.3pp。

→ **建议修正**: 改为 `up to 1.2 pp` 或 `up to $\sim$1 pp`

---

### ❌ 待人工确认

**1. QLoRA 实验描述 "6-gen LOGO" vs 源数据 4-gen 5-fold CV**

appendix_qlora.tex 和 appendix_classifier.tex 均声称 "6-generator LOGO"，但 `plan012_qwen06b_results.json` 明确使用 4 generators (pythia-1b, olmo-2-1b, qwen3-0.6b, qwen3-1.7b) + 5-fold stratified CV。F1=0.905 值一致（0.9052→0.905），但**实验协议描述**需确认：是否有独立的 6-gen LOGO 结果文件，还是附录描述有误。

**2. XGBoost baseline 0.789 来源**

appendix_qlora 和 appendix_lofo 均引用 "6-gen LOGO XGBoost 3-class F1=0.789"。但：
- `finer_ordinal_results.json` GBT_3class = 0.7836（6-gen LOGO, 但值 = 0.784 ≠ 0.789）
- `plan012_xgboost_matched.json` = 0.8048（4-gen 5-fold CV）
- appendix_classifier.tex XGBoost avg = 0.789

最可能来源是 appendix_classifier 中的 6-gen LOGO 实验（未找到对应 JSON）。建议确认 `rp_lofo_corrected.json` 或 `lofo_ablation_results.json` 是否包含此值。

**3. Instruct LOGO binary F1=0.487 来源**

appendix_instruct.tex line 50 声称 "Three-generator instruct LOGO yields binary F1=0.487"。未在已检查的 JSON 文件中找到此数值。可能在 `exp052_instruct_eval.json` 或其他未读取的 instruct 结果文件中。

**4. ±3–4% batch estimation**

Conclusion 引用 "±3–4% batch estimation; Appendix error-analysis"。未在 `comprehensive_error_analysis.json` 截断输出中找到。需完整读取该文件确认。

**5. η² >48× 边界极其紧凑**

即使用正确的比较（location η²_depth vs shape η²_depth），最小比值为 0.341/0.007 = 48.7×。仅仅 "barely >48×"。如果使用更精确的小数位（如 η²_depth(ent max) = 0.0073），比值可能<48。建议验证原始 ANOVA 输出的精确 η² 值。

---

### 修复完整性确认

- **Cohen's d 0.55 残留**：**无** ✓ — grep 未找到任何 entropy_std 与 0.55 关联的残留。所有出现的 0.55 均为其他上下文（LOFO drop、PCA loading、per-family DDR table 中的 entropy_mean）。
- **TTR ρ -0.63 残留**：**无** ✓ — grep 未找到 "TTR -0.63" 的任何实例。Results.tex 正确使用 -0.62。
- **d ≤ 0.08 残留**：**无** ✓ — grep 未找到 `d ≤ 0.08` 或 `d\leq 0.08` 的任何实例。正文使用 `d < 0.10`。
- **"excluding all Pythia" 残留**：**无** ✓ — grep 未找到 "excluding.*Pythia" 的任何实例。

---
