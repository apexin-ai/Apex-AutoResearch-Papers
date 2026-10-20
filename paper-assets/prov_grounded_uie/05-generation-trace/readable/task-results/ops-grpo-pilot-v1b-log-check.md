# ops grpo pilot v1b log check

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_grpo_pilot_v1b_log_check_20260513T001130_result.json`
- **Structured JSON:** [`307512f2f932695ce569.json`](../../sessions/30/307512f2f932695ce569.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**grpo_pilot_v1b 结果：DONE / negative**

| 指标 | 值 |
|------|-----|
| 步数 | 20/20 完成 |
| 运行时间 | 40 min |
| reward (step 1) | 0.8206 |
| reward (step 20) | 0.5955 |
| reward 变化 | **-0.2251** (持续下降) |
| KL | 极低 (~8.3e-5) |
| train_loss | 0.0129 |
| checkpoint | `outputs/grpo_pilot/final` |

训练正常完成，模型已保存，但 reward 从 0.82 单调下降到 0.60。KL 极低说明策略几乎没偏离，但 reward 仍在降——可能是 reward function 信号不够强、或 batch size 太小 (effective bs=4) 导致高方差梯度。

Registry 已更新为 DONE/negative，cron 已清除。

---
