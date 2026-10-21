# analysis retnet hgrn2 only decoupling

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_retnet-hgrn2-only-decoupling_20260520T045441_result.json`
- **Structured JSON:** [`58e4464b22d12e050c81.json`](../../sessions/58/58e4464b22d12e050c81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**Cross-arch σ（LAMBADA accuracy，RetNet vs HGRN2）**

| Ratio | RetNet | HGRN2 | σ |
|-------|--------|-------|---|
| pure | 0.5166 | 0.4842 | **0.0162** |
| h24-1 | 0.5152 | 0.5003 | 0.0075 |
| h12-1 | 0.5071 | 0.5030 | **0.0020** |
| h6-1 | 0.4972 | 0.5088 | 0.0058 |
| h3-1 | 0.5032 | 0.5139 | 0.0053 |

σ 非严格单调（h12-1 处达最小值 0.002 后轻微回弹），但 pure→h24-1→h12-1 前三步单调递减，且所有 hybrid σ ≤ 0.0075，较 pure 的 0.0162 至少降 54%。Spearman ρ = -0.7。

**Per-example Jaccard（RetNet-HGRN2）**

所有 4 个 hybrid ratio 的 helped/hurt Jaccard 均在 0.085-0.108 范围内浮动（helped range = 0.022, hurt range = 0.010），确认 saturation。

**结论：`decoupling_holds_without_GDN`** — 排除 GDN 后，两个信号（σ 收敛 + Jaccard 饱和）均成立。对 MF-3（GDN confound）攻击面的最强回应：decoupling 不依赖有 16-head confound 的 GDN。

唯一需注意的是 σ 非完美单调（论文中可表述为 "converges" 而非 "monotonically decreases"），但趋势清晰。

---
