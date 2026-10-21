# paper figure fig4 window ablation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig4_window_ablation_20260517T010556_result.json`
- **Structured JSON:** [`f952e7da99ee6c1766cd.json`](../../sessions/f9/f952e7da99ee6c1766cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**输出文件**:
- PDF: `artifacts/figures/paper/fig4_window_ablation.pdf`
- PNG: `artifacts/figures/paper/fig4_window_ablation.png`
- 生成脚本: `artifacts/figures/paper/fig4_window_ablation.py`

**数据来源**: `exp_007_window_ablation/results.json`（canonical，balanced weights），包含 W=1,3,5,10,15,20,25 × 3 models 完整数据。

**图表内容**: 3-panel line plot（双栏宽度 6.5"），展示随 W 增大：
- R1-8B: balanced accuracy 0.778→0.810，precision 0.693→0.822，FPR 0.097→0.048（单调改善）
- QwQ-32B: 类似趋势但幅度较小
- R1-32B: accuracy 在 W=10 达峰后回落，FPR 改善有限

数值与 registry 中已知数据点一致，验证通过。

---
