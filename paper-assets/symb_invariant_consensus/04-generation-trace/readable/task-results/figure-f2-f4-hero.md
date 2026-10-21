# figure f2 f4 hero

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_f2-f4-hero_20260517T162912_result.json`
- **Structured JSON:** [`ea9bf591a5b4463f4010.json`](../../sessions/ea/ea9bf591a5b4463f4010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图已生成并注册。

**F2 (Per-problem Scatter)**:
- 307 个数据点（235 ProofWriter + 72 FOLIO）
- 4 类 marker：no-flip (276), correct flip (16), wrong flip (15), neutral flip (0)
- Flip rate 随 vote entropy 递增：Q1=0%, Q2=2.2%, Q3=10%, Q4=35.4%
- Correct vs wrong flip 几乎对半，符合预期叙事

**F4 (C0 vs Gap)**:
- 10 个 model x domain 条件，5 色区分 model，4 种 marker 区分 domain
- y=0 虚线参考线，每个点带标签
- Delta 在 [-3.33, +6.67] 波动，无明显 C0 相关趋势

**输出文件**:
- `/root/symb_invariant_consensus/artifacts/figures/f2_per_problem_scatter.{pdf,png}`
- `/root/symb_invariant_consensus/artifacts/figures/f4_c0_vs_gap.{pdf,png}`
- 绘图脚本：`/root/symb_invariant_consensus/scripts/plot_hero_figures.py`

---
