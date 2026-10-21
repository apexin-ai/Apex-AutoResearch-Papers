# paper figure training dynamics

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_training_dynamics_20260523T085100_result.json`
- **Structured JSON:** [`f2eba14cc5427f7db2a6.json`](../../sessions/f2/f2eba14cc5427f7db2a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF (21KB) 和 PNG (64KB) 均已生成。

**数据来源：**
- TF GAR-ours：registry `phase2_4way_eval_heldout`（Base=0.013, TG=0.50, UG=0.51, LoRA=0.50）
- AR GAR-ours：任务指定值（Base=0.019, TG=0.064, UG=0.033, LoRA=0.037）
- Gap 倍数：TG=7.8×, UG=15.5×, LoRA=13.5×

**设计特点：**
- Log Y 轴单轴（避免 dual Y-axis），TF 和 AR 自然分离在不同量级
- 虚线 slope 连接每个 variant 的 TF→AR 值，直观展示 collapse 幅度
- 配色与 fig3 一致（green=TF/IID, orange=AR/model-gen）
- 3.33×2.5 inch column-width，serif 字体

**输出文件：**
- `figures/paper/fig_training_dynamics.pdf`
- `figures/paper/fig_training_dynamics.png`
- 生成脚本：`figures/paper/gen_fig_training_dynamics.py`

---
