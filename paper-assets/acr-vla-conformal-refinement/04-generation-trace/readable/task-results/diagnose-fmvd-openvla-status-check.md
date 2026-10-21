# diagnose fmvd openvla status check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_fmvd-openvla-status-check_20260519T181308_result.json`
- **Structured JSON:** [`59b4a44887bdaad98752.json`](../../sessions/59/59b4a44887bdaad98752.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实验状态汇报

### 任务 1: FMVD Phase 1 (cuda:5)

**状态: ALIVE** — PID 901444, CPU 377%, GPU 5 占用 2911 MiB

**进度: 6/10 tasks 完成 (30/50 episodes)**，正在跑第 7 个 task。每 episode ~140s。

已完成 tasks:

| Task | 成功率 | 备注 |
|------|--------|------|
| pick_up_the_alphabet_soup | 0/5 | 全 FAIL |
| pick_up_the_cream_cheese | 0/5 | 全 FAIL |
| pick_up_the_salad_dressing | 1/5 | ep4 OK (137 steps) |
| pick_up_the_bbq_sauce | 0/5 | 全 FAIL |
| pick_up_the_ketchup | 0/5 | 全 FAIL |
| pick_up_the_tomato_sauce | 1/5 | ep4 OK (120 steps) |

**JSON 尚未生成**（脚本完成后才写入）。预计剩余 ~47 分钟（4 tasks × 5 eps × ~140s）。

注意：当前整体 SR 只有 2/30 = 6.7%，这是 SmolVLA 在 object benchmark 上的 FMVD baseline 数据。Spearman rho 要等全部跑完才能算。

---

### 任务 2: OpenVLA eval (cuda:4)

**状态: ALIVE** — PID 900134, GPU 4 占用 23006/24564 MiB

**进度: Task 1 完成，Task 2 进行中 (25/50 trials)**

- **Task 1** (pick_up_the_alphabet_soup): **SR = 80%** (40/50 success)
- **Task 2**: 50% done (25/50 trials)，~60s/trial

**整体进度**: 75/500 trials = **15%**。预计剩余 ~7 小时（425 trials × ~60s）。

---

### 服务器上还有其他活跃 tmux sessions:
- `eval-argmin-object-k5-seed44-r2`
- `eval-obs-only-spatial-norm02-seed46-r2`
- `eval-vla-only-goal-seed44-r2`
- `eval-vla-only-goal-seed45`

---
