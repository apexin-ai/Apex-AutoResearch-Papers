# ops deploy cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_cqa1_20260522T041545_result.json`
- **Structured JSON:** [`da5c7108484247470e4f.json`](../../sessions/da/da5c7108484247470e4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常，模型正在加载中，无 Error。

## 汇报

**环境状态**：cqa1-33015 — 4x RTX 4090 D 24GB, Python 3.12.3, torch 2.8.0+cu128, CUDA OK。修复了 lerobot groot dataclass 兼容问题（patch `__init__.py`）。

**4 个实验部署结果**：

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | `eval_pi05_random_k0925_spatial_seed43` | 5786 | 运行中，加载模型 |
| 1 | `eval_pi05_random_k09_spatial_seed43` | 5866 | 运行中，加载模型 |
| 2 | `eval_pi05_l2norm_k095_spatial_seed43` | 5943 | 运行中，加载模型 |
| 3 | `eval_pi05_l2norm_k09_spatial_seed43` | 6087 | 运行中，加载模型 |

全部进程存活，日志无 Error，模型从 `/root/autodl-tmp/pi05_libero_finetuned` 离线加载中。

---
