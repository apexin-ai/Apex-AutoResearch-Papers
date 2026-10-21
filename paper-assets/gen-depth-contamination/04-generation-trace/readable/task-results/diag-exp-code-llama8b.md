# diag exp code llama8b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_code_llama8b_20260519T080749_result.json`
- **Structured JSON:** [`7fc1fab5c643307adbfc.json`](../../sessions/7f/7fc1fab5c643307adbfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析成功完成。汇报如下：

## 诊断结果

**生成数据**：depth 0-5 全部完整，features.csv 也已生成（33000 行）。崩溃仅发生在 Step 5 Analysis 阶段。

**Bug 修复**：代码中已有 try/except 修复（第 462-466 行），将 `int(r["doc_id"])` 包裹在 try 块中，ValueError 时 fallback 为保留原始字符串。这个修复在当前代码中已经存在（可能是之前有人加的，但进程崩溃后未重跑）。无需额外修改。

**分析结果** (K* = 2)：

| 对比 | AUC | JSD |
|------|-----|-----|
| depth 0 vs 1 | 0.9161 ± 0.0040 | 0.060406 |
| depth 1 vs 2 | 0.7394 ± 0.0101 | 0.047034 |
| depth 2 vs 3 | 0.5112 ± 0.0095 | 0.003473 |
| depth 3 vs 4 | 0.5200 ± 0.0137 | 0.003026 |
| depth 4 vs 5 | 0.4996 ± 0.0069 | 0.002892 |

- **K\* = 2**（AUC > 0.60 的最大 depth）
- Ordinal MAE = 1.2542, Accuracy = 0.3485
- Top features: freq_entropy, surp_d1_mean, surp_d2_mean

结果文件已写入 `results/exp_code_llama8b/`（pairwise_auc.json, jsd.json, ordinal_results.json, feature_importance.json, summary.txt）。

---
