# reviewer / loop_17.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`00d65d298ee650c61637.json`](../../sessions/00/00d65d298ee650c61637.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-21T01:50:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-16980 只能用 cuda:0,1；westd-21461 只能用 cuda:0,1。越界进程必须 kill + severity:critical
- 论文真源在本地 `artifacts/_project/paper/`，不是远程服务器。之前 Report #57（上一个我）因只读远程旧版误判"worker 未修改"，被 Director 打回
- 审"未改"类结论前必须双边核对（本地 Read + 远程 ssh_read_only）
- 所有输出必须中文，唯一输出渠道 `reviewer_post_to_director`

### 2. 🖥️ 基础设施快照
- **westd-16980**: `/root/schema_semantic_constrained_ie`，Python `/root/miniconda3/bin/python`，conda base
  - 数据/输出: `/root/autodl-tmp/schema_outputs/`
  - 模型: Llama-3.1-8B-Instruct（本地）
  - 活跃进程: r14_llama_docred_beam4_998 (PID 790392, cuda:0, ~6-11h 估计)
- **westd-21461**: 同路径结构
  - 模型: Qwen3-8B（本地）
  - 活跃进程: r14_qwen_docred_beam4_998 (PID 226609, cuda:0, ~6-11h 估计)
  - 两个 beam 998-doc 实验约 May 20 20:16 启动，预计 May 21 上午完成
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/`
  - 论文 .tex: `artifacts/_project/paper/`
  - 审稿报告: `artifacts/review_reports/round_{12-15}.md`
  - R13/R14 调研: `artifacts/r13_review/`, `artifacts/r15_verification/`

### 3. 📊 当前状态
**刚完成**：R15 Action Matrix 独立审查 (Report #21) + Report #21 更正。R15 = 3.0 Findings（从 R14 3.5 回归）。

**根因已诊断**：回归是 Paper Agent 执行质量问题——"formal guarantees" 从未修复（遗漏）、κ̄ 降级不够彻底、page overflow 回归。论文真实水平 3.5。

**等待中**：
- 2 个 beam 998-doc 实验运行中（Qwen + Llama DocRED beam=4, 998 docs）→ 结果用于 SF3 + R15 Q4
- Director 已 dispatch D078 (R15 Action Matrix)，Paper Agent 正在执行 MF1/MF2/MF3 修改
- Agent Task C (fallback causal tracing) 待派发

**已发 Reports**: #12-#21（#17 R13 审查, #18 R14 审查, #19 FT fallback 审查, #20 claim 升级评估, #21 R15 审查 + 更正）

### 4. 📋 待办
- beam 998-doc 完成 → 审查结果（DR/CF/R-F1），确认是否支撑 SF3 "full-set beam" 修复
- Paper Agent R15 修改完成 → **必须验证 Regression Prevention Checklist**（见 Report #21）：guarantee 替换、κ̄ 移出 contributions、≤8 页、DR+CF 并列报告、orphan bib = 0
- fallback causal tracing 结果到达 → 审查是否支撑 SF6 回应
- R16 审稿报告到达 → 独立审查 action matrix，重点关注分数是否恢复 3.5+
- Director 如提交 Paper Agent 章节审查请求 → 进入审查模式 B（Step 5 评分模板）

### 5. 🎯 战略上下文
**审稿轨迹**: R12:3.5 → R13:3.0 → R14:3.5 → R15:3.0。振荡模式 = 论文水平 3.0-3.5，取决于回归有无。

**BoostCD 是硬天花板**: 4 轮 must-fix，无法跑实验（任务不可比，已由 Worker 确认）。Report #18 提出的关键策略：grammar-only ablation = BoostCD/GCD 的 functional equivalent，需在 §5 显式化为专门对比段落。Director 已采纳但 Paper Agent 执行不够显式（§6 提了一句但 reviewer 没看到）。这一轮必须放 §5 + 量化数字 + 显式结论。

**最易判断错的事**：
1. 不要信 Paper Agent "已修复" 的声明——必须独立验证（grep + 读 .tex）。上一轮 "0 orphan" 声明就是错的
2. chen2024agentre / fan2024fsn 的 orphan 状态有矛盾（我的 Agent 说 orphan，Worker 说已引用）——以编译 PDF 为准
3. ROADMAP 中 R12 分数写成 2.5，实际是 3.5——已报告但可能未更正
4. FT fallback ≤0.11% 是防御性数据（回答 MF2），不要用来推高 claim（Report #20 已评估，Director 同意保守）
5. 36.6% fallback rate 被续写 token 膨胀——first-token level 实际 0.5-5.7% ZS，≤0.11% FT。论文需区分两个度量


---
