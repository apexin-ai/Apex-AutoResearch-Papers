# GSM8K DS Importance ii_low = 0.0 — Root Cause Diagnosis

**Date**: 2026-05-15  
**Server**: westd-22162, `/root/autodl-tmp/pacs/`  
**Model**: DeepSeek-R1-Distill-Qwen-7B (fp16, eager attention)

---

## Executive Summary

ii_low = 0.0 是 **两个独立 bug 交互** 的结果，不是 GSM8K 短 trace 的自然特性：

1. **fp16 NaN 污染 kv_importance** → `_select_kv_to_evict` 对全-NaN importance 做 `topk` → 退化的 eviction pattern（全部集中在序列中后段）
2. **低稀疏 tokens 系统性位于序列前段** → 因果注意力下，evicted KV positions 全在 low_sparsity tokens 之后 → KV masking 对 low_sparsity 零效果 → `ppl_kv = ppl_dense` → II = 0

Aggregate perplexity 全 NaN 同根同源：fp16 forward pass 产生 NaN CE losses。

---

## 诊断任务 1：n=3 Diagnostic Run — ii_low = 0 根因

### 诊断数据

| Problem | seq_len | low_sparsity max pos | KV evicted range | evicted accessible to low | ii_low |
|---------|---------|---------------------|------------------|--------------------------|--------|
| gsm8k_test/13 | 961 | 405 | [482, 721] | **0** | 0.0 |
| gsm8k_test/51 | 744 | 377 | [373, 558] | 5 | null (all NaN) |
| gsm8k_test/54 | 2145 | 1058 | [1074, 1609] | **0** | 0.0 |

### Per-segment PPL 值（非 NaN 示例）

Problem 0, low_sparsity segment [215, 227] (13 tokens):
```
ppl_dense (cached) = 1.059570
ppl_dense (fresh)  = 1.059570
ppl_attn           = 1.833008    ← head masking 有效果
ppl_kv             = 1.059570    ← KV masking 零效果 (= dense!)
ppl_both           = 1.833008    ← = ppl_attn (KV 无贡献)
II = 1.833008/1.059570 - 1.833008/1.059570 - 1.059570/1.059570 + 1 = 0.0000000000
```

Problem 2, low_sparsity segment [634, 650] (17 tokens):
```
ppl_dense = 1.160156
ppl_attn  = 1.429688
ppl_kv    = 1.160156    ← = dense
ppl_both  = 1.429688    ← = attn
II = 0.0000000000
```

### 机制确认

**`ppl_kv ≡ ppl_dense`** 对所有非 NaN 的 low_sparsity segments 成立。原因：

1. `kv_importance` 全部 NaN (272/272 positions)
2. `_select_kv_to_evict` 对 NaN importance 执行 `importance / position_counts`（仍是 NaN），然后 `topk(n, largest=False)` 在全 NaN tensor 上返回 **implementation-dependent** indices
3. 实际 eviction 集中在序列 50%-75% 位置区间（如 [482, 721] in seq_len=961）
4. Low_sparsity tokens 全部在序列 0-40% 位置（因为低稀疏 = 早期推理阶段）
5. 因果注意力：token t 只能 attend to positions ≤ t → 被 evict 的 positions 全在 low_sparsity tokens 之后 → KV eviction 无效 → `ppl_kv = ppl_dense`
6. II = R_both - R_attn - R_kv + 1 = R_attn - R_attn - 1 + 1 = **0.0**

### 根因 #1: kv_importance NaN 来源

```
kv_importance: shape=(961,), min=nan, max=nan, zeros=0
head_importance all-zero layers: 0/28    ← 无 layer 被跳过
```

`compute_dense_forward_with_importance` 中：
- 各 layer 的 attention weights 通过 `attn_f.isnan().any()` 检查（28 层全通过）
- 但 `kv_importance.add_(attn_f.sum(dim=(0,1)).cpu())` 在 fp16 下执行 sum → **fp16 partial sum overflow** 产生 NaN
- NaN 通过 `add_` 传播：一旦某个 position 变成 NaN，后续所有 layer 的累加都保持 NaN
- 最终 kv_importance 272/272 positions 全部 NaN

**验证**：plain `compute_dense_ce_losses`（无 hooks）同样产生 41/271 NaN CE losses。fp16 溢出是模型本身的问题，非 hooks 引起。

### 根因 #2: 大量 NaN PPL → 部分 problems ii_low = None

50 题中 26 题 ii_low = None（非 0.0），因为该问题所有 low_sparsity segments 的 ppl_dense 全部 NaN：
- `ppl_from_cached_losses` 对 NaN CE losses 过滤后如果无有效值 → 返回 NaN
- `ppl_d > 0` 判断 NaN → False → ii_val = NaN → 不进入 `phase_ii_vals_for_problem` → `rec["ii_low"] = None`

24 题 ii_low = 0.0：至少有一个 low_sparsity segment 的 CE losses 中含非 NaN 值 → ppl_dense 有效 → II 计算走正常路径 → 但因 KV masking 无效得到 0.0。

---

## 诊断任务 2：QW Importance 输出检查

**QW importance 输出不为空**，文件存在且完整：
```
/root/autodl-tmp/pacs/analysis_output/gsm8k/qw_importance/
  profiling_results.json  (3.2 MB, May 16 00:47)
  generations.json        (156 KB, May 16 00:47)
```

