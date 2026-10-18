# fix cqa1 restart random095 s44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-restart-random095-s44_20260527T224618_result.json`
- **Structured JSON:** [`49974800d1204adf56f1.json`](../../sessions/49/49974800d1204adf56f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型仍在 CPU 上加载中（π0.5 较大，加载到 GPU 前需要先读取全部权重到 CPU，通常需 10-15 分钟）。进程 PID 801342 CPU 占用 99%，加载正常。

**部署完成：**
- 服务器: cqa1-33015, cuda:3 (CUDA_VISIBLE_DEVICES=3)
- 新 PID: **801342**（python 主进程），801340（wrapper bash）
- 日志: `~/runs/importance_margin_vla_compress/eval_pi05_random_k095_long_seed44_strict_cqa1.log`
- 状态: 模型权重加载中，预计几分钟后开始推理并占用 GPU 显存

---
