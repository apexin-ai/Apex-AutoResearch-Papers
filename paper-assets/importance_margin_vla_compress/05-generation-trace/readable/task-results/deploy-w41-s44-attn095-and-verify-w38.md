# deploy w41 s44 attn095 and verify w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_w41-s44-attn095-and-verify-w38_20260527T220124_result.json`
- **Structured JSON:** [`edc2e4e94116d800211d.json`](../../sessions/ed/edc2e4e94116d800211d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载中，还未占满 GPU 显存（加载完成后才会显示在 nvidia-smi）。日志确认已正常启动。

## 汇报

### Task 1: w41 cuda:3 部署 Attn k=0.95 s44
- **已部署**，PID: **255172**
- 日志: `~/runs/importance_margin_vla_compress/eval_pi05_attn_k095_long_seed44_strict_w41.log`
- 模型加载中，日志输出正常（`suite=libero_10, prune=attention, keep=0.95`）

### Task 2: w38 cuda:0/1 实验状态
- **PID 672324** (Attn k=0.85 s44, cuda:0): 运行中，已跑 **15h24m**，状态 Rl+
- **PID 672401** (Random k=0.7 s44, cuda:1): 运行中，已跑 **15h22m**，状态 Rl+

---
