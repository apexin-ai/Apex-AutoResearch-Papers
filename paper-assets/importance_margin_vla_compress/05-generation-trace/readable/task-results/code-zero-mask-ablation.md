# code zero mask ablation

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_zero_mask_ablation_20260525T120536_result.json`
- **Structured JSON:** [`3e366b7b893d7f01656b.json`](../../sessions/3e/3e366b7b893d7f01656b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在可用工具列表中。脚本已写好：

**文件**: `artifacts/eval_pi05_zeromask_ablation.py`

**新增的两种 prune_mode**:
- `zero_mask_random` — 随机选 k 个 token 保留，其余值置零，序列长度不变
- `zero_mask_l2norm` — 按 L2 norm 选 top-k 保留，其余值置零，序列长度不变

**关键区别**：原有 pruning 函数返回 `(pruned_emb, n_keep)` 其中 shape 变小；zero-mask 函数返回 `(masked_emb, n_tokens)` 其中 shape 不变，低重要性 token 的值被设为 0.0。`pruned_embed_prefix` monkey-patch 统一处理两种情况——返回的 `n_out` 决定了 pad_masks 和 att_masks 的长度。

**运行示例**:
```bash
# zero-mask ablation
python eval_pi05_zeromask_ablation.py --prune_mode zero_mask_random --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 42

# 对照组（physical pruning，复现已有数据）
python eval_pi05_zeromask_ablation.py --prune_mode random --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 42
```

脚本同时支持所有 5 种模式（none/random/l2norm/zero_mask_random/zero_mask_l2norm），输出 JSON 中增加了 `is_zeromask` 和 `ablation` 字段以区分实验类型。

---
