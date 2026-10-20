# Handover — 2026-05-18

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| gpqa_ds_random_s020 | Cross-task generalization: random eviction control on GPQA Diamond. DS-R1 random s020 to establish baseline phase gradient (expected NS or weak) for strategy specificity comparison. | — | — | — |
| gpqa_ds_importance_s030 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s030 as fourth condition. | — | — | — |
| gpqa_ds_importance_s025 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s025 as third condition (after s015 success, s020 running). | — | — | — |

## 待处理
（无）

## 近期结论
- **c8_llama_n250** (failed): Cross-architecture replication at n=250: LLaMA-8B (DeepSeek-R1-Distill-Llama-8B) should reproduce phase-modulated compound severity with large effect sizes (d_z>0.5) across all sparsity levels, confirming the phenomenon is not architecture-specific to Qwen2ForCausalLM. ← 基于 c3_llama
- **c10_lang_s020_s025** (success): Language switching dose-response: s=0.20 and s=0.25 conditions fill the gap between s=0.15 (4% switch rate) and s=0.30 (40%), verifying monotonic dose-response rather than threshold effect in language control disruption. ← 基于 c10_lang_switching
- **c8_llama_n250_fixed** (success): Phase-gated compound sparsity produces a monotonically increasing interaction index gradient (low > mid > high phase) in LLaMA-8B on MATH-500, with importance-based masking yielding at least 1.5x larger gradients than random masking across all sparsity levels (0.15-0.30), because importance-based selection preferentially removes redundant heads in exploration phases while preserving critical computation in verification phases. ← 基于 c3_llama
  [c8_llama_n250_fixed_analysis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c8_llama_n250_fixed/report/c8_llama_n250_fixed_analysis_2d3b67.md)

## 趋势
成功 70 / 负向 17 / 失败 17 / 共 134

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-22162: 无 GPU 信息

## 告警
- mvp_interaction_index_profiling: 训练失败 — unknown
- mvp_ii_profiling_v4: 训练失败 — unknown
- mvp_ii_profiling_v4b: 训练失败 — unknown
- mvp_ii_profiling_v4c: 训练失败 — unknown
- mvp_ii_profiling_v4d: 训练失败 — unknown
- mvp_ii_profiling_v4-random: 训练失败 — unknown
- mvp_v4a_r2: 训练失败 — unknown
- mvp_v4b_r2: 训练失败 — unknown
- mvp_v4c_r2: 训练失败 — unknown
- mvp_v4_legacy_s025: 训练失败 — unknown
- mvp_v4_legacy_s035: 训练失败 — unknown
- mvp_v4_float32_s030: 已被终止 — unknown
- mvp_v5_fixed_s020: 已被终止 — unknown
- mvp_v5_fixed_s030: 已被终止 — unknown
- qwen_importance_s015: 已被终止 — unknown
- qwen_importance_s020: 已被终止 — unknown
- qwen_importance_s025: 已被终止 — unknown
- qwen_importance_s030: 已被终止 — unknown
- v6_random_s030: 训练失败 — unknown
- v6_random_s030_r2: 训练失败 — unknown
- bf16_random_s015: 已被终止 — unknown
- bf16_random_s020: 已被终止 — unknown
- bf16_random_s025: 已被终止 — unknown
- bf16_random_s030: 已被终止 — unknown
- bf16_qwen_importance_s015: 已被终止 — unknown
- bf16_qwen_importance_s020: 已被终止 — unknown
- bf16_qwen_importance_s025: 已被终止 — unknown
- bf16_qwen_importance_s030: 已被终止 — unknown
- bf16_ds_imp_s015: 已被终止 — unknown
- bf16_ds_imp_s020: 已被终止 — unknown
- bf16_ds_imp_s025: 已被终止 — unknown
- bf16_ds_imp_s030: 已被终止 — unknown
- c3_llama_arch: 已被终止 — unknown
- c2_ds_n500: 已被终止 — unknown
- c2_qw_n500: 训练失败 — unknown
- r9c2-spike: 已被终止 — unknown
- r9c2-spike-v2: 已被终止 — unknown
- r9c2-spike-v3: 已被终止 — unknown
- acc_ds_dense_8k: 已被终止 — unknown
- acc_ds_s015_8k: 已被终止 — unknown
- acc_ds_s020_8k: 已被终止 — unknown
- acc_ds_s025_8k: 已被终止 — unknown
- acc_ds_s030_8k: 已被终止 — unknown
- gsm8k_qw_rand_s025: 训练失败 — unknown
- gsm8k_qw_rand_s030: 训练失败 — unknown
- c8_llama_n250: 训练失败 — unknown
- c10-lang-s020-s025: 已被终止 — unknown
