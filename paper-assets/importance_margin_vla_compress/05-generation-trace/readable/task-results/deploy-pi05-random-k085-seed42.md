# deploy pi05 random k085 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-random-k085-seed42_20260521T200058_result.json`
- **Structured JSON:** [`7ce53bce05ed6e2c01b5.json`](../../sessions/7c/7ce53bce05ed6e2c01b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **Bug 修复**: 已删除 `eval_pi05_pruning_libero.py` 第 82 行的 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)`，grep 确认文件中不再有该行。GPU0 上的 k=0.95 和 fixed-mask 进程未受影响。

2. **k=0.85 已部署**: PID 626630，westd-41074 GPU1，tmux session `eval_pi05_random_k085_object_seed42`。GPU1 当前 3MiB（模型加载中）。

3. **Registry 已更新**: `eval_pi05_random_k085_object_seed42` → RUNNING，spec 含 server/gpu_id/pid/seed/checkpoint_source 等完整 provenance。

---
