# diagnose kv importance direction

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_kv-importance-direction_20260514T010837_result.json`
- **Structured JSON:** [`f5fbbbe84e192347b64a.json`](../../sessions/f5/f5fbbbe84e192347b64a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整报告。

---

## 代码审查

### `_select_kv_to_evict()` 逻辑 (interaction_index.py)

```python
candidates = importance[1:]              # 排除 BOS
_, indices = candidates.topk(num_to_evict, largest=False)  # 选最小值
indices = indices + 1
mask[indices] = 0.0                      # 驱逐
```

`largest=False` → 选择 importance 值最小的位置驱逐。

### `kv_importance` 计算方式 (interaction_index.py, `compute_dense_forward_with_importance`)

```python
kv_importance = torch.zeros(seq_len)
for l in range(num_layers):
    attn_f = attentions[l][0].float()               # (num_heads, seq, seq)
    head_importance[l] = attn_f.norm(dim=(-2, -1))   # Frobenius norm per head
    kv_importance += attn_f.sum(dim=(0, 1))           # sum over heads + query positions
```

`kv_importance[k]` = 所有层、所有 head、所有 query 对 key position k 的 attention 之和。**高值 = 被广泛关注 = 重要。**

## 排序方向判断

`topk(largest=False)` 选最小值驱逐 → **排序方向本身是正确的**。高 importance = 重要 = 保留，低 importance = 不重要 = 驱逐。固定 NaN 后验证：
- 被驱逐位置 importance 均值: **194.02**
- 被保留位置 importance 均值: **764.77**
- 确实在驱逐 importance 更低的位置 ✓

## 是否存在 invert bug

**不存在排序方向反转。** 但存在更严重的问题：

## 🚨 真正的 Bug：Layer 27 NaN 中毒

**Layer 27（最后一层）的 attention weights 在 float16 下全是 NaN。**

诊断数据：
```
NaN layers: [27]
Buggy kv_importance NaN count: 160/160   ← 所有位置全是 NaN
Fixed kv_importance NaN count: 0/160     ← 跳过 layer 27 后正常
```

**因果链：**
1. `attentions[27]` 在 float16 下包含 NaN（最后一层数值不稳定）
2. `kv_importance += NaN_tensor` → 整个 accumulator 变 NaN
3. `topk(largest=False)` 在全 NaN 输入上行为未定义，产生伪随机偏差选择
4. NaN topk 结果系统性偏向 Q3 区域（buggy: Q1=0, Q2=0, Q3=39, Q4=9），导致集中驱逐后半段 context
5. 这比 random eviction（均匀分布）更具破坏性

对比：

| | importance (buggy) s=0.3 | random s=0.3 |
|---|---|---|
| high_sparsity kv_ppl | **408.98** | **6.77** |
| mid_sparsity kv_ppl | **604.37** | (similar scale) |

## Sanity check 数据

### 修复后 kv_importance 分布（跳过 NaN 层）
```
Q1 [0:40]  mean=1989.39   ← 早期位置 importance 高（positional bias）
Q2 [40:80] mean=433.39
Q3 [80:120] mean=393.18
Q4 [120:160] mean=208.05  ← 后期位置 importance 低
```

### 修复后 eviction 分布 (s=0.3)
```
Q1: 0, Q2: 8, Q3: 11, Q4: 29   ← 仍然偏向后期，但至少是基于真实 importance
Evicted importance: 194.02
Kept importance:    764.77
```

### Buggy eviction 分布 (NaN topk)
```
Q1: 0, Q2: 0, Q3: 39, Q4: 9   ← 完全集中在 Q3，无信息量
```

## 结论

**(a) 排序方向正确。** `largest=False` 驱逐最小值，符合"高 importance = 重要 = 保留"的语义。

**(b) cumulative_attention_received 作为 importance proxy 有局限。** 存在强 positional bias（早期位置天然累积更多 attention），修复 NaN 后仍会倾向驱逐近期 token。但这是 metric 选择问题，不是 bug。

**(c) 存在 NaN 中毒 bug（Layer 27）。** 这是导致 importance-based 比 random 差 26-60 倍的**根本原因**。修复方案：

```python
# compute_dense_forward_with_importance 中的循环改为：
for l in range(num_layers):
    attn_f = attentions[l][0].float()
    if torch.isnan(attn_f).any():
        continue
    head_importance[l] = attn_f.norm(dim=(-2, -1)).cpu()
    kv_importance += attn_f.sum(dim=(0, 1)).cpu()
    del attn_f
```

---
