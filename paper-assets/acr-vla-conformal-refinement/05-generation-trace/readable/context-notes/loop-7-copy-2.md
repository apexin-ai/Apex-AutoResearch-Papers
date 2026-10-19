# agent / loop_7.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`879d3da1884f35f01a90.json`](../../sessions/87/879d3da1884f35f01a90.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T04:40:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- **bjb1-18228 GPU 白名单**: cuda:0,1,2,3（4× RTX 4090）。当前全部在跑 spatial eval，不可中断
- **bjb1-32546 GPU 白名单**: cuda:0,1,2,3,4,5（6× RTX 4090）。全满载 object eval
- **bjb2-28827 GPU 白名单**: cuda:0,1,2,3,4,5（6× RTX 4090）。全满载 magnitude sweep
- **bjb2-40593**: 1× RTX 4090D，D024 决定 kill v4-default-r3（norm=1.42），尚未执行
- **Claim 1 framing 裁决禁止在 spatial 全 10 task 完成前做出**（D025 硬约束）。当前 perdof 42%@5tasks vs obs_only 48%@5tasks vs argmin 37.5%@8tasks，gap 在噪声范围内
- **CoRL 论文只剩 Claim 1**（D022 砍 Claim 3 SRPO，D023 砍 Claim 2 ACI/COC）。不要尝试恢复已砍 claim

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base。模型 `/root/autodl-tmp/models/smolvla_libero/`，CRM checkpoints `/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,obs_only,scalar_unc}/crm_best.pt`，数据 `/root/autodl-tmp/libero_data/`，日志 `/root/autodl-tmp/logs/`
- **bjb1-32546**: 同上路径结构（独立实例），submit_training_job 提交，日志在 `~/runs/acr-vla-conformal-refinement/`
- **bjb2-28827**: 同上路径结构，SmolVLM2+CRM+code 已就绪。6 个 magnitude sweep 实验直接 python 启动
- **活跃进程 16 个**（全部 cron 监控中，reconcile 确认全部 still running）：
  - bjb1-18228: PID 231421/253085/270097/288939
  - bjb1-32546: PID 9659/11116/13797/14003/17222/18808
  - bjb2-28827: PID 13185/13456/13728/14260/14854/15190
- **活跃 Worker 2 个**: `worker_ops_collect-spatial-bjb1-18228` + `worker_ops_collect-object-bjb1-32546`（正在收集中间结果）

### 3. 📊 当前状态
上一轮 session 完成了：D021-D025 决策、object eval 全 6 GPU 部署、magnitude sweep 全 6 GPU 部署、spatial eval 中间指标收集。

**Spatial eval (bjb1-18228, ~5-7h 剩余)**:

| 实验 | Mode | Tasks | SR | 趋势 |
|------|------|-------|----|------|
| argmin-only | reconvla K=10 | 8/10 | 37.5% | 接近完成，预计最终 ~34% |
| v4-small (perdof) | acr_vla, norm=0.1 | 5/10 | 42.0% | +4.5pp over argmin，边缘 |
| obs-only-r2 | crm_obs_only, norm=0.1 | 5/10 | 48.0% | 领先 perdof 6pp |
| v4-scalar | crm_scalar, norm=0.1 | 2/10 | 80.0% | 仅 easy tasks，不可信 |

**Object eval (bjb1-32546, 刚启动 ~2h)**:
- reconvla-object / perdof / obs-only / scalar 全部 0/10 tasks（模型已加载，rollout 中）
- vla-only-object: 3/10 tasks, 10%；vla-mean-object: 0/10 刚启动

**Magnitude sweep (bjb2-28827, 刚启动 ~1.5h)**:
- perdof norm ∈ {0.03, 0.05, 0.2, 0.3} + obs-only norm ∈ {0.05, 0.2}，全部 spatial benchmark

**等待中**:
- 2 个 collection Worker 正在跑，完成后会回调
- 所有 16 个 cron 活跃，实验完成时自动回调
- bjb2-40593 v4-default-r3 待 kill（D024 已决策但未执行）

### 4. 📋 待办（条件触发式）
- **spatial eval 全 10 task 完成** → 汇总四路 SR，计算 binomial CI，做 Claim 1 framing 裁决（Scenario A/B/C/D 见 paper_framing.md）
- **perdof > obs_only ≥ 5pp (Scenario A)** → "per-DOF conformal features 有独特价值" narrative，立即启动 Paper Agent
- **perdof ≈ obs_only ± 3pp (Scenario B, 当前最可能)** → 转 "uncertainty-conditioned learned correction" narrative，per-DOF 降为 ablation 变体，magnitude sweep 成为独立贡献
- **CRM correction < 3pp over argmin (Scenario D)** → Claim dead，向 Director 汇报 pivot
- **object eval 完成** → cross-benchmark validation，确认 spatial 结论是否泛化
- **magnitude sweep 完成** → 绘制 norm vs SR 曲线，找最优 norm，验证 0.1 是否已最优
- **bjb2-40593** → 执行 kill v4-default-r3，释放 GPU 跑 reconvla-object n=20（或其他）
- **collection Worker 回调** → 更新 registry metrics，刷新 report.md，判断是否需向 Director 汇报

### 5. 🎯 战略上下文
- **核心悬念**：CRM learned correction 到底有没有用？当前 perdof 仅 +4.5pp over argmin（42% vs 37.5%），obs_only +10.5pp（48%），但都只有 5/10 tasks。后 5 个 task 包含困难任务（on_stove 历史 0%），会拉低所有方法的 SR
- **决策链**：D001→D003(MVP pass)→D008(需 fine-tuned VLA)→D009(社区 checkpoint)→D018(normalization fix)→D019(magnitude control)→D020(obs_only training loss 更好)→D021(重新瞄准 CoRL)→D022-D023(砍到单 Claim)→D025(等全量结果)
- **最容易判断错的事**：不要看到 scalar 80%@2tasks 就认为 scalar 最好——那 2 个是最 easy 的 task，perdof/obs_only 在同样 task 上也是 80-100%。必须等全 10 task
- **容易踩的坑**：(1) bjb1-18228 spatial eval 用的是直接 nohup 启动而非 submit_training_job（历史遗留），cron 仍在监控但日志路径在 `/root/autodl-tmp/logs/` 而非 `~/runs/`；(2) eval-acr-object-v4-perdof 的 mode 在 log 里显示 `crm_perdof` 而非 `acr_vla`——这是正常的，evaluate.py 内部映射；(3) Baselines 已锁定（spatial: VLA-only 30%, VLA-mean 31%, argmin 34%; object: VLA-only 13%），不要重跑
- **DDL**：CoRL abstract ~May 26（11 天），full paper ~Jun 2（18 天）。单 claim 论文，关键是实验证据足够强


---
