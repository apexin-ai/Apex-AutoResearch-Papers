# recovery dual gpu crash

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recovery_dual-gpu-crash_20260516T055312_result.json`
- **Structured JSON:** [`a20695d059e1baaa5fe4.json`](../../sessions/a2/a20695d059e1baaa5fe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**严重阻碍：**
1. **磁盘 100% 满** — 无法运行 eval 或训练
2. **plan018_random_b01_s45 没有 checkpoint**（只有 README + reward_log）— 无法 resume，必须重训
3. **sweep_isr_b02_s44/checkpoint-400 不完整**（2/4 shards）— 必须用 checkpoint-350

需要清理磁盘才能继续。安全可删目录（均为 DONE/success，有完整 metrics，无 needs-re-eval 标记）：

| 目录 | 大小 | 实验 |
|------|------|------|
| sweep_isr_b02_s44/checkpoint-400 | 8.8G | 不完整，无用 |
| sweep_isr_b02_s43 | 31G | 已完成，metrics 已记录 |
| sweep_isr_b02_s42_v2 | 31G | 已完成，metrics 已记录 |
| sweep_isr_b005_s42 | 31G | 已完成，metrics 已记录 |

删这 4 个可释放 ~100G，足够 eval + 重训。

是否执行清理？另外确认：plan018-random-b01-s45-r2 既然没有 checkpoint，要从 base model 全量重训 500 步（不是 resume）。

---
