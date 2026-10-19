# agent / loop_20.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_20.md`
- **Structured JSON:** [`0085a9c7bd978f219319.json`](../../sessions/00/0085a9c7bd978f219319.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: idle_timeout
updated: '2026-05-17T22:05:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb2-28827 GPU 白名单: cuda:0~5（全部分配给本项目）
- bjb1-32546 GPU 白名单: cuda:0~5
- K=1 和 K=10 结果**不得混比**。K=10 只作 supplementary evidence
- train-crm-k1-accg-object-seed42-v2 的 conclusion 字段当前是 "failed"（之前误设），需要根据 Worker 分析结果更正
- eval-k1-crm-accg-object-seed42/43/44 三个 eval 实验刚刚注册（用的是 fallback 模型 checkpoint，不是 v2 模型），它们依赖的是 train-crm-k1-accg-object-seed42-fallback

### 2. 🖥️ 基础设施快照
- 服务器 bjb2-28827: 工作目录 /root/acr-vla-conformal-refinement/
- 服务器 bjb1-32546: 工作目录 /root/acr-vla-conformal-refinement/
- 服务器 bjb1-18228: OpenVLA eval 实验（eval-openvla-object-vla-only-seed42 在 ANALYZING）
- 数据集: /root/autodl-tmp/libero_data/libero_object/ (72507 samples)
- W&B project: acr-vla-conformal-refinement
- 关键 run: crm-k1-v2-accg-multistage-object（刚完成的 v2 训练）
- 活跃进程（reconcile_crons 确认）:
  - eval-perdof-object-norm02-seed46 (pid 389051)
  - eval-perdof-object-norm01-seed47-bjb1 (pid 414817)
  - eval-obs-only-object-norm03-seed46 (pid 416568)
  - eval-perdof-object-norm01-seed46-r2 (pid 393646)
  - eval-obs-only-object-default-seed46 (pid 422357)
  - eval-perdof-object-default-seed46 (pid 423767)
  - eval-obs-only-object-norm005-seed43-r2 (pid 433500)
  - eval-perdof-object-norm02-seed47 (pid 404983)
  - eval-random-selection-object-seed42 (pid 395256)
  - eval-perdof-object-norm02-seed45-r2 (pid 634438)
  - eval-obs-only-object-norm005-seed43-r3 (pid 633649)
  - eval-obs-only-object-norm02-k5-seed42 (pid 633736)
  - eval-obs-only-object-norm02-k20-seed42 (pid 636713)
  - eval-k1-crm-accg-object-seed42/43/44（刚注册，cron 跳过中）

### 3. 📊 当前状态
- **刚做完**: Session 启动初始化（reconcile crons + read registry/roadmap/report）
- **正在做**: 已派 Worker `worker_analysis_train-crm-k1-accg-v2_20260517T180340` 分析 train-crm-k1-accg-object-seed42-v2 的训练结果（读 log + W&B + checkpoint）。**Worker 尚未回调**。
- **等待中**:
  - Worker 回调 → 根据结论更新 registry（修正 conclusion 字段）、汇报 Director
  - 13 个 eval 实验 cron 监控中
  - eval-openvla-object-vla-only-seed42 也在 ANALYZING（bjb1-18228），可能也需要分析
- **Registry 待处理**: report.md 中列的 PREPARING 实验都在排队等 GPU/结果

### 4. 📋 待办（条件触发式）
- Worker analysis 回调 → 更新 train-crm-k1-accg-object-seed42-v2 的 conclusion/metrics/checkpoint_path → 汇报 Director
  - 如果 val_loss < 0.006505（优于 fallback）→ conclusion=success，建议用 v2 checkpoint 启动 3-seed eval
  - 如果 val_loss ≥ 0.006505 → conclusion=negative，向 Director 汇报"多阶段特征未改善"，推导下一步
- eval-k1-crm-accg-object-seed42/43/44 完成 → 分析 ACCG fallback 模型在 K=1 eval 的表现 vs VLA-only baseline (10.8%)
- eval-openvla-object-vla-only-seed42 分析回调 → 这是 OpenVLA baseline（plan_801），记录 metrics 作为 OpenVLA K=1 VLA-only baseline
- eval-random-selection-object-seed42 完成 → random selection baseline 数据（plan_600）
- eval-obs-only-object-norm02-k5/k20-seed42 完成 → K sweep 数据（plan_601）

### 5. 🎯 战略上下文
- **投稿目标**: CoRL 2026，DDL ~Jun 2（剩 ~16 天）
- **核心方向 (D049)**: Narrative B+ — obs_only CRM 单步纠正 frozen VLA。三大贡献: (1) K=1 单采样实用性, (2) conditioning-magnitude interaction insight, (3) 跨 VLA 验证 (SmolVLA + OpenVLA)
- **K=10 已锁定**: obs_only 17.5% vs argmin 12.3%, Fisher p=0.0074（作 supplementary）
- **K=1 CRM 是关键缺口**: 目前 K=1 fallback（单阶段 960D）= VLA-only (10.0% vs 10.8%)，即 K=1 CRM 尚未超越 baseline。train-crm-k1-accg-object-seed42-v2 用多阶段特征尝试突破这个瓶颈
- **易错点**:
  - v2 实验的 conclusion 字段当前是 "failed"（历史误设），不要基于这个判断。等 Worker 分析真实结果后再更新
  - eval-k1-crm-accg-object-seed42/43/44 用的是 **fallback** checkpoint（不是 v2），不要混淆
  - D050 记录: K=1 ACCG fallback = VLA-only，说明单阶段方案已证实不够。v2 是多阶段改进尝试
  - 如果 v2 也 negative，需要按 on-experiment-done skill 产出 Framing 提案（从证伪推导下一步），不能默默开下一个实验


---
