# analysis arc easy per example full

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_arc-easy-per-example-full_20260520T092702_result.json`
- **Structured JSON:** [`ba210943950e0baa906a.json`](../../sessions/ba/ba210943950e0baa906a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 artifacts 全部注册完成。以下是关键结果摘要：

### A. Per-Example Classification (ARC-Easy, N=2376)

| Arch | Ratio | Helped | Hurt | Net |
|------|-------|--------|------|-----|
| GDN | h24-1 | 178 | 185 | **-7** |
| GDN | h12-1 | 176 | 206 | **-30** |
| GDN | h6-1 | 170 | 157 | **+13** |
| GDN | h3-1 | 171 | 180 | **-9** |
| RetNet | h24-1 | 158 | 168 | **-10** |
| RetNet | h12-1 | 163 | 146 | **+17** |
| RetNet | h6-1 | 159 | 147 | **+12** |
| RetNet | h3-1 | 144 | 184 | **-40** |
| HGRN2 | h24-1 | 160 | 119 | **+41** |
| HGRN2 | h12-1 | 159 | 111 | **+48** |
| HGRN2 | h6-1 | 185 | 118 | **+67** |
| HGRN2 | h3-1 | 164 | 146 | **+18** |

HGRN2 在所有 ratio 下 attention 层都有正向 net effect；GDN/RetNet 混合。

### B-C. Jaccard + Null Model

所有 24 个 Jaccard 比较均显著高于 null model（22/24 p<0.001，2/24 p<0.01）。Normalized ES 范围 0.035–0.135，说明跨架构 helped/hurt 重叠虽然显著但绝对幅度低——不同架构倾向于在不同样本上受 attention 影响。

### D. Convergence σ

mean σ 在 pure(0.0964) → h24-1(0.1067) → h12-1(0.1052) → h6-1(0.0948) → h3-1(0.0990) 之间无单调趋势。Spearman ρ=-0.20, p=0.78 (ns)——attention ratio 与跨架构分歧无显著线性关系。

### E. Multiplicity Metrics

| Benchmark | Ratio | α (ambiguity) | δ (discrepancy) |
|-----------|-------|---------------|-----------------|
| ARC-Easy | pure | 0.205 | 2.55 |
| ARC-Easy | h24-1 | 0.226 | 2.98 |
| ARC-Easy | h12-1 | 0.223 | 3.12 |
| ARC-Easy | h6-1 | 0.201 | 2.32 |
| ARC-Easy | h3-1 | 0.210 | 2.66 |
| LAMBADA | pure | 0.307 | 0.61 |
| LAMBADA | h24-1 | 0.300 | 0.58 |
| LAMBADA | h12-1 | 0.316 | 0.55 |
| LAMBADA | h6-1 | 0.294 | 0.53 |
| LAMBADA | h3-1 | 0.296 | 0.55 |

LAMBADA 的 α 高于 ARC-Easy（~0.30 vs ~0.21），但 δ 低得多（~0.55 vs ~2.7），说明 LAMBADA 上架构间分歧更频繁，但一致正确时 confidence 更接近。ARC-Easy 上 h12-1 的 δ 最高（3.12），表明该 ratio 下即使都答对，3 个架构的 confidence 差异最大。

---
