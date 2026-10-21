# paper figure fig3 gate shift

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig3_gate_shift_20260519T202802_result.json`
- **Structured JSON:** [`2e13ca2fb08e7091510f.json`](../../sessions/2e/2e13ca2fb08e7091510f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 3 已生成并注册。

**输出**:
- PDF: `figures/paper/fig3_gate_shift.pdf`
- PNG: `figures/paper/fig3_gate_shift.png`
- 生成脚本: `figures/paper/gen_fig3_gate_shift.py`

**两面板内容**:
- **(a)** Cleveland dot plot — top-5 层的 gate turn conditioning，early turn (蓝) vs late turn (橙红) 连线图，diff 标注在右侧，stats box 含 Wilcoxon p=3.73×10⁻⁸, r=0.975
- **(b)** Log-scale grouped bar chart — 4 模型 IID eval (绿) vs model-generated (橙红)，TG 的 30× GAR gap 用双向箭头+粗体标注突出；UG/LoRA-only 的 model-gen 数据标 "n/a"（未评估）；背景色带区分 IID/model-gen regime

**数据来源均已验证**: panel (a) 取自 `phase2_tg_s42_v7` registry 的 `eval_gate_dynamic_range_top5`，panel (b) IID 取自 `phase2_4way_eval`，model-gen 取自 v7 eval metrics。所有字号 ≥ 7pt。

---
