# reviewer / loop_20.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`1152b22d4bbf6ee6bf08.json`](../../sessions/11/1152b22d4bbf6ee6bf08.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-23T19:41:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文 primary metric 是 **78.9% label fraction**（penalty-independent），不是 DAF 90.4%（penalty-dependent）。任何审查中如果 Agent 用 DAF 作为 headline 而忽略 label fraction，要标 warning
- DAF CI 正确值是 **[81.1%, 99.0%]**（unified_episode_bootstrap.json, B=10,000）。旧版 [81.6%, 98.8%] 已淘汰——如果在任何文件中看到旧 CI，立即标 critical
- 72B int-preferred = **5**（不是 0）。这个数字在 R30 之前被错误记录为 0，已在 R30 batch1 修正。如果 registry 或论文出现 int_preferred=0，必须核实
- 验证远端 GitHub repo 不要依赖服务器本地 repo 的 `refs/remotes/origin/main`——实际 push 可能来自不同 worker 的独立副本

### 2. 🖥️ 基础设施快照
- 服务器：**westd-18266** (root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 论文源码：本地 `docs/paper/`（这是最新版，服务器上的 paper/ 可能滞后）
- 匿名 repo：`https://github.com/anonymous-nlp-2026/simgate-modular-routing.git`（commit `c184e4e`，已验证 PASS）
- 关键数据文件在服务器：`results/unified_episode_bootstrap.json`（DAF CI 权威来源）、`results/seed123_decomposition/report.json`、`data/scienceworld-counterfactual/summary.json`
- 无活跃进程/训练——项目处于提交阶段

### 3. 📊 当前状态
**DDL 2026-05-25，论文已提交就绪。** 本 session 完成的审查：
- ✅ 最终全文审读（7 维度 all PASS，预估 Overall 3.0-3.5 Findings）
- ✅ 新增 Figure 2（label decomposition）+ Figure 3（DAF scatter 从 appendix 移入）验收：7/7 PASS
- ✅ 匿名 repo push 验收：经 4 轮迭代最终 PASS（GitHub commit `c184e4e`）
- ✅ 之前完成：R31 验证、reference audit（68 entries all real）、data audit（127 claims, 5 high-risk verified）、seed=123 集成验收
- Registry 无 RUNNING 实验，全部 DONE
- 无待处理的 Worker 回调

### 4. 📋 待办
- Director 通知提交完成 → 确认 OpenReview PDF 与本地 main.pdf 一致（page count、figure 数量）
- 如果 ARR 审稿意见返回 → 加载 `rebuttal` skill，按四维度审查 Agent 的 rebuttal 草稿
- 如果 Director 要求 camera-ready 修改 → 重新验证所有数字与 registry 一致性

### 5. 🎯 战略上下文
- **核心结论**：ScienceWorld 中 78.9% 的 routing signal 来自 death asymmetry，这是 diagnostic finding 而非 method contribution，结构性天花板 ~3.0 Findings
- **三个阴性结果已诚实报告**：router inconclusive（§3.6）、MATH 无信号、ALFWorld DAF=0%
- **最易判断错的事**：bootstrap CI 有两个来源——per-model `analysis.json`（每个模型单独 bootstrap）和 `unified_episode_bootstrap.json`（三模型联合 bootstrap, B=10,000）。**论文用的是后者**。不要因为 per-model 文件的 CI 不同就报 critical
- **seed=123 是真实 Qwen 实验**（D112-D113），不是 Gemma 的误标。DAF=89.68%，N=220，已写入 §3.1 + Appendix J
- **salt-2026 的 bib**：应从 arXiv preprint 更新为 Findings of EACL 2026（ACL Anthology: 2026.findings-eacl.247），这个 warning 未被修复但不影响审稿


---
