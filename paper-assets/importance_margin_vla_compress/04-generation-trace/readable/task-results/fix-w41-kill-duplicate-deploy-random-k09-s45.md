# fix w41 kill duplicate deploy random k09 s45

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_w41_kill_duplicate_deploy_random_k09_s45_20260528T004601_result.json`
- **Structured JSON:** [`7f02a5ac1d8afb9ace5e.json`](../../sessions/7f/7f02a5ac1d8afb9ace5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志显示模型正在加载，但 nvidia-smi 还没显示 GPU 0 上的进程（模型加载阶段尚未分配 GPU 显存）。这是正常的——等模型加载完毕后会上 GPU。

完成：
- **已杀** w41:cuda:0 上的重复 l2norm k=0.95 s43（PID 383800），registry 已更新为 DONE/killed
- **已部署** `eval_pi05_random_k09_long_seed45_strict_w41` 在 w41:cuda:0，PID 453194，模型加载中正常启动

---
