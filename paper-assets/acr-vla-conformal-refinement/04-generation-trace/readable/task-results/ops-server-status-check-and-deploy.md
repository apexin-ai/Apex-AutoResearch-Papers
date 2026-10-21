# ops server status check and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-status-check-and-deploy_20260516T070931_result.json`
- **Structured JSON:** [`c40bc4b0b4e146879df0.json`](../../sessions/c4/c40bc4b0b4e146879df0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态

**bjb1-18228** (4× 4090) — 全部在跑，无空闲:
| GPU | 实验 | PID | 状态 | 运行时间 | GPU Util | VRAM |
|-----|------|-----|------|----------|----------|------|
| cuda:0 | eval-acr-object-v4-default-r2 | 390936 | alive (Rl+) | 12:58:39 | 20% | 1941/24564 MiB |
| cuda:1 | eval-perdof-object-seed44 | 452982 | alive (Ss+) | 02:12:53 | 16% | 5200/24564 MiB |
| cuda:2 | eval-obs-only-object-norm02-seed44-r2 | 428406 | alive (Ss+) | 05:37:12 | 22% | 3804/24564 MiB |
| cuda:3 | eval-argmin-object-seed44-r2 | 428117 | alive (Ss+) | 05:37:20 | 20% | 4233/24564 MiB |

**bjb1-32546** (6× 4090) — cuda:0/4/5 空闲:
| GPU | 实验 | PID | 状态 | 运行时间 | GPU Util | VRAM |
|-----|------|-----|------|----------|----------|------|
| cuda:0 | — | — | **空闲** | — | 0% | 2 MiB |
| cuda:1 | eval-vla-mean-object-seed44 | 212655 | alive (Ss+) | 02:11:10 | 25% | 5165/24564 MiB |
| cuda:2 | eval-obs-only-object-norm03-seed44 | 220777 | alive (Ss+) | 01:03:50 | 19% | 5665/24564 MiB |
| cuda:3 | eval-obs-only-object-norm02-seed43-r2 | 148788 | alive (Ss+) | 12:11:33 | 22% | 1942/24564 MiB |
| cuda:4 | — | — | **空闲** | — | 0% | 2 MiB |
| cuda:5 | — | — | **空闲** | — | 0% | 2 MiB |

**bjb2-28827** (6× 4090) — 全部在跑，无空闲:
| GPU | 实验 | PID | 状态 | 运行时间 | GPU Util | VRAM |
|-----|------|-----|------|----------|----------|------|
| cuda:0 | eval-mag-perdof-norm003-object | 105938 | alive (Ss+) | 14:22:20 | 18% | 1942 MiB |
| cuda:1 | eval-mag-perdof-norm005-object | 109650 | alive (S) | 14:11:31 | 18% | 1942 MiB |
| cuda:2 | eval-mag-perdof-norm03-object-r3 | 140759 | alive (Rl+) | 11:44:56 | 19% | 2411 MiB |
| cuda:3 | eval-mag-perdof-norm02-seed43-object-r3 | 144504 | alive (Ss+) | 11:35:21 | 19% | 2411 MiB |
| cuda:4 | eval-mag-obsonly-norm005-object | 101610 | alive (S) | 14:40:06 | 17% | 1942 MiB |
| cuda:5 | eval-mag-obsonly-norm03-object | 103028 | alive (S) | 14:39:35 | 18% | 1942 MiB |

**bjb2-40593** (1× 4090 D):
| GPU | 实验 | PID | 状态 | GPU Util | VRAM |
|-----|------|-----|------|----------|------|
| cuda:0 | eval-vla-only-object-seed44-r2 | 286989 | **已完成 (EXIT_CODE=0)** | 12% | 5628 MiB |

## 空闲 GPU

- **bjb1-32546: cuda:0, cuda:4, cuda:5** — 确认空闲 (0% util, 2 MiB VRAM)
- **bjb2-40593: cuda:0** — 进程已完成，但残留 5628 MiB 显存（可能需 kill 残留进程释放）

Director 猜测的 bjb1-18228:cuda:1 和 bjb1-32546:cuda:1 实际都在跑（16%/25% util）。

## 部署结果

两个实验部署到 **bjb1-32546** 空闲 GPU：

| 实验 | GPU | PID | 服务器 |
|------|-----|-----|--------|
| eval-scalar-object-seed44-r2 | cuda:0 | 226869 | bjb1-32546 |
| eval-obs-only-object-norm01-seed44 | cuda:4 | 227077 | bjb1-32546 |

前次 scalar-seed44 在 bjb2-40593 的日志无 traceback/error（17行，正常执行到 rollout 5/10 后进程消失），推测被 OOM kill 或外部终止，非代码 bug。bjb1-32546 上 checkpoint 存在，正常部署。

## 异常

- **bjb2-40593**: eval-vla-only-object-seed44-r2 已完成 (EXIT_CODE=0, 05:58 UTC)，但 GPU 仍占 5628 MiB 显存 + 12% util，可能有子进程未退出
- **bjb1-18228:cuda:0** (pid=390936): 运行近 13 小时，实际命令是 `crm_perdof --seed 42`（不是 acr-default），注册名可能有误

---
