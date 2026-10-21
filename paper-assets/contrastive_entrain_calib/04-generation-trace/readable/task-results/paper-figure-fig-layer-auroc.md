# paper figure fig layer auroc

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_layer_auroc_20260520T080959_result.json`
- **Structured JSON:** [`aba35b8242616bf73258.json`](../../sessions/ab/aba35b8242616bf73258.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册。

**输出文件：**
- PDF: `artifacts/figures/fig_layer_auroc.pdf`
- PNG: `artifacts/figures/fig_layer_auroc.png`
- 数据: `artifacts/figures/fig_layer_auroc_data.json`

**数据来源说明：**
- **Qwen3-8B**: v2→v2.1 transfer test 全 36 层 per-layer AUROC（100 samples）。完整展示从 L0 (~0.53, near chance) 到 L19 处急升、到 L32 (~0.77) 的 emergence 曲线。
- **Llama-3-8B**: 5-fold CV mean per layer，仅 L16-31（提取脚本只覆盖了这些层）。L16 为 CV best (0.779)，与 Qwen L19 的 ~50% depth 一致。

**局限性：** 两模型使用不同评估方法（transfer vs CV），绝对值不可直接比较。若需完全一致的评估方法，需要 SSH 到服务器重新运行全层 per-layer 5-fold CV。Llama L0-15 缺失，需加载模型重新提取。

---
