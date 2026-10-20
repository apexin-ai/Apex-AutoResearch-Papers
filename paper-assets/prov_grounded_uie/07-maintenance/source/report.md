# Handover — 2026-05-14

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- dpo_candgen_cuda0（准备中）
- dpo_pilot_v1（准备中）

## 近期结论
- **dpo_candgen_v3_gpu1** (failed): DPO candidate generation (part 2/2, v3): resume from index 1925 after rewards.py TypeError fix (Line 216+224: str() cast for integer sentence indices). Prompts 1514-3026, 1102 remaining. ← 基于 dpo_candgen_v2_gpu1_r3
- **dpo_candgen_v3_gpu0** (failed): DPO candidate generation (part 1/2, v3): resume from index 380 after rewards.py TypeError fix (Line 216+224: str() cast for integer sentence indices). Prompts 0-1513, 1134 remaining. ← 基于 dpo_candgen_v2_gpu0
- **dpo_candgen_v2_gpu1_r3** (failed): DPO candidate generation (part 2/2, r3): prompts 1514+, no --max_samples (fixed slicing bug: script applies max_samples before resume_from). --device cuda:0 with CUDA_VISIBLE_DEVICES=1.

## 趋势
成功 6 / 负向 4 / 失败 9 / 共 25

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-37397: 无 GPU 信息

## 告警
- sft_baseline_v1: 训练失败 — unknown
- sft_baseline_v2: 已被终止 — unknown
- sft_eval_v3: 训练失败 — unknown
- posthoc_nli_v1: 训练失败 — unknown
- grpo_pilot_v1: 已被终止 — unknown
- posthoc_nli_v2: 已被终止 — unknown
- grpo_pilot_v2: 已被终止 — unknown
- grpo_v2_final_eval: 已被终止 — unknown
- dpo_candgen_cuda1: 已被终止 — unknown
- dpo_candgen_v2_gpu0: 训练失败 — unknown
- dpo_candgen_v2_gpu1: 训练失败 — unknown
- dpo_candgen_v2_gpu1_r2: 训练失败 — unknown
- dpo_candgen_v2_gpu1_r3: 训练失败 — unknown
- dpo_candgen_v3_gpu0: 训练失败 — unknown
- dpo_candgen_v3_gpu1: 训练失败 — unknown
