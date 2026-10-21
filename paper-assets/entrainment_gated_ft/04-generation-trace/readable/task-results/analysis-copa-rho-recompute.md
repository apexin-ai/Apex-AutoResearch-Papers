# analysis copa rho recompute

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_copa-rho-recompute_20260519T170027_result.json`
- **Structured JSON:** [`d699db0a7f2278cd3582.json`](../../sessions/d6/d699db0a7f2278cd3582.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。汇总：

---

### 完整结果

**COPA Accuracy 矩阵：**

| Config | Attn Ratio | GDN | RetNet | HGRN2 | Transformer | cross-arch σ |
|--------|-----------|-----|--------|-------|-------------|-------------|
| pure | 0.000 | 0.79 | 0.74 | 0.80 | 0.77 | 0.02625 |
| h24-1 | 0.040 | 0.75 | 0.79 | 0.77 | 0.77 | 0.01633 |
| h12-1 | 0.077 | 0.80 | 0.76 | 0.79 | 0.77 | 0.01700 |
| h6-1 | 0.143 | 0.75 | 0.76 | 0.79 | 0.77 | 0.01700 |
| h3-1 | 0.250 | 0.78 | 0.79 | 0.78 | 0.77 | 0.00471 |

**Cross-arch σ 序列:** [0.02625, 0.01633, 0.01700, 0.01700, 0.00471]

**Spearman ρ = -0.6669, exact permutation p = 0.2667** (two-tailed, n=5, 120 permutations)

### 哪个数据源是错的

| 数据源 | ρ | p | 正确？ |
|--------|---|---|--------|
| **Registry (exp-011)** | -0.667 | 0.267 | **正确** |
| **Summary JSON** | +0.300 | 0.683 | **错误** |
| 重算结果 | -0.667 | 0.267 | 基准 |

### Bug 根因

`xstorycloze_convergence_analysis.py` 第 ~108 行硬编码了 COPA 占位值：
```python
copa_supp = {"rho": 0.3, "raw_p": 0.6833}  # placeholder
```
这是 **HellaSwag 的值**被误用为 COPA placeholder，从未被实际计算替换。

### 修复内容

1. **`all_benchmark_convergence_summary.json`** — `copa_supplementary` 已从 `{rho: 0.3, p: 0.683}` 修正为 `{rho: -0.6669, p: 0.2667}`
2. **`xstorycloze_convergence_analysis.py`** — 硬编码占位值已替换为从 exp011 原始 JSON 实时计算 COPA Spearman ρ 的代码
3. **`convergence_table.csv`** — 无需修改，已是正确值 (ρ=-0.67, p=0.2667)
4. **Registry (exp-011)** — 无需修改，已是正确值

---
