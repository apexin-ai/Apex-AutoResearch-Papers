# recursive_gen_depth_est — Research Dashboard

> 最后更新: 2026-05-20 20:02 UTC | 更新原因: 更新为项目收尾状态——论文定稿，等用户确认投稿/归档

## 核心方向
Ordinal generation depth estimation：给定文本，估计其经历了多少轮递归生成（d0-d3）。详见 paper_framing.md。

## 当前阶段
**项目收尾 — 论文定稿完成，等用户确认投稿/归档**

## 当前进展
- **核心矩阵 9/9**：69-86% 4-class (mean 78.4%)；d1-d3: 59-82%
- **14B Cross-Scale 完成**：3 策略全覆盖，EDD₀.₇₀=0，accuracy 2× chance（50.8%）
- **Binoculars 收敛验证**：78.1% vs 78.4% (p>0.05)；Merged-30 82.6% (+4.2pp)
- **Membership Inference Baselines 完成**：DetectGPT 28.8% / Min-K% 33.2% / Binoculars threshold 69.8%
- **DeBERTa/RoBERTa-DCOL**：neural << RF，simple features beat neural
- **Accumulation v3**：mix25 70.1% / mix50 69.1%（full-replacement ceiling 84.2%）
- **R16 Fresh Review 3.0 Findings**：3 critical 全部修复（14B EDD=0 reframe / novelty 降调 / cross-strategy scope）
- **蒸馏独立验证**：25 篇论文确认 "No paper estimates recursive generation depth" novelty gap
- **论文编译通过**：25 页无 warning，8 页主文 + unlimited refs + limitations

## 收尾状态
- 论文定稿 ✅（R16 修改 + Reviewer 终审 PASS + 蒸馏验证）
- review_issues.yaml 更新 ✅（N1-N3 resolved, W2/W6-W8 wont_fix with reasons）
- 蒸馏完成 ✅（research + writing skills 生成）
- 审稿申请已提交 ⏳（apr_20260520T135843_ifm3 待用户确认）
- **等用户决定**：提交 ARR / 跳过内审直接投 / 归档

## GPU 预算
- gpu-6000pro-2: 项目配置 1× RTX PRO 6000 (cuda:0)
- 无 RUNNING 实验
- 用户明确指示不做新实验

## 评分预期
- R16 评分：3.0 Findings
- 修改后预期：~3.0-3.5（Findings 接收有把握）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D052 | 2026-05-22 | Accumulation EDD=3 preserved across all 3 cells; u | accum_v3, accum_olmo_temp_001, accum_pythia_nuc_002 |
| D051 | 2026-05-22 | Upgrade accumulation from pilot to systematic 3-ce | accum_pythia_nuc_002, accum_olmo_temp_001, accum_v3 |
| D050 | 2026-05-20 | D050: 14B 三策略全部完成 — nucleus 54.05% / temp09 50.5%  | qwen25_14b_topk50, qwen25_14b_temp09, qwen25_14b_scale_002, binoculars_14b_temp09 |
| D049 | 2026-05-19 | D049: Feature ablation 确认 6 core ppl features 是 ba | feature_ablation_overlap_001, binoculars_ordinal_baseline_001 |
| D048 | 2026-05-19 | D048: Binoculars 推翻 near-chance 假设 — 叙事从"二元检测失败"重构 | binoculars_ordinal_baseline_001, detectgpt_ordinal_baseline_004, mink_ordinal_baseline_002, deberta_pilot_gpt2xl_temp09 |
| D047 | 2026-05-19 | DeBERTa pilot 确认 simple features beat neural — Acc | deberta_pilot_gpt2xl_temp09, deberta_pilot_pythia_temp09, n2_deberta_finetune_001, dcol_roberta_v6_001 |
| D046 | 2026-05-19 | D046: 方法升级从 CORAL (方案1) 切换到 Cross-strategy domain  | cross_strategy_loo_zscore_001 |
| D045 | 2026-05-19 | D045: Method 升级——CORAL ordinal regression 作为主分类器，R | accum_v3_mix50, accum_v3_mix25, qwen25_14b_temp09, qwen25_14b_topk50 |
| D044 | 2026-05-19 | D044: Round 13 审稿 Action Matrix 执行 — 1 critical fi | qwen25_14b_temp09, qwen25_14b_topk50 |
| D043 | 2026-05-19 | D043: Round 12 审稿 Action Matrix — 2 must-fix + 7 s | qwen25_14b_temp09, qwen25_14b_topk50 |

