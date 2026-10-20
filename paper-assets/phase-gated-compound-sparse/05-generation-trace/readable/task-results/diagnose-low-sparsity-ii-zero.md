# diagnose low sparsity ii zero

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_low-sparsity-ii-zero_20260514T001512_result.json`
- **Structured JSON:** [`ba7265f67ac18316c36e.json`](../../sessions/ba/ba7265f67ac18316c36e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Let me write the definitive analysis.

## 根因

**v4a/v4b (sparsity ≤ 0.2): Possibility A（非 bug）**

代码位置：`interaction_index.py:_select_kv_to_evict()` (line 259-282)

```
candidates = importance[1:]           # 排除 BOS
_, indices = candidates.topk(num_to_evict, largest=False)  # 驱逐最不重要的位置
```

机制链：
1. `kv_importance[pos]` = 所有 layer/head/query 对 position `pos` 的注意力权重之和（`compute_dense_forward_with_importance`, line 335-340）
2. 驱逐全局最不重要的 20% 位置
3. low_sparsity token **定义上**就是注意力集中的 token——它们只关注少数高重要性位置
4. 被驱逐的低重要性位置本来就不在 low_sparsity token 的注意力目标中
5. fp16 下 softmax 的长尾精确为 0.0，所以在 `attention_mask` 中将已经为 0 的位置置零 = no-op
6. 结果：`kv_ppl == dense_ppl` (1.1105)，`both_ppl == attn_ppl` (1.2986)，`II = 0.0`

数学验证（自洽性）：
```
v4b: mean(attn) + mean(kv) - mean(dense) = 1.2986 + 1.1105 - 1.1105 = 1.2986 == mean(both) ✓
v4a: 1.1640 + 1.1105 - 1.1105 = 1.1640 == mean(both) ✓
```

Random masking（v3）为什么非零：`torch.randperm(seq_len-1)[:num_to_evict]` 均匀驱逐，20% 概率命中 low_sparsity token 的注意力目标 → kv_ppl > dense_ppl → II > 0

---

**v4c (sparsity=0.3): 数据 BUG**

v4c 的 II=0.0 [0,0] 与其 PPL 数据**数学上矛盾**：

```
若所有 segment 的 II=0，则 mean(both) 应 = mean(attn) + mean(kv) - mean(dense)
预测: 1.6722 + 11.0278 - 1.1105 = 11.5895
实际: 14.3898
差值: 2.80 — 证明 per-segment II 不全为 0
```

在 30% eviction 下，importance-based 也开始驱逐 low_sparsity token 的注意力目标（kv=11.03 >> dense=1.11），但 II 被错误报告为 0.0。可能原因：生成 v4c 时的代码版本与当前不同（无 git 历史可查），或聚合逻辑有 bug。

## 证据

| 实验 | sparsity | dense | kv | attn | both | II | 自洽 |
|------|----------|-------|------|------|------|----|------|
| v4a | 0.1 | 1.1105 | 1.1105 | 1.1640 | 1.1640 | 0.0 | ✓ |
| v4b | 0.2 | 1.1105 | 1.1105 | 1.2986 | 1.2986 | 0.0 | ✓ |
| v4c | 0.3 | 1.1105 | 11.0278 | 1.6722 | 14.3898 | 0.0 | **✗ BUG** |
| v3 | 0.2 | 1.1105 | 4.7013 | 1.9960 | 8.0771 | 1.13 | ✓ |

v4a/v4b 中 `kv == dense` 且 `both == attn`，证实 KV eviction 对 low_sparsity token 完全无效果——不是 mask 没应用（high/mid phase 的 kv PPL 爆到 100-400），而是被驱逐的位置恰好是 low_sparsity token 不关注的位置。

## 影响范围

- **high/mid phase 不受影响**：v4b high II=21.29, mid II=21.87，KV eviction 在这些 phase 效果巨大
- **s02 PASS verdict 仍然有效**：基于 low vs mid CI non-overlap 的判定依赖的是 II 差异，而 low=0 vs mid=21.87 确实不重叠
- **v4c 需要重跑**：sparsity=0.3 的 low_sparsity II 数据不可信

## 建议

1. **v4a/v4b 无需修复**。II=0 是 importance-based eviction 的固有属性：它天然保护 low_sparsity（简单/confident）token。这本身是一个有意义的发现——importance-based eviction 的 KV 节省对简单推理步骤零损失。

2. **v4c 需要用当前代码重跑** `--sparsity_levels 0.3`，获取 low_sparsity 的真实 II 值（预计非零，因为 30% eviction 已经足以影响 low_sparsity token）。

3. **方法论调整（可选）**：如果需要在 low_sparsity phase 测量 compound interaction，应当使用 **phase-local eviction**（在每个 phase 的 attention window 内按比例驱逐），而非全局 importance 排序。全局 importance 排序下 low_sparsity 的 II=0 是 eviction 策略的 artifact，不是 compound sparsity 无交互的证据。

---
