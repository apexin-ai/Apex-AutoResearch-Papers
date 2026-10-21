# director / loop_2.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`063ab572bfe11d1d72ea.json`](../../sessions/06/063ab572bfe11d1d72ea.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-21T17:32:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验，纯 API 调用 + 论文写作项目
- 论文主文严格 8 页限制（EMNLP 2026 via ARR May cycle），Limitations/refs/appendix 不算
- Authorization scope 相关 claim 必须用 "suggestive" 而非 "definitive"——κ=0.385 是 Reviewer 反复盯的点
- Incompleteness 排名必须带 confound caveat——不能单独说 "consistently high" 不提 information-addition confound
- "robust two-tier" 已全文替换为 "two-tier"，不要再引入 "robust" 修饰

### 2. 🖥️ 基础设施快照
- 纯本地项目，无远程服务器
- 论文源码：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/`
- 主文件：`main.tex`，用 `\input{sections/X}` 引入各章节
- 根目录有 stale copies（`experiments.tex` 等），实际用的是 `sections/` 下的
- 编译：`cd docs/paper && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
- 补充分析数据：`artifacts/round8_supplementary/round8_supplementary_analyses.json`（bootstrap cluster + ranking CI + clause variance）
- 回归表数据：`artifacts/full_study/analysis/information_delta.json`
- 审稿 issue tracker：`artifacts/review_issues.yaml`

### 3. 📊 当前状态
**刚完成**：Round 8 Action Matrix 全部 15 条修复（3 Critical + 9 Warning + 3 Minor/补充）。具体：
- N1: SESOI external anchor + Anvari & Lakens 2021 + margin dependence 承认 + Ward's bootstrap cluster (Appendix H)
- N2: C4 auth scope 全文降级 "suggestive" + within-judge bootstrap ranking 99.5% stability
- N3: 完整回归表 Appendix G + Abstract confound caveat 强化
- W1-W9: API 超参数、condition blinding、C3 expansion、testable predictions P1/P2、bib 清理、数据可用性声明、clause-level variance (Appendix I)、per-type reliability limitation

**已编译验证**：14 页总计，主文 8 页（Conclusion 在 p8 结束），无 LaTeX warnings。

**等待中**：Reviewer 验证回复（已 `post_to_reviewer` 提交完整验证请求）。Reviewer 回复后需要：
1. 如全部 PASS → 提交 Round 9 审稿（`submit_paper_to_review`）
2. 如有 FAIL → 按 Reviewer 指出的问题修复后再提交

### 4. 📋 待办
- Reviewer 验证回复 PASS → `submit_paper_to_review` 提交 Round 9（推荐 `fresh` mode，因为本轮改动大）
- Reviewer 验证回复有 FAIL → 逐条修复，重新编译验证页数，再次提交 Reviewer
- Round 9 审稿完成 → 处理审稿报告（`review-report-action` skill），目标 3.5→4.0
- M1 (ferrari_defects_2018 bib key) 和 M2 (Ethics Statement) 是 camera-ready 级修正，不影响评分，可后续处理

### 5. 🎯 战略上下文
- 项目处于 **审稿迭代阶段**：Round 8 得分 3.5 (Borderline Conference)，目标 4.0 (Conference)
- 核心论文 story：policy ambiguity 对 LLM agent 的因果影响 (+34pp)，six-type taxonomy，Differential Nocuity framework
- **最大提分杠杆**：N1 (SESOI anchor) 和 N3 (confound transparency) 是两个 Reviewer 共识的 Critical，修好了对评分影响最大
- **易判断错的事**：
  - 不要把 root-level `experiments.tex` 当真源——`main.tex` 用的是 `sections/experiments.tex`
  - 页面预算极紧（恰好 8 页），任何新增文字都需要等量删减
  - bootstrap cluster stability 34.3% 不算高——不要过度声称 cluster 结果 "confirms" tier structure，用 "corroborates" / "consistent with"
  - Round 8 是 fresh review（非 continue），Round 9 建议也用 fresh mode 因为改动量大


---
