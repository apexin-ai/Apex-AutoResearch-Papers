# deploy cqa1 gpu01 director final 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu01_director_final_0527_20260526T234613_result.json`
- **Structured JSON:** [`0211ee44854ac3ab8f10.json`](../../sessions/02/0211ee44854ac3ab8f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 实验正常运行，已开始 Task 1/10。

## 部署结果

| GPU | 实验 | 状态 |
|-----|------|------|
| **GPU 0** | OpenVLA Goal Random k=0.5 | **已有结果，无需重跑**。Registry 显示 `eval_openvla_random_k05_goal_seed42` 已完成：**overall_sr = 52.2%** (261/500)，在 westd-27271 上运行成功 |
| **GPU 1** | OpenVLA Object Attn k=0.95 | **已启动** — PID 832020, 14.9GB VRAM, 正在评估 Task 1/10 |

**GPU 0 说明**: `eval_openvla_random_k05_goal_seed42` 在 registry 中已是 DONE/success 状态，有完整的 per-task SR 数据。Goal Random 曲线数据点：k=0.9→79.6%, k=0.85→78.6%, k=0.7→68.4%, **k=0.5→52.2%**。如果 Director 仍需要在 cqa1-33015 上重跑验证，请确认，我立即部署。

---
