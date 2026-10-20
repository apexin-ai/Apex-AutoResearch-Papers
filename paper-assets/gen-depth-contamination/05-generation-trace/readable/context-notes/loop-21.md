# reviewer / loop_21.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_21.md`
- **Structured JSON:** [`1d4b277acb3fae6beef0.json`](../../sessions/1d/1d4b277acb3fae6beef0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_wall_time
updated: '2026-05-23T19:41:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-22115 GPU 白名单未明确配置，但当前无 RUNNING 训练实验，不构成风险
- 论文正文严格 ≤8 页（EMNLP 2026）；Limitations/Ethics/References 不计入
- Abstract ≤200 words（当前 ~147）
- 正文禁止 em-dash（—），en-dash 仅用于数字范围
- 一篇文章只能有一个 Limitations section，放正文，appendix 不能有
- 引用审计已发现 3 条 bib entry 曾含编造作者（已修复），任何新增引用必须 WebSearch 验证真实性

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-22115 (root, 4×RTX PRO 6000 Blackwell 98GB) + westd-42896 (root, 2×Blackwell 98GB)
- 远程代码：`/root/autodl-tmp/gen-depth-contamination`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- 论文源码：`docs/paper/`，PDF：`artifacts/gen-depth-contamination_20260523.pdf`（542K, 18pp → 最新可能 19pp，Round 29 修复后需重新编译确认）
- 匿名仓库：`https://github.com/anonymous-nlp-2026-2/gen-depth-contamination`
- Registry：126 DONE, 0 RUNNING, 0 PENDING
- 活跃进程：无（全部实验已完成）
- Bootstrap K* 数据：服务器 `results/bootstrap_kstar/`；Runtime benchmark：`results/runtime_benchmark/`

### 3. 📊 当前状态
Round 29 审稿修复执行中（3.5/5 → 目标 4.0）。DDL 2026-05-25。

**已完成的证据任务**：
- Bootstrap K* 不确定性分析 ✓（8/10 configs 100% 稳定，结果强）
- Runtime benchmark ✓（44.7 ms/doc, 22.4 docs/sec）
- Figure 4 heatmap 字号放大 + v1 回退修复 ✓（v2 AUC 图-文不一致已修正）

**Paper Agent 写作任务状态不明**（我是 Reviewer，只看 worker 结果）：
- MF-1 filtering 定位转变、MF-2 continuation-mode 限定、SF-1~SF-6 写作修复 — 均已派发，未见最终编译验证 worker
- Bootstrap K* 数据和 runtime 数据已产出，等 Paper Agent 写入论文

**等待中**：
- Paper Agent 完成全部写作修复后的最终编译 worker
- Director 可能触发 Round 30 审稿

### 4. 📋 待办
- Paper Agent 写作修复编译完成 → 审查：(a) MF-1 Abstract/Conclusion filtering 声明是否限定为 extreme contamination；(b) MF-2 "generator-agnostic" 是否加了 continuation-mode；(c) discussion.tex L12 "single generation pass renders text indistinguishable" 是否已修正（这是事实错误）；(d) bootstrap K* 数据是否写入正文；(e) runtime 数据是否在 appendix
- Director 触发 Round 30 审稿 → 对比 Round 29 issues 是否真正解决（特别关注 MF-1 复发第 5 轮风险）
- 新增引用（Kirchenbauer 2023 watermarking）→ 验证 bib 真实性
- 最终 PDF → 逐页视觉审查（重点 Figure 4 回退后的 p6、新增 bootstrap 表/段落）

### 5. 🎯 战略上下文
- 核心结论：K*≤2 for web text（one-wash laundering），arXiv K*=3。这是 empirical measurement，不是方法创新。
- Round 29 的 3 个 Must-Fix：(1) filtering overclaim 复发第 4 轮（前 3 轮写作弱化全失败，本轮换路径为 measurement validation）；(2) generator-agnostic 仅限 continuation mode（纯写作限定）；(3) K* 样本不稳定（bootstrap 已提供强证据）
- **最易判断错的事**：discussion.tex 中 "one-wash laundering" 的定义。K*=2 意味着 depth-1 仍可与 depth-2 区分，"one wash" 不是说一次生成就抹掉所有信号——是说 90%+ 信号集中在 0→1 边界。如果看到 "single generation pass renders text indistinguishable" 仍在论文中，必须 CRITICAL 打回。
- **Figure 4 陷阱**：已回退到 v1（6-class ordinal accuracy, 4 模型），确保 caption 说的是 accuracy/retention 而不是 AUC。如果看到 v2（3 模型 AUC heatmap），说明回退失败。
- **Mistral-7B 数据**：已改用 exp_019b cross-scored 值。若看到 0v1=.9170 或 1v2=.5750（旧值），说明残留未清。
- **LLaMA-8B C4 bootstrap 99.9% K*=2 vs 10K K*=1 张力**：bootstrap 是 within-sample stability，10K 是 between-sample variability，两者互补不矛盾，论文需明确区分。


---
