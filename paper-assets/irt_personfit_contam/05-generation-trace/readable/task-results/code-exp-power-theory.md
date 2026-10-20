# code exp power theory

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-power-theory_20260520T095630_result.json`
- **Structured JSON:** [`65a43acb2321c754d4cc.json`](../../sessions/65/65a43acb2321c754d4cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-power-theory 完成。结果汇总：

**理论验证通过** — R²(two-sided)=0.957, R²(left-tail)=0.976, R²(mean lz*)=0.995

**核心发现**:
1. **δ ∝ √n**: 检测力信号随 √n_items 增长（√n scaling R²≥0.87），解释了 MMLU(14K) >> ARC-C(295) 的 power 差异
2. **Inverted-U 机制**: lz* 均值在 π≈81-85% 处从负转正——中等污染产生 aberrant pattern (lz*<0)，高污染产生 over-consistent pattern (lz*>0)。左尾检测只捕获前者，因此呈 inverted-U；两侧检测捕获两端，消除 inverted-U
3. **最小 items 指南**: 80% power 需要 ~8K items (15% contam), ~3K (25%), ~1K (50%)

**产出** (`artifacts/power_theory/`):
- `theory_derivation.md` — 含 LaTeX 公式的完整推导
- `theory_vs_simulation.png` — 6 panel 对比图
- `minimum_items_table.csv` — 15 行指南表
- `inverted_u_theory.md` — 拐点理论解释
- `fit_metrics.json` + `power_theory_summary.json`

---
