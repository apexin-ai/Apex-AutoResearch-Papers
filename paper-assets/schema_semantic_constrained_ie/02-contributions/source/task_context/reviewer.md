---
loop: 21
reason: idle_timeout
updated: '2026-05-25T19:57:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文真源在本地 `artifacts/_project/paper/`，不是远程服务器。之前 Report #57 因只读远程残留旧版误判"worker 未修改"，已记入 memory。审查"未改"类结论前必须双边核对。
- Abstract ≤200 words（当前 ~134 words，安全）
- Limitations 必须在正文（不在 appendix），当前已正确放置（main.tex L68-93）
- EMNLP 2026 long paper 正文严格 8 页限制（当前刚好 8 页，§7 曾压缩修复超限）
- 70B LoRA S2 过度约束（R-F1 暴跌 -8pp），论文不应 claim S2 在 70B 上有效
- `_anonymous_repo.json` 包含 GitHub PAT 明文，已提醒 Director 提交后撤销

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 + westd-21461，均已标记可释放，GPU 空闲
- 远程代码根：`/root/schema_semantic_constrained_ie`
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`
- 匿名代码仓库：`https://github.com/anonymous-nlp-2026/schema_semantic_constrained_ie`，final commit `7ef1fe4`，push 时间 2026-05-25T09:08:21Z
- 活跃进程：无（0 RUNNING 实验，无 cron，无 tmux session）

### 3. 📊 当前状态
Loop #21 完成了匿名代码仓库推送 worker 的审查（PASS，1 warning 关于 PAT 明文）。164 实验全部 DONE（133 success / 15 negative / 11 failed+killed）。论文 submission-ready，等用户手动提交 ARR（DDL May 25 今天）。无任何 RUNNING/PREPARING 实验，无待处理 worker/cron/Director 决策。

### 4. 📋 待办
- Director 通知 final freeze → 做最终 PDF 视觉审查（`paper-visual-review` skill），检查页数、undefined refs、图表渲染
- Director 要求选 Fig1 版本（v7 vs v7b）→ 如果选 v7b(Morandi) 需确认灰度打印可读性
- 提交后收到审稿意见 → 切换到 rebuttal 模式（加载 `rebuttal` skill）
- 任何新 worker 完成通知 → 按审查维度审查

### 5. 🎯 战略上下文
- 核心发现：non-additive layer interaction（grammar 3% + semantic 24% → composed 94%），论文最独特贡献
- 最危险攻击面 A1："known techniques composed, not novel"。Intro 已 reframe 为 insight/finding（C1 non-additive, C2 decidability analysis showing, C3 去掉 Preliminary）。§6 PICARD 区分已强化（static declared types vs dynamic inferred types）
- 预估评分 3.0-3.5（Findings to Borderline Conference）
- Fig1 当前是 v7b (Morandi)，Loop #20 标过 warning（低对比度可读性风险），Director 未明确选版本
- 15 个阴性实验 vs 论文覆盖度已审计通过（13 显式覆盖，2 可合理省略）
- 60 条 bib（7 orphans 已清理），正文 8 页 — 均在限制内
