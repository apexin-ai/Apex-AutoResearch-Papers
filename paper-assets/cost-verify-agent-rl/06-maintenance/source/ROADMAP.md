# cost-verify-agent-rl — Research Dashboard

> 最后更新: 2026-05-25 15:16 UTC | 更新原因: 用户确认审稿等待期不做额外实验/rebuttal 预准备

> 最后更新: 2026-05-25 | 更新原因: 用户确认审稿等待期不做额外实验/rebuttal 预准备

## 核心方向
Step-independent agent RL 的双机制信用分配病理诊断（信息丢失 M1 + 符号错误归因 M2）+ episode-level 修复。详见 paper_framing.md。

## 当前进展
- **阶段**: 审稿等待期 — ARR 2026-05-25 AoE 已提交
- **投稿目标**: EMNLP 2026 via ARR
- **状态**: 所有实验已停止（用户指令），等待审稿结果，不做额外准备
- **Round 2 审稿**: Overall 3.0，16/17 项修改完成（N2 Cell B 多 seed 因时间约束未完成）
- **理论框架**: 「不同口径」framework 数据验证 PASS
- **数据审计**: P0/P1 全部修复，Reviewer 独立确认 PASS
- **编译**: 0 critical warnings，主文 ≤8 页合规

## Seed 分类 (N=11, 最终)
| 类别 | Seeds | 比例 |
|------|-------|------|
| Collapsed | seed2048, seed42, seed8 | 3/11 = 27% |
| Stagnant (NS vs SFT) | seed100, seed200, seed300, seed2 | 4/11 = 36% |
| Generalized (p<0.01) | seed1†, seed4, seed5, seed6 | 4/11 = 36% |

† seed1 用 RAGEN built-in eval，checkpoint 不可用

## 近期任务
- [ ] 等待 ARR 审稿结果（预计 4-6 周）
- [x] ARR 提交（2026-05-25）
- [x] Round 2 全部 16/17 项审稿修改
- [x] 数据审计 P0/P1 修复 + Reviewer 确认

## GPU 状态
| 服务器 | GPU | 状态 |
|--------|-----|------|
| bjb1-17606 | cuda:0 | 🔴 已停止，无实验运行 |

## GPU 预算
本项目保留 bjb1 ×1（cuda:0）。审稿等待期间不消耗 GPU 资源。

## 保留资产
- SFT checkpoint（bjb1）
- hsweep 实验数据（bjb1）

## 核心风险
1. **Cell B 单 seed 数据**: Table 1 Cell B 仅 seed1（5.97%），其他 cell 有多 seed，statistical power 不对称，审稿人高概率质疑
2. **Eval 可复现性**: T=0.4 eval 方差（seed5: 20pp range）— Limitations 已说明
3. **OOD 泛化 seed-dependent**: 仅 4/11 generalized — 诚实讨论
4. **Cell C 缺失**: 无法独立隔离 M2 — Discussion 已承认

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D145 | 2026-05-24 | D145: Table 1 Cell B seed 数修正 — 5.97% 实为 seed1 onl | factorial_h2_episodeadv_seed1, factorial_h2_episodeadv_seed2 |
| D144 | 2026-05-24 | Round 6 Action Matrix: Cell B seed2 OOD eval first | factorial_h2_episodeadv_seed1, factorial_h2_episodeadv_seed2 |
| D143 | 2026-05-24 | Cell D ScienceWorld：立即启动 SFT 数据生成（CPU 并行 hsweep），h | scienceworld_sft_data_gen, hsweep_h10_seed2_retry2 |
| D142 | 2026-05-24 | D140 修正：禁止用 ALFWorld SFT 数据做 ScienceWorld Cell D，必 | scienceworld_sft_data_gen |
| D141 | 2026-05-24 | D139 修正：hsweep_h10_seed2_retry 实际健康（96% GPU），继续跑而非 | hsweep_h10_seed2_retry |
| D140 | 2026-05-24 | Cell D SFT 数据修复设 1h 硬截止：超时则用旧数据或放弃 Cell D | scienceworld_sft_data_gen |
| D139 | 2026-05-24 | 放弃 hsweep h=10 seed2（两次失败），seed1 数据足以支撑 h-sweep 图 | hsweep_h10_seed2, hsweep_h10_seed2_retry |
| D138 | 2026-05-23 | D137 修正——采纳 Reviewer 的 2×2 框架（训练稳定性 × OOD 泛化）和修正后的 | exp029_seed100_step10_ood_eval, exp029_seed200_step5_ood_eval |
| D137 | 2026-05-23 | 放弃 "gradual emergence" claim（D136 修正）：seed100 step | exp029_seed100_step10_ood_eval, exp029_seed200_step5_ood_eval, exp029_seed100_resume_step10 |
| D136 | 2026-05-22 | 采纳 Reviewer 建议调整 OOD claim 措辞：从 binary "healthy ge | exp029_seed100_resume_step10, exp029_seed200_episode_v4 |




