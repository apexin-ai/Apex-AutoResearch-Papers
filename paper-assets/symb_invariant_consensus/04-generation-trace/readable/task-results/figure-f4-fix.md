# figure f4 fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_f4-fix_20260517T163816_result.json`
- **Structured JSON:** [`0702ba9b9d7e947f3d53.json`](../../sessions/07/0702ba9b9d7e947f3d53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

F4 修复完成。

**变更摘要**：
- 删除 2 个 superseded 数据点（exp-011 LLaMA-8B D012, Qwen-14B D012）
- 添加 QwQ-32B PW 单条件（C0=0.026, Δ=-5.9pp, n=17）
- Marker size ∝ sqrt(n/60)，n=804 的点明显大于 n=60
- 添加 95% CI error bars（binomial SE propagation）
- 保留视觉规范：y=0 虚线、色盲友好配色、形状区分 domain、无标题、去上右边框

**输出文件**：
- `westd-32608:/root/symb_invariant_consensus/artifacts/figures/f4_c0_vs_gap.pdf`
- `westd-32608:/root/symb_invariant_consensus/artifacts/figures/f4_c0_vs_gap.png` (300dpi)

**脚本**：`scripts/plot_f4_fixed.py`（独立可运行），`scripts/plot_hero_figures.py` 的 F4 部分也已同步更新。

---
