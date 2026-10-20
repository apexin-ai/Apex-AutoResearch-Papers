# ops check mistral7b completion

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-mistral7b-completion_20260519T111634_result.json`
- **Structured JSON:** [`79146265a87851eb190e.json`](../../sessions/79/79146265a87851eb190e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能之前已被清除）。

## 汇报

**进程状态**：PID 107037 已退出，实验实际成功完成（之前被 cron 误判为 failed）。

**数据完整性**：全部 6 个 depth 各 5500 行，完整。

**分析结果**：

| Depth Pair | AUC | CI (±) | JSD |
|---|---|---|---|
| 0 vs 1 | **0.9191** | 0.0017 | 0.046984 |
| 1 vs 2 | **0.6152** | 0.0120 | 0.011845 |
| 2 vs 3 | 0.5293 | 0.0091 | 0.003717 |
| 3 vs 4 | 0.5286 | 0.0104 | 0.003206 |
| 4 vs 5 | 0.5099 | 0.0060 | 0.003083 |

- **K\* = 2**（AUC > 0.60 的最大 depth），与 Qwen/LLaMA 一致
- Ordinal classification: MAE = 1.3191, Accuracy = 0.3243
- Top features: freq_entropy, surp_d2_mean, surp_d1_mean

**结论**：Mistral-7B 在 code domain 的 K\*=2，与 Qwen/LLaMA 结果一致，说明 code domain 的 K\* 是 domain-governed 而非 model-intrinsic。Mistral 的 one-wash (K\*=1) 仅限 C4 domain。

**Registry**：status=DONE, conclusion=success, metrics 已写入。Cron 已不存在，无需删除。

---
