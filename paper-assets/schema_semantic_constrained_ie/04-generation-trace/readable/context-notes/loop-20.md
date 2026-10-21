# reviewer / loop_20.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`679ea379158aab83c276.json`](../../sessions/67/679ea379158aab83c276.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-25T08:09:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文真源在本地 `artifacts/_project/paper/`，不是远程服务器。之前 Report #57 因只读远程残留旧版误判"worker 未修改"，已记入 memory。
- Abstract ≤200 words（当前 ~134 words，安全）
- Limitations 必须在正文（不在 appendix），当前已正确放置（main.tex L68-93）
- 一篇文章只能有一个 limitations section
- EMNLP 2026 long paper 正文严格 8 页限制（当前刚好 8 页，§7 压缩过一次修复超限）

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 + westd-21461，均已标记可释放，GPU 空闲
- 远程代码根：`/root/schema_semantic_constrained_ie`
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`
- 匿名代码仓库已 push，`_anonymous_repo.json` 已持久化
- LoRA adapters 已从 westd-21461 备份
- 活跃进程：无（0 RUNNING 实验，无 cron，无 tmux session）

### 3. 📊 当前状态
论文 submission-ready，等用户手动提交 ARR（DDL May 25）。164 实验全部 DONE（133 success / 15 negative / 11 failed+killed）。

本轮（Loop #20+）我完成了：
- Novelty 防御审查 → 4 项建议全部被采纳（C1/C2/C3 reframe + PICARD 区分）✅ 已验证
- 15 个阴性实验 vs 论文覆盖度审计 → PASS（13 显式覆盖，2 可合理省略）
- ROADMAP 更新审查 → 所有 claim 验证通过
- Figure 1 v6/v7/v7b 三轮审查 → v7b (Morandi) 标 warning（低对比度可读性风险）
- Figure 4 beam-pareto redraw 审查 → PASS
- 多轮 appendix 交叉引用新增验证 → 10 个新 label 全部存在

等待中：无 worker / cron / Director 决策待处理。

### 4. 📋 待办
- Director 通知 final freeze → 做最终 PDF 视觉审查（`paper-visual-review` skill），检查页数、undefined refs、图表渲染
- Director 要求选 Fig1 版本（v7 vs v7b）→ 如果选 v7b 需确认灰度打印可读性
- 提交后收到审稿意见 → 切换到 rebuttal 模式（加载 `rebuttal` skill）
- 任何新 worker 完成通知 → 按审查维度审查

### 5. 🎯 战略上下文
- 核心发现：non-additive layer interaction（grammar 3% + semantic 24% → composed 94%），论文最独特的贡献
- 最危险攻击面 A1："known techniques composed, not novel"。当前 intro 已 reframe 为 insight/finding（C1 non-additive, C2 decidability analysis showing, C3 去掉 Preliminary）。§6 PICARD 区分已强化（static declared types vs dynamic inferred types）
- 预估评分 3.0-3.5（Findings to Borderline Conference）
- 易错点：Fig1 当前是 v7b (Morandi)，如果 Director 未明确选择版本就提交，可能用的是低对比度版本
- S2 70B 退化（-8pp R-F1）已诚实披露，不需要额外处理
- 60 条 bib（7 orphans 已清理），abstract ~134 words，正文 8 页 — 均在限制内


---
