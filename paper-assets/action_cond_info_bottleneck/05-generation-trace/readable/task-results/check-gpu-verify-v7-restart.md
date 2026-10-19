# check gpu verify v7 restart

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-verify-v7-restart_20260516T114840_result.json`
- **Structured JSON:** [`ad970133c7a8fb719cdd.json`](../../sessions/ad/ad970133c7a8fb719cdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v7 已开始训练，step 100 在跑了。汇总：

**v7 (acib_v7_contrastive) — 正在训练**
- PID 959184/959189 存活，运行 1m13s
- GPU 1: 16.2GB 显存，87% 利用率，460W
- 日志已到 step 100/20000，loss=1.2258，1.7 steps/s

**v6 (acib_v6_conditioned) — 已完成**
- PID 866194 已退出，exit code 0
- 20000 步训练完成，耗时 4.3h（完成于 2026-05-16T10:59:27Z）
- checkpoint-20000/checkpoint.pt 存在

**GPU 状态**
| GPU | 显存 | 利用率 | 温度 |
|-----|------|--------|------|
| GPU 0 | 0MB / 98GB | 0% | 33°C |
| GPU 1 | 16.2GB / 98GB | 87% | 60°C |

GPU 0 空闲，可用于其他任务。

---
