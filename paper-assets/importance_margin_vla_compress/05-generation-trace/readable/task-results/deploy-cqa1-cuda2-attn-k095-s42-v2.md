# deploy cqa1 cuda2 attn k095 s42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_cuda2_attn_k095_s42_v2_20260528T004516_result.json`
- **Structured JSON:** [`4248b3270753c157b83b.json`](../../sessions/42/4248b3270753c157b83b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功。

- **exp_id**: `eval_pi05_attn_k095_long_seed42_strict_v2`
- **server**: cqa1-33015, GPU 2, PID 901260
- **状态**: 正在加载模型（Config 已打印：suite=libero_10, prune=attention, keep=0.95, eps=50）
- GPU 尚未在 nvidia-smi compute apps 中出现，模型正在 CPU 加载阶段，约 2 分钟后会上 GPU

前次崩溃原因（缺 offline flags 导致 httpx.ConnectError）已修复，本次命令包含完整 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`。

---
