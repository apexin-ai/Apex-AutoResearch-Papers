# code fix eval pipeline d075

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_eval_pipeline_d075_20260519T135241_result.json`
- **Structured JSON:** [`7ada44a3c440b0b29891.json`](../../sessions/7a/7ada44a3c440b0b29891.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 1. 代码 Diff

**文件**: `src/lm_eval_sparse_uniform.py`（两台服务器均已修改）

**Bug**: `teal_masks()` 中 score 计算使用 `mag * hard_mask`，当 `hard_mask=0` 时 score 退化为 0，导致 top-k 无法正确排序神经元。

**修复**:
```diff
-                hard_mask = (logits > 0).float()
-                mag = intermediates[layer_idx].abs().float()
-                scores = (mag * hard_mask).mean(dim=(0, 1))
+                scores = torch.sigmoid(logits).mean(dim=(0, 1))
```

**新增 sanity check** (in `_uniform_topk_masks`):
```python
        actual_sparsity = 1 - masks[li].float().mean()
        assert abs(actual_sparsity - sparsity_target) < 0.02, f"Layer {li}: sparsity {actual_sparsity:.3f} deviates from target {sparsity_target:.3f}"
```

### 2. 服务器状态
- westd-34887: ✅ 已更新
- westd-41718: ✅ 已更新

### 3. Dry-run 结果 (Qwen-14B, 48 层, target=0.301)

所有 48 层 sparsity 范围 **0.2896 ~ 0.3011**，全部在 ±0.02 容差内。Model-level sparsity = **0.2975**。无任何 FAIL 层。

### 4. 结论

修复成功，可以开始重跑 3 seed eval。sigmoid(logits) 作为 score 保留了 predictor 对每个 neuron 的连续重要性估计，per-layer top-k 能正确工作。

---
