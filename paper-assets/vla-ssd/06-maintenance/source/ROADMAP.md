# vla-ssd — Research Dashboard

> 最后更新: 2026-05-26 13:05 UTC | 更新原因: 论文 v14 终稿状态同步——全部改进完成，Reviewer 最终审查通过，等待用户提交

> 核心方向详见 paper_framing.md（D095→D105 修正链）

## 核心方向
VLA 微调如何重组 instruction routing——跨架构 × 跨任务。R² exit collapse 在所有 VLM→VLA 转换一致出现 (6/6, Δ=0.156-0.455)，VLA→VLA 转换无实质性 collapse (0/4, Δ=0.033-0.086)。三个 NLP controls (Llama-2-chat + Phi-3-mini + Qwen2.5-3B-Instruct) 确认 VLA-specificity (均 Δ=0.000)，覆盖 3/3 backbone families。

## 当前进展
- **阶段**: 论文 v14 终稿就绪，等待用户提交
- **实验**: 107 success / 17 negative / 7 failed / 154 total。Reviewer 逐条审查 17 negative，确认无需重试（D110）
- **统计加固**: seed robustness (4 seeds × 3 cells, std < 0.02)、bootstrap CI (MCCV 1000 iter)、permutation test (p=0.008)、post-hoc power analysis (power=0.37, n≥21)
- **Reviewer 内部评估**: CoRL 2026 中稿率 45-60% (MEDIUM-HIGH)
- **写作**: v14 — 全部 A-G 7 项 appendix 补强 + proofreading + notation 扫描 + §4.6 specificity caveat + camera-ready QA 全部完成
- **编译**: 0 error, 8 页正文, 42 页含 appendix
- **字体**: Type 3 文本字体全部清除，mathtext glyph 残留（CoRL 可接受），Worker 修复中
- **Abstract DDL (5/26)**: 已过，用户未确认提交状态（D109）
- **Paper DDL (5/29)**: 论文就绪，等待用户操作 OpenReview 提交

## 近期任务
- [x] 全部实验完成（107 success）
- [x] NLP controls 3/3 覆盖
- [x] 论文 v14 终稿（A-G 补强 + proofreading + notation + QA）
- [x] Reviewer 17 negative 逐条审查（D110：无需重试）
- [x] Reviewer story 最终审视（claim-evidence alignment 良好）
- [x] Camera-ready 格式检查（CoRL 2026 模板合规）
- [x] §4.6 L1 ablation specificity caveat
- [x] Post-hoc power analysis + BayesianVLA 引用
- [ ] Type 3 mathtext 字体完全清除（Worker 进行中，非阻塞）
- [ ] 用户确认 abstract 提交状态
- [ ] 用户操作 Paper 提交 (DDL 5/29)

## GPU 预算
westd-19183: 2× RTX PRO 6000 — 释放请求已提交 Manager 5 次未回复。全部实验完成，Reviewer 确认无可行实验（D108, D110）。GPU 保留仅因 Manager 未批准释放。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D112 | 2026-05-26 | 关闭 action-head decoding 实验线——discrete token pipeli | action_head_decoding_openvla_goal, action_head_decoding_openvla_goal_untrained |
| D111 | 2026-05-26 | 启动 action-head decoding 实验：区分 exit collapse vs for | action_head_decoding |
| D110 | 2026-05-26 | GPU 利用终结：Reviewer 逐条审查 17 个 negative，确认无一值得重试，GPU  | specificity_control_action, behavioral_smoketest |
| D109 | 2026-05-26 | Abstract DDL (5/26 11:59 UTC) 收口：用户未确认作者列表，提交状态未知， | — |
| D108 | 2026-05-26 | GPU 空置终结确认：v14 全部改进完成后无可跑实验，等待 Manager 批准释放 | qwen_nlp_control, clustered_bootstrap_reanalysis_v3 |
| D107 | 2026-05-26 | n=9 behavioral correlation 为设计硬约束，五种扩展方案均不合法，终结讨论 | clustered_bootstrap_reanalysis_v3, qwen_nlp_control |
| D106 | 2026-05-26 | Abstract Plan B: 用户 08:00 UTC 5/26 未确认则发最终提交包，abst | — |
| D105 | 2026-05-24 | 启动 Qwen NLP control 作为唯一额外实验——闭合 stated limitation | phi3_nlp_control, nlp_finetuning_control_v1 |
| D104 | 2026-05-24 | 不跑 behavioral ablation 实验。GPU 保留用于审稿应急，当前全力写作收尾 | behavioral_pilot_v2 |
| D103 | 2026-05-23 | Significance 提升走 framing 路径（Design Implications +  | phi3_nlp_control, nlp_finetuning_control_v1 |

