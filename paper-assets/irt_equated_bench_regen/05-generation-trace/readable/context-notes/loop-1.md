# director / loop_1.md

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`21b40463466be82f4e2b.json`](../../sessions/21/21b40463466be82f4e2b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-22T19:16:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 分配，无远程服务器配置。所有实验（MH-DIF 分析）都在本地 CPU 完成
- 论文主文本严格 8 页限制（EMNLP 2026 ARR），appendix/references 无限
- De-dup K=20 的正确数据是 19.7%±0.9%（random selection），不是旧的 29.1%（deterministic selection，已废弃）
- ρ=-0.597 不能作为 capability evolution 的证据——semi-synthetic 证明 contamination + ceiling effect 也产生 ρ≈-0.52。论文已修正为 "suggestive but not diagnostic"
- "ICC" 在本项目有两个不同含义：model-level pairwise Pearson r ≈ 0.46（within-family similarity）vs item-level ICC = 0.0465（DEFF formula 用的）。论文中不能混用

### 2. 🖥️ 基础设施快照
- 无远程服务器（execution 未配置）。所有分析由 Agent spawn worker 在本地跑
- 论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/`
- 主 tex：`paper/main.tex`，各 section 在 `paper/sections/`
- METABENCH 数据：Agent 有现成的 response matrix 和 MH-DIF pipeline（基于 plan_001 代码）
- 无活跃进程 / 无 tmux / 无 cron 实验任务

### 3. 📊 当前状态
刚完成 4 条提分路径的实验 + 论文 patch：
- **Base-vs-instruct decomposition**（commit b4b12a2）→ 写入 §5.1，方向反转 χ²=563 作为 mechanism separation 主证据
- **Introduction framing 强化**（commit 4fd36c1）→ Contribution 2 升级为 "temporal DIF audit framework"
- **ρ-gradient overclaim 修正 + semi-synthetic gradient signatures**（commit 1772348）→ 删除 "ruling out ceiling effects"，加入 ceiling effect caveat + difficulty-dependent injection 结果
- 时间粒度 DIF：ρ 跨时间窗口一致（-0.59±0.01），rebuttal 材料
- 模型规模 DIF：Small underpowered，Medium/Large ρ 一致为负，rebuttal 材料
- Open vs Closed：METABENCH 无 closed-source 模型，不可行

Registry: 无 RUNNING/PREPARING 实验。R20 内审已提交（submit_paper_to_review, continue mode），等审稿结果回来。

### 4. 📋 待办
- R20 审稿报告回来 → 按 review-report-action skill 处理（Holistic Pass → Per-Comment Action Matrix）
- 如果 R20 ≥ 3.5 → 可以考虑提交或做最后一轮 polish
- 如果 R20 仍 3.0 → 评估是否还有可做的实验（NUDIF 全量扩展到 57 subjects 是候选）
- 用户如果确认要提交 → paper_compile_and_check(paper_dir="paper/") 做最终检查
- DDL 5/25 AoE，还有 ~3 天

### 5. 🎯 战略上下文
- **评分历史**：R17=3.0 → R18=3.5 → R19=3.0（数据错误+stale framing 导致掉分，已修复）→ R20 pending
- **核心 claim**：~27-29% MMLU items exhibit temporal DIF；web-overlap 和 DIF 是 orthogonal constructs；base-vs-instruct decomposition 提供 mechanism separation 证据
- **结构性天花板**：W-C3（MH-DIF 是 1988 方法，无 algorithmic novelty）无法通过实验解决，只能通过 framing（已做）。W-C1（因果不可分）已通过 base-vs-instruct + ceiling effect caveat 部分解决
- **易错点**：(1) 不要把 ρ=-0.597 再拿来论证 capability evolution，这个 claim 已被 semi-synthetic 实验 disqualify；(2) 论文 "two convergent methods" 不是 three（de-dup 不再是 convergence 证据，而是 power-scaling 独立证据）；(3) paper_compile_and_check 会报 "16 pages > 8 limit"，这是误报——包含了 appendix，main text 是 8 页
- **决策链**：D038（base-vs-instruct 实验）→ D039（4 组 decomposition 全速推进）。用户（孙震）明确要求不受时间约束、全速推进所有提分路径


---
