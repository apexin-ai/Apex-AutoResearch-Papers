# code r7 layer heatmap fix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r7_layer_heatmap_fix_20260518T055921_result.json`
- **Structured JSON:** [`92084558eb88a7ef7184.json`](../../sessions/92/92084558eb88a7ef7184.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成。验证汇总：

- **R1-8B**: biased=L14, corrected=L14 → 单条绿色虚线，标注 "corrected = biased (L14)"
- **OT-7B**: biased=L0（红色虚线），corrected=L16（绿色虚线）
- **QwQ-32B**: biased=L2（红色虚线），corrected=L60（绿色虚线）— 不变
- **R1-32B**: biased=L10（红色虚线），corrected=L63（绿色虚线）— 不变

输出文件：
- PDF: `/root/autodl-tmp/contrastive_trace_safety/docs/paper/figures/fig_layer_heatmap.pdf` (46KB)
- PNG: `/root/autodl-tmp/contrastive_trace_safety/docs/paper/figures/fig_layer_heatmap.png` (237KB)

绘图脚本保存在 `scripts/plot_layer_heatmap.py`，后续可直接修改重跑。

---
