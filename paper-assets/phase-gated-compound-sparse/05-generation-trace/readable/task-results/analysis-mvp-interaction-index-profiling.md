# analysis mvp interaction index profiling

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_interaction_index_profiling_20260513T195650_result.json`
- **Structured JSON:** [`cfdedee1d887b8620419.json`](../../sessions/cf/cfdedee1d887b8620419.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结论

**MVP FAIL — 代码 bug，非假设失败。**

### 根因

`interaction_index.py` 第 ~210 行，KV mask 展平逻辑错误：

```python
flat_kv_mask = kv_mask.min(dim=0).values  # 取 28 层交集
```

`_select_kv_to_evict` 在每层**独立随机**选位置 evict。`min(dim=0)` 要求位置在**全部 28 层**都未被 evict 才保留。存活概率：
- s=0.3: 0.7^28 = **0.07%**
- s=0.5: 0.5^28 ≈ **0%**

结果：attention mask 全零 → NaN logits → NaN perplexity → NaN II。

### 可用数据

`dense` 和 `attn` 条件正常工作，phase segmentation 健康（execution 25 segments, reasoning 96, transition 192，均 ≥ 20）。attn-only 已展现 phase-dependent 差异（execution 对 head pruning 最敏感，474× dense PPL）。

### 修复方案

最简修复：`_select_kv_to_evict` 改为 layer-uniform（所有层 evict 相同位置）。单行改动，重跑 ~0.5h。

报告已写入 `artifacts/mvp_ii_analysis.md` 并注册。

---
