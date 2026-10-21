# reviewer / loop_13.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`02c2a4da94605c3cb6f6.json`](../../sessions/02/02c2a4da94605c3cb6f6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-26T16:53:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19183 上 cuda:0 和 cuda:1（2× RTX PRO 6000 96GB）。项目已无实验可跑，GPU 释放请求已提 Manager 5 次未回复。
- 论文处于 anonymous submission 模式（`\author{Anonymous}`，无 `[final]` flag）。任何修改不得引入 identifying information。
- Paper DDL 2026-05-29，用户需自行操作 OpenReview 提交。Reviewer 不执行实验、不修改文件、不提交。
- 17 个 negative 结果经 D110 决策终结——不再重试任何一个。

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，代码根目录 `/root/vla-ssd`，数据盘 `/root/autodl-tmp/vla-ssd/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型 checkpoints：`/root/autodl-tmp/vla-ssd/checkpoints/`（openvla-7b, tracvla, nora 等）
- 数据集：`/root/autodl-tmp/vla-ssd/data/libero/`（4 suites × 10 tasks × 50 demos）
- 实验结果：`/root/autodl-tmp/vla-ssd/results/`
- 本地论文：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/`
- 活跃进程：无。全部实验已完成（107 success / 17 negative / 7 failed）。无 tmux session / cron。

### 3. 📊 当前状态
**刚完成**：
1. 17 个 negative 逐条审查（结论：无一值得重试）→ posted D110
2. 论文 story 最终审视（claim-evidence alignment 良好，1 个 warning：§4.6 specificity caveat 建议加一句）
3. Camera-ready QA（CoRL 2026 格式合规，2 个 non-blocking warning：appendix overfull hbox + 参考文献格式不统一）
4. ROADMAP 更新审查（与审查结论一致，无异常）

**Registry 状态**：全部 DONE，无 RUNNING/PREPARING。

**等待中**：
- 用户确认 abstract 提交状态（DDL 5/26 已过）
- 用户操作 paper 提交（DDL 5/29）
- Type 3 mathtext 字体清除（Worker 进行中，非阻塞）
- Manager 批准 GPU 释放

### 4. 📋 待办（条件触发式）
- Director 转发章节修改审查请求 → 模式 B 对抗审查（先读 paper-quality-lessons skill）
- Director 转发 Framing 调整提案 → 读 negative-framing-review skill，四维度审查
- 论文被 rebuttal → 读 rebuttal skill，对照 `artifacts/anticipated_rebuttal_v2.md`（9 个预期问题已准备好）
- Worker 报告 Type 3 字体修复完成 → 验证 `pdffonts main.pdf` 无 Type 3 残留
- ROADMAP 再次更新 → 快速一致性检查（当前状态 = 等待提交，无实验变动）

### 5. 🎯 战略上下文
**核心结论**：VLM→VLA 微调产生 exit collapse（ΔR²=0.16-0.46），VLA→VLA 不产生（<0.10），NLP controls 确认 VLA-specificity（0.000）。L1 instruction attention 是继承的，非训练产物。三个分析方法（probe + counterfactual + L1 profiling）构成跨架构分解。

**关键决策链**：D101（Weak Reject 4.5/10 → 统计框架重构）→ D102（转 effect size threshold）→ D103（framing 路径）→ D105（Qwen NLP control 闭合 limitation）→ D107（n=9 硬约束终结）→ D110（17 negative 终结，GPU 释放）

**易错点**：
- **n=9 behavioral correlation（ρ=0.583, p=0.10）是设计硬约束**，不可通过 sub-split/bootstrap/augmentation 扩展。D107 已终结讨论。别再试。
- **L1 "instruction-dominant" 分类是 attention-based，不是 functional-specificity**。specificity_control_action 显示 ablating non-instruction heads 产生类似 d 值（0.565 vs 0.65）。论文用 "distributed redistribution" 处理。审稿人可能攻击这个点——准备好 rebuttal。
- **OpenVLA reference 是 VLA（OXE-pretrained），不是 VLM**。TracVLA/NORA reference 才是 VLM。这个不对称是论文的核心设计，不是 bug。
- **counterfactual sensitivity 跨 metric 不可比**：Cohen's d（OpenVLA/TracVLA）vs cosine distance（NORA/reference VLMs），论文已反复强调。
- **页数**：ROADMAP 写 42 页，main.log 编译显示 40 页。可能编译版本差异，不影响合规。


---
