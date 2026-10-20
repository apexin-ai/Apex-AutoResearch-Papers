# analysis plan 009 figure update

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_009_figure_update_20260515T162610_result.json`
- **Structured JSON:** [`14058545b084d5450b2c.json`](../../sessions/14/14058545b084d5450b2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 已更新并注册。更新内容：

- **Panel (a)**: bf16 GRPO 训练 reward 曲线（绿色虚线，三角标记）已加入
- **Panel (b)**: bf16 GRPO ckpt-80 (0.446) 和 ckpt-100 (0.455) 两个数据点，标注"112% of SFT"——与 QLoRA 的 0.217 (53% of SFT) 形成鲜明对比
- **Panel (c)**: bf16 evi_f1 数据点加入，annotation 改为"QLoRA-specific decoupling"
- **summary.json**: bf16 eval 数据（含 per-checkpoint 的 rel_f1/evi_f1/EDCR）已填入，`key_finding` 字段已更新

输出文件：
- `artifacts/plan_009_grpo_forgetting/grpo_forgetting_dynamics.pdf`
- `artifacts/plan_009_grpo_forgetting/grpo_forgetting_dynamics.png`
- `artifacts/plan_009_grpo_forgetting/summary.json`

---
