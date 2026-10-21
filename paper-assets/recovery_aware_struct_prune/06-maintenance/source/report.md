# Handover — 2026-05-31

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- floor_ablation_0p3_cka_only_20: Floor ratio ablation: lowering the MLP floor from 0.4 to 0.3 allows more aggressive pruning of unimportant layers while CKA-only criterion preserves critical structure. If floor=0.3 maintains GSM8K accuracy within 2pp of floor=0.4 baseline, it demonstrates robustness of CKA-guided pruning to floor choice.（已分配 ? GPU:?，等待提交）
- floor_ablation_0p5_cka_only_20: Floor ratio ablation: raising the MLP floor from 0.4 to 0.5 constrains pruning to be more conservative. If floor=0.5 improves GSM8K accuracy over floor=0.4, it suggests CKA-only criterion benefits from a higher minimum layer size. Maps the sensitivity curve of floor parameter on recovery quality.（已分配 ? GPU:?，等待提交）
- …另有 38 项

## 近期结论
- **eval_gsm8k_grpo_alpha4_20_v2** (killed): α=4.0 GRPO maintains reward 0.15-0.26 (vs α=1.0 collapse to ~0.008), predicting GSM8K accuracy significantly above α=1.0 baseline. v1 timed out at 774/1319 showing 62.93% interim — full eval needed to confirm α-dependent collapse hypothesis. ← 基于 eval_gsm8k_grpo_alpha4_20

## 趋势
成功 273 / 负向 23 / 失败 84 / 共 422
accuracy: 0.268 →（近 3 次 success）
avg_response_length: 1110.462 ↑（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westb-23072: 无 GPU 信息
westd-32935: 空闲 cuda:0, cuda:1, cuda:2, cuda:3

