# check openvla precompute completion

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_openvla-precompute-completion_20260520T183144_result.json`
- **Structured JSON:** [`c278fa5a471e045f95ea.json`](../../sessions/c2/c278fa5a471e045f95ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. Precompute 状态：**已完成**
- 进程 365151 已退出
- 文件数：74,508（含 manifest.json + 74,507 个 sample .pt 文件）
- 总大小：6.0G

### 2. OpenVLA obs feature 维度

| 字段 | Shape | dtype |
|------|-------|-------|
| `multi_scale_obs` | `(4, 4096)` | float32 |
| `obs_features` | `(4096,)` | float32 |
| `vla_action` | `(6,)` | float32 |
| `expert_action` | `(6,)` | float32 |
| `task_name` | str | - |

Manifest 确认：`obs_dim=4096`, `action_dim=6`, 4 层 multi-scale（layers 7/15/23/31），backbone=openvla。

### 3. CRM 代码兼容性

**需要调整 `--obs_dim`。** `crm_k1_model.py` 默认 `obs_dim=960`（SmolVLA），OpenVLA 的 hidden size 是 4096。训练命令需要显式传 `--obs_dim 4096`。

`train_crm.py` 已有 `--obs_dim` 参数，无需改代码。建议训练命令：

```bash
/root/miniconda3/bin/python3 /root/acr-vla-conformal-refinement/src/train_crm.py \
  --benchmark object \
  --cache_dir /root/autodl-tmp/crm_cache_k1_openvla/object \
  --K 1 \
  --obs_dim 4096 \
  --epochs 30 \
  --batch_size 256
```

---
