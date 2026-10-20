# director / loop_14.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`3620c27551d37b39c46c.json`](../../sessions/36/3620c27551d37b39c46c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-28T11:05:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文主文必须 ≤ 8 页（当前 v12 正好 8 页，任何新增内容必须同时压缩等量空间）
- Figure 4 已从 wrapfigure 改为全宽 figure[t]，width=0.80\columnwidth，再改回 wrapfigure 会重新引发重叠问题
- float 间距已压缩到极限（textfloatsep=6pt, floatsep=6pt, intextsep=4pt），不要再缩
- GPU 释放已请求 Manager 7 次未响应，不要自行释放或在白名单外操作 GPU
- 论文 DDL 5/29（今天），用户需自行操作 OpenReview 提交

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183 (connect.westd.seetacloud.com)，工作目录 /root/vla-ssd
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd
- 论文源文件：上述 workspace 的 docs/paper/（main.tex 入口）
- 提交包：artifacts/submission_package/（main.pdf + supplementary_code.tar.gz + SUBMIT_GUIDE.md）
- 图表脚本：scripts/（gen_fig_matrix_heatmap.py, plot_r2_collapse.py, plot_counterfactual_bar.py, plot_l1_attention.py）
- figures 是 symlink：docs/paper/figures → artifacts/figures/paper
- 实验 artifacts：artifacts/clustered_bootstrap_reanalysis_v3/（权威数据源）
- GPU：2 张分配，0 张在用，107 个成功实验全部完成
- 活跃进程：无（无 RUNNING 实验，无 tmux，无 cron 任务）

### 3. 📊 当前状态
**刚做完**：用户要求的一系列格式修改（v6-v12），包括三级标题→paragraph、表头加粗、图字体放大、Figure 4 改全宽左右布局、主文压回 8 页。

**正在进行**：Agent 正在执行全面数据+事实验证（数值一致性、事实性、叙事一致性、交叉引用四个维度），由用户吴俊豪要求。验证完成后需汇总结果并发送最新 PDF 给用户。

**之前的验证结果**：59/59 PASS，5 项 CANNOT VERIFY（远程服务器数据），Reviewer 评估 5 项均不影响核心 claim。

**Registry**：156 个实验，109 成功，0 RUNNING，11 PENDING（不会再跑）。审稿阶段进行中（review_chat_id: oc_554a5023cde4d603635cf97e6ab8151a）。

### 4. 📋 待办
- Agent 数据验证回调 → 汇总 PASS/FAIL 报告 → 编译最终 PDF → 上传给用户吴俊豪
- 若验证发现 FAIL → 立即修复对应数值，重新编译
- 用户确认 PDF 无问题 → 提醒用户去 OpenReview 操作提交（我们不能代操作）
- 用户要求任何格式改动 → 改完后必须验证主文仍 ≤ 8 页

### 5. 🎯 战略上下文
- 项目核心结论：VLM→VLA 微调伴随 exit-layer collapse（ΔR²=0.16-0.46），VLA→VLA 无此现象（<0.10），NLP controls 也无（=0.000）。L1 instruction attention 主要继承自预训练 backbone。
- 论文版本历史：v6（三级标题改）→ v7（abstract 加数值）→ v8（caption 优化）→ v9-v10（Fig4 图例修复）→ v11（Fig4 改全宽）→ v12（压回 8 页，当前版本）
- Discussion 在 v12 中被精简：去除了重复的 ρ=0.583 统计值，合并了 "cross-architecture decomposition" 结论句。核心 claim 未丢失。
- 易错点：gen_fig_matrix_heatmap.py 的 cell 尺寸被 Agent 在硬编码清理时误回退过一次（0.88→1.0 被还原），已修复，注意后续修改不要再回退
- 用户有两个人：周雪阳（主要研究者，一直在给格式反馈）和吴俊豪（刚加入，问了 GPU 和数据验证）
- Reviewer 和 Director 都刚批准 RESET_BOTH，新 session 启动后 Reviewer 是干净的


---
