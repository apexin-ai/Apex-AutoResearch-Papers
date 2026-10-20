# train 34685 vanilla detach ln batch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_34685_vanilla_detach_ln_batch_20260526T084439_result.json`
- **Structured JSON:** [`a2eeaaaf07ffa8495316.json`](../../sessions/a2/a2eeaaaf07ffa8495316.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部启动成功，训练正常进行中。

| 实验 | GPU | PID | 显存占用 | GPU利用率 | 速度 |
|------|-----|-----|---------|----------|------|
| vanilla_v2_s1 | cuda:0 | 419107 | 62193 MiB | 99% | ~1.08 it/s |
| vanilla_v2_s2 | cuda:1 | 419342 | 62231 MiB | 98% | ~1.08 it/s |
| detach_ln_s3 | cuda:2 | 419641 | 62203 MiB | 99% | ~1.08 it/s |

预计训练时长：50005 steps / 1.08 it/s ≈ **12.9 小时**。Registry 已全部更新为 RUNNING。

---
