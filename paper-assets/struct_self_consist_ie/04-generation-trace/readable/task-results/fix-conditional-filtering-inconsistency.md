# fix conditional filtering inconsistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_conditional_filtering_inconsistency_20260514T124449_result.json`
- **Structured JSON:** [`a73f1b8d9ec578ead3e2.json`](../../sessions/a7/a73f1b8d9ec578ead3e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器代码完全一致，均已使用正确的 `greedy_f1 > 0` 定义。

---

## 完成总结

### 排查结果

**根因**：6 处代码中，5 处使用了错误的 conditional 定义 `any(sample_f1 > 0)`（只要任一 sample 有 F1>0 即保留），而标准定义是 `greedy_f1 > 0`（排除 greedy 完全无提取能力的实例）。

**影响**：以 RE 为例，错误定义产生 n_cond=331，正确定义产生 n_cond=238，差 93 个实例（greedy F1=0 但某些 sample 偶然 F1>0 的 knowledge-gap 实例被错误保留）。

### 修复状态

| 脚本 | 修复前状态 | 当前状态 |
|------|-----------|---------|
| `exp001_postprocess.py` | 已正确 | ✅ |
| `run_mvp_pilot.py` | 此前已修复 | ✅ |
| `analyze_exp015_unified.py` | 此前已修复 | ✅ |
| `analyze_logprob_baseline.py` | 此前已修复 | ✅ |
| `analyze_component_wise_re.py` | 此前已修复 | ✅ |
| `analyze_exp002_conll2003.py` | 此前已修复 | ✅ |
| `analyze_exp004_re_diagnostic.py` threshold_sensitivity | **本次修复** | ✅ |
| `analyze_exp004_re_diagnostic.py` bootstrap | 此前已修复 | ✅ |

### 产出
1. **诊断报告**: `output/conditional_filter_diagnosis.json` (autodl-5090)
2. **修正 metrics**: `output/exp001_n16_seed42/corrected_conditional_metrics.json` — 重算验证 n_cond 与 `exp001_all_signals_report.json` 完全一致
3. **Registry**: `exp_001_ner_n16_scierc` metrics 已为正确值，无需更新
4. **gpu-5090-4x-2**: 代码已同步，正在运行的实验将使用正确定义

---
