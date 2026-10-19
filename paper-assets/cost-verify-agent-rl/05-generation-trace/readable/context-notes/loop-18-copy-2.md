# agent / loop_18.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`6e07ffc0402da139cd19.json`](../../sessions/6e/6e07ffc0402da139cd19.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-19T10:02:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-17606 GPU 白名单: cuda:0,1。westd-47453 GPU 白名单: cuda:0,1,2,3。白名单外的 GPU 即使 Director 指令也必须 push back
- exp029_episode_level_seed2 在 bjb1 2×GPU 上已失败 8+ 次（CUDA OOM），不要再在 bjb1 上重试相同配置——必须等 westd 4卡或 Director 批准新方案
- seed 1 的 step 15 checkpoint 在 bjb1 `/root/autodl-tmp/checkpoints/exp029-seed2/global_step_15/`，step 20 已确认损坏并删除。hsweep_h2 seed1/seed2 共享 checkpoint 目录（`/root/autodl-tmp/checkpoints/hsweep-h2/`），seed2 覆盖了 seed1 的 global_step_15
- 核心 claim（23.88% OOD）建立在单 seed 上，论文不能在 seed 2 结果出来前声称 "robust"

### 2. 🖥️ 基础设施快照
- **bjb1-17606**: 工作目录 `/root/cost-verify-agent-rl/RAGEN`，Python `/root/miniconda3/bin/python`，磁盘 ~120GB free（/root/autodl-tmp）。当前 GPU 空闲（exp029_seed2 反复失败后无进程）
- **westd-47453**: 工作目录 `/root/autodl-tmp/cost-verify-agent-rl/RAGEN`，Python `/root/miniconda3/bin/python`，磁盘 ~810GB free
- **westd 活跃进程**:
  - factorial_h2_episodeadv_seed1: PID 475745, westd cuda:0,1, step 9/15, W&B 6liw7fm1
  - gsweep_g100_h5_seed1: westd cuda:2,3, W&B da7701tk（刚从 g095 killed 后启动）
- **Cron**: reconcile 确认 factorial + gsweep_g100 两个 cron 活跃
- **W&B project**: cost-verify-agent-rl
- 预置镜像: `aml-train`（两台服务器均可用）

### 3. 📊 当前状态
刚处理 exp029_seed2 第 8+ 次失败 CRON 回调。已派诊断 Worker (`worker_diagnose_exp029-seed2-persistent-failure_20260518T172904`) 读取最新日志 `exp029_seed2_resume_step15_fixA.log`，**等待回调**。已向 Director 汇报持续故障并建议方案 A（等 westd GPU 释放后用 4 卡跑）。

**Registry RUNNING**:
- `factorial_h2_episodeadv_seed1` — Cell B 关键实验，step 9/15，KL 膨胀 1.77，step 10 val 是关键拐点
- `gsweep_g100_h5_seed1` — γ=1.0 控制组，刚启动

**Registry PENDING**:
- `factorial_h2_episodeadv_seed2` — 等 Director 审批 + westd cuda:0,1 释放

**等待中**:
- 诊断 Worker 回调（exp029_seed2 持续失败根因）
- Director 对 exp029_seed2 方案的决策（A/B/C 三选一）
- factorial step 10 val cron 回调（最关键数据点）

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调到 → 读报告，更新 registry notes，如有新发现补充汇报 Director
- Director 决策 exp029_seed2 方案 → 按决策执行（大概率方案 A 等 westd）
- factorial cron 回调（step 10 val）→ 按 on-experiment-done 流程处理：更新 registry + 3-cell 分解比例 + 汇报 Director
- factorial 完成（15/15）→ westd cuda:0,1 释放 → 立即提交 factorial_seed2（已 PENDING 等审批）或 exp029_seed2（取决于 Director 优先级）
- gsweep_g100 完成 → westd cuda:2,3 释放 → 看 ROADMAP 下一个 gsweep 或其他实验
- gsweep_g095 已确认 negative（step 5 collapsed, val=0%）→ 需向 Director 汇报（如果上一个 session 未汇报）

### 5. 🎯 战略上下文
- **核心 framing (D070)**: 3-cell 分解——information loss 89% (17.9pp) + sign misattribution 11% (2.2pp)。两者正交：info loss 限制学习上限，sign misattribution 是 collapse trigger
- **P0 风险 (C3)**: 统计 power。核心 claim 全部单 seed。exp029_seed2 + factorial_seed2 是解决 C3 的唯一路径。exp029_seed2 持续失败是当前最大瓶颈
- **决策链**: D062(放弃contrarian)→D067(catastrophic→fragility)→D068(OOD reeval 23.88%)→D069(GPU priority shift to seeds)→D070(3-cell分解)
- **易错点**:
  1. 不要在 bjb1 上再试 exp029_seed2 相同配置——已证明 2×GPU 不够。只有 Director 明确批准新方案才能重试
  2. factorial step 10 val 是决定 Cell B 最终数值的关键——如果显著偏离 step 5 的 5.97%，3-cell 分解比例需要重算，paper_framing.md 需要更新
  3. gsweep_g095 negative (collapsed) 是预期内的——γ=0.95 h=5 复现了 h-sweep 的 collapse pattern，不是坏消息
  4. Worker 池 < 2 = 失职——诊断 Worker 回调后如果没有其他 CPU 任务，找文献调研/论文起草等并行铺开


---
