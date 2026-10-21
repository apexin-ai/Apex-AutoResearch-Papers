# diagnose gpu utilization all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-utilization-all-servers_20260520T183116_result.json`
- **Structured JSON:** [`881e25485d3aa3ffca9a.json`](../../sessions/88/881e25485d3aa3ffca9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-40593

| GPU | 利用率 | 显存 | PID | 状态 | 说明 |
|-----|--------|------|-----|------|------|
| 0 | 0% | 0 / 24564 MiB | — | **空闲** | 无任何 GPU 进程 |

仅有 tensorboard、jupyter-lab、http.server 等后台服务，无 tmux，无 eval/train 进程。**完全空闲，可部署。**

---

## bjb1-18228（4 GPU）

| GPU | 利用率 | 显存 | PID | 状态 | 说明 |
|-----|--------|------|-----|------|------|
| 0 | 27% | 2563 / 24564 MiB | 477008 | 正常运行 | `random_selection` spatial seed42 K=10 norm0.2 |
| 1 | 0% | 1 / 24564 MiB | — | **空闲** | 无进程占用 |
| 2 | 37% | 3408 / 24564 MiB | 477286 | 正常运行 | `crm_obs_only` object seed44 norm0.05 |
| 3 | 37% | 3408 / 24564 MiB | 477496 | 正常运行 | `crm_obs_only` object seed44 norm0.03 |

3 个 eval 进程均从 01:31 启动，已运行约 ~4h，CPU 367-379%，状态 `Rl+`（活跃）。**GPU 1 完全空闲，可部署。**

---

## bjb1-32546（6 GPU）

| GPU | 利用率 | 显存 | PID | 状态 | 说明 |
|-----|--------|------|-----|------|------|
| 0 | 34% | 3132 / 24564 MiB | 542128 | 正常运行 | `crm_obs_only` spatial seed50 norm0.2 |
| 1 | 29% | 3406 / 24564 MiB | 542405 | 正常运行 | `crm_perdof` object seed50 norm0.2 |
| 2 | 26% | 2900 / 24564 MiB | 534993 | 正常运行 | `crm_obs_only` object seed44 K=5 norm0.2 |
| 3 | 19% | 3308 / 24564 MiB | 542620 | 正常运行 | `vla_only` object seed49 K=1 |
| 4 | 35% | 3409 / 24564 MiB | 542894 | 正常运行 | `crm_obs_only` object seed51 norm0.2 |
| 5 | 42% | 3060 / 24564 MiB | 535074 | 正常运行 | `crm_obs_only` object seed44 K=20 norm0.2 |

6 个 GPU 全部满载 eval 任务，从 01:20-01:32 启动，已运行 ~4h。**无空闲 GPU。**

---

## 总结

| 类别 | GPU |
|------|-----|
| **完全空闲（可部署）** | bjb2-40593 GPU 0、bjb1-18228 GPU 1 |
| **低利用率但正常（eval 在跑）** | bjb1-18228 GPU 0/2/3、bjb1-32546 全部 6 GPU — 利用率 19-42% 是 LIBERO rollout 间 env.reset() 的正常表现 |
| **stuck 进程** | 无 |

---
