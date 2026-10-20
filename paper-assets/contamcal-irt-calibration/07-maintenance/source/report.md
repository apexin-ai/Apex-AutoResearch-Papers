# Handover — 2026-05-23

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）
- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）
- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）
- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）
- sft_gemma2_s0_sweep_v2（准备中）
- falcon3-7b-download（准备中）
- falcon3-7b-dl-v2（准备中）
- falcon3-7b-dl-v3（准备中）
- falcon3-7b-dl-v4（准备中）
- falcon3-7b-dl-v5（准备中）
- …另有 34 项

## 近期结论
- **analysis_dif_comparison** (success): Non-uniform DIF (gamma outside discrimination bracket) provides comparable or better model fit than uniform DIF (gamma inside bracket) on MMLU, as measured by WAIC/LOO and PPP, justifying the current modeling choice.
  [DIF Model Comparison (Uniform vs Non-uniform)](/api/workspace-files/projects/contamcal-irt-calibration/artifacts/analysis_dif_comparison/report/dif_model_comparison.md)
- **eval_falcon3_d000_gsm8k_s42_v2** (success): Falcon3-7B GSM8K d000 baseline to compute cross-benchmark transfer delta. Needed for Figure 3 heatmap (currently N/A).
- **eval_falcon3_d000_gsm8k_s42** (failed): Falcon3-7B GSM8K d000 baseline to compute cross-benchmark transfer delta. Needed for Figure 3 heatmap (currently N/A).

## 趋势
成功 287 / 负向 10 / 失败 76 / 共 389

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
cqa1-21977: 无 GPU 信息

## 告警
- eval_14b_mmlu_arc_westd: 训练失败 — unknown
- eval_7b_batch1_westd: 训练失败 — unknown
- eval_7b_batch_cqa1: 已被终止 — unknown
- eval_phi4_mmlu_arc_westd: 训练失败 — unknown
- eval_qwen7b_s123_cqa1: 训练失败 — unknown
- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown
- exp006-oracle-gsm8k-extended: 训练失败 — unknown
- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown
- exp006-pooled-s1only-gsm8k: 训练失败 — unknown
- exp_001_eval_05B_aligned_batch: 训练失败 — unknown
- exp_001_eval_05B_d000_s42: 训练失败 — unknown
- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown
- exp_001_eval_05B_d100: 训练失败 — unknown
- exp_001_eval_05B_d100_aligned: 训练失败 — unknown
- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown
- exp_001_eval_05B_d100_v2: 训练失败 — unknown
- exp_001_eval_15B_d000_s42: 训练失败 — unknown
- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown
- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown
- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown
- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown
- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown
- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown
- exp_001_sft_05B_d025_s123: 已被终止 — unknown
- exp_001_sft_100pct_05B: 训练失败 — unknown
- exp_001_sft_15B_d005_s123: 训练失败 — unknown
- exp_001_sft_3B_d000_v3: 训练失败 — unknown
- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown
- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown
- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown
- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown
- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown
- exp_001_sft_d005_05B: 已被终止 — unknown
- exp_001_sft_d005_05B_v2: 训练失败 — unknown
- exp_001_sft_d025_05B: 训练失败 — unknown
- exp_001_sft_d025_05B_v2: 训练失败 — unknown
- exp_001_sft_d025_3B: 训练失败 — unknown
- exp_001_sft_d100_15B: 训练失败 — unknown
- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown
- exp_002_signals_05B_s123_batch: 训练失败 — unknown
- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown
- exp_002_signals_3B: 训练失败 — unknown
- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown
- exp_002_signals_3B_v2: 已被终止 — unknown
- exp_002_signals_3B_v3: 已被终止 — unknown
- exp_002_signals_3B_v4: 训练失败 — unknown
- exp_002_signals_3B_v5: 训练失败 — unknown
- exp_002_signals_3B_v6: 训练失败 — unknown
- exp_002_signals_3B_v8: 训练失败 — unknown
- exp_002_signals_3B_v8_recovery: 训练失败 — unknown
- exp_002_signals_3B_v9: 训练失败 — unknown
- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown
- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown
- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown
- exp_004_fisher_heatmap_w4: 训练失败 — unknown
- exp_004_sim_sweep: 训练失败 — unknown
- exp_004_sim_sweep_v2: 训练失败 — unknown
- exp_004_sim_sweep_v3: 训练失败 — unknown
- exp_004_sim_sweep_v4: 训练失败 — unknown
- exp_004_sim_sweep_v5: 训练失败 — unknown
- exp_004_sim_sweep_v6: 已被终止 — unknown
- exp_005_noise_prop: 训练失败 — unknown
- exp_005_noise_prop_v2: 训练失败 — unknown
- exp_005_noise_prop_v3: 训练失败 — unknown
- exp_006_cross_family_irt_j16: 训练失败 — unknown
- exp_006_irt_05B: 已被终止 — unknown
- exp_006_irt_05B_v1: 训练失败 — unknown
- exp_006_j16_theta_extraction: 训练失败 — unknown
- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown
- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown
- exp_006_pooled_gsm8k_v1: 训练失败 — unknown
- exp_006_theta_extraction_j13: 训练失败 — unknown
- exp_008_base_pretrained_eval: 训练失败 — unknown
- exp_008_instruct_rl_proxy: 训练失败 — unknown
- gsm8k_gemma2_s42_westd: 训练失败 — unknown
- retrain_gemma2_d100_s123: 已被终止 — unknown
- retrain_qwen14b_d100_s123: 已被终止 — unknown
- sft_gemma2_s123_sweep: 训练失败 — unknown
- sft_qwen14b_s123_sweep: 训练失败 — unknown
- sft_falcon3_7b_d000_s42: 训练失败 — unknown
- sft_falcon3_7b_d005_s42: 训练失败 — unknown
- sft_falcon3_7b_d025_s42: 训练失败 — unknown
- sft_falcon3_7b_d050_s42: 训练失败 — unknown
- eval_falcon3_d000_s42: 训练失败 — unknown
- eval_falcon3_d005_s42: 训练失败 — unknown
- eval_falcon3_d025_s42: 训练失败 — unknown
- sft_yi15_9b_d000_s42: 训练失败 — unknown
- signals_falcon3_d100_s42: 训练失败 — unknown
- sft_yi15_9b_d000_s42_v2: 训练失败 — unknown
- eval_falcon3_d100_gsm8k_s42: 训练失败 — unknown
- sft_falcon3_7b_d100_s123: 训练失败 — unknown
- eval_falcon3_d000_gsm8k_s42: 训练失败 — unknown
