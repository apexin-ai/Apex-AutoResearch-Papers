# diagnose deepseek cwm repo s123

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_deepseek-cwm-repo-s123_20260517T160336_result.json`
- **Structured JSON:** [`a4967fdc93a5cd15f893.json`](../../sessions/a4/a4967fdc93a5cd15f893.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**训练仍在进行中，未完成。**

| 指标 | 值 |
|------|-----|
| 当前进度 | 9418/13266 (71%) |
| train_loss | 0.0004 (健康) |
| eval_loss | **nan** (epoch 1.0 和 2.0 均为 nan) |
| best_metric | inf (无法选出 best checkpoint) |
| best/ 目录 | 不存在 |
| GPU 3 利用率 | 99%, 18GB/32GB |
| 预估剩余时间 | ~8.5h (3848 steps × ~8s/step) |

**问题：`eval_loss: nan`**

日志有明确报错：`Token indices sequence length is longer than the specified maximum sequence length for this model (21612 > 16384)`。验证集中存在超过模型 max position embeddings (16384) 的样本，导致 eval forward pass 溢出产生 nan。由于 `best_metric: inf`，训练结束后 `best/` 目录不会被创建。

**影响**：训练本身正常收敛（train_loss 持续下降），但无法通过 eval_loss 选出最优 checkpoint。训练完成后只能使用最后一个 checkpoint（checkpoint-13266）或手动从 checkpoint-4422/8844 中选择。

**行动**：保留 cron 继续监控，不更新 registry 状态。训练完成后需要决定如何选择最终 checkpoint（建议用最后一个 checkpoint，因为 train_loss 趋势正常）。

---
