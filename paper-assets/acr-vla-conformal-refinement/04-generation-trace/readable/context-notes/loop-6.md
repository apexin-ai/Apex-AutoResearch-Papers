# director / loop_6.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`8a06595268bade96516f.json`](../../sessions/8a/8a06595268bade96516f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T19:14:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 gpu_ids，当前 4 台服务器共 17 张卡，不可用白名单外的卡
- bjb2-28827 全部 6 张 GPU 跑 magnitude sweep，不要 kill 任何进程腾卡——这些是 paper figure 3 的数据源
- seed=43 六方对比是关键路径，bjb1-18228 (4 GPU) + bjb1-32546 (部分) 上的 seed=43 实验绝对不能中断
- CRM 参数量以 checkpoint 实际值为准（Agent 正在查），不要用旧 ICLR 的 337K 或估算的 250K
- Paper Agent 已启动写作，不要重复派 Paper Agent 写 Method——它已经在写了

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4 GPU): seed43 obs_only / argmin / perdof + v4-default-r2 ablation
- **bjb1-32546** (6 GPU): seed43 vla-mean / scalar / obs_only-norm02-r2 + magnitude sweep spatial
- **bjb2-28827** (6 GPU): magnitude sweep object (obs_only norm 0.03/0.05/0.3 + perdof norm 0.03/0.05/0.3)
- **bjb2-40593** (1 GPU): obs_only norm=0.03 spatial
- 代码路径: `/root/acr-vla-conformal-refinement`（所有服务器）
- 全部 17 个实验由 cron 自动监控（每 120s 检查），Reviewer 已确认 PASS
- 12 个历史 PREPARING 实验待 Agent 批量 kill（已下指令，在 Agent queue 中）

### 3. 📊 当前状态
**刚做完**：审批 writing_plan.yaml 并启动 Paper Agent 写 Method section；审批 2 个 PENDING 实验并填满所有空闲 GPU；处理 Reviewer 报告修复死进程 + 清理历史实验。

**RUNNING (17)**：
- Seed=43 六方对比 (8 GPU): obs_only / argmin / perdof / scalar / vla_mean / vla_only — 各 4-6/10 task，预计 24-48h 完成
- Magnitude sweep object (6 GPU): obs_only + perdof × norm {0.03, 0.05, 0.3}
- Magnitude sweep spatial 补缺 (2 GPU): obs_only norm=0.03, obs_only norm=0.3
- v4-default-r2 ablation (1 GPU): 无 magnitude control，确认 catastrophic failure

**等待**：
- Agent queue depth=1（CRM 参数量查询 + 历史实验清理）
- Paper Agent 独立写 Method section，完成后会汇报
- 所有实验完成由 cron 回调触发

### 4. 📋 待办
- Seed=43 全部 10 task 完成 → Fisher exact test + bootstrap CI（combined 200 trials）→ p < 0.05 则 paper go，p > 0.05 则评估加 n_rollouts
- Seed=43 obs_only vs argmin gap < 3pp → 触发 kill criteria，项目危险；≥ 5pp → 确认 core claim
- Agent 回报 CRM 精确参数量 → 转发给 Paper Agent
- Magnitude sweep 全部完成 → 画 fig3（SR vs norm ε 曲线）
- Paper Agent 完成 Method section → 审阅，推进 Experiments section（5/19 deadline）
- Abstract DDL 5/26 前必须有 seed=43 统计结果 + 完整 abstract

### 5. 🎯 战略上下文
- **Core claim**: obs_only CRM +7.0pp over argmin on object (19.0% vs 12.0%)，超过 5pp 门槛但需 seed=43 统计确认
- **Honest negative**: per-DOF conformal features 无效（11.0% ≈ argmin 12.0%），这是 paper 的学术贡献之一不是缺陷
- **Spatial 是 null result**: 所有方法 30-35%，CRM 在 spatial 上无效。已决定 honest reporting，不 bury
- **Magnitude control 是第三个 claim**: norm=1.42 → 0% catastrophic，obs_only 对 norm 鲁棒而 perdof 在高 norm 崩塌
- **易错点**: seed=43 早期信号（4/10 task）显示 obs_only gap 缩小（+2.5pp vs seed=42 同期 +7.5pp），但后 6 task 包含大 gap task，不要提前恐慌。等全部 10 task 再判断
- **Paper framing 已从 ICLR 转 CoRL**，旧 .tex 全部作废，Paper Agent 全部重写
- 决策链关键节点: D027 kill criteria → D029 spatial dead → D030 object +7pp confirmed → D031 seed=43 doubling → D032 magnitude sweep → D033 writing plan approved


---
