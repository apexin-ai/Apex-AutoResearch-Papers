# research plan 009 forgetting figure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_009_forgetting_figure_20260515T184800_result.json`
- **Structured JSON:** [`4bd1e58572b34431ad79.json`](../../sessions/4b/4bd1e58572b34431ad79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出：**
- 绘图脚本：`/root/autodl-tmp/freige/scripts/plot_forgetting_dynamics.py`
- 图表 PDF：`/root/autodl-tmp/freige/figures/grpo_forgetting_dynamics.pdf`
- 图表 PNG：`/root/autodl-tmp/freige/figures/grpo_forgetting_dynamics.png`
- 已注册：`art_20260515_eace0b` (PNG), `art_20260515_319233` (PDF)

**图表内容（3 panels）：**
- **(a) Training Reward**：bf16 reward 显著高于 QLoRA（1.5-3.0 vs 0.1-1.2）
- **(b) Rel-F1**：QLoRA 从 SFT baseline (0.41) 暴跌至 ~0.01（lr=5e-6）或 ~0.22（lr=5e-5）；bf16 稳定在 0.45+
- **(c) Evi-F1**：QLoRA lr=5e-6 反升至 0.85（超 SFT baseline 0.80）；QLoRA lr=5e-5 降至 0.57；bf16 稳定在 0.81

**数据来源：**
- 训练曲线：trainer_state.json（bf16_ced_g8, qlora_ced_kl001, qlora_ced_lr5e6）
- 评估指标：registry 中 eval_grpo_g8_bf16 / mvp2_eval_ced_kl001_r4_multi / mvp2_eval_lr5e6_r1_ckpt* 系列

---
