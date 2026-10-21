# Handover — 2026-05-25

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- pd_a055_s49_fp32（准备中）
- pd_a055_s48_fp32（准备中）
- pd_a055_s47_fp32（准备中）
- pd_a055_s46_fp32（准备中）
- pd_a055_s45_fp32（准备中）
- pd_a050_s49_fp32（准备中）
- pd_a050_s48_fp32（准备中）
- pd_a050_s47_fp32（准备中）
- pd_a050_s46_fp32（准备中）
- pd_a050_s45_fp32（准备中）
- …另有 11 项

## 近期结论
- **c2_opt13b_a050_s42_fp32** (negative): OPT-1.3B at α=0.50 seed 42: cross-architecture validation of phase diagram transition region — if canary→downstream lead-lag is architecture-general, PermG forward detection should match Pythia-410M rates (6/8)
  [c2_opt13b_a050_s42_fp32_d102](/api/workspace-files/projects/distrib_canary_collapse/artifacts/c2_opt13b_a050_s42_fp32/data/c2_opt13b_a050_s42_fp32_d102.json)
- **c2_opt13b_a050_s43_fp32** (failed): OPT-1.3B at α=0.50 seed 43 replication: cross-seed consistency of PermG forward detection in the transition region on a non-Pythia architecture
- **null_fpr_s51_fp32** (success): Null experiment (α=0.00) for FPR estimation: no synthetic data contamination, all detection methods should show p>0.05, contributing to narrower FPR CI with 15 seeds

## 趋势
成功 154 / 负向 5 / 失败 23 / 共 212
累计 GPU: 8.4h

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-19828: 空闲 cuda:0, cuda:1

## 告警
- mvp_rep42: 已被终止 — unknown
- mvp_rep43: 已被终止 — unknown
- mvp_rep44: 已被终止 — unknown
- mvp_v2_rep42: 已被终止 — unknown
- mvp_v2_rep43: 已被终止 — unknown
- mvp_v2_rep44: 已被终止 — unknown
- mvp_v3_rep42: 训练失败 — unknown
- mvp_v3_rep43: 训练失败 — unknown
- alpha_sweep_a025_s42: 已被终止 — unknown
- alpha_sweep_a025_s42_v2: 已被终止 — unknown
- alpha_sweep_a010_s42: 已被终止 — unknown
- alpha_sweep_a060_s42: 已被终止 — unknown
- plan_006_s42: 训练失败 — unknown
- plan_006_s43: 已被终止 — unknown
- gen_wiki_gpt2m_a100_s42: 已被终止 — unknown
- plan_006_s42_resume: 已被终止 — unknown
- gen_wiki_gpt2m_a100_s42_v2: 已被终止 — unknown
- generalize_pythia1b_c4_a100_s42: 训练失败 — unknown
- interv_pred_s43: 已被终止 — unknown
- alpha_sweep_a060_s42_v2: 已被终止 — unknown
- alpha_sweep_c4_a050_s42: 已被终止 — unknown
- gen_gpt2m_a100_s43: 已被终止 — unknown
- scale_14b_a050_s42_bf16: 已被终止 — unknown
- alpha_sweep_a010_s42_bf16: 已被终止 — unknown
- gen_opt13b_a100_s43_bf16: 已被终止 — unknown
- alpha_sweep_a005_s42: 已被终止 — unknown
- qwen35_08b_wiki_a100_s42: 已被终止 — unknown
- interv_pred_a075_s42: 已被终止 — unknown
- smollm3_3b_wiki_a100_s42: 已被终止 — unknown
- smollm3_3b_wiki_a100_s42_v2: 训练失败 — unknown
- alpha_sweep_a060_s42_fp32: 已被终止 — unknown
- interv_pred_a075_s42_fp32: 已被终止 — unknown
- alpha_sweep_a060_s42_fp32_v2: 已被终止 — unknown
- interv_pred_a075_s42_fp32_v2: 已被终止 — unknown
- alpha_sweep_a040_s42_fp32: 训练失败 — unknown
- scale_69b_a100_s43_fp32: 训练失败 — unknown
- interv_pred_14b_s42_fp32: 已被终止 — unknown
- phase_diagram_t25_a060_s42_fp32: 训练失败 — unknown
- phase_diagram_t25_a045_s42_fp32: 训练失败 — unknown
- phase_diagram_t25_a050_s42_fp32: 训练失败 — unknown
- phase_diagram_t20_a060_s43_fp32: 训练失败 — unknown
- phase_diagram_t25_a060_s42_fp32_v2: 训练失败 — unknown
- phase_diagram_t25_a050_s42_fp32_v2: 训练失败 — unknown
- phase_diagram_t25_a075_s43_fp32: 训练失败 — unknown
- phase_diagram_t10_a050_s43_fp32: 训练失败 — unknown
- phase_diagram_t25_a075_s43_fp32_v2: 训练失败 — unknown
- scale_14b_t10_a050_s42_fp32: 训练失败 — unknown
- scale_14b_t10_a060_s42_fp32: 训练失败 — unknown
- scale_14b_t10_a075_s42_fp32: 训练失败 — unknown
- scale_14b_t15_a050_s42_fp32: 训练失败 — unknown
- scale_14b_t15_a060_s42_fp32: 训练失败 — unknown
- scale_14b_t10_a050_s42_fp32_19828: 训练失败 — unknown
- c2_opt13b_a050_s43_fp32: 训练失败 — unknown
