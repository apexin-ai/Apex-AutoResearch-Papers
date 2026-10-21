# director / loop_6.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`9e8a6dd8561fa46a37bc.json`](../../sessions/9e/9e8a6dd8561fa46a37bc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-24T01:44:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- DDL: EMNLP 2026 ARR 截止 2026-05-25，用户需在 OpenReview 手动提交
- 论文严格 8 页正文限制，当前 33 页（8 主体 + appendix）已合规
- Abstract 200 词限制，当前 188 词已合规
- 匿名 repo 已推送到 GitHub（commit fe038d9, 54 files），不要再改 remote URL（已配好 HTTPS+token）
- 本项目无活跃 GPU 实验，所有实验已完成，不需要分配 GPU

### 2. 🖥️ 基础设施快照
- 本地工作目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文源码: `docs/paper/` (main.tex + sections/*.tex)
- 匿名 repo: `/tmp/anon_repo/`（已 push 到 GitHub anonymous remote）
- 服务器 westd-15904: SSH 不可达，0 GPU，已建议用户释放（用户未回复）
- 无活跃进程 / 无 tmux / 无 cron 任务
- 数据源文件: `artifacts/_project/data/` 下有 table3 summaries、r14_a5_summary.md、qwq_l63_appendix_results.json

### 3. 📊 当前状态
**所有提交前工作已完成**：
- 数据审计：4 处修正已应用（OT-7B CI 14.4→14.0, position mediation 9→12pp, Fig3 caption 4.8→4.83%, Fig1 caption L0-L2→L0-L10）
- 质量检查 5 项全通过（related work ≥15 refs, appendix 无 Limitations, abstract 188w, 8p compliant, citations complete）
- qwq bib 补了 howpublished={Qwen Blog}
- 匿名 repo 补齐 src/ 和 19 个 scripts，已 push
- AI Assistants section 用 `\section*` 绕过 LaTeX counter overflow，编译正常
- Registry 无 RUNNING/PREPARING 实验
- Round 35 review 因用户长时间未回复已触发 Plan B 跳过
- 无等待中的 Worker 回调 / Cron

### 4. 📋 待办
- 用户回复确认 westd-15904 可释放 → 通知 Manager 释放服务器
- 用户提交 OpenReview 后反馈问题 → 协助解决
- 如收到审稿报告 → Read `review-report-action` skill，按协议处理
- 如用户要求新一轮 review → 调 `submit_paper_to_review` 提交

### 5. 🎯 战略上下文
- 核心发现：layer selection metric 是 hidden-state safety probing 的关键规格选择，单独改变 metric 可逆转结论（CR-composite → shallow layers → p=0.83 vs threshold-based → deep layers → p<0.005）
- HS advantage 是 encoder-conditional 且与 position 部分重叠——这是 boundary condition，不是 weakness
- 4 个模型：R1-8B (validated), OT-7B (validated), QwQ-32B (significant but suggestive), R1-32B (exploratory, below MDE)
- 论文定位为 methodological analysis paper（不是 method paper），贡献是 metric-induced layer selection bias + boundary conditions + negative results
- 易错点：不要把 safe-trace FPR 和 step-level FPR 混淆；paper 里 "11-50%" 是跨模型 HS static FPR 范围（OT-7B 11.1%, QwQ 50%），不是单模型指标
- 所有数据修正已完成并编译，不要再改数字除非发现新的 source mismatch


---
