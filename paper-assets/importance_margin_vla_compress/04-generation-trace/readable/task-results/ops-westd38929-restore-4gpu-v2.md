# ops westd38929 restore 4gpu v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-restore-4gpu-v2_20260521T072333_result.json`
- **Structured JSON:** [`f87ebee7aeba76d35387.json`](../../sessions/f8/f87ebee7aeba76d35387.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。4 个实验全部在 westd-38929 上运行：

| GPU | exp_id | mode | k_ratio | PID | VRAM |
|-----|--------|------|---------|-----|------|
| 0 | `eval_openvla_l2norm_k07_object_seed42_v2` | l2norm_prune | 0.7 | 1945 | 15.6GB |
| 1 | `eval_openvla_random_k03_object_seed42_v2` | random_prune | 0.3 | 2478 | 15.7GB |
| 2 | `eval_openvla_random_k07_object_seed42` | random_prune | 0.7 | 3110 | 15.6GB |
| 3 | `eval_openvla_l2norm_k05_object_seed42_v2` | l2norm_prune | 0.5 | 3825 | 15.6GB |

注意：任务指令中 `--mode` 参数有误（`l2norm`/`random`），实际脚本接受 `l2norm_prune`/`random_prune`，已修正。`--device` 参数脚本不支持，已移除。所有实验已注册 RUNNING 状态。

---
