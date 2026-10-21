# train detect remove q03 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_detect_remove_q03_seed42_20260524T210433_result.json`
- **Structured JSON:** [`0a00dcbb035d598e67dd.json`](../../sessions/0a/0a00dcbb035d598e67dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动。

**detect_remove_q03_seed42 状态汇总：**

| 项目 | 值 |
|------|-----|
| 数据 | 116,935 样本（q_score < 0.3） |
| PID | 984296 |
| GPU | cuda:3 |
| 进度 | 39/6103 steps（~1%） |
| 速度 | ~2.08s/step |
| 预计耗时 | ~3.5 小时（约 00:35 完成） |
| Loss | ~2.5-3.5 范围，正常下降中 |
| tmux session | `detect_remove_q03_seed42` |

weighting_method=uniform 确认生效（weighted_loss = unweighted_loss），mean_q 在 0.02-0.18 范围，符合过滤后低污染数据的预期。

---
