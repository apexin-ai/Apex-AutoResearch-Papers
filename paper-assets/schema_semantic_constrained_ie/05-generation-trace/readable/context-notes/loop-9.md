# director / loop_9.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`fa968ed890a287e88a41.json`](../../sessions/fa/fa968ed890a287e88a41.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-23T19:44:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- EMNLP 2026 ARR deadline: **May 25, 2026**（距今 ~40h）。论文已完成编译（40页，零 critical warning），等用户在 OpenReview 提交
- 论文数据已全部审计修正完毕，**不要再改任何数字**除非用户明确要求——上一轮 6 处修正已验证正确
- GPU 已全部释放通知 Manager（4张卡 0% 利用率），**不要再分配 GPU 跑实验**
- 匿名仓库已推送 GitHub（34文件，commit af26cba），**不要再 push**——token 可能已过期

### 2. 🖥️ 基础设施快照
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`
- 主 tex：`main.tex`（134行，25个 appendix \input），编译入口
- 匿名仓库本地副本：`/tmp/anon_repo/`（已推送，与 GitHub 一致）
- 无活跃服务器/进程/tmux/cron——项目处于纯提交等待状态
- 审稿阶段已启动，review_chat_id: `oc_01fc90ae186a4ed432770f7601995139`

### 3. 📊 当前状态
所有工作已完成：
- 数据正确性审计：6处修正已应用（lucky violations 0.49→0.24%、62% on average→on SciERC、~31%→30-51%、beam latency 1.39×→~1.5×、70B baseline caption、+0.50→+0.49）
- 匿名仓库：34/34文件一致性已验证
- GPU释放：已通知 Manager
- 论文编译：40页，零 critical warning
- Registry 中无 RUNNING/PREPARING 实验
- 无等待中的 Worker 回调 / Cron

### 4. 📋 待办
- 用户确认 OpenReview 提交完成 → 项目可进入等审稿阶段，无需额外动作
- Manager 确认 GPU 释放 → ACK 即可
- 如用户要求最后修改 → 改后重新编译验证，不要引入新数字错误
- 收到审稿报告 → Read `review-report-action.skill.md`，按 Holistic Pass + Per-Comment Action Matrix 处理

### 5. 🎯 战略上下文
- 项目核心：OntoCoDec 两层约束解码（grammar + semantic），DR 从 15-18% 降至 ≤0.21%（fine-tuned S1），beam k=4 消除所有违反类型
- 关键决策链：S1 推荐为默认配置（S2 在 70B 严重掉 R-F1）；beam k=2 是 Pareto 最优（零shot部署推荐）
- **易踩的坑**：
  - beam latency 有两个参照系——section5_runtime 用 "relative to greedy S1"（1.39×），appendix beam_search 用 "relative to unconstrained"（1.54-1.63×，不同硬件）。Abstract/intro 已改为 ~1.5× 模糊处理，不要再改回 1.39×
  - lucky violations 有两个指标：%gold（0.24%）和 %TP（0.49%），用不同分母。正文和 appendix 主表用 %gold，appendix_downstream_analysis 详细表用 %TP
  - 70B DocRED baseline: 998-doc 是 14.98%，200-doc subset 是 13.45%——sample size 差异，不是 bug


---
