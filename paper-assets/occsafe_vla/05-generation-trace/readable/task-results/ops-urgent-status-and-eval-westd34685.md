# ops urgent status and eval westd34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_status_and_eval_westd34685_20260523T195030_result.json`
- **Structured JSON:** [`a3055ee4ddaccba8fa28.json`](../../sessions/a3/a3055ee4ddaccba8fa28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部仍在训练中，无一完成。

| 实验 | PID | GPU | Step | 进度 | ETA |
|------|-----|-----|------|------|-----|
| reverse_cutoff_s0 | 408059 | cuda:2 | 48112/50005 | 96% | ~32 min |
| cutoff_25k_s0 | 408207 | cuda:3 | 48234/50005 | 96% | ~30 min |
| cutoff_15k_s0 | 443639 | cuda:1 | 4380/50005 | 9% | ~12 h |
| cutoff_45k_s0 | 456023 | cuda:0 | 3433/50005 | 7% | ~12 h |

**reverse_cutoff_s0** 和 **cutoff_25k_s0** 约 30 分钟后完成。未启动 eval。

**磁盘**: `/root/autodl-tmp` 200G/350G (58%), 151G 可用。

**建议**: 30 分钟后再查一次，届时前两个实验应已完成，可立即提交 eval。

---
