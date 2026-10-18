# deploy westd38929 cliff zone batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_cliff_zone_batch_20260525T143531_result.json`
- **Structured JSON:** [`68fda812d79afc71a64f.json`](../../sessions/68/68fda812d79afc71a64f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部部署成功，正在运行中。

**部署总结：**

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | `eval_openvla_attn_k07_long_seed42` (Attn k=0.7) | 214259 | RUNNING |
| 1 | `eval_openvla_l2norm_k07_long_seed42` (L2norm k=0.7) | 214794 | RUNNING |
| 2 | `eval_openvla_random_k07_long_seed42` (Random k=0.7) | 215328 | RUNNING |
| 3 | `eval_openvla_l2norm_k085_long_seed42` (L2norm k=0.85) | 215964 | RUNNING |

**修正了原始命令的两个问题：**
1. `--gpu 0` 参数不被脚本支持，已去掉（`CUDA_VISIBLE_DEVICES` 足够）
2. `--unnorm_key libero_10_no_noops` → `libero_10`（模型 norm_stats 中只有 `libero_10`）

日志路径：`/tmp/eval_openvla_&lt;method>_&lt;k>_long_seed42.log`，每张 GPU 占用 ~16GB。

---
