# reviewer / loop_4.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`ca70a3f755e15a6a840b.json`](../../sessions/ca/ca70a3f755e15a6a840b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-23T19:45:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 0 GPU，全部实验通过 API 完成，无服务器进程需要监控
- EMNLP 2026 正文严格 8 页限制，当前 analysis.tex 用了 `\enlargethispage{28\baselineskip}`，任何正文扩展都极度危险
- Abstract ≤200 words（当前 ~155 words，安全）
- Limitations 只能有一个，在正文里，appendix 不能有 limitations section
- κ 重标注后需同步更新 5+ 位置：abstract、intro L21 contribution (3)、analysis L13、appendix human_validation、limitations——漏改任一处即数据不一致 CRITICAL

### 2. 🖥️ 基础设施快照
- 无远程服务器，所有工作在本地 workspace
- 工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/`
- 论文源：`docs/paper/sections/*.tex`，主文件 `docs/paper/main.tex`
- 重标注材料：`artifacts/reannotation/`（4 文件：guideline, sheet, sample script, traces）
- 无活跃进程 / tmux / cron

### 3. 📊 当前状态
全部写作优化已完成并 commit（HEAD = `1b1058d`，工作树干净）。我已验证：
- 术语统一（convergent nocuity 全文一致）
- Writing quality pass（contribution 措辞、Discussion Jaccard 数据、caption 信息密度、inline failure examples）
- Pre-submission hardening（limitations 3 项补充、v2 mitigation 在 Discussion、appendix 术语）
- 重标注材料齐全

无 RUNNING/PREPARING 实验。等待用户 5/24 完成 κ 重标注。DDL 2026-05-25。

### 4. 📋 待办
- κ 重标注结果到达 → 验证新 κ 值，检查 paper 5+ 位置更新一致性（abstract human κ=0.15→新值、intro contribution (3) κ=0.34-0.52→新值、analysis L13、appendix human_validation、limitations）
- 若 κ ≥ 0.4 → 验证 contribution (3) 是否从 "initial evidence" 升级为更强措辞
- 若 κ < 0.35 → 验证是否诚实披露，不降级整体贡献
- 提交前 → 最终 PDF 编译确认页数（\enlargethispage{28} 是否安全）、reference audit、stale file check

### 5. 🎯 战略上下文
当前评估 Overall ~3.75（Borderline Conference）。写作改善已榨干（最多 +0.1），4.0 的 binding constraint 是 human κ 重标注（0.15→0.4+）。κ 成功则 contribution (3) type-mechanism dissociation 从 "initial evidence" 升级为 supported claim，整体可达 4.0。

易错点：
- `convergent nocuity` 是统一术语，不要回退为 `systematic nocuity`（已在 1b1058d 统一）
- Discussion ¶3 的 `$-$36.0\,pp` 是 Table 1 Δpp 反向（ambiguity resolution effect），不是 mitigation 实验结果（mitigation 是 -18.0pp）——别搞混
- C4 (model×type interaction) 是 exploratory，C3 (layer effect) 是 inconclusive——这两个 claim 的强度标签不要搞反
- ROADMAP 关键发现 6 条数据全部与论文一致，已交叉验证


---
