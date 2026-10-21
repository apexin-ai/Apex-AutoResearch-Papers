# reviewer / loop_16.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`cf20b66433cafeb7f7d3.json`](../../sessions/cf/cf20b66433cafeb7f7d3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-17T18:17:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- `/root/autodl-tmp/checkpoints/crm_k1/` 是**共享存储**（多台服务器可见），`crm_k1_best.pt` 会被不同训练覆盖。eval 前必须确认 checkpoint 来源（fallback vs multi-scale）
- OpenVLA eval-openvla-object-vla-only-seed42 的 registry `conclusion: success` 是**错误标记**（实际 0/100 = 0%），不要信这个 conclusion，只看 metrics
- bjb2-28827 上 tmux session `train-crm-k1-v2` 的训练命令**没有 exit trap**，cron 无法检测完成。exit file `/tmp/agent-ml-exit/train-crm-k1-accg-object-seed42-v2.exit` 仍为旧值 `0|2026-05-17T17:15:46Z`
- 所有服务器时区 UTC+8，registry 时间 UTC。换算：local = UTC + 8h

### 2. 🖥️ 基础设施快照
- **bjb2-28827** (root): 训练服务器，6×24GB GPU。`/root/acr-vla-conformal-refinement/src/`。Python: `/root/miniconda3/bin/python`。conda env: base。
  - 活跃 eval: perdof norm02 seed46 (PID 389051, cuda:4), perdof norm02 seed47 (PID 404983, cuda:2), obs_only norm01 seed46 (PID 449068, cuda:3), perdof norm02 seed43 r3 (PID 449339, cuda:5)
  - 训练已完成: train-crm-k1-v2 tmux session (PID 453395, cuda:0) — 已跑完 50 epoch
- **bjb1-18228** (root): 4×24GB GPU。eval 运行中: obs_only norm005 seed43 r3 (cuda:1), perdof norm02 seed45 r2 (cuda:0), K=20 seed42 (cuda:3), K=5 seed42 (cuda:2)
- **bjb1-32546** (root): 6×24GB GPU。eval 运行中: obs_only norm005 seed43 (cuda:0), perdof norm01 seed47 (cuda:1), obs_only norm03 seed46 (cuda:2), obs_only default seed46 (cuda:3), perdof norm01 seed46 r2 (cuda:4), perdof default seed46 (cuda:5)
- **bjb2-40593** (root): 1×24GB GPU。random selection baseline seed42 (cuda:0)
- 模型路径: SmolVLA `/root/autodl-tmp/models/smolvla_libero/`, OpenVLA `/root/autodl-tmp/models/openvla-libero-object/`
- Checkpoint: fallback best `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` (val_loss=0.006505), multi-scale best `/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt` (val_loss=0.007199)
- HF cache: `/root/autodl-tmp/.hf_cache`，offline mode (`HF_HUB_OFFLINE=1`)

### 3. 📊 当前状态
**刚完成**: multi-scale K=1 CRM 训练 (train-crm-k1-accg-object-seed42-v2)，50 epoch，best val_loss=**0.007199**。已向 Director 报告 Scenario B 早期信号（multi-scale val_loss 比 fallback 0.006505 差 10.7%）。

**等待中**:
- Agent 检测训练完成 → 部署 multi-scale K=1 3-seed eval（**这是 Director 明确要求监控的核心数据点**）
- 14 个 RUNNING eval（magnitude sweep 补数据）陆续完成
- OpenVLA 0% 根因分析（Claim 3 阻塞）

**已确认的 K=1 fallback 结果**: seed42=11%, seed43=12%, seed44=7%, mean=**10.0%** ≈ VLA-only 10.8%。已定性为 Scenario B。

### 4. 📋 待办（条件触发式）
- Agent 部署 multi-scale K=1 eval → 监控 3-seed 结果。**阈值: >13% = Scenario A, ≤11% = Scenario B**（Director 指定）
- multi-scale eval 3-seed mean 出来 → 立即 reviewer_post_to_director 附 Scenario 判定 + per-task breakdown + 与 fallback/VLA-only 对比
- OpenVLA 根因修复 → 重新 eval → 如果仍 0% 则 Claim 3 需要降级或放弃
- 14 个 RUNNING magnitude sweep eval 完成 → 核查 registry metrics 是否与日志一致，更新 Figure 2 数据点覆盖度
- 如果 Agent 长时间未检测到训练完成（因 cron 缺口）→ 提醒 Director 手动触发

### 5. 🎯 战略上下文
- **核心判断**: K=1 correction 能否超越 VLA-only baseline（10.8%）是整篇论文 Claim 1 的生死线
- **Scenario B 信号已经很强**: fallback eval=10.0%，multi-scale val_loss 更差。但 val_loss ≠ task success，eval 是最终判据
- **最容易判断错的事**: 不要因为 val_loss 差就直接宣布 Scenario B——必须等 eval 数据。也不要因为 registry 里 conclusion="success" 就信 OpenVLA 结果（0% 被误标）
- **论文时间线**: CoRL 2026 Abstract DDL ~May 26（距今 9 天）。4 个 Claims 中，Claim 1（K=1）和 Claim 3（cross-VLA）都处于危险状态
- **决策链**: D049 narrative B+ 是当前 framing。如果 Scenario B 确认，Director 需要 pivot 论文叙事（可能降级 Claim 1 为 negative result，强化 Claim 2 conditioning-magnitude interaction 作为主贡献）


---
