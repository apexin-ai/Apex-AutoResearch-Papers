# ops fig p3 composition scatter

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig-p3-composition-scatter_20260525T153949_result.json`
- **Structured JSON:** [`2aaff48cff7a821b9cb9.json`](../../sessions/2a/2aaff48cff7a821b9cb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个图都已生成，视觉检查通过：

**Figure A (Panel Composition)**: API 模型占比越高，panel ASR 越低（更鲁棒）。K=7 下降最陡、ASR 最低。趋势清晰，误差条合理。

**Figure B (Cross-benchmark K_eff)**: MMLU 与 ARC 的 K_eff 高度相关（r = 0.901），点大致沿对角线分布但 ARC 侧略高。K=3/5/7 三组清晰分层。

输出文件：
- `docs/paper/figures/fig_panel_composition.pdf` + `.png`
- `docs/paper/figures/fig_keff_cross_benchmark.pdf` + `.png`

---
