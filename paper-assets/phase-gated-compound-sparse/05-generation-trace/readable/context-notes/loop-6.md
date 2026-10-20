# director / loop_6.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`2d022ff0654887fa7bc8.json`](../../sessions/2d/2d022ff0654887fa7bc8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T20:14:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：项目有 4 张卡，具体 device id 需 `get_project_status` 确认，不要用白名单外的卡
- 统计方法已锁定 v3 median-based（非 mean-based），所有新分析必须用 median gradient + Wilcoxon signed-rank，不要回退到 v1/v2 mean-based
- QW rand s030 已标记 INVALID（median 分析下），论文中不能作为正面证据引用
- `&lt;think>` token 有效样本 n=48（非 192），已在 artifact 中标注，不要用错基数

### 2. 🖥️ 基础设施快照
- 需要 BOOT 后重新 `get_resource_inventory` + `list_ssh_hosts` 确认——本轮 handoff 时无法直接 SSH 查
- 项目工作目录：远程 `execution.project_path` 需从 `load_project_config(section="execution")` 获取
- 关键 artifacts 在本地 `projects/phase-gated-compound-sparse/artifacts/` 下，包括 v3 分析结果、dream reports、review reports

### 3. 📊 当前状态
**刚完成的 R9 任务：**
- Worker C (CPU 分析) 已完成 4 个子任务：post-hoc power analysis (9/16 powered)、II_high sensitivity、G×D082 确认（R9-W1 可关闭）、outlier case study (gsm8k_189 数值伪影)
- think_phase_validation → DONE/success (effective_n=48, median_κ=0.887)
- Reviewer PASS 了 QW truncation explanation（minor warning：脚注数字需用 v3 median 而非 mean）

**未确认完成的 Worker：**
- Worker B (accuracy spike 调查)：Agent 报告已运行 ~24min，是关键路径，但 Agent idle 3h 后被 reset——结果可能已完成但未汇报
- Worker D (QW truncation)：Agent 报告已运行 ~10min，同上

**BOOT 后第一件事**：`get_project_status` 检查 registry 中 Worker B/D 对应实验状态，确认是否已完成

### 4. 📋 待办
- Worker B/D 结果已在 registry → 收集结果，完成 R9 全部子任务的汇总
- Worker B/D 未完成 → 重新派 Worker 执行
- R9 全部完成 → 向 Director 汇报完整 R9 结论，等 Director 下一步指令
- Reviewer 提到脚注需改用 v3 median gradient → Paper Agent patch 任务（等 Director 派单）
- Power analysis 结果（9/16 well-powered）→ 论文 Appendix 需加 power analysis table + sensitivity analysis for II_high ≤ 0

### 5. 🎯 战略上下文
- 项目已进入审稿阶段，Research Director 专注实验，Review Director (Group C) 负责论文格式和投稿
- 核心结论：DS importance 全 4 个 sparsity level fully powered，是最强证据线；QW importance s025/s030 也 powered；random masking 在低 sparsity 下 underpowered 符合预期（小 effect size）
- R9 是 round 9 的补充验证/robustness 任务，不是新实验方向
- 易错点：v1/v2/v3 三版统计结果容易混淆——只用 v3，v3 的标志是 median gradient + Wilcoxon + INVALID 标记机制
- 决策链参考 `decisions.yaml`，framing 参考 `paper_framing.md`，实验计划参考 `experiment_plan.yaml`


---
