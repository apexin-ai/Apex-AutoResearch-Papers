# analysis plan 009 forgetting figure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_009_forgetting_figure_20260515T174224_result.json`
- **Structured JSON:** [`0bcb72cb19ef7537c122.json`](../../sessions/0b/0bcb72cb19ef7537c122.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据汇总完成。结果：

**三个 GRPO 实验的 per-checkpoint 数据已汇总到 CSV**:
`artifacts/plan_009_forgetting_data.csv`

### 数据概览

| 实验 | 量化 | G | lr | eval步数 | rel_f1 范围 | evi_f1 范围 | EDCR 范围 |
|------|------|---|----|----|-----------|-----------|----------|
| qlora_ced_kl001_lr5e5 | QLoRA-4bit | 4 | 5e-5 | 10-100 (每10步) | 0.003→0.217 | 0.423→0.720 | 0.854→0.998 |
| qlora_ced_lr5e6 | QLoRA-4bit | 4 | 5e-6 | 20-100 (每20步) | 0.007→0.014 | 0.628→0.850 | 0.988→0.994 |
| bf16_ced_g8 | bf16-LoRA | 8 | 5e-5 | 80/90/100 | 0.446→0.455 | 0.803→0.809 | 0.632→0.641 |

### 缺失数据（需后续补跑）

1. **qlora_ced_kl001_lr5e5 step 40**: eval 目录存在但 metrics.json 为空（eval 未完成）
2. **qlora_ced_kl001_lr5e5 step 70/80**: eval OOM killed (exit -9)，无 metrics
3. **bf16_ced_g8 step 10-70**: 无 eval 数据（仅评估了 step 80/90/100）
4. **bf16_ced_g8 训练 reward**: step 15/30/40/55/70/80/95 的 trainer_state 中无 reward 字段（可能是 checkpoint-save-only 日志条目）

### 关键发现

- **QLoRA 4-bit lr=5e-5**: rel_f1 从 0.003 升至 0.217，但 evi_f1 从 0.72 降至 0.57 — 经典 forgetting 解耦
- **QLoRA 4-bit lr=5e-6**: rel_f1 基本不动（~0.01），evi_f1 反而从 0.63 升到 0.85 — 学得太慢
- **bf16 LoRA G=8**: rel_f1=0.455 远超 QLoRA，evi_f1=0.809 也更高，EDCR 低至 0.63 — 精度保持下同时提升双指标

---
