# ops check cqa1 gpu2 xvla k095

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cqa1-gpu2-xvla-k095_20260520T202614_result.json`
- **Structured JSON:** [`30d279da45bdd9da3d58.json`](../../sessions/30/30d279da45bdd9da3d58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

- **进程 948547 已死**，无日志文件、无结果文件
- **服务器只有 2 块 GPU**（GPU 0 和 GPU 1），根本不存在 GPU 2——这就是崩溃原因
- 两块 GPU 当前均被占用：
  - GPU 0: PID 67609 — `eval_openvla_l2norm_libero.py k=0.7 seed43`（已运行 2h13m）
  - GPU 1: PID 921279 — `train_openvla_smart_compress.py`（已运行 9h39m）

**无法立即重启**：没有空闲 GPU。需要等 GPU 0 上的 eval 完成后才能在 GPU 0 上启动 X-VLA k=0.95 seed42 评估。重启时需将 `CUDA_VISIBLE_DEVICES=2` 改为 `CUDA_VISIBLE_DEVICES=0`。

是否要等 GPU 0 的任务结束后自动重启？

---
