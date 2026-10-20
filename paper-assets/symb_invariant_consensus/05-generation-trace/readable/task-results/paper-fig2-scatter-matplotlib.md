# paper fig2 scatter matplotlib

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig2-scatter-matplotlib_20260525T053327_result.json`
- **Structured JSON:** [`061d7a1ee444f32aace8.json`](../../sessions/06/061d7a1ee444f32aace8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。验证数据点：

- **14 个点**（排除了无 κ 的 StrategyQA 和 FOLIO ICL）
- **κ 值来源**：independence table（Mistral seeds/LogiQA/Qwen 系列）+ cross-model table（LLaMA κ=0.41, Qwen2.5-14B PW κ=0.62）
- **注意**：task 中 Qwen2.5-14B PW κ=0.82 与 cross-model table 中 κ=0.62 不一致，使用了论文表格的权威值 0.62
- **配色**：柔和粉/绿/天蓝/蓝灰/暖橙，与 Figure 3 风格统一
- **标注**：4 处关键注释（Mistral PW, LLaMA, Qwen3 PW, Qwen3 think），全用深灰色文字
- **3s-agg 误差条**：std=2.70，半透明同色

改动：
1. 新脚本 `docs/paper/figures/gen_f2_kappa_scatter_v2.py`
2. 输出 `f2_regime_scatter_v2.pdf` + `.png`
3. `experiments.tex` 第 45 行引用更新为 `f2_regime_scatter_v2`

---
