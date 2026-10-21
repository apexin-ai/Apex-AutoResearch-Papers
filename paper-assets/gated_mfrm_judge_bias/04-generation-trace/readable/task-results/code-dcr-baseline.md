# code dcr baseline

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcr_baseline_20260522T010215_result.json`
- **Structured JSON:** [`7fb48f3bc855fe04edfe.json`](../../sessions/7f/7fb48f3bc855fe04edfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

## 产出总结

**文件:**
- `/root/gated_mfrm_judge_bias/baselines/dcr_baseline.py` — 完整实现
- `/root/gated_mfrm_judge_bias/baselines/test_dcr.py` — 11 个测试全通过

**s1-s4 映射方案:**

| Signal | DCR Level | 我们的计算方式 | 映射理由 |
|--------|-----------|---------------|----------|
| s1 | Semantic | 模型 n 均分相对 cohort 的 z-score → sigmoid 映射到 [0,1] | 语义层污染表现为整体分数膨胀 |
| s2 | Information | 模型 n 逐题得分与 item easiness 的 Pearson 相关 | 信息层污染 = 在"大家都觉得简单"的题上过度获益 |
| s3 | Data | 模型 n 满分率（命中 max_score 的 entry 比例） | 数据层污染 = 直接记忆答案 → ceiling effect |
| s4 | Label | 所有 judge 对模型 n 同时给高分的 item 比例 | 标签层污染 = 完美复现预期答案 → judge 一致高分 |

**验证结果:**
- `Spearman(true_c, dcr_scores) = 0.504, p = 0.023` — DCR 的 contamination 估计与 G-MFRM 真实 `c` 参数显著正相关，baseline 有效。

---
