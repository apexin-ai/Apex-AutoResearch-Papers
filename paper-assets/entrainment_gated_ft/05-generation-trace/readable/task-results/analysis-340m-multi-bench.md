# analysis 340m multi bench

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_340m-multi-bench_20260522T002147_result.json`
- **Structured JSON:** [`24fa419f0c0af5fecd71.json`](../../sessions/24/24fa419f0c0af5fecd71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

---

## 340M Multi-Benchmark Multiplicity Analysis — 结果

### 340M vs 1.3B α 对比表

| Benchmark | 340M α_all | 1.3B α_all | Δ | 340M α_pure | 1.3B α_pure | Δ_pure |
|-----------|-----------|-----------|--------|------------|------------|--------|
| HellaSwag (acc_norm) | 0.334 | 0.302 | +0.031 | 0.167 | 0.148 | +0.019 |
| PIQA | 0.366 | 0.278 | +0.089 | 0.181 | 0.143 | +0.038 |
| ARC-Easy | 0.564 | 0.434 | +0.130 | 0.289 | 0.205 | +0.084 |
| **Mean** | **0.421** | **0.338** | **+0.084** | | | |

### Convergence ρ (exact permutation p)

| Benchmark | 340M ρ | p | 1.3B ρ | p |
|-----------|--------|------|--------|------|
| HellaSwag | +0.40 | 0.517 | +0.40 | 0.517 |
| PIQA | +0.30 | 0.683 | −0.50 | 0.450 |
| ARC-Easy | −0.10 | 0.950 | +0.30 | 0.683 |

所有 p>0.45 — **无显著 convergence 趋势**（两个 scale 均如此）。

### Jaccard 统计

| Benchmark | 340M J_helped | 1.3B J_helped | 340M J_hurt | 1.3B J_hurt |
|-----------|--------------|--------------|-------------|-------------|
| HellaSwag | 0.084 | 0.095 | 0.083 | 0.085 |
| PIQA | 0.090 | 0.091 | 0.085 | 0.094 |
| ARC-Easy | 0.098 | 0.092 | 0.103 | 0.099 |

所有 Jaccard p=0.000（显著高于 chance），但绝对值低（~0.08-0.10），说明 helped/hurt 集合 architecture-specific。

### 结论

**Multiplicity 是 scale-dependent in magnitude, scale-invariant in pattern:**
1. 340M 比 1.3B 高 ~8pp 平均 α（smaller models disagree more）
2. 但定性 pattern 一致：低 Jaccard、无 convergence、per-ratio α 稳定
3. ARC-Easy 差距最大（+13pp），可能因为 340M 在该 benchmark 整体准确率最低（~55% vs ~70%）

产出已保存: `artifacts/paper_data/340m_multi_bench_analysis.json` (artifact: `art_20260522_4c676a`)

---
