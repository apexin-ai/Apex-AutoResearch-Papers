---
loop: 14
reason: max_messages
updated: '2026-05-25T15:39:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验在跑，无服务器资源分配——纯论文写作/投稿阶段
- 匿名仓库 commit author 必须是 `Anonymous <anonymous@example.com>`，本地 anon_repo git config 已设好，不要改
- 匿名仓库 URL 含 PAT token，force push 后必须清除 remote URL 中的 token
- EMNLP 2026 硬约束：正文 ≤8 页、Abstract ≤200 words、Limitations 在正文（不在 appendix）、ARR Checklist 在 OpenReview form 不在 PDF

### 2. 🖥️ 基础设施快照
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/`
- 编译：`paper_compile_and_check(project="struct_self_consist_ie")` pdflatex
- 匿名仓库：GitHub private repo，本地 clone 在 `docs/paper/` 同级的 `anon_repo/` 目录
- 无远程服务器在用，无 GPU 分配，无活跃进程/tmux/cron
- 模板文件 `acl.sty` + `acl_natbib.bst` 已与官方 acl-org/acl-style-files 完全一致

### 3. 📊 当前状态
DDL 日（2026-05-25）最终冲刺。本轮完成的工作：
- **Table 1 脚注修复**：星号标注与底线重叠，`\vspace` 从 -6pt → +3pt，已确认分开
- **Appendix 空白压缩**：floatsep/textfloatsep/captionskip 全面压缩，46→45 页
- **审计报告修复**：AUROC 0.82 引用从 tab:multiseed 改为 §5.1（最危险的叙事不一致）；tab:multiseed 描述改为 "on SciERC"；3 处 AI em-dash 改为逗号/从句
- **Related Work 第二 paragraph 扩充**：3→7 篇引用（+xu2024llmie, wang2025gptner, gero2023selfverification, wadhwa2023revisiting），第三 paragraph 压缩补偿
- **匿名仓库 author 泄漏修复**：amend + force push，所有 8 个 commit 均为 Anonymous，旧 hash 404
- **ACL 模板对齐检查**：acl.sty/bst 完全一致，preamble 9 个核心包完全一致，正文恰好 8 页
- **引用验证**：60 条 bib，5 条 info-inconsistency 均确认为真实论文
- 当前编译状态：45 页，0 critical warning，PASS
- Registry 无 RUNNING/PREPARING 实验
- 无等待中的 Worker 回调或 Cron

### 4. 📋 待办
- 用户完成 OpenReview 手动提交 → 无需我方操作
- 用户要求同步匿名仓库最新改动 → `director_post_to_main_agent` 让 Agent 执行 git add/commit/push（注意 author 设置）
- 用户要求再次审稿 → `submit_paper_to_review` with `recommended_review_mode="fresh"`（距上次改动大，建议 fresh）
- 收到 Review Director 审稿报告 → 按 review-report-action skill 处理（Holistic Pass → Per-Comment Action Matrix）

### 5. 🎯 战略上下文
- 项目核心结论：NER 的 self-consistency 存在 correlation-selection gap——QE 信号预测质量好（AUROC 0.82）但选择无用。根因是 degeneracy（12-68%）+ signal alignment collapse（α→0）
- 论文定位：diagnostic/analysis contribution，不是 method paper。Holm-corrected p_adj=0.055 是 borderline，Abstract 已用 "conditional gains" 降级
- 关键决策链：GroupKFold probe 结果（CoNLL 0.882, FewNERD 0.636, SciERC 0.630）已写入论文；Narrative B（diagnostic framework）已 patch 完成
- 易错点：(1) tab:multiseed 只有 SciERC 数据，不要引用它来支撑跨数据集的 claim（本轮刚修过）；(2) appendix 有 37 个 section，\alphalph 不能删；(3) Discussion 只有 7 行，审稿人可能追问，但 DDL 日不冒险加内容
