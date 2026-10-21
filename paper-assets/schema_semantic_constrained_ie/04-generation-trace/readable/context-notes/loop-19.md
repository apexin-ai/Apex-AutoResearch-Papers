# reviewer / loop_19.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`1336134d73105184b025.json`](../../sessions/13/1336134d73105184b025.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-23T19:44:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-21461 cuda:0,1 / westd-16980 cuda:0,1。越界进程立即 CRITICAL
- 论文真源在**本地** `artifacts/_project/paper/`，不是远程服务器。之前 Report #57 因只读远程旧版误判"worker 未修改"（已存 feedback memory）
- EMNLP 2026 硬约束：abstract ≤200 words、主文 ≤8 页、Limitations 在正文不在 appendix、ARR Checklist 在 OpenReview form 不在 PDF
- §7 L16 已修正 ">90%" → "26-52%"（M033），任何新写入不得重新引入此错误数字

### 2. 🖥️ 基础设施快照
- 服务器：westd-21461 + westd-16980，代码根 `/root/schema_semantic_constrained_ie`
- 本地论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`
- Registry：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml`（164 实验，全部 DONE）
- 活跃进程：无。4 GPU 全部空闲，无 RUNNING 实验，无 cron 任务
- 编译状态：main.pdf 已编译通过，40 页，8 页主文，零 undefined refs

### 3. 📊 当前状态
**阶段**：论文 submission-ready，等匿名仓库 token → final freeze → May 25 EMNLP ARR 提交

**刚完成**：
- R26 Action Matrix 全部 8 项修复的独立验证（全部 PASS）
- 提交前全文三维度审查（claim 强度 / story 优化 / GPU ROI）
- ROADMAP 状态不一致修复（sf2_70b_prompt_sensitivity 实际 DONE 但 ROADMAP 标 failed，已通知 Director）
- 匿名化快速检查：`\author{Anonymous ACL submission}`，无 github/gitlab/HF 链接泄露

**无 RUNNING/PREPARING 实验**。两个 submit-prep worker failed（ARR checklist + code anonymization），均非阻塞：checklist 在 OpenReview 手填，匿名化审计 worker 已另行完成（status=done）。

### 4. 📋 待办
- 用户提供匿名仓库 token → 确认推送后检查仓库无身份泄露
- Director 要求最后一次编辑（如提升 "97.6-100% FP" 到 intro）→ 验证新文本数据一致性 + 重新计算 word count
- Final compile 冻结 → pdf_to_images 目视确认页数/排版
- 提交后若收到新审稿意见 → 按 rebuttal skill 流程

### 5. 🎯 战略上下文
**核心结论链**：非加性层组合（3%+24%→94%）是论文最独特发现；70B 84% vs 8B 24% 是 scale insight 但仅 single-family（Llama）；beam k=4 消除所有违规 at 8B 但 70B 有 1 residual CF。

**下一个"我"最易犯的错**：
1. **Tot 计算用 DR+CF**（不包含 RV/ET），因为 S1 下 RV=ET=0。之前的 ">90%" 错误就是混淆了计算口径
2. **不要重新计算旧数据**——Table 2 所有 32 cells + 4 ΔDR 已在本轮全部手动验证通过，不需要再验
3. **GoLLIE 在 SciERC 上 R_F1=0**（只预测 5 条关系），发表的 63.6-70.1% 是 ACE05 supervised。不要引用任何 "55-65%" 的数字
4. **论文评分现实**：R26 给 Overall 3.0（Findings），核心差距是单家族 70B + 无 GoLLIE 组合实验，DDL 前无法安全弥补。建议 freeze 提交


---
