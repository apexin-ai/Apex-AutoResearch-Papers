# agent / loop_26.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_26.md`
- **Structured JSON:** [`fb1971027373dd08d3e3.json`](../../sessions/fb/fb1971027373dd08d3e3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 26
reason: idle_timeout
updated: '2026-05-25T17:40:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- **CoRL 2026 DDL = 2026-05-29**（≤4天），5/25 晚前需完成所有主要实验 + 写摘要
- bjb2-40593 的 GPU 分配信息缺失（report.md 显示"无 GPU 信息"），提交实验前必须先确认 gpu_ids 白名单
- bjb1-18228 GPU 0 跑 π0.5 CRM 训练、GPU 3 跑 Long precompute，不可抢占
- Table 1 当前用 K=10，K=2 τ-sweep 是补充实验，不要混入 Table 1 主数据
- 叙事升级目标（D139）：需证明 Adaptive > VLA-only on Spatial/Goal/Object（3 suites 全正向），Object 目前仅 +0.1pp，是最薄弱环节

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: π0.5 CRM 3-suite 统一训练(GPU 0, ETA ~04:00 UTC) + Long precompute(GPU 3, pid=114507)
- **bjb1-32546**: τ-sweep/K-sweep 补充实验(6 GPU)，活跃 cron: eval-k2-tau010-spatial-s42-r2(pid=327574), eval-k2-tau020-spatial-s42(pid=788081), eval-k2-tau030-spatial-s42(pid=475008)
- **bjb2-28827**: D139 种子扩展(6 GPU)，无活跃 cron 显示
- **bjb2-40593**: eval-k2-tau015-spatial-s42 刚超时失败，GPU 状态未知
- **cqa1-32758**: D139 种子扩展(6 GPU)，无活跃 cron 显示
- 活跃 cron 共 5 个：precompute-pi05-long-2048-r2, train-crm-pi05-unified-3suite-r2, eval-k2-tau010/020/030-spatial-s42
- 代码仓库路径：服务器上通常在 `/root/acr-vla-conformal-refinement/`，评估脚本 `evaluate.py` 或 `src/evaluate.py`

### 3. 📊 当前状态
**刚做完**：收到 eval-k2-tau015-spatial-s42 失败 cron 回调，已 spawn Worker (`worker_diagnose_eval-k2-tau015-spatial-s42_20260525T004449`) 诊断超时原因（EXIT_CODE=124, wall_clock=7228s ≈ 2h）。

**RUNNING 实验**：
- `precompute-pi05-long-2048-r2` — π0.5 Long horizon precompute (bjb1-18228)
- `train-crm-pi05-unified-3suite-r2` — π0.5 CRM 3-suite 统一训练 (bjb1-18228)
- `eval-k2-tau010-spatial-s42-r2` — K=2 τ=0.10 Spatial (bjb1-32546)
- `eval-k2-tau020-spatial-s42` — K=2 τ=0.20 Spatial (bjb1-32546)
- `eval-k2-tau030-spatial-s42` — K=2 τ=0.30 Spatial (bjb1-32546)

**等待中**：
- Worker 回调：diagnose worker 正在读 bjb2-40593 日志，诊断超时根因
- π0.5 CRM 训练完成(ETA ~04:00 UTC) → 需立即部署 3 suites eval
- D139 种子扩展结果（s48/s49）— 可能已在 bjb2-28827/cqa1-32758 完成但未通过 cron 报告，需要检查
- eval-pi05-vla-only-object-s43 在 report.md 显示 RUNNING 但未出现在 cron reconcile 中，状态不明

### 4. 📋 待办（条件触发式）
- diagnose Worker 回调 → 读诊断结论，若是单纯超时（rollout 跑完大半）→ 加大 timeout 重试；若是 GPU 问题 → 换服务器重试
- τ-sweep 三个实验(tau=0.10/0.20/0.30) cron 回调 → 汇总 τ-sweep 全部结果（含重试的 tau=0.15），更新 registry + report.md，向 Director 汇报 τ-sweep 完整数据
- train-crm-pi05-unified-3suite-r2 完成 → 立即部署 π0.5 CRM eval（3 suites × 多 seed），π0.5 non-CRM 18 jobs 已审批
- D139 种子扩展全部到齐 → 更新 Table 1 为 8-seed，运行 paired t-test，确认叙事升级是否成立
- 所有主要实验完成 → 触发 Paper Agent 写最新摘要（5/25 晚 deadline）

### 5. 🎯 战略上下文
- **项目核心**：ACR-VLA = Adaptive Conformal Refinement for frozen flow-matching VLAs。CRM 预测 correction，Adaptive gating 决定何时 apply。
- **叙事升级（D139-D146）**：从 "harm avoidance"（CRM 不伤害）→ "CRM + Adaptive 共同提升"。需要 Adaptive > VLA-only 在 3 suites 全正向。Spatial 已显著(p=0.0049 paired)，Goal/Object 需更多种子确认。
- **Mechanism analysis（plan_302）已完成**：K=10 时 30×30 协方差 rank=9，21/30 维度纯噪声 → obs_only 优于 per-DOF 的根因。这是论文 Appendix 材料。
- **Table 1 report 策略（D145）**：n=7 时 p<0.01 为阈值；当前 3-seed 数据见 ROADMAP Table 1。
- **易错点**：
  - eval-pi05-vla-only-object-s43 状态不明（report 说 RUNNING 但 cron 没追踪到），下一个"我"需要主动查
  - bjb2-40593 和 bjb1-18228 的 GPU 分配信息在 report.md 显示缺失，操作前必须查 `get_project_status` 的 gpu_ids
  - K=2 实验是补充实验（τ-sweep），不要与 Table 1 的 K=10 主实验混淆
  - Object suite 是最薄弱的（Adaptive vs VLA-only 仅 +0.1pp），如果 8-seed 后仍不显著，可能需要调整 claim 强度


---
