# director / loop_3.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`cecce351f0269be3f8df.json`](../../sessions/ce/cecce351f0269be3f8df.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-22T00:22:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- 无 GPU 项目，全部实验通过 API 调用完成，不涉及 GPU 分配
- 论文主文严格 8 页限制（EMNLP 2026 ARR），Conclusion 当前恰好在 page 8 底部，任何文本增加都可能溢出
- ARR Responsible NLP Checklist 在 OpenReview submission form 手动填写，不在论文 PDF 中
- 3 个保留的 orphan bib entries（yu_causal_2026, lin_ask_to_clarify_2025, mu_can_llms_2023）是审稿建议引用，Round 11 结果出来前不删不引
- ferrari_defects_2018 bib key 实际是 Rosadini 2019，已决定保持现状避免破坏引用链

### 2. 🖥️ 基础设施快照
- 服务器：localhost（ubuntu），无远程服务器
- 论文目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/`
- 产出目录：`projects/policy_ambiguity_safety/artifacts/`
- EMNLP checklist 草稿：`artifacts/emnlp_arr_checklist_draft.md`（已校对通过）
- 编译：pdflatex，15 页总计，主文 8 页，0 undefined refs
- 无活跃进程 / 无 tmux / 无 cron

### 3. 📊 当前状态
**刚完成**：Round 10 全部修复 + 验证 + submission-ready 最终检查 + 叙事线审视修复（Conclusion 对齐）
**Registry**：plan_009 PREPARING（cross-judge agreement 实验，一直未启动，非阻塞）；其余 15 个全 DONE
**等待中**：
- Round 11 审稿审批卡待用户确认（A 群 19:58 发出，apr_20260521T195816_4esu）
- 用户回复 3 项：API cost 实际金额、代码 license（默认 MIT）、GitHub URL

### 4. 📋 待办
- Round 11 审稿审批通过 → 等审稿结果 → 按报告处理协议逐条处理
- Round 11 评分 ≥4.0 → 论文基本定稿，清理 3 个保留 orphan bib，准备最终提交
- Round 11 仍 3.5 → 分析剩余提分点，评估是否需要加实验或仅文本微调（当前判断：Round 10 已执行审稿人全部升分条件，大概率升分）
- 用户确认 API cost/license/URL → 更新 checklist 草稿，标记 submission-ready

### 5. 🎯 战略上下文
- **核心 story**：policy ambiguity 因果导致 +34pp 违规（OR=15.1），incompleteness 是一致性最高风险类型（7/7 模型 ≥46%），agents 展现 Disambiguation Deficit（<11% awareness）
- **关键决策链**：D020 framing pivot（Uniform→Differential Nocuity）→ D022 Round 1 审稿 Action Matrix → Round 9/10 连续 3.5，核心问题是 claims-evidence calibration gap → Round 10 执行全部升分条件（弱化 auth scope/hierarchy claims + 4 项 robustness 分析）
- **易错点**：
  1. Conclusion 和 Abstract/Intro 的 claim 措辞必须一致——之前 Conclusion 漏改 "two-tier type hierarchy"（已修复）
  2. Kendall's W 五模型 p=0.072 不显著，不要说 "confirms" hierarchy，只能说 "moderate concordance"
  3. Auth scope 52pp 必须始终伴随 κ=0.385 caveat，不能单独呈现
  4. Limitations 8 段看着长但不计入页限，审稿人评价为 S3 (transparency)，不要删
  5. consistency check 工具只扫 experiments.tex，报的 orphan 大部分是假阳性，必须全文 grep 验证


---
