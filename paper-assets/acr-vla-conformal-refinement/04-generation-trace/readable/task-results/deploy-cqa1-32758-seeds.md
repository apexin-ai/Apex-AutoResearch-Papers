# deploy cqa1 32758 seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-32758-seeds_20260524T062601_result.json`
- **Structured JSON:** [`099aaff5e906ebe0dcb0.json`](../../sessions/09/099aaff5e906ebe0dcb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 GPUs deployed and running (each at ~6.5GB / 12-22% util):

## 部署结果

**关键发现**：原 task 列出的 4 个 spatial s45/s46 实验**已全部完成**（见 `eval_spatial_*seed45/seed46.json`）。registry 中也已记录 DONE。CoRL 5-seed 矩阵 (Spatial / Goal / Object) 基本完整，**剩余真正空缺只在 Long s46**——4 个原本 RUNNING 的实验在 bjb1-32546 死于 `python: command not found`（conda 未激活），从未产生 JSON。

**6 GPU 部署清单（全部 cqa1-32758，Long 套件）**：

| GPU | tmux session | Exp ID | mode | seed |
|-----|-----|------|------|------|
| 0 | long-adapt-s46-r2 | eval-supp-long-adapt-tau025-s46-r2 | adaptive_conformal_crm τ=0.25 | 46 |
| 1 | long-crm-s46-r2 | eval-supp-long-crm-norm005-s46-r2 | crm_obs_only norm=0.05 | 46 |
| 2 | long-reconvla-s46-r2 | eval-supp-long-reconvla-s46-r2 | reconvla K=10 | 46 |
| 3 | long-k2mean-s46-r2 | eval-supp-long-k2mean-s46-r2 | vla_only K=2 mean | 46 |
| 4 | long-adapt-s47 | eval-supp-long-adapt-tau025-s47 | adaptive_conformal_crm τ=0.25 | 47 (6-seed) |
| 5 | long-vla-s47 | eval-supp-long-vla-only-s47 | vla_only K=2 mean | 47 (6-seed) |

**Registry 状态**：4 个旧 RUNNING entries 已 conclusion=failed；6 个新 entries 已 PENDING→QUEUED→ALLOCATED→RUNNING（带完整 spec）。

**Step 4 (reconvla obj 收割)**：cuda:2/cuda:4 在我连入时已无 tmux session（任务在 ssh-disconnect 后或自然结束时清理掉了），registry 中 `eval-supp-reconvla-obj-s45/s46` 已是 DONE 状态。无需额外收割。

预计 5-6 小时全部完成（Long max_steps=520，每实验 ~10×20=200 rollouts）。

---
