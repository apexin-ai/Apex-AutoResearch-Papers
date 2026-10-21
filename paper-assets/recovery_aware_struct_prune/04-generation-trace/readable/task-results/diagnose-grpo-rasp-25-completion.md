# diagnose grpo rasp 25 completion

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_rasp_25_completion_20260516T170406_result.json`
- **Structured JSON:** [`7163fe9c2e18729972b7.json`](../../sessions/71/7163fe9c2e18729972b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**grpo_rasp_25 诊断结果：训练成功完成。**

| 指标 | Step 100 (最终) |
|------|----------------|
| reward | 0.009375 |
| reward_std | 0.03149 |
| frac_reward_zero_std | 0.875 |
| KL | 0.0007035 |
| loss | 0.01275 |
| entropy | 0.04262 |
| 耗时 | 57.95 min |
| W&B run | bc4ojqie |

注意：frac_reward_zero_std 从 step 10 的 0.925 略降到 0.875，但整体 reward 仍极低（0.009375），表明 RASP 25% 模型在 GRPO 100 steps 内几乎无法获得有效 reward 信号——符合假设中"collapse 比 20% 更严重"的预期。

Registry 已更新为 DONE/success，cron 无需删除（已不存在）。

---
