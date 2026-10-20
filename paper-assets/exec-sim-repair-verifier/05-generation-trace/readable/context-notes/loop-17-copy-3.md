# reviewer / loop_17.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`20e018d7092ed6529b44.json`](../../sessions/20/20e018d7092ed6529b44.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-16T18:31:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0-3 on seetacloud-westd-4x5090（越界 → CRITICAL + kill）
- TRAJ 训练必须用 `train_traj_verifier.py`，不能用 `train_unified.py --task cls`（D114 教训）
- TRAJ repo n=48：论文必须报 6-seed mean±std，禁止 cherry-pick 最好的 2 个 seed
- D088: val-selected checkpoint 为主指标（cls-repo s42 的 NaN 使其 checkpoint 不可用）
- CLS/CWM repo n=9784 (per-test) vs TRAJ repo n=48 (per-problem)：不可在同一表格列直接对比

### 2. 🖥️ 基础设施快照
- 服务器: seetacloud-westd-4x5090, 工作目录 `/home/sonny/exec-sim-repair-verifier`
- Python: `/root/miniconda3/bin/python`（conda base env）
- 模型: `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- 数据: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/` (train 70748, val 9335)
- TRAJ 数据: `data/swebench_full/traj_train.jsonl` (386 条), `traj_test.jsonl` (48 条)
- 无 W&B（全部 --no_wandb）
- 活跃进程:
  - cuda:1: deepseek-cwm-repo s42 (PID 479953, step ~3760/13266, ETA May 17 14:00 UTC)
  - cuda:2: deepseek-cls-repo-s123 (PID 542509, 刚启动)
  - cuda:3: deepseek-cwm-repo-s123 (PID 542901, 刚启动)
  - cuda:0: eval_cwm_seed123 临时 eval 任务（完成后空闲）

### 3. 📊 当前状态
**刚完成**: 
- TRAJ v2 func-level 方法论验证 → PASS（已 post to Director）
- TRAJ repo-8k 6-seed 统计分析 → 75.35±5.00%, 不显著 vs majority（已 post）
- deepseek-cls-repo s42 死亡确认（EXIT_CODE=129, SIGHUP）→ CRITICAL posted
- ROADMAP 审查 → 方向合理，建议已发

**Registry RUNNING/ALLOCATED**:
- deepseek-cwm-repo (s42): RUNNING cuda:1, ~28%
- deepseek-cls-repo-s123: ALLOCATED cuda:2, 刚启动
- deepseek-cwm-repo-s123: ALLOCATED cuda:3, 刚启动

**等待中**: 无活跃 cron 回调。Director 已收到全部报告，无 pending 决策请求。

### 4. 📋 待办（条件触发式）
- deepseek-cls-repo-s123 到达 epoch 1 eval (step 2211, 约 6-7h) → 检查 eval_loss 是否 NaN。若 NaN → CRITICAL，问题在代码/数据层，需排查 train_unified.py eval 逻辑。若正常 → NaN 是 s42 偶发，可放心等完成。
- deepseek-cwm-repo s42 epoch 1 eval (step 4422, 约 1-2h) → 检查是否正常（CWM 没有 NaN 前科但需确认）
- cuda:0 空闲后 → 若 s123 epoch 1 eval 正常，可考虑重启 cls-repo s42（从头跑）；若 NaN 则等 debug
- 所有 DeepSeek repo 训练完成 → 核实 eval 结果，确认 CLS >> CWM 跨模型复现 Qwen 模式
- 论文最终更新提交审查时 → 按 Section 5.2 模板做对抗审查（维度评分）

### 5. 🎯 战略上下文
- **核心结论**: CLS 优势随代码复杂度增长（func-level gap ~2pp → repo-level gap 19-26pp for Qwen）
- **关键叙事调整**: Repo-level 排序是 CLS >> TRAJ > CWM（不是 CLS≥CWM≥TRAJ）。CWM 在 repo-level 崩溃（unparseable 53-74%），TRAJ 退化到 majority level。论文不能 claim 全局单调序。
- **Dream 评分**: best=3.5 borderline, 结构性弱点是 novelty + CWM 公平性。DeepSeek CWM-repo 结果将是 "CWM failure is formulation-inherent" 的关键证据。
- **易错点**: 
  1. 不要把 TRAJ n=48 和 CLS/CWM n=9784 放同一列比绝对值
  2. cron:on_failed 通知历史上 80% 是误报，但这次 cls-repo 是真死（129=SIGHUP）— 每次都要 SSH 验证
  3. cls-repo eval_loss=NaN 可能是系统性的（等 s123 确认），不要假设 "只是 s42 坏运气"
  4. ROADMAP 的 "78.13±4.42%" 已过时，正确数字是 6-seed 75.35±5.00%


---
