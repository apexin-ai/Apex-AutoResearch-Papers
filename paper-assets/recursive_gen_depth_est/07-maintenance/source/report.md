# Handover — 2026-05-23

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- accum_v2_mix25（准备中）
- accum_v2_mix50（准备中）

## 近期结论
- **qwen25_7b_selfref_001** (success): Recursive generation depth signal (d0-d3) should persist in Qwen2.5-7B with self-reference feature extraction, similar to 14B scale results, supporting that the phenomenon is not model-scale-specific. ← 基于 cross_scale_qwen7b_001
- **plan_020_bootstrap_ci** (success): B=10,000 bootstrap resampling of per-sample 5-fold CV predictions provides stable 95% CIs for the 9 atlas cells, confirming that B=1,000 CIs had already converged.
- **plan_018_ordinal_baseline_v2** (success): Binary detection methods (Binoculars, Fast-DetectGPT) produce continuous scores that primarily distinguish d0 vs d1+; their ordinal resolution across d1/d2/d3 is near-chance, lacking the depth gradient captured by our 19-feature statistical pipeline.

## 趋势
成功 95 / 负向 14 / 失败 17 / 共 150

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
gpu-6000pro-2: 无 GPU 信息

## 告警
- mvp_pipeline_001: 已被终止 — unknown
- mvp_pipeline_002: 已被终止 — unknown
- mvp_pipeline_003: 已被终止 — unknown
- mvp_pipeline_004: 已被终止 — unknown
- mvp_pipeline_base_002: 已被终止 — unknown
- mvp_pipeline_base_003: 已被终止 — unknown
- mvp_pipeline_pythia_001: 已被终止 — unknown
- mvp_pipeline_qwen_base_004: 已被终止 — unknown
- cross_model_olmo_001: 训练失败 — unknown
- dcol_deberta_001: 训练失败 — unknown
- cross_model_olmo_temp09_001: 已被终止 — unknown
- dcol_deberta_002: 训练失败 — unknown
- dcol_deberta_003: 已被终止 — unknown
- olmo_temp09_002: 已被终止 — unknown
- dcol_deberta_004: 已被终止 — unknown
- dcol_deberta_005: 训练失败 — unknown
- cross_model_loo_001: 已被终止 — unknown
- depth_extension_binary_pairwise_001: 训练失败 — unknown
- depth_extension_olmo_d4d5_001: 训练失败 — unknown
- pythia7b_cross_scale_001: 已被终止 — unknown
- wild_data_redpajama_dolma_001: 已被终止 — unknown
- wild_data_calibration_002: 训练失败 — unknown
- cross_scale_llama3_8b_001: 训练失败 — unknown
- cross_model_recursive_chain_001: 训练失败 — unknown
- cross_scale_llama3_8b_002: 训练失败 — unknown
- qwen25_14b_scale_001: 训练失败 — unknown
- plan_018_binoculars_baseline: 已被终止 — unknown
- detector_ord_baseline_001: 已被终止 — unknown
- downstream_benchmark_001: 训练失败 — unknown
- qwen25-1p5b-instruct-001-phase45: 已被终止 — unknown
- qwen25-1p5b-instruct-001-ph45: 已被终止 — unknown
- qwen25-1p5b-instruct-001-ph45v2: 已被终止 — unknown
- qwen25-1p5b-instruct-001-ph45v3: 已被终止 — unknown
- qwen25-1p5b-instruct-002: 已被终止 — unknown
- qwen25_14b_scale_003: 训练失败 — unknown
- accum_mix50: 训练失败 — unknown
- accum_mix25: 训练失败 — unknown
- mink_ordinal_baseline_001: 已被终止 — unknown
- detectgpt_ordinal_baseline_001: 已被终止 — unknown
- detectgpt_ordinal_baseline_003: 训练失败 — unknown
- accum_pythia_nuc_001: 训练失败 — unknown
