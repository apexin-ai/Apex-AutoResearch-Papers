# director / loop_10.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`94aa0d64d5ab37b21073.json`](../../sessions/94/94aa0d64d5ab37b21073.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-17T18:03:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- K=1 和 K=10 结果**禁止交叉比较**。K=10 数据仅作 supplementary evidence。用户硬要求 (D049)
- CRM 设计禁止直接照搬已有论文的命名模块（如 FiLM）。标准方法（attention/MLP/L2 loss）可用，但组合和动机必须原创
- LIBERO 并发上限：每台服务器最多 4 个 LIBERO 评估进程，否则渲染资源耗尽导致 hang (M005)
- 4 台服务器均为本项目分配：bjb2-40593, bjb1-18228, bjb1-32546, bjb2-28827。GPU 全归本项目
- CoRL 2026 为唯一投稿目标（abstract DDL ~May 26, full paper DDL ~Jun 2），禁止 fallback 到低级会议

### 2. 🖥️ 基础设施快照
- **bjb2-28827** (connect.bjb2.seetacloud.com): 6×4090, 工作目录 /root/acr-vla-conformal-refinement/src/。K=1 multi-stage 训练主机。SmolVLA 模型 + LIBERO HDF5 数据 + K=1 multi-scale precompute cache (65,223 samples) 均在此
- **bjb1-32546** (connect.bjb1.seetacloud.com): 6×4090, K=1 ACCG eval 主机（fallback eval 已完成）。SmolVLA + ACCG fallback checkpoint 在此
- **bjb1-18228** (connect.bjb1.seetacloud.com): 4×4090, OpenVLA eval 主机。OpenVLA-7B-LIBERO-Object (LoRA r=32) 已下载 + 4 个 compatibility patches 已打
- **bjb2-40593** (connect.bjb2.seetacloud.com): 6×4090, 辅助 eval 主机
- Python: 各服务器 /root/miniconda3/bin/python 或系统 Python
- W&B: bjb2-28827 未配置 wandb login，训练必须用 --no_wandb
- ACCG 架构: MultiScaleCRM, 327,522 params, 4-layer hooks text_model [3,7,11,15], action-conditioned sigmoid gating

### 3. 📊 当前状态
**刚完成**：
- K=1 ACCG fallback eval 3 seeds 结果收集：seed42=11%, seed43=12%, seed44=7%, mean=10.0%。与 VLA-only 10.8% 无显著差异 → **Scenario B 确认** (D050)
- 发现 train-crm-k1-accg-object-seed42-v2（multi-stage 训练）因 W&B key 崩溃 (M010)，precompute 75min 已完成，已派 urgent 指令加 --no_wandb 重启

**RUNNING**：
- `train-crm-k1-accg-object-seed42-v2`: multi-stage 训练重启中（bjb2-28827 cuda:0），训练 ~20min
- `eval-openvla-object-vla-only-seed42`: OpenVLA K=1 baseline（bjb1-18228），进度未知
- `eval-k1-crm-accg-object-seed44`: 可能已完成，需确认

**Agent 队列**：2 条消息（urgent W&B 修复 + 全面状态摸底+GPU填满指令），Agent 刚重置

**严重问题**：report 显示 bjb1-32546 和 bjb2-28827 共 12 张 GPU 全部空闲。已在摸底指令中要求 Agent 立即填满。

### 4. 📋 待办（条件触发式）
- Multi-stage training 完成 → 立即部署 3-seed eval（bjb1-32546 或 bjb2-28827 空闲卡）→ 这是 Claim 1 最后 rescue
- Multi-scale eval 3-seed mean > 13% → Scenario A 成立，Claim 1 = "K=1 with rich multi-scale features improves frozen VLA"
- Multi-scale eval 3-seed mean ≤ 11% → Scenario B 确认，Claim 1 改写为 mechanism insight（"K=1 redistributes task success; K=10 selection necessary for net gains"），立即更新 paper_framing.md
- OpenVLA baseline 完成 → 收集 success_rate，作为 plan_802 (OpenVLA+CRM) 的 baseline
- Agent 摸底结果返回 → 确认所有空闲 GPU 已部署实验（plan_600 random selection, plan_601 K sweep, plan_602 latency, 低 norm 补 seed 等）
- 所有关键数据到齐 → 激活 Paper Agent 启动写作流程

### 5. 🎯 战略上下文
- **核心决策链**：D049（K=1+OpenVLA方向）→ D050（K=1 fallback=VLA-only，Scenario B）
- **Narrative B+ (D049)**：mechanism insight (conditioning-magnitude interaction) + K=1 practicality + cross-VLA validation。目前 K=1 practicality 这条腿站不住（fallback 数据），multi-scale 是 rescue
- **已锁定硬证据**：K=10 obs_only 6v6 Fisher p=0.0074 (17.5% vs 12.3%)；magnitude sweep obs_only stable 15-17.5%，perdof collapse 14→0%
- **Per-task redistribution 发现**：K=1 correction 在 VLA-only 弱的任务上提升、强任务上降低，净效果为零。无论 multi-scale 结果如何，这个 pattern 本身有论文价值
- **易错点**：(1) 不要混淆 fallback model（单层 obs_feat）和 multi-scale model（4层融合）的结果；(2) 旧 direct_correction seed42=14% 看似更好但是 single seed，不能直接与 3-seed mean 比；(3) OpenVLA K=10 inference ~50s/step，这是 K=1 motivation 的重要论据
- **DDL 紧迫性**：CoRL abstract DDL May 26 = 9 天，full paper Jun 2 = 16 天。multi-scale 结果 ~3h 后决定 framing，之后必须立即启动 Paper Agent


---
