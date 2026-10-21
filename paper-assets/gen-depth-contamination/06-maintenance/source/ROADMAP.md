# gen-depth-contamination — Research Dashboard

> 最后更新: 2026-05-24 04:52 UTC | 更新原因: 论文提交就绪，Round 29 修复 + 两轮数据核查全部完成

## 核心方向
Prompt-chain recursive generation 下 K* discrimination boundary 的 empirical characterization：K*≤2 universal for web text（one-wash laundering），domain-dependent variation（arXiv K*=3）。详见 paper_framing.md。

## 当前进展
- **阶段**: EMNLP 2026 ARR May — 提交就绪
- **DDL**: 2026-05-25
- **Round 29 修复**: 全部完成（3 MF + 6 SF + 2 Minor + 数据核查 11 处修复）
- **数据核查**: 两轮完成，全文数字与 registry/artifacts 精确匹配
- **PDF**: 19 页（正文 8 页），0 critical warnings
- **匿名仓库**: commit `5abb1d3`，public，171 文件（code/ 122 + paper/ 49）
- **实验**: 165 registered, 126 DONE (95 success), 39 pending (post-submission backlog)

## 近期任务
- [x] Round 29 全部修复项（3 MF + 6 SF + 2 Minor）
- [x] Figure 4 字号修复 + 内容回滚验证
- [x] 数据自查第一轮（7 处修复）
- [x] 数据自查第二轮（4 处修复）
- [x] 匿名仓库同步 + requirements.txt
- [x] 服务器审计（westd-42896 已释放）
- [ ] OpenReview 提交（运维手动）
- [ ] ARR 审稿后根据反馈决定补实验方向

## GPU 预算
cqa1-22115: 4×RTX PRO 6000 Blackwell 98GB（空闲，提交前无实验需求）
westd-42896: 已释放

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D112 | 2026-05-25 | exp_014 独立指标结果定位为 rebuttal 补充证据，采用 "weak but direc | exp_014_naturalistic_v2, exp_014_independent_metrics |
| D111 | 2026-05-23 | D111: DDL前整合44个未引用实验数据——Code domain(4域)、14B/32B sc | seed_gemma27b_c4_s42, exp_013_cross_transfer |
| D110 | 2026-05-23 | arXiv K*=3 bootstrap CI: 仅LLaMA-8B通过CI，升级"two"→"th | arxiv_ci_llama8b, arxiv_ci_mistral7b, arxiv_ci_qwen7b |
| D109 | 2026-05-23 | Round 27 (3.5/5) Action Matrix: framing tightening | exp_019 |
| D108 | 2026-05-23 | Gemma-27B K*=1 (cross-scored), Gemma-2B 10K K*=2 ( | seed_gemma27b_c4_s42, exp_gemma2b_10k |
| D107 | 2026-05-22 | 发现 Pythia 主表/域表使用自评分 AUC（0.6539）而非声称的 Qwen cross-s | exp_001_pythia_depth, exp_002_olmo_depth |
| D106 | 2026-05-22 | 接受 LLaMA-8B 为 K*=1 (strict Bonferroni)，10K 结果作为 sa | exp_llama8b_10k |
| D105 | 2026-05-22 | D105: 10K between-sample variability 预案——5K 主表不变，1 | exp_pythia14b_c4_10k, exp_qwen_cont_10k, exp_llama8b_10k |
| D104 | 2026-05-22 | 叙事结构升级：headline 从 count-based (6/10 K*=2) 切换为 univ | — |
| D103 | 2026-05-22 | Round 26 Action Matrix 定稿：arXiv CI 呈现 + Bonferroni | — |

