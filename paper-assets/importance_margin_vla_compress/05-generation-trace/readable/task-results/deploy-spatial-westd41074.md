# deploy spatial westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_spatial_westd41074_20260522T015613_result.json`
- **Structured JSON:** [`1cb38a18e2395ca68e5f.json`](../../sessions/1c/1cb38a18e2395ca68e5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在运行。部署完成，汇总：

**westd-41074 GPU 状态：**
| GPU | 占用 | 实验 |
|-----|------|------|
| 0 | 10572 MiB, 34% | `eval_pi05_random_k07_spatial_seed42` (PID 914366, k=0.7, 179/256 tokens) |
| 1 | 10630 MiB, 23% | `eval_pi05_random_k095_spatial_seed42` (PID 910636, k=0.95, 243/256 tokens) |
| 2 | 28555 MiB | VTC 训练（不动） |
| 3 | 27535 MiB | VTC 训练（不动） |

**已完成实验：**
- `eval_pi05_l2norm_k085_object_seed42_v4`: **SR=98.0%** (490/500) — registry 已更新为 DONE

**新部署：**
- 实验 1 (GPU 1): π0.5 random k=0.95 Spatial — 已在 T0 ep=10, 100%
- 实验 2 (GPU 0): π0.5 random k=0.7 Spatial — 模型已加载，开始 eval

预计每个实验 ~60-120 min 完成。

---
