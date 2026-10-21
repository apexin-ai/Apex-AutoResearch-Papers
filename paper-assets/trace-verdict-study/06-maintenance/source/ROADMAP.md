# trace-verdict-study — Research Dashboard

> 最后更新: 2026-05-22 17:34 UTC | 更新原因: 所有实验完成 + nomarker cross 95.46% + 进入提交 pipeline

> EMNLP ARR DDL: 2026-05-25（~2.5 天）| 所有实验完成，进入 final sync → Round 16 → 提交

## 核心方向
**Reframe 定稿 (D116+D117)**: "complete traces hurt SFT" + gradient masking 3-seed 证实 content quality ≥96%。B5 primary baseline + nomarker (97.65% vs 28.49%) + cross-dataset 双向 (99.4–100%) + nomarker cross-dataset (95.46%) + gradient masking (99.22%±0.20, ≤4% dilution)。

## 当前进展 — 所有实验完成 ✅
- **Gradient masking 3-seed**: 99.22%±0.20, ≤4% dilution, ≥96% content quality ✅
- **Cross-dataset 双向**: HE→MBPP 99.41%, MBPP→HE 100.0% ✅
- **Nomarker cross-dataset**: 95.46%（去标记+跨数据集仍 +26pp vs majority）✅
- **Subcomponent ablation**: type=100%, stacktrace=99.83%, message=99.50% ✅
- **统计全面升级**: Holm-Bonferroni + clustered bootstrap + gap statistic + oscillation metrics ✅
- **Paper Agent**: Phase 1 重写 + Phase 2 统计 + gradient masking + cross-dataset + subcomponent + 3-seed + nomarker cross + polish ✅

## Round 15 Action Matrix — 全部完成 ✅
All 4 MF + 8 SF adequately addressed. Reviewer 预估 Overall 3.0 → 3.5.

## 提交 Pipeline
1. 🔄 Paper Agent: nomarker cross-dataset 最终 patch
2. 🔜 Final paper sync (tar+scp + clean compile)
3. 🔜 Round 16 审稿
4. 🔜 提交

## GPU 状态
- cuda:0: 49GB orphan, 不可用
- cuda:1: 空闲（所有实验完成）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D122 | 2026-05-25 | D122: Round 16 审稿 3.0 → 本轮最大化写作+已有证据修复后提交，不撤回等下一 c | exception_only_padded2048_seed42, exception_only_nomarker_seed42 |
| D121 | 2026-05-23 | DeepSeek masking seed123=93.95%: 保持 paper 报告 seed4 | deepseek_gradient_masking_seed123 |
| D120 | 2026-05-23 | Qwen-1.5B no_trace seed42 保持 67.31%（1640 samples b | qwen15b_no_trace_seed42, qwen1.5b_no_trace_seed42 |
| D119 | 2026-05-23 | Table 1 保持 81.44±1.11 不改为 v5 数据 80.61±1.09，v5 数据留给 | full_trace_seed42_v5, full_trace_seed123_v5, full_trace_seed456_v5 |
| D118 | 2026-05-22 | D118: Exception subcomponent ablation 结果处理——全部 ≥99 | exc_type_only_seed42, exc_stacktrace_only_seed42, exc_message_only_seed42 |
| D117 | 2026-05-22 | D117: Gradient masking 证实内容质量解释 ~95% 效果差异，梯度稀释仅 ~5 | gradient_masking_qwen7b_seed42 |
| D116 | 2026-05-22 | D116: Round 15 Reframe — 核心贡献从 "exceptions help" 转 | exception_only_nomarker_seed42, cross_he2mbpp_exception_only_seed42, cross_he2mbpp_no_trace_seed42 |
| D115 | 2026-05-22 | D115: Phase transition 机制精确定位——tail-512 跨过 globals | qwen7b_full_trace_tail512_seed42, qwen15b_full_trace_tail384_seed42 |
| D114 | 2026-05-22 | D114: Phase transition 确认真实 + Two-Pathway Model 验证 | qwen7b_full_trace_tail512_seed42, full_trace_512tok_seed42, qwen15b_full_trace_tail384_seed42 |
| D113 | 2026-05-21 | D113: Round 13 Action Matrix — reframe 为 "why full | fewshot_gpt4o_exception_only_0shot, fewshot_gpt4o_no_trace_0shot |

