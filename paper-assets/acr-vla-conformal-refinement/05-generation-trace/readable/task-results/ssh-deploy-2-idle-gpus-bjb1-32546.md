# ssh deploy 2 idle gpus bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-2-idle-gpus-bjb1-32546_20260517T102430_result.json`
- **Structured JSON:** [`edf43003839d7295191a.json`](../../sessions/ed/edf43003839d7295191a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 GPU 占用情况：

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 1942 MiB | 忙（PID 319128） |
| 1 | 5665 MiB | 忙（PID 414824, perdof norm=0.1 seed47，运行 ~3min） |
| 2 | 2 MiB | **空闲** |
| 3 | 1906 MiB | 忙（PID 322337） |
| 4 | 4736 MiB | 忙（PID 393646） |
| 5 | 1942 MiB | 忙（PID 319463） |

只有 cuda:2 空闲。cuda:1 正在跑实验。

两个选择：
1. 先在 cuda:2 部署一个实验，等 cuda:1 的任务跑完再部署另一个
2. 两个实验都部署在 cuda:2 上串行跑

怎么处理？

---