50/50 完成，log 显示正常结束。但 QW importance 同样出现 ii_low = 0.0：
```
II[low_sparsity, 0.15]: mean=+0.0000  95%CI=[+0.0000, +0.0000]
II[low_sparsity, 0.20]: mean=+0.0000  95%CI=[+0.0000, +0.0000]
II[low_sparsity, 0.25]: mean=+0.0000  95%CI=[+0.0000, +0.0000]
II[low_sparsity, 0.30]: mean=+0.0000  95%CI=[+0.0000, +0.0000]
```

**根因相同**：QW importance 使用相同的 `compute_dense_forward_with_importance` → 同样的 kv_importance NaN → 同样的退化 eviction → 同样的 ii_low = 0。

---

## 诊断任务 3：Aggregate Perplexity NaN 根因

**全部 NaN**（DS importance 和 QW importance 均是）：
```json
{
  "high_sparsity": {"0.15": {"dense": NaN, "attn": NaN, "kv": NaN, "both": NaN}, ...},
  "low_sparsity":  {"0.15": {"dense": NaN, "attn": NaN, "kv": NaN, "both": NaN}, ...},
  "mid_sparsity":  {"0.15": {"dense": NaN, "attn": NaN, "kv": NaN, "both": NaN}, ...}
}
```

**根因**：聚合代码 `round(float(np.mean(vals)), 4)` 中，`vals` list 包含 NaN 值（来自 fp16 NaN CE losses）→ `np.mean()` 含 NaN → 结果 NaN。

**修复**：聚合时过滤 NaN：`np.nanmean(vals)` 或 `[v for v in vals if not np.isnan(v)]`。

---

## 诊断任务 4：Bootstrap N 参数

```python
# run_profiling_gsm8k.py line 65
N_BOOTSTRAP = 1000
```

MATH-500 使用 `N=10000`。GSM8K 用 `N=1000`，需统一到 10000。

**附注**：bootstrap 调用处有 unpacking bug：
```python
mean, ci_low, ci_high = bootstrap_interaction_index(samples, ...)
```
`bootstrap_interaction_index` 返回 6-key dict，3 变量 unpacking 应导致 `ValueError`。但结果文件确实存在 — 推测运行时使用的是旧版函数（返回 3 元素）。当前代码与运行时代码不一致，需确认。

---

## Bug 清单与修复方案

### Bug 1 (Critical): kv_importance NaN → 退化 KV eviction

**位置**: `pacs/profiling/interaction_index.py` — `compute_dense_forward_with_importance`

**修复方案 A（推荐）**: importance 计算用 float32
```python
# 在 hook 中: 
attn_f = output[1].float()  # fp16 → fp32 before norm/sum
```

**修复方案 B**: NaN 保护
```python
# _select_kv_to_evict 中 topk 之前:
importance = importance.nan_to_num(0.0)  # NaN → 0（最低重要性，优先 evict）
```

**建议**: 同时实施 A+B（A 治本，B 防御性兜底）

### Bug 2 (Critical): fp16 NaN 在 dense CE losses

**位置**: `pacs/profiling/interaction_index.py` — `compute_dense_ce_losses` 和 `compute_dense_forward_with_importance`

**修复**: forward pass 用 float32 logits 计算 CE
```python
ce_losses = F.cross_entropy(logits[:-1].float(), labels[1:], reduction="none")
# ↑ 已有 .float() 在 compute_perplexity 中，但 compute_dense_ce_losses 缺失
```

实际上 `compute_dense_ce_losses` 没有 `.float()` 转换：
```python
# 当前（有 bug）:
return F.cross_entropy(shift_logits, shift_labels, reduction="none")
# 应改为:
return F.cross_entropy(shift_logits.float(), shift_labels, reduction="none")
```

### Bug 3 (Medium): Aggregate perplexity 不过滤 NaN

**位置**: `run_profiling_gsm8k.py` — 聚合循环

```python
# 当前:
cond: round(float(np.mean(vals)), 4)
# 应改为:
cond: round(float(np.nanmean(vals)), 4) if vals else float("nan")
```

### Bug 4 (Low): Bootstrap unpacking

**位置**: `run_profiling_gsm8k.py` line ~454

```python
# 当前:
mean, ci_low, ci_high = bootstrap_interaction_index(...)
# 应改为:
result = bootstrap_interaction_index(...)
ii_out[pname][level_str] = {
    "mean": result["mean"], "ci_low": result["ci_low"], "ci_high": result["ci_high"],
}
```

### Issue 5 (Config): Bootstrap N 不一致

`N_BOOTSTRAP = 1000` → 改为 `10000` 与 MATH-500 一致。

---

## 结论

| 问题 | 根因 | 严重度 |
|------|------|--------|
| ii_low = 0.0 (24/50) | NaN kv_importance → eviction 全在序列后段 → 对 early low_sparsity tokens 无效 | Critical (bug) |
| ii_low = None (26/50) | fp16 NaN CE losses → ppl_dense = NaN | Critical (bug) |
| Aggregate PPL = NaN | NaN 值未过滤即求均值 | Medium (bug) |
| DS random FAIL | 同根因：NaN importance 使 random vs importance 对比失效 | Critical (same root) |
| Bootstrap N = 1000 | Config 不一致 | Low (config) |

**ii_low = 0.0 不是 GSM8K 短 trace 的自然特性。修复 fp16 NaN 后应能获得有意义的 low_sparsity II 值。**

---

## 推荐优先级

1. **立即修复** Bug 1 + Bug 2（importance float32 + CE losses float32）→ 重跑 DS importance + QW importance
2. **同步修复** Bug 3（nanmean）+ Bug 4（bootstrap unpacking）+ Issue 5（N=10000）
3. **重跑验证** 修复后跑 n=5 quick validation，确认 ii_low ≠ 0 且 aggregate PPL 非 NaN
