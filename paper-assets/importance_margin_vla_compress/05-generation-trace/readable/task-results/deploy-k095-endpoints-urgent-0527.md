# deploy k095 endpoints urgent 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_k095_endpoints_urgent_0527_20260527T010559_result.json`
- **Structured JSON:** [`7b6c18a7021067cd99f0.json`](../../sessions/7b/7b6c18a7021067cd99f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部部署完成并已进入 RUNNING 状态。

## 部署汇总

| # | 实验 | 服务器 | GPU | PID | 状态 |
|---|------|--------|-----|-----|------|
| 1 | Goal Attn k=0.95 | westd-38929 | cuda:0 | 949253 | 运行中，已开始 Task 1/10 (256→243 tokens) |
| 2 | Goal Random k=0.95 | cqa1-33015 | cuda:3 | 876797 | 运行中，已开始 Task 1/10 |
| 3 | Long L2norm k=0.95 | westd-38929 | cuda:1 | 949447 | 运行中，已开始 Task 1/10 (256→243 tokens) |
| 4 | Long Attn k=0.95 | westd-38929 | cuda:3 | 950007 | 运行中，已开始 Task 1/10 (256→243 tokens) |

注：cqa1-33015 的 `eval_openvla_l2norm_libero.py` 有 GPU 选择 bug（`cuda:{args.gpu}` + `CUDA_VISIBLE_DEVICES` 冲突），已修复为始终用 `cuda:0` + 环境变量控制物理 GPU。

---
