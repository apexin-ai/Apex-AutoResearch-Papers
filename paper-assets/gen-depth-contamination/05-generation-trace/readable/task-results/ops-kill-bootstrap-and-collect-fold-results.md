# ops kill bootstrap and collect fold results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-bootstrap-and-collect-fold-results_20260518T221009_result.json`
- **Structured JSON:** [`dd01a2ee84a5b6726300.json`](../../sessions/dd/dd01a2ee84a5b6726300.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告完成。

## 结果汇总

### A. 进程 Kill
- PID 86210 已通过 SIGTERM 成功终止，`ps aux` 确认无残留进程。

### B. GPU 释放
- cuda:0 已完全释放：**0MiB / 24564MiB**，GPU-Util 0%。

### C. Fold-based AUC 确认（与预期一致）

| Depth Pair | AUC (5-fold CV) | 95% CI | JSD |
|---|---|---|---|
| 0 vs 1 | **0.9838** | [0.9820, 0.9855] | 0.2263 |
| 1 vs 2 | 0.8969 | [0.8937, 0.9001] | 0.1046 |
| 2 vs 3 | 0.8100 | [0.8052, 0.8147] | 0.0752 |
| 3 vs 4 | 0.7624 | [0.7543, 0.7706] | 0.0654 |

### D. Per-fold CI
`pairwise_auc.json` 包含完整 per-fold 数据，CI 按 `mean ± 1.96 * std / sqrt(5)` 计算。CI 区间窄且合理（与 bootstrap 的虚高区间形成对比）。

### E. LaTeX 表格
写入路径：`artifacts/exp_qwen_retrain_chain/paper/qwen_retrain_results.tex`

所有 pair AUC > 0.60，K* ≥ 4 成立。Bootstrap 结果（`bootstrap_ci.json`）已废弃不用。

---
