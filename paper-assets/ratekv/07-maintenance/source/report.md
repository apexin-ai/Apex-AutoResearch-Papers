# Handover — 2026-05-16

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| mistral_multi_seed_ppl_v2 | Mistral-7B 3-seed PPL v2 (seeds 42/123/456): Flat model, k=2. Fix: CUDA_VISIBLE_DEVICES mapping for GPU 1. Retry of mistral_multi_seed_ppl. | — | — | — |
| llama_multi_seed_ppl | Llama-3.1-8B 3-seed PPL (seeds 42/123/456): Spike model, k=2. Expect constrained ≈ uniform across seeds, confirming null result is statistically robust (Δ < seed std). | — | — | — |

## 待处理
- phi3_medium_hires_profiling_check（准备中）

## 近期结论
- **yi_8k_eval** (negative): Yi-1.5-9B 8K long-context eval: Spike shape (c=0.71, t1/t5=0.90). Expect no MCKP benefit at 8K — Spike control for Spread-specific long-context amplification claim.
- **mistral_multi_seed_ppl** (failed): Mistral-7B 3-seed PPL (seeds 42/123/456): Flat model, k=2. Expect constrained ≈ uniform across seeds, confirming null result is statistically robust (Δ < seed std).
- **mistral_8k_eval** (negative): Mistral-7B 8K long-context eval: Flat shape (c=0.22). Expect no MCKP benefit at 8K — Spike/Flat control for Spread-specific long-context amplification claim.

## 趋势
成功 65 / 负向 23 / 失败 14 / 共 121

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-37397: 无 GPU 信息

## 告警
- mvp_001: 训练失败 — unknown
- sanity_001: 训练失败 — unknown
- mvp_002: 训练失败 — unknown
- sanity_002: 训练失败 — unknown
- mvp_003: 训练失败 — unknown
- sanity_003: 训练失败 — unknown
- c4_cross_dataset_eval: 已被终止 — unknown
- l0_only_heuristic: 已被终止 — unknown
- l0_heuristic_baseline: 已被终止 — unknown
- greedy_constrained_ablation: 已被终止 — unknown
- cross_domain_calibration: 已被终止 — unknown
- c4_cross_dataset_eval_v2: 已被终止 — unknown
- cross_domain_calibration_v2: 已被终止 — unknown
- multi_seed_lowres: 已被终止 — unknown
- qwen72b_profiling: 已被终止 — unknown
- qwen25-hires-profiling: 已被终止 — unknown
- yi15_hires_float32_profiling: 已被终止 — unknown
- mistral_hires_bf16_2bitonly: 训练失败 — unknown
- mistral_hires_bf16_2bitonly_v2: 训练失败 — unknown
- mistral_hires_bf16_2bitonly_v3: 已被终止 — unknown
- w2_unconstrained_baselines: 已被终止 — unknown
- w9_compounding_scaling: 已被终止 — unknown
- qwen7b_8k_spotcheck: 已被终止 — unknown
- mistral_hires_constrained_mckp: 训练失败 — unknown
- phi3_medium_hires_profiling: 训练失败 — unknown
- qwen_compounding_sweep: 已被终止 — unknown
- gemma2_downstream_k2_4task: 训练失败 — unknown
- gemma2_downstream_k8_4task: 训练失败 — unknown
- falcon7b_hires_profiling: 已被终止 — unknown
- deepseekvl_hires_profiling: 已被终止 — unknown
- falcon7b_hires_profiling_v2: 已被终止 — unknown
- internlm2_constrained_mckp: 训练失败 — unknown
- mistral_multi_seed_ppl: 训练失败 — unknown
