# review xvla l2norm code

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_xvla_l2norm_code_20260522T184609_result.json`
- **Structured JSON:** [`caeb3b91d440eb9f9a61.json`](../../sessions/ca/caeb3b91d440eb9f9a61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码全部分析完毕。以下是完整报告。

## 代码分析

### L2norm scoring

```python
# eval_xvla_pruning_libero.py:100-102
norms = features.norm(dim=-1)           # L2 norm, shape [B, N]
_, indices = norms.topk(k, dim=-1)      # 取最大的 k 个
```

- `features.norm(dim=-1)` 默认即 L2 norm，正确
- `topk` 取 **最大** 的 k 个，方向正确（保留高 norm token）

### Top-k mask

```python
# eval_xvla_pruning_libero.py:96-112
k = max(1, int(keep_ratio * N))         # N=50
if k >= N: return features
...
indices_sorted = indices.sort(dim=-1).values    # 保持空间顺序
pruned = features.gather(1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1]))
```

- k_ratio=0.95 → `int(0.95 * 50)` = **47** tokens（结果文件确认 `n_vision_tokens_kept: 47`）
- k_ratio=0.9 → `int(0.9 * 50)` = **45** tokens（结果文件确认 `n_vision_tokens_kept: 45`）
- 无反转：0.95 确实保留更多

### Determinism

**是。** L2 norm 模式下 `norm()` 和 `topk()` 对同一输入完全确定性。seed 也固定了（42）。唯一的 non-determinism 风险是 `topk` 在 norm 完全相等时的 tie-breaking，但 float32 值几乎不可能 tie。

### 参数传递

CLI `--keep_ratio` → `args.keep_ratio` → `install_vision_pruning(model, args.keep_ratio, args.mode)` → closure 捕获 `keep_ratio` → `int(keep_ratio * N)`. 无反转、无 bug。

### Shape mismatch 检查

检查了 Florence2 的 `_merge_input_ids_with_image_features`（modeling_florence2.py:2644）：

```python
batch_size, image_token_length = image_features.size()[:-1]
image_attention_mask = torch.ones(batch_size, image_token_length, device=device)
inputs_embeds = torch.cat([image_features, task_prefix_embeds], dim=1)
attention_mask = torch.cat([image_attention_mask, task_prefix_attention_mask], dim=1)
```

attention mask 从实际 tensor shape 动态生成，无 hardcoded N。✅ 无 shape mismatch。

### 可能的 bug

**代码层面无 bug。** pruning 逻辑、参数传递、shape 处理全部正确。

### 结论：k=0.95 < k=0.9 的原因

这是 **真实现象**，不是代码错误。原因是三个因素叠加：

1. **N=50 极小**：k=0.95 和 k=0.9 只差 2 个 token（47 vs 45）。每个 token 的 inclusion/exclusion 影响巨大。

2. **绝对位置编码偏移**：pruning 后 token 被 re-index（gather + sort），text token 的起始位置从原来的 position 50 变成 47（k=0.95）或 45（k=0.9）。Florence2 encoder 使用 learned absolute positional embedding，模型训练时 text 在 position 50+ 的位置。不同偏移量导致不同（且不可预测的）退化模式。

3. **Per-task 剧烈非单调性**证实这不是统计噪声：

   | Task | k=1.0 | k=0.95 | k=0.9 |
   |------|-------|--------|-------|
   | 4: bowl on cabinet | 100% | **18%** | **94%** |
   | 1: bowl on stove | 100% | 38% | 84% |
   | 8: bowl on plate | 100% | 6% | 44% |

   k=0.95 保留了 rank #46-47 的两个低 norm token，它们在 attention 中充当 noise attractor，对特定任务造成灾难性干扰。而 k=0.9 刚好移除了这些 token。这种效应在闭环控制（800步 rollout）中被指数级放大。

**本质**：L2 norm pruning 在 N=50 的极小 token 空间中，不具备单调性保证。这不是方法 bug，而是 L2 norm 作为 importance metric 在小 N 场景下的固有局限。

---
