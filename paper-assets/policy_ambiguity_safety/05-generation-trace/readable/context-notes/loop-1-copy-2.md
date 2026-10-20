# agent / loop_1.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`8ee09435f38b04f82850.json`](../../sessions/8e/8ee09435f38b04f82850.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T17:32:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU，全部实验走 OpenRouter API proxy（`http://47.94.22.126/v1`）
- τ²-bench 拼写必须是 `$\tau^2$-bench`（Barres 2025），绝对不能改成 τ-bench
- 论文正文严格 8 页限制（EMNLP 2026），每次编辑后必须编译确认。当前刚好卡在 8 页边界，加 1-2 行就可能溢出
- C4 (model×type interaction) 所有措辞必须标注 [Exploratory]，不可升级为 primary claim
- C3 (layer effect) 标注 inconclusive，不可声称 significant
- plan_015 escalation 数据的 mechanism 引用 §6 = 5 模型数据，violation rates = 7 模型，不可 overclaim mechanism 覆盖 7 模型

### 2. 🖥️ 基础设施快照
- 无远程服务器，全部本地执行
- 工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/`
- 论文源码：`docs/paper/sections/*.tex`，主文件 `docs/paper/main.tex`
- Python venv：`artifacts/.venv/`（Python 3.14），`source artifacts/.venv/bin/activate`
- API config：`artifacts/config.py` + `artifacts/config_local.py`
- 全部实验数据：`artifacts/full_study/`（episodes, judgments, analysis）
- 人工标注：`artifacts/human_annotation_100episodes_{1,2}.jsonl`
- 活跃进程：无 tmux/cron。1 个 Worker 正在运行（见§3）

### 3. 📊 当前状态
**刚完成**：plan_014（perturbation n=300）和 plan_015（auth_scope escalation 方向）的论文整合。三处 perturbation 数字更新（§4 ×2, §5.1 ×1）+ Discussion escalation 句。编译 12 页 / 正文 8 页。

**正在运行**：
- Worker `worker_analysis_r6w6_per_type_human_agreement_20260521T150951` — 计算 per-type human-LLM binary κ（从 human_annotation + full_study judgments）
- **任务 2 (R6-W4 C4 logistic regression) 尚未 spawn**！Director 指令要求并行两个 Worker，但只成功 spawn 了任务 1 就被 WRITE HANDOFF 打断

**Registry**：plan_014 DONE/success, plan_015 DONE/success。其他 13 个实验全 DONE。无 RUNNING/PREPARING。

**等待中**：
- Worker r6w6 回调 → 需要处理结果 + 汇报 Director
- C群二审反馈（已提交，等待中）
- plan_009 人工标注（标注者 2026-05-21 到位，材料已就绪）

### 4. 📋 待办
- **立即**：spawn R6-W4 Worker（C4 logistic regression robustness check）— 被 handoff 打断未执行。Director 原始指令在上一条消息，数据在 `artifacts/full_study/judgments/`，输出到 `artifacts/round6_supplementary/c4_logistic_robustness.json`
- Worker r6w6 回调到达 → 读取 `artifacts/round6_supplementary/per_type_human_agreement.json`，汇报 Director（关注 auth_scope κ 是否偏低）
- Worker r6w4 回调到达 → 读取 `artifacts/round6_supplementary/c4_logistic_robustness.json`，汇报 Director（关注 interaction LR test significance + top-3 terms）
- Director 指令论文整合 → 更新对应 tex 文件，编译确认 8 页
- C群二审反馈到达 → 按反馈逐条处理

### 5. 🎯 战略上下文
- **项目阶段**：C群二审已提交（Overall 3.0 → 目标 3.5+），正在做 Soundness 加固分析。当前 round6 supplementary 是 Reviewer 要求的补充证据
- **核心结论**：ambiguous clauses +34pp violations (OR=15.1), three-tier type hierarchy (incompleteness > mid-cluster > coreferential), auth_scope = canary type (12-64% cross-model), incompleteness = universal blind spot (46-62% all 7 models)
- **Soundness 瓶颈**：error analysis 仅 LLM-coded（plan_009 人工标注是关键提分项），n=50 per cell power 有限
- **易错点**：
  - 页面预算极紧（p8 左栏 Discussion 刚好结束），任何正文添加都需要等量压缩
  - experiments.tex 被外部修改过（§5.2 TOST 段措辞调整为 "two-tier structure among five types"），不要 revert
  - Appendix E Table E1 用了 `\resizebox{\columnwidth}{!}`，不要去掉
  - plan_010 原始 perturbation 数据（n=120）已被 plan_014（n=300）取代，论文中所有 perturbation 数字应引用 plan_014


---
