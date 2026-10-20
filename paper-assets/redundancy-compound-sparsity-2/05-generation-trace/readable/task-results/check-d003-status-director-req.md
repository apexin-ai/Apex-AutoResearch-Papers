# check d003 status director req

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d003_status_director_req_20260512T153325_result.json`
- **Structured JSON:** [`634a1c7d89074c140c9d.json`](../../sessions/63/634a1c7d89074c140c9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D003 状态总结

### GPU
| GPU | 型号 | 显存 | 利用率 | 温度 |
|-----|------|------|--------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 32093 / 97887 MiB (33%) | 27% | 34°C |
| 1 | RTX PRO 6000 Blackwell (98GB) | 31763 / 97887 MiB (32%) | 52% | 45°C |

### 进程状态
两个实验都**在线运行中**，启动于 22:29，已运行 ~64 分钟。无 exit 文件，无结果 JSON。

### EXP1: d003_reasoning_traces (GPU 0, PID 28311)
- 已完成策略：`full`, `ema_0.7` (PPL=1.2706, 耗时 1178s)
- **当前**：`ema_0.5` prefill 阶段，**70% (33/47)**，每步 ~16.2s
- ema_0.5 prefill 剩余 ~3.8 min，之后还有 eval 阶段 (~7 min)

### EXP2: d003_wikitext_32k (GPU 1, PID 28390)
- 已完成策略：`full`, `ema_0.7`（以及更多——exp2 进度更快）
- **当前**：`ema_0.5` eval 阶段，**49% (3190/6554)**，~14.3 it/s
- ema_0.5 eval 剩余 ~3.9 min

### 预估完成时间
- 每个策略耗时约 20-25 分钟（prefill + eval）
- 已完成 2 个策略 + 第 3 个策略（ema_0.5）进行中
- 不确定总共有多少策略（可能还有 ema_0.3, ema_0.1 等）。如果共 5 个策略，预计还需 **~50-70 分钟**；如果共 7 个，则 **~90-120 分钟**

---
