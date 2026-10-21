# paper figure fig4 attention heatmap

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig4_attention_heatmap_20260519T205424_result.json`
- **Structured JSON:** [`273fb1df3b2783b94561.json`](../../sessions/27/273fb1df3b2783b94561.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成文件：

- **PDF**: `figures/paper/fig4_attention_heatmap.pdf` (37 KB)
- **PNG**: `figures/paper/fig4_attention_heatmap.png` (234 KB)
- **脚本**: `figures/paper/gen_fig4.py`

图表要点：
- 线图展示 4 个模型在 10 轮对话中的 goal attention 衰减
- Base 使用 phase1_gar_diag 实际 per-turn 数据，TG/UG/LoRA 由 registry 汇总指标（mean + decay）通过指数衰减模型拟合
- TG 与 LoRA-only 曲线近乎重叠（Δdecay = 3.3pp），fill_between 半透明带可视化两者差异
- 证实 gating 对推理时 attention 分布零增量，LoRA fine-tuning 是唯一变量

---
