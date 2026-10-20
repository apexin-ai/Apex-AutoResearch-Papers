# ops 34685 gpu check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-gpu-check_20260526T192918_result.json`
- **Structured JSON:** [`7e2b87588faf8919fc03.json`](../../sessions/7e/7e2b87588faf8919fc03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 is actually at 99% now — the initial 0% was a momentary snapshot. Here's the full summary:

## westd-34685 状态汇报

### GPU 使用情况
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 37%→99%* | 62231/97887 MiB | **占用中** |
| cuda:1 | 0%→99%* | 62231/97887 MiB | **占用中** |
| cuda:2 | 99% | 62203/97887 MiB | **占用中** |
| cuda:3 | 99% | 62203/97887 MiB | **占用中** |

*初始查询抓到瞬时低谷，nvidia-smi 二次确认 GPU 1 实际 99%

### 进程状态
| 实验 | PID | 状态 | 运行时间 | GPU |
|------|-----|------|----------|-----|
| vanilla_v2_s1 | 419107 | **存活** | 10h44m | cuda:0 |
| vanilla_v2_s2 | 419342 | **存活** | 10h44m | cuda:1 |
| detach_ln_s3 | 419641 | **存活** | 10h44m | cuda:2 |
| cutoff_25k_s1_v2 | 453581 | **存活** | 10h20m | cuda:3 |

### 训练进度
- **cutoff_25k_s1_v2**（唯一有日志的）: step **37367/50005 (75%)**, ~1.08 it/s, ETA ~3h15m（约 UTC 06:45 完成）
- **其他 3 个实验**: 无 agent-ml 日志、无 wandb 目录。但启动时间比 cutoff 早 ~23 分钟，速度相近，估算进度约 **~38800/50005 (78%)**，ETA 约 UTC 06:20 完成
- 所有实验已保存 20000 和 30000 checkpoint

### 结论
**4 张 GPU 全部被占用，所有训练正在正常运行。** Director 说的"4 张空闲 GPU"与实际情况不符。预计全部训练在 May 27 07:00 UTC 前完成，远在 C003 deadline (May 28 12:00 UTC) 之前。

---
