# paper figure fig4 real data redraw

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig4_real_data_redraw_20260520T030639_result.json`
- **Structured JSON:** [`1bf6b97f557caa3f9433.json`](../../sessions/1b/1bf6b97f557caa3f9433.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

### Part 1: per-turn goal attention 数据
已提取并保存到 `artifacts/fig4_attention_real_data.json`。4 个模型 × 10 turns × 3 convs 的 layer-averaged goal attention：

| Turn | Baseline | TG | UG | LoRA-only |
|------|----------|-----|-----|-----------|
| T1 | 0.053 | 0.058 | 0.058 | 0.061 |
| T2 | 0.018 | 0.029 | 0.025 | 0.024 |
| T3 | 0.012 | 0.016 | 0.016 | 0.017 |
| T4 | 0.010 | 0.023 | 0.020 | 0.018 |
| T5 | 0.011 | 0.035 | 0.032 | 0.027 |
| T6 | 0.007 | 0.011 | 0.011 | 0.011 |
| T7 | 0.007 | 0.011 | 0.010 | 0.010 |
| T8 | 0.008 | 0.028 | 0.028 | 0.028 |
| T9 | 0.004 | 0.008 | 0.008 | 0.008 |
| T10 | 0.007 | 0.013 | 0.011 | 0.012 |

Baseline 衰减最快（T1→T9 跌 92%）。TG/UG/LoRA 在 T4-T8 维持显著更高的 goal attention，但 T8 的方差极大（std ≈ mean），源于 N=3 中一个 conv 在特定层有极高 attention。

### Part 2: conv_length_gar_scaling 数据
- 本地已有报告：`artifacts/_project/report/conv_length_gar_scaling_report.md`（N=45，5 turns per-turn GAR 数据）
- 服务器 `~/runs/turn_residual_gating/` 下无对应原始数据文件

### Part 3: fig4 重绘
- `artifacts/fig4_attention_heatmap.pdf`
- `artifacts/fig4_attention_heatmap.png`

---
