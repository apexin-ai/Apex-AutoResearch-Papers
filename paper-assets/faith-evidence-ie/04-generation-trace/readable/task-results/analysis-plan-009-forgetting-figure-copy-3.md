# analysis plan 009 forgetting figure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_009_forgetting_figure_20260515T175822_result.json`
- **Structured JSON:** [`957c3bfbbd3327f0d85f.json`](../../sessions/95/957c3bfbbd3327f0d85f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。

**文件**:
- `artifacts/plan_009_grpo_forgetting/grpo_forgetting_dynamics_v5.pdf` (矢量) + `.png`
- `artifacts/plan_009_forgetting_data_v5.csv` (完整数据)
- `artifacts/plan_009_grpo_forgetting/summary_v5.json`

**相比 v4 的改进**:
- QLoRA kl001 eval 从 2 个点扩展到 5 个 (step 10/50/60/90/100)
- bf16 G=8 eval 从 2 个点扩展到 3 个 (step 80/90/100)
- Step 0 = SFT baseline 显式标注
- Okabe-Ito 色盲友好配色，更清晰的标注

**论文引用关键数据点**:

| 指标 | QLoRA lr=5e-5 | QLoRA lr=5e-6 | bf16 G=8 | SFT baseline |
|------|--------------|--------------|----------|-------------|
| rel_f1 | 0.217 (-46.6%) | 0.014 (-96.6%) | **0.455 (+12.1%)** | 0.406 |
| evi_f1 | 0.575 (-28.0%) | **0.850 (+6.6%)** | **0.809 (+1.3%)** | 0.798 |
| EDCR | 0.854 | 0.988 | **0.632** | 0.712 |

**Narrative**: QLoRA GRPO 选择性摧毁 relation extraction 同时保留/提升 evidence extraction（task decoupling）。bf16 GRPO 两项指标均改善，证明 forgetting 是 QLoRA-specific 而非算法缺陷。

---
