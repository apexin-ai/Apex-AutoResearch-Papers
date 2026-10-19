# agent / loop_24.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_24.md`
- **Structured JSON:** [`431c4809b8dbc1f2447f.json`](../../sessions/43/431c4809b8dbc1f2447f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 24
reason: idle_timeout
updated: '2026-05-22T23:10:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 17 张：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5。白名单外的 GPU 即使 Director 指令也必须 push back
- Loss 变体 val_loss 不可直接跨变体比较（perdof 用 inverse-variance 加权，loss 数值尺度不同）。最终比较只看下游 robot eval success rate
- SmolVLA Plan A 核心结果已 LOCKED（Object 18.3%±2.1%, Spatial 35.0%±1.0%），不可修改
- π0.5 baseline 已 LOCKED（Object 81.5%±0.5%, Spatial 84.2%±1.0%）
- CoRL 2026 DDL: 2026-05-29，剩余 ≤7 天

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 工作目录 /root/acr-vla-conformal-refinement, Python /root/miniconda3/bin/python, conda base。磁盘 400G/438G(4%)
- **bjb1-32546**: 同上结构, 磁盘 400G/438G(4%)
- **bjb2-28827**: 同上结构, 磁盘 399G/439G(5%)
- **bjb2-40593**: 磁盘紧张 46G/437G(90%) ⚠️
- CRM cache: /root/autodl-tmp/crm_cache_v5/（14570 samples, Object+Spatial）
- Loss 变体 checkpoint 目录: /root/autodl-tmp/checkpoints/crm_loss_variants/{mse,perdof_weighted,conformal_guided,combined}/crm_best.pt（在 bjb1-18228）
- 活跃进程: eval-pi05-crm-object-seed42/43/44 (bjb1-32546 cuda:0-2, PID 218131/218420/218700), eval-pi05-crm-spatial-seed42/43/44 (bjb2-28827 cuda:0-2, PID 148748/149025/149307), crm-loss-combined (bjb1-18228 cuda:3, PID 845729)

### 3. 📊 当前状态
刚处理 crm-loss-mse-baseline CRON 回调。三个 loss 变体训练已完成（mse/perdof/conformal），combined 仍在跑。

**RUNNING 实验 (7)**:
- eval-pi05-crm-object-seed42/43/44 — π0.5 + CRM Object eval（Track 1）
- eval-pi05-crm-spatial-seed42/43/44 — π0.5 + CRM Spatial eval（Track 1）
- crm-loss-combined — 第 4 个 loss 变体，epoch ~48/50，即将完成

**ANALYZING (3)**:
- crm-loss-mse-baseline — 等分析 Worker 完成
- crm-loss-conformal — 等分析 Worker 完成
- crm-loss-perdof — 已有 metrics（val_loss=0.000124），conclusion=success

**等待中的 Worker 回调 (4)**:
- worker_analyze_crm-loss-mse-conformal — 分析 mse + conformal 日志并推进 DONE
- worker_deploy_precompute-goal-long-bjb2 — Goal/Long precompute（Track 3）
- worker_code_pi05-server-mode — π0.5 代码适配
- worker_analyze_crm-loss-perdof — 可能已完成（registry 已有 metrics）

**已向 Director 汇报**: loss 变体训练进展 + 10 张空闲 GPU，等 Director 指示是否立即开始 loss 变体下游 eval

### 4. 📋 待办
- analyze Worker 回调到达 → 确认 mse/conformal checkpoint 有效 → 准备下游 eval（每个变体 × Object × 3 seeds）
- crm-loss-combined CRON 回调 → 分析第 4 个变体 → 四个变体全部就绪后铺 eval
- π0.5 eval (6个) CRON 回调 → 收集 success rate → 写入论文（ceiling effect 预期，framing "no-harm + selective improvement"）
- precompute-goal-long Worker 完成 → merge cache → 训练统一 4 套件 CRM（Track 3）
- pi05-server-mode Worker 完成 → 推进 Track 4 OpenVLA-OFT baseline eval
- Director 批准 loss 变体 eval → 用 bjb1-18228 cuda:0-2 + 其他空闲 GPU 铺开
- 10 张空闲 GPU 必须尽快填满——loss 变体 eval 是最直接的填充对象

### 5. 🎯 战略上下文
- **四线并行**: Track 1 π0.5 eval(RUNNING) / Track 2 loss 变体(训练接近全部完成) / Track 3 四套件统一 CRM(precompute中) / Track 4 OpenVLA-OFT(代码适配中)
- **Method paper 定位**（D106，用户最高权限指令），不是 analysis paper
- **验证矩阵**: SmolVLA Object+Spatial LOCKED; π0.5 Object+Spatial 在跑; Goal/Long/OpenVLA-OFT 待铺
- **易错点**: perdof val_loss=0.000124 看起来比 mse=0.002080 好 17 倍，但这是加权 loss 的数值假象，不能在汇报中声称 "perdof 更好"——必须等 eval success rate
- **易错点**: bjb2-40593 磁盘只剩 46G，不要在上面跑大实验
- **关键决策链**: D105(π0.5 baseline locked) → D106(method paper) → D107(最小可行论文范围 + OpenVLA-OFT diversity gate)


---
