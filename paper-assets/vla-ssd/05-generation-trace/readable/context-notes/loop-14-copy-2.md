# agent / loop_14.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`109863b0d2ca0e738048.json`](../../sessions/10/109863b0d2ca0e738048.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-27T06:20:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配，无实验在跑——纯论文写作阶段
- 论文 body 必须 ≤8 页，无 `\enlargethispage`（R15-N4 格式违规已复发两次，第三次 = CRITICAL）
- Discussion 已用 `\paragraph{Practical implications and conclusion.}` 合并段落省间距，不可再拆回两个 `\paragraph`
- 所有 figure vspace 已统一为 `-4pt`，不可回退到 `-6pt/-8pt`
- 动态因果语言已清理（"produces/drives/shapes" → "is associated with"），新增文本必须延续 correlational phrasing
- "replacing rollout evaluation" 已被 Director 标为 overclaim（SF-2），必须用 "supplement"

### 2. 🖥️ 基础设施快照
- 纯本地论文项目，无远程服务器/GPU
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文源码：`docs/paper/`（main.tex → abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, appendix.tex, references.bib）
- 编译：`cd docs/paper && pdflatex -interaction=nonstopmode main.tex`（需跑两遍解 cross-ref）
- 产出目录：`artifacts/`（rebuttal 在 `artifacts/_project/paper/anticipated_rebuttal_v2.md`）
- 活跃进程：无。无 cron，无 Worker，无 tmux session

### 3. 📊 当前状态
刚完成 R17 审稿 3 SF + 1 Minor 修复，已汇报 Director，等待 Director 回复。

具体完成项：
- SF-1：删除 `\enlargethispage`，精简 Practical Implications（10→5 句），详细论述移入 Appendix `Extended Practical Implications`
- SF-2：`replacing` → `supplement` + 内联 evidence qualification + `observed` 限定
- SF-3：Appendix permutation test 描述扩展（明确 transition-type shuffle、9 trained values、test statistic）
- M-1：`non-significant at conventional levels` 已内联

编译状态：0 errors, 0 undefined refs, 0 Type 3 fonts, 43 pages, body 8 pages, References page 9

Registry：无 RUNNING/PREPARING 实验。全部实验线已关闭（D112 关闭 Action-Head Decoding）

### 4. 📋 待办
- Director 回复 R17 修复确认 → 无进一步动作（或按 Director 指令继续修改）
- Director 要求提交 → 确认 camera-ready checklist 全绿（当前 11/12 passed, 1 minor），执行最终编译
- Director 要求新一轮 review → 读 `review-reviewer-session-start` skill，执行全文审查
- 任何新增文本 → 必须检查 (a) 不引入因果语言 (b) body 仍 ≤8 页 (c) 无 Type 3 fonts

### 5. 🎯 战略上下文
- 投稿目标：CoRL 2026（DDL 5/29）
- 核心 story：VLM→VLA fine-tuning 的 exit collapse 是 training-associated（ΔR² 0.16-0.46），VLA→VLA 和 NLP controls 无此现象；L1 instruction routing 是 inherited backbone property
- 论文经历多轮 Reviewer 审查（R15→R17），主要扣分项是 venue fit / practical impact（4/10），已通过扩展 use cases 和正面重构 specificity 来改善
- 易错点：
  - 页面空间极其紧张——任何文本增加都可能突破 8 页，必须先编译验证
  - specificity caveat 已从防御性改为正面 "distributed instruction integration" 框架，不要改回去
  - anticipated_rebuttal_v2.md 已有 12 个 Q&A（Q1-Q12），新增 Q 时注意更新开头 "twelve"
  - 44 个未引用 labels 已清理，但保留了顶层 section labels（sec:introduction 等）
  - Appendix 新增了 `sec:extended_practical_implications`，Discussion 里有 cross-ref 指向它


---
