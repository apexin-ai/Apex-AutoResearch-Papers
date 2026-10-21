# ops 34685 gpu verify

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-gpu-verify_20260526T214409_result.json`
- **Structured JSON:** [`e000ff7eaf053ca9d3c5.json`](../../sessions/e0/e000ff7eaf053ca9d3c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

**GPU 状态：4 张全部在用，没有空闲。**

| GPU | 显存占用 | 利用率 | 实验 |
|-----|---------|--------|------|
| 0 | 62231/97887 MiB | 99% | vanilla_v2_s1 |
| 1 | 62231/97887 MiB | 99% | vanilla_v2_s2 |
| 2 | 62203/97887 MiB | 49% | detach_ln_s3 |
| 3 | 62203/97887 MiB | 83% | cutoff_25k_s1_v2 |

**PID 状态：4 个 PID 全部存活**，运行时间均约 12h 58m。

**训练进度：尚未完成，均在 40k-50k 之间。**

| 实验 | 最新 checkpoint | 预计剩余 |
|------|----------------|----------|
| vanilla_v2_s1 | 40000 | 无日志，但进程活跃 |
| vanilla_v2_s2 | 40000 | 无日志，但进程活跃 |
| detach_ln_s3 | 40000 | 无日志，但进程活跃 |
| cutoff_25k_s1_v2 | 40000 | step 45622/50005，剩余 ~67min（1.08 it/s） |

**结论：Director 说的"4 张 GPU 空闲"是错误的。4 个训练任务都在正常运行中，预计还需 1-2 小时全部完成。**

---
