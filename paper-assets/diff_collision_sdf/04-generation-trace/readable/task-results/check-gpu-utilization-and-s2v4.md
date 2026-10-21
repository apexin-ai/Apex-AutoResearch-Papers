# check gpu utilization and s2v4

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_utilization_and_s2v4_20260527T220456_result.json`
- **Structured JSON:** [`cbb4702d9527d234c78c.json`](../../sessions/cb/cbb4702d9527d234c78c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报

### westd-35807

| GPU | 利用率 | 显存 | 任务 | 进度 | ETA (UTC) |
|-----|--------|------|------|------|-----------|
| cuda:0 | **0%** | 0/96GB | 空闲，eval sentinel (PID 875618) 等待 cuda:3 完成 | — | eval 触发 ~06:20 |
| cuda:1 | 100% | 27/96GB | Phase2 Stage1 (seed0, λ=0.005, PID 856552) | **9646/10000** | **~06:35** (~28min) |
| cuda:2 | 100% | 27/96GB | s2_v4 (seed2, λ=0, PID 856471, --resume) | **15935/30000** | **~00:10 May 29** (~18h) |
| cuda:3 | 100% | 27/96GB | spatial_bowl baseline (seed0, PID 341425) | **29829/30000** | **~06:20** (~14min) |

自动化脚本：
- PID 872754 `auto_stage2_seed0.sh` — 等 cuda:1 Phase2 Stage1 完成后触发 Stage2
- PID 875618 `auto_eval_spatial_bowl_sentinel.sh` — 等 cuda:3 spatial_bowl 完成后在 cuda:0 触发 eval

### westd-45947

| GPU | 利用率 | 显存 | 任务 | 进度 | ETA (UTC) |
|-----|--------|------|------|------|-----------|
| cuda:0 | **0%** | 0/96GB | 空闲，eval sentinel (PID 553643) 等待 cuda:1 完成 | — | eval 触发 ~08:50 |
| cuda:1 | 100% | 27/96GB | λ=0.1 s2 (seed2, λ=0.1, PID 425058) | **27852/30000** | **~08:50** (~2h45m) |

lora_baseline_s2 已完成 (May 27 10:36 退出)。

---

### s2_v4 状态确认

- **正常运行**，PID 856471 存活，已运行 7h40m
- 当前 step 15935/30000 (53%)，从 checkpoint resume 后重新计数
- 最新 checkpoint: step 14000 (03:37 UTC)，step 12000 (01:01 UTC)
- 速度 ~4.64s/step，剩余 14065 steps → **~18h，ETA 00:10 UTC May 29**
- best_loss = 0.00651 @ step 4000

---

### 空闲 GPU 利用建议

**westd-35807:cuda:3** — spatial_bowl ~14min 后完成，cuda:3 释放且无后续任务。**最佳候选**，可跑新实验。

**westd-35807:cuda:0** — spatial_bowl eval 将在 ~06:20 自动触发，eval 耗时约 1-2h。eval 完成后 cuda:0 释放。**eval 前不建议跑任务**（只剩 ~14min）。

**westd-35807:cuda:1** — Phase2 Stage1 ~28min 后完成，`auto_stage2_seed0.sh` 会自动接 Stage2。**无需干预**。

**westd-45947:cuda:0** — eval sentinel 等 λ=0.1 完成 (~08:50)。虽有 ~2.5h 空窗，但如果训练提前完成 eval 会立刻启动。**建议不跑任务，保留给 eval，避免冲突风险**。

**总结**：近期可用 GPU 只有 **westd-35807:cuda:3**（~06:20 UTC 后释放）。如有合适的短/长实验可安排上去。

---
