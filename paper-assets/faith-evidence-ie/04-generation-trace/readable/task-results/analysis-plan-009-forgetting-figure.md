# analysis plan 009 forgetting figure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_009_forgetting_figure_20260515T162745_result.json`
- **Structured JSON:** [`64ce05592f732035d294.json`](../../sessions/64/64ce05592f732035d294.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 1. 数据点统计
- **4 个 GRPO 训练 run** 的 step-level reward 轨迹（共 96 个数据点）
- **3 个 run** 有 checkpoint eval 数据（共 9 个 eval 数据点）
- **1 个 SFT baseline** 对照

### 2. 数据维度齐全/缺失

| 维度 | 状态 |
|------|------|
| Training reward (step-level) | 4/4 run 齐全 |
| rel_f1 eval | 3/4 (bf16 G=4 缺 eval) |
| evi_f1 eval | 3/4 |
| EDCR eval | 3/4 |
| **缺失** | bf16 G=4 无 eval；QLoRA kl001 早期 checkpoint (step 10-80) 无 eval；bf16 G=8 早期 checkpoint (step 10-70) 无 eval；flatnli/extract reward type 无 eval |

### 3. 图的内容和关键发现

**2×2 四面板图 (`grpo_forgetting_dynamics_v4.pdf/png`)**：

- **(a) Training Reward**: bf16 runs 达到 1-4 reward，QLoRA 仅 0.2-1.4。bf16 reward 2-6× 高于 QLoRA。
- **(b) Relation F1**: bf16 G=8 达 0.455 (+12.1% vs SFT)，QLoRA kl001 崩到 0.217 (-46.6%)，QLoRA lr5e6 崩到 0.014。
- **(c) Evidence F1**: QLoRA lr5e6 的 evi_f1 持续上升到 0.850 但 rel_f1 接近 0 → **task decoupling**。bf16 G=8 evi_f1=0.809。
- **(d) EDCR**: QLoRA 产生 85-99% distractor citations，bf16 仅 63%。

### 4. 文件路径
- 图: `artifacts/plan_009_grpo_forgetting/grpo_forgetting_dynamics_v4.pdf` / `.png`
- 数据汇总: `artifacts/plan_009_grpo_forgetting/summary_v4.json`
- Reward 轨迹: `artifacts/plan_009_grpo_forgetting/reward_trajectories.json`
- 服务器脚本: `/root/autodl-tmp/artifacts/plan_009_grpo_forgetting/plot_forgetting_v4.py`

---