## 告警
- eval_math500_grpo_rasp_20: 训练失败 — unknown
- eval_math500_grpo_rasp_20_v2: 训练失败 — unknown
- eval_math500_grpo_rasp_20_v3: 训练失败 — unknown
- eval_math500_grpo_standard_20: 训练失败 — unknown
- eval_math500_sft_cka_only_20: 已被终止 — unknown
- eval_pass_k8_standard_20_grpo_qwen_math: 训练失败 — unknown
- eval_postprune_cka_only_30: 已被终止 — unknown
- eval_sft_alpha_0p5: 已被终止 — unknown
- eval_sft_cka_only_20_full: 训练失败 — unknown
- eval_sft_cka_only_20_full_v2: 已被终止 — Superseded by eval_sft_cka_only_20_n1319 which was submitted by fix worker
- eval_sft_rasp_20_seed123: 训练失败 — unknown
- eval_sft_rasp_20_seed456: 训练失败 — unknown
- eval_sft_rasp_qwen_math: 已被终止 — unknown
- eval_sft_standard_20_full: 训练失败 — unknown
- eval_sft_standard_20_n1319: 训练失败 — unknown
- eval_sft_standard_20_seed123: 训练失败 — unknown
- eval_sft_standard_20_seed456: 训练失败 — unknown
- eval_sft_standard_qwen_math: 已被终止 — unknown
- grpo_rasp_20: 已被终止 — unknown
- grpo_rasp_20_4096: 训练失败 — unknown
- grpo_rasp_qwen_math: 已被终止 — unknown
- grpo_rasp_rlvr_20: 训练失败 — unknown
- grpo_stage2_rasp_20: 已被终止 — unknown
- grpo_stage2_rasp_20_v3: 训练失败 — unknown
- grpo_stage2_rasp_20_v4: 已被终止 — unknown
- grpo_stage2_rasp_20_v5: 已被终止 — unknown
- grpo_stage2_rasp_20_v6: 训练失败 — unknown
- grpo_stage2_rasp_20_v7: 训练失败 — unknown
- grpo_stage2_standard_20: 已被终止 — unknown
- grpo_stage2_standard_20_v2: 训练失败 — unknown
- grpo_stage2_standard_20_v6: 训练失败 — unknown
- grpo_stage2_standard_20_v7: 训练失败 — unknown
- grpo_standard_20: 已被终止 — unknown
- grpo_standard_qwen_math: 已被终止 — unknown
- grpo_unpruned_baseline: 训练失败 — unknown
- inference_bench_full: 训练失败 — unknown
- inference_speedup_plan016: 训练失败 — unknown
- mvp_rasp_pipeline: 训练失败 — unknown
- mvp_rasp_pipeline_v2: 训练失败 — unknown
- scoring_ablation_batch_v2: 训练失败 — unknown
- scoring_ablation_magnitude_20: 训练失败 — unknown
- sft_alpha4_0_westd: 训练失败 — unknown
- eval_math500_sft_cka_only_20_v2: 训练失败 — unknown
- eval_gsm8k_grpo_cka_only_20: 训练失败 — unknown
- inference_bench_cka_only_20: 训练失败 — unknown
- eval_math500_grpo_standard_20_fair: 训练失败 — unknown
- eval_math500_sft_cka_only_20_v3: 训练失败 — unknown
- grpo_standard_20_extended_300: 训练失败 — unknown
- eval_math500_sft_cka_only_20_v4: 训练失败 — unknown
- eval_math500_sft_standard_20_2048: 已被终止 — unknown
- eval_humaneval_grpo_standard_20_fair_2048: 训练失败 — unknown
- eval_humaneval_grpo_standard_20_fair_2048_v2: 训练失败 — unknown
- eval_humaneval_sft_cka_only_20_2048: 训练失败 — unknown
- eval_humaneval_grpo_rasp_20_1p5b_2048: 已被终止 — unknown
- eval_humaneval_sft_rasp_20_2048_v3: 已被终止 — unknown
- eval_humaneval_sft_standard_20_2048_v4: 已被终止 — unknown
- grpo_shortgpt_20: 训练失败 — unknown
- eval_mbpp_grpo_standard_20: 训练失败 — unknown
- eval_mbpp_sft_standard_20: 训练失败 — unknown
- eval_mbpp_sft_standard_20_v3: 训练失败 — unknown
- eval_mbpp_sft_standard_20_clean: 训练失败 — unknown
- eval_mbpp_sft_shortgpt_20: 训练失败 — unknown
- eval_mbpp_grpo_shortgpt_20: 训练失败 — unknown
- eval_gsm8k_grpo_standard_20_step50: 已被终止 — unknown
- pipeline_cka_only_15: 训练失败 — unknown
- pipeline_standard_15: 训练失败 — unknown
- qwen_math_7b_feasibility: 训练失败 — unknown
- sft_qwen_math_standard_20: 训练失败 — unknown
- sft_qwen_math_standard_20_v2: 训练失败 — unknown
- grpo_standard_15_seed123: 训练失败 — unknown
- grpo_standard_15_seed456: 训练失败 — unknown
- grpo_standard_15_seed123_v2: 训练失败 — unknown
- grpo_standard_15_seed456_v2: 训练失败 — unknown
- eval_gsm8k_grpo_standard_15_seed123: 训练失败 — unknown
- eval_gsm8k_grpo_standard_15_seed456: 训练失败 — unknown
- grpo_standard_15_seed123_v4: 已被终止 — unknown
- grpo_standard_15_seed456_v4: 已被终止 — unknown
- eval_gsm8k_grpo_standard_15_seed123_v2: 训练失败 — unknown
- eval_gsm8k_grpo_standard_15_seed456_v2: 训练失败 — unknown
- eval_gsm8k_grpo_cka_only_25: 训练失败 — unknown
- eval_gsm8k_grpo_cka_only_25_v2: 训练失败 — unknown
- eval_gsm8k_grpo_random_20: 训练失败 — unknown
- eval_math500_sft_standard_25_v2: 训练失败 — unknown
- eval_math500_grpo_cka_only_25: 已被终止 — unknown
- eval_math500_sft_cka_only_25: 已被终止 — unknown
- eval_math500_grpo_random_20: 已被终止 — unknown
- eval_math500_grpo_standard_25: 已被终止 — unknown
- eval_math500_grpo_cka_only_20_v3: 已被终止 — unknown
- eval_math500_sft_random_20: 训练失败 — unknown
- pipeline_alpha4_0: 训练失败 — unknown
- pipeline_alpha4_0_v2: 训练失败 — unknown
- sft_alpha4_20_manual: 训练失败 — unknown
- eval_gsm8k_grpo_alpha4_20: 训练失败 — unknown
- eval_math500_grpo_alpha4_20: 训练失败 — unknown
- eval_math500_sft_cka_only_20_v5: 训练失败 — unknown
- eval_math500_sft_cka_only_20_v6: 已被终止 — unknown
- eval_gsm8k_sft_alpha4_20: 训练失败 — unknown
- eval_gsm8k_grpo_alpha4_20_v2: 已被终止 — unknown
- eval_gsm8k_sft_alpha4_20_v3: 已被终止 — unknown
- eval_math500_grpo_standard_20_fair_2048: 已被终止 — unknown
- eval_gsm8k_sft_alpha4_20_v4: 训练失败 — unknown
- eval_math500_sft_random_20_v2: 训练失败 — unknown
- pipeline_alpha0p5_20: 训练失败 — unknown
- pipeline_alpha2p0_20: 训练失败 — unknown
- eval_gsm8k_grpo_qwen_math_cka_only_20: 已被终止 — unknown
- pipeline_depth_first_20: 训练失败 — unknown
- eval_gsm8k_grpo_random_20_seed123: 已被终止 — unknown
- eval_gsm8k_grpo_qwen_math_cka_only_20_n500: 已被终止 — unknown
- eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2: 训练失败 — unknown
- eval_math500_sft_rasp_alpha1p0_20: 已被终止 — unknown
- eval_math500_sft_cka_only_20_westb: 已被终止 — unknown
- E_MATH500_SFT_QWEN_CKA: 训练失败 — unknown
- eval_gsm8k_sft_qwen_math_cka_only_20_n500: 训练失败 — unknown
- floor_ablation_0p6_cka_only_20: 训练失败 — unknown
- eval_gsm8k_postprune_cka_only_30_n1319: 已被终止 — unknown
- eval_math500_grpo_standard_20_fair_2048_v3: 已被终止 — unknown
- eval_math500_grpo_standard_20_fair_2048_v3b: 已被终止 — unknown
- eval_math500_sft_cka_only_20_fixed: 训练失败 — unknown
- eval_math500_sft_standard_20_fixed: 训练失败 — unknown
- grpo_random_20_retrain: 训练失败 — unknown
- eval_math500_sft_standard_25_fixed: 已被终止 — unknown
<!-- 已截断：超过 150 行限制，已执行 Pre-compaction Flush -->
