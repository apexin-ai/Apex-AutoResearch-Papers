# diagnose v4c scope inconsistency

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v4c-scope-inconsistency_20260514T003342_result.json`
- **Structured JSON:** [`1a1ec25764ef8d6a2f4a.json`](../../sessions/1a/1a1ec25764ef8d6a2f4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have the complete picture. Here's the analysis:

---

## Scope 分析

### PPL 聚合方式
**Per-segment 算术平均**（`run_profiling.py:384-390`）。每个 problem 的每个 phase segment 贡献一个 PPL 值，NaN **按 condition 独立过滤**：

```python
for cond in ["dense", "attn", "kv", "both"]:
    vals = ppl_per_phase_level[pname][level_str][cond]
    valid = [v for v in vals if not (isinstance(v, float) and v != v)]  # 过滤 NaN
    cond_means[cond] = round(float(np.mean(valid)), 4)
```

关键：dense/attn/kv/both 四列的均值**可以来自不同数量的 segment**（各自独立去 NaN）。

### II 计算方式
**Per-segment 计算**，然后 bootstrap 取 mean/CI（`run_profiling.py:351-361`）：

```python
ppl_d = ppls["dense"]
if ppl_d > 0:   # NaN > 0 is False
    ii_val = r_both - r_attn - r_kv + 1
else:
    ii_val = float("nan")
```

II 要求**同一 segment 的 4 个 PPL 全部有效**，任一条件产生 NaN → 该 segment 的 II 被排除。

### Scope 不一致——数学证明

如果 454 个 low_sparsity segment 的 II 全为 0.0，则对每个 segment i：

    both_i - attn_i = kv_i - dense_i

求和后：

    mean(both) - mean(attn) = mean(kv) - mean(dense)

**实际数据 (v4c)**：
- `14.3898 - 1.6722 = 12.7176`
- `11.0278 - 1.1105 = 9.9173`
- **差值 = 2.8003 ≠ 0**

数学上不可能所有 II = 0.0。**PPL 和 II 来自不同的 segment 子集。**

**对比 v4b**：`0.0000 = 0.0000`，完全一致。v4b 中 kv_ppl = dense_ppl 精确相等（20% eviction 对 low_sparsity token 零影响），II = 0 是真实的。

## 根因机制

**Float16 级联失败** → `both` 条件产生 NaN：

1. KV eviction (30%) 去掉重要 KV 位置 → 某些 segment 的 attention 输出极端化
2. Head masking hook (`interaction_index.py:119`) 对这些极端值乘以 0：
   ```python
   reshaped = reshaped * head_mask_expanded  # inf * 0 = NaN
   ```
3. NaN 向后传播到 logits → CE loss = NaN → `ppl_both = NaN`
4. **但 kv-only 条件无 head masking**，hidden states 虽然极端但不触发 inf*0 → `ppl_kv` 有效（且值很大）
5. 结果：这些 segment 的高 `kv_ppl` 纳入 mean(kv)=11.03，但 II 被排除（NaN）
6. 剩余 segment 的 KV 几乎无影响 → II ≈ 0.0 精确

## v4c per-problem 数据（采样 5 个 problem）

JSON 中未存储 per-segment PPL/II（只存聚合值），但可以推断：

| problem_id | low_sp tokens | n_segs | kv对这些token的影响 |
|---|---|---|---|
| test/algebra/2470 | 426 | 5 | 多数segment kv≈dense，少数segment kv>>dense但both=NaN |
| test/prealgebra/192 | 292 | 4 | 同上 |
| test/intermediate_algebra/134 | 705 | 6 | 同上 |
| test/algebra/841 | 527 | 7 | 同上 |
| test/algebra/478 | 264 | 4 | 同上 |

每个 problem 的 low_sparsity token 数充足（最少 264 tokens），无 0-token 问题。

## v4b per-problem 数据（对比）

v4b 使用完全相同的 50 problems、相同的 phase 分割（454 segments、32349 tokens）。

| condition | dense | attn | kv | both |
|---|---|---|---|---|
| v4b low_sp PPL | 1.1105 | 1.2986 | **1.1105** | **1.2986** |
| v4c low_sp PPL | 1.1105 | 1.6722 | **11.0278** | **14.3898** |

v4b 中 `kv = dense` 且 `both = attn` **精确相等** → 20% KV eviction 对 low_sparsity 零影响 → II = 0.0 是真实的。v4c 中 30% eviction 开始影响部分 segment，但这些 segment 的 II 被 NaN 过滤掉了。

## 结论

**Scope 不一致，具体差异如下：**

1. **PPL 聚合**：按 condition 独立过滤 NaN，每个 condition 的均值可能来自不同数量的 segment
2. **II 聚合**：要求 4 个 condition 同时有效，任一 NaN 则排除该 segment
3. **实际影响**：v4c low_sparsity 中，有 KV 影响的 segment 在 `both` 条件下产生 NaN（float16 inf×0），其高 `kv_ppl` 仍纳入均值（拉高到 11.03），但 II 被排除，导致 II = 0.0 [0, 0]
4. **v4b 无此问题**：20% sparsity 下 KV 对 low_sparsity 零影响，四列无 NaN，scope 一致

**建议修复**：在 `run_profiling.py` 的 II 计算中，使用与 PPL 相同的 segment 子集（只取 4 个 condition 全部有效的 segment 来计算 mean PPL），或者将 forward pass 转为 float32 计算以避免 NaN。

---
