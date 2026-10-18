# fix cqa1 gpu mapping and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_gpu_mapping_and_deploy_20260525T101621_result.json`
- **Structured JSON:** [`3e0fa7c92f13d39e13ac.json`](../../sessions/3e/3e0fa7c92f13d39e13ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，GPU 记录从 cuda:1 修正为 cuda:0。

**总结：**
- PID 213747 的 GPU 映射 bug 确认：未设 CUDA_VISIBLE_DEVICES，`--gpu 1` 无效，实际在 GPU 0 运行。Registry 已修正。
- 优先级 1 实验 (`eval_pi05_l2norm_k085_long_seed43_v3`) 已在 GPU 1 上正确运行 (PID 252122)。
- **4 个 GPU 全满，无法部署 `eval_pi05_random_k03_long_seed43_v4`。** 需等某个实验完成后再部署。

---
