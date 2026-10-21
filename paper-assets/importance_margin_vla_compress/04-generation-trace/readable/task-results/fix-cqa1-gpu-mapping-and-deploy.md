# fix cqa1 gpu mapping and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_gpu_mapping_and_deploy_20260525T095647_result.json`
- **Structured JSON:** [`1c8cce246c473d0a2f18.json`](../../sessions/1c/1c8cce246c473d0a2f18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新实验 PID 252122 已确认加载到 **物理 GPU 1**（9743MiB），`CUDA_VISIBLE_DEVICES=1` 映射正确。

## 汇总

| PID | exp_id | `--gpu` 参数 | 预期 GPU | 实际 GPU | 状态 |
|-----|--------|-------------|---------|---------|------|
| 79848 | eval_pi05_random_k085_goal_seed42_postfix_v3 | 0 | GPU 0 | — | **已结束** |
| 213747 | eval_pi05_l2norm_k09_long_seed43_postfix | 1 | GPU 1 | **GPU 0** ❌ | 运行中（GPU 映射错误，但已跑很久不终止） |
| 80238 | eval_pi05_random_k085_long_seed42_postfix_v3 | 2 | GPU 2 | **GPU 2** ✅ | 运行中 |
| 80572 | eval_pi05_l2norm_k085_long_seed42_postfix_v3 | 3 | GPU 3 | **GPU 3** ✅ | 运行中 |
| **252122** | **eval_pi05_l2norm_k085_long_seed43_v3** | 0 (CVD=1) | **GPU 1** | **GPU 1** ✅ | **新部署，已确认** |

关键发现：
- GPU 2/3 的实验 `--gpu` 参数恰好与物理 GPU 编号一致，映射正确
- GPU 1 的实验（PID 213747）`--gpu 1` 却跑在 GPU 0，原因是未设 `CUDA_VISIBLE_DEVICES`，脚本内部 GPU 选择逻辑可能有问题
- 新实验通过 `CUDA_VISIBLE_DEVICES=1 --gpu 0` 已确认正确映射到物理 GPU 1

---
