# reviewer / loop_5.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`847e08c0d5ef85f80a52.json`](../../sessions/84/847e08c0d5ef85f80a52.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-25T03:21:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无远程 GPU 训练，所有实验通过 API 调用完成（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3），无 cuda 设备约束
- 论文目标 venue: EMNLP 2026 ARR，**8 页正文硬限**（references 无限，Limitations 不计页数）
- Abstract ≤ 200 words（当前 ~137 words，合规）
- Limitations 只能有一个 section 在正文，appendix 不能有 Limitations section
- **per-type κ 有两套数值不能混用**：human-LLM κ（n=32-34/type, from tab:per_type_agreement）vs dual-judge calibration κ（n≈16/type, from dual_judge_calibration.json）。R33 曾因混用导致 CRITICAL

### 2. 🖥️ 基础设施快照
- 服务器：localhost(ubuntu)，纯本地执行
- 工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/`
- 论文源码：`docs/paper/`（main.tex + sections/*.tex）
- 产出目录：`artifacts/`（分析 JSON、episode 数据等）
- 图表目录：`docs/paper/figures/`（8 张图，全部 PDF 矢量格式）
- 无活跃进程、无 tmux、无 cron

### 3. 📊 当前状态
刚完成全面视觉质量审查（逐页 P1-P8 + 逐图 8 张 + 逐表 4 张 + 被删表数据覆盖验证）。所有审查报告已通过 `reviewer_post_to_director` 提交。

已完成的审查轮次：
- R31（C3 降级、页面预算）→ PASS
- R32（incompleteness reframing、convergent nocuity +8.3pp 修正）→ PASS
- R33（per-type κ 修正、token interaction appendix、MH OR）→ PASS（含 1 次 FAIL 返工）
- Fig 1 修复验证（Conditional Precedence + M5）→ PASS
- Fig 2 forest plot → PASS
- Fig variance decomp（worker failed due to API overload but figure saved）→ PASS
- 全文视觉审查 → 2 warnings（Fig 4 sparse + P7/P8 密度失衡），无 critical

Registry 全部 DONE，无 RUNNING/PREPARING 实验。DDL ~5/26。

### 4. 📋 待办
- Director 回复视觉审查报告 → 若要求修 Fig 4（cross-benchmark），审查新版本
- 论文编译最终版提交前 → 建议做一轮 abstract word count 确认 + Limitations section 存在性确认（check_figures_and_layout 误报了 Limitations missing，实际 `\section*{Limitations}` 存在）
- 若 Director 要求 pre-submission 全文一致性终检 → 重点核验：所有正文数字 vs registry/analysis JSON 一致性

### 5. 🎯 战略上下文
- 核心贡献 2 条：C1（causal effect +34.0pp / +31.0pp excl incomp）+ C2（convergent nocuity 41.3% → consensus monitoring blind）
- C3（type-mechanism dissociation）已降级为 1 句 exploratory reference in intro
- **incompleteness 是全文最敏感的叙事点**：信息添加 confound 导致其 +49.2pp 是上界；token interaction 显著（p=0.0004）但 within-type 不显著（auth p=0.709, incomp p=0.150）；dual-number 呈现（+34.0 overall / +31.0 excl incomp）是 R32 确定的策略
- **最易判断错的事**：per-type κ 的两套数值。experiments.tex L50 用 human-LLM κ（0.479-0.904），Table 2 footnote 用 dual-judge κ（0.385）。两者来源不同、n 不同、含义不同，绝不能交叉引用
- SOPBench 是 "cross-benchmark evaluation" 不是 "replication"（R33 已统一术语）


---
