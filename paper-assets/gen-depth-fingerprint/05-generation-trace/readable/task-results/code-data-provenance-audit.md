# code data provenance audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-provenance-audit_20260517T105358_result.json`
- **Structured JSON:** [`86250f68da8b604b4432.json`](../../sessions/86/86250f68da8b604b4432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是逐项验证报告。

---

## 1. Cross-model chains binary F1=0.764 under 5-fold CV
- **论文声称**: binary F1=0.764 under 5-fold CV (results.tex:13)
- **数据文件**: `results/cross_model_chains_results.json`
- **文件中数字**: `cross_model.binary_f1 = 0.7635`（5-gen 子集，n=2964）
- **判定**: ✅ 0.7635 四舍五入至 3 位 = 0.764

## 2. 5-class LOGO F1 drops to ≈0.50
- **论文声称**: 5-class LOGO F1 drops to ≈0.50；appendix 报 0.501±0.038
- **数据文件**: `results/finer_ordinal_results.json` (6-gen GBT)
- **文件中数字**: `GBT_5class.macro_f1 = 0.5010`
- **判定**: ✅ 0.5010 → 0.501；与 appendix 表中 "Average 0.501±0.038" 一致
- **注意**: `8gen_finer_depth.json` (8-gen XGBoost) 给出 0.4878，不同协议不同数字；论文使用的是 6-gen GBT 结果

## 3. QLoRA fine-tuning recovers 3-class F1=0.905
- **论文声称**: 3-class F1=0.905 ±0.003 (appendix_qlora.tex:19)
- **数据文件**: `results/plan012_qwen06b_results.json`
- **文件中数字**: `macro_f1_3class = 0.9052, macro_f1_3class_std = 0.0032`
- **判定**: ✅ 0.9052 → 0.905；std 0.0032 → 0.003

## 4. Paraphrastic chains binary F1=0.671
- **论文声称**: binary F1=0.671 (limitations.tex:15)
- **数据文件**: `results/plan006_paraphrastic_comparison.json`
- **文件中数字**: `paraphrase_signal.binary_f1_gen1_vs_gen2plus.mean = 0.6711`
- **判定**: ✅ 0.6711 → 0.671

## 5. OLMo-2-1B-Instruct LOGO F1=0.338
- **论文声称**: OLMo-Instruct LOGO F1=0.338 (discussion.tex:29)
- **数据文件**: `results/review_p1c_olmo_instruct.json`
- **文件中数字**: `instruct_logo_f1 = 0.3379`；per_generator `olmo-2-0425-1b-instruct.macro_f1 = 0.3379`
- **判定**: ✅ 0.3379 → 0.338

## 6. Qwen3-0.6B chat template 0.667
- **论文声称**: Qwen3-0.6B with chat template to 0.667 (limitations.tex:7)
- **数据文件**: `results/review_p1c_qwen06b_instruct.json`
- **文件中数字**: `logo_7gen.per_generator.qwen3-0.6b-instruct.macro_f1 = 0.6674`
- **判定**: ✅ 0.6674 → 0.667

## 7. OLMo base "vs. 0.764"
- **论文声称**: "OLMo-2-1B-Instruct drops to LOGO F1=0.338 (vs. 0.764 base)" (limitations.tex:7)
- **数据文件**: `results/review_p1c_olmo_instruct.json`
- **文件中数字**: `base_olmo_logo_f1 = 0.7633`
- **判定**: ⚠️ OLMo base LOGO F1 = 0.7633 → 四舍五入为 **0.763**，论文写 0.764。0.764 实际是 cross-model chains 的整体 binary F1（来自 `cross_model_chains_results.json` 的 0.7635），不是 OLMo 单独的 base LOGO F1。差 0.001，疑似复制粘贴混淆。
  - **对比**: Qwen base 的引用没有此问题（0.8158 → 0.816 ✅）

## 8. Sampling sensitivity: robust at t∈[0.5,0.7], degrades at t=1.0 (-6pp)
- **论文声称**: robust at t∈[0.5,0.7], degrades at t=1.0 (-6pp)
- **数据文件**: `results/sampling_ablation.json`
- **文件中数字**:
  - `low_t05_p08.3class_f1 = 0.785`
  - `default_t07_p09.3class_f1 = 0.7877`
  - `high_t10_p095.3class_f1 = 0.7258`
  - `f1_range_pp = 6.19`
- **判定**: ✅ t=0.5 和 t=0.7 差距仅 0.3pp（稳健），t=1.0 下降 6.2pp ≈ "-6pp"

## 9. Topic drift R²=0.082
- **论文声称**: "Topic drift accounts for <9% of feature variance (R²=0.082)" (discussion.tex:21)
- **数据文件**: `results/review_topic_drift_results.json`
- **文件中数字**: `drifting_feature_correlations.entropy_mean_vs_semantic_drift.rho = -0.2859`
- **推导**: R² = (-0.2859)² = 0.0817 ≈ 0.082
- **判定**: ✅ R² 为最强 Spearman 相关系数的平方，0.0817 → 0.082
- **注意**: JSON 中未直接存储 R²，需从 rho 推导。论文对"feature variance"的措辞是上界（entropy_mean 是最强相关的特征）

## 10. LOFO binary F1=0.686
- **论文声称**: "average binary F1=0.686 (Δ=−0.8pp vs. LOGO)" (results.tex:14)
- **数据文件**: `results/8gen_lofo_family.json`
- **文件中数字**:
  - pythia: 0.6867, olmo: 0.7073, qwen: 0.687, llama: 0.708, mistral: 0.6433
  - `average.binary_f1 = 0.6865`
  - 真实均值: (0.6867+0.7073+0.687+0.708+0.6433)/5 = 0.68646
- **判定**: ✅ 0.68646 四舍五入至 3 位 = 0.686
- **注意**: 论文附带的 "Δ=−0.8pp vs. LOGO" 无法复现。LOGO binary F1（table3_v6: 0.7014）与 LOFO 0.686 之差为 -1.5pp，而非 -0.8pp。⚠️ delta 值可能有误

## 11. Cross-type transfer at 0.753
- **论文声称**: "cross-type transfer at 0.753" (discussion.tex:11)
- **数据文件**: `data/prompt_type_results.json`
- **文件中数字**: `lopto_f1.avg = 0.7525`（continuation: 0.762, elaboration: 0.7622, rewriting: 0.7334）
- **判定**: ✅ 0.7525 四舍五入至 3 位 = 0.753 (第4位=5，进位)

---

## 汇总

| # | 实验 | 论文数字 | 数据数字 | 判定 |
|---|------|---------|---------|------|
| 1 | Cross-model chains binary F1 | 0.764 | 0.7635 | ✅ |
| 2 | 5-class LOGO F1 | ≈0.50 (0.501) | 0.5010 | ✅ |
| 3 | QLoRA 3-class F1 | 0.905 | 0.9052 | ✅ |
| 4 | Paraphrastic binary F1 | 0.671 | 0.6711 | ✅ |
| 5 | OLMo-Instruct LOGO F1 | 0.338 | 0.3379 | ✅ |
| 6 | Qwen3-0.6B instruct F1 | 0.667 | 0.6674 | ✅ |
| 7 | OLMo base "0.764" | 0.764 | 0.7633 | ⚠️ 应为 0.763 |
| 8 | Sampling t=1.0 降幅 | -6pp | -6.2pp | ✅ |
| 9 | Topic drift R² | 0.082 | 0.0817 (推导) | ✅ |
| 10 | LOFO binary F1 | 0.686 | 0.68646 | ✅ |
| 11 | LOPTO cross-type transfer | 0.753 | 0.7525 | ✅ |

**需修复**:
1. **⚠️ #7**: limitations.tex 和 discussion.tex 中 OLMo base 对比值 "0.764" 应为 **0.763**（数据 0.7633）。0.764 是 cross-model chains 整体 binary F1，不是 OLMo 单模型的 base LOGO F1。
2. **⚠️ #10 delta**: results.tex 中 "Δ=−0.8pp vs. LOGO" 与数据不一致（LOGO binary F1=0.701 vs LOFO 0.686 = -1.5pp）。

---
