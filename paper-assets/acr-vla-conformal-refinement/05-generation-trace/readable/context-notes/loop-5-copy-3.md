# reviewer / loop_5.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`394acd028ae63c536384.json`](../../sessions/39/394acd028ae63c536384.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T22:16:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb2-40593 上的 `/root/autodl-tmp/crm_cache/` 是 v4 cache（6D state，D016 修复前），**不可用于有效训练**。有效 cache 只有 bjb1-18228 上的 `/root/autodl-tmp/crm_cache_v5/`（8D state，post-D016）
- eval-acr-spatial-v4-obs-only 当前使用了**错误 checkpoint**（bjb2 invalidated `/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt`），正确的是 bjb1 `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`——已报 Director，等其决策是否 kill
- eval-acr-spatial-v4-default 已确认：v3-norm perdof + default max_correction_norm=1.42 仍然 0/5 失败。**default correction 在任何 checkpoint 下都有害**，eval 必须用 clipped norm（0.05-0.1）
- 无项目级 gpu_ids 约束（constraints.yaml 为空），但两服务器资源紧张，注意不要踩其他项目的卡

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 4×24GB GPU, conda base, `/root/acr-vla-conformal-refinement/`
  - 有效 checkpoints: `/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,obs_only,scalar_unc}/crm_best.pt`
  - 有效 cache: `/root/autodl-tmp/crm_cache_v5/spatial/`（12167 samples）
  - SmolVLA: `/root/autodl-tmp/models/smolvla_libero/`
  - LIBERO data: `/root/autodl-tmp/libero_data/`
  - 活跃进程: eval-acr-spatial-v4-small (cuda:3, PID 253085), eval-tiny-correction-spatial (cuda:2, PID 232815), eval-argmin-only-spatial (cuda:1, PID 231421)
- **bjb2-40593**: 1×24GB GPU, conda base, `/root/acr-vla-conformal-refinement/`
  - 活跃进程: eval-acr-spatial-v4-obs-only (cuda:0, PID 199257) — **用的是错误 checkpoint**
  - eval-vla-mean-spatial 已完成（DONE, 31% estimated）
- 无 W&B 配置

### 3. 📊 当前状态
刚完成：v3-norm 全系列训练 ablation 审查。核心发现：obs_only val_loss=0.0165 远优于 perdof=0.0358（54% better）——已报 Director CRITICAL。Director 提出反驳逻辑（distribution shift 下 conformal 更有价值），我给出了评估。

RUNNING 实验（4个）:
- `eval-acr-spatial-v4-small`（v3-norm perdof, norm=0.1）: 1/10 tasks, T1=60%, eta ~8h
- `eval-tiny-correction-spatial`（v2 perdof, norm=0.05）: 3/10 tasks, avg 53.3%, eta ~8h  
- `eval-argmin-only-spatial`（K=10 argmin, no CRM）: 3/10 tasks, avg 53.3%, eta ~8h
- `eval-acr-spatial-v4-obs-only`（**错误 checkpoint**, bjb2）: 刚启动

等待：Director 对 obs_only checkpoint 错误的处理决策；三个诊断 eval 的完整结果

### 4. 📋 待办（条件触发式）
- eval-acr-spatial-v4-small 完成 → 核心判断：v3-norm perdof + 0.1 correction 是否 > baseline 34%。如果 < 34% → CRM correction 机制根本无效，需要 Gated CRM 或放弃 CRM
- eval-tiny-correction-spatial 完成 → 对比 argmin-only；如果 tiny-correction ≈ argmin-only → CRM correction 在 0.05 norm 下等效于 passthrough，价值为零
- eval-argmin-only-spatial 完成 → 对比 VLA mean (31%)；如果 argmin >> mean → 样本选择本身有价值，paper framing 可转向 "sample selection + gated correction"
- Director 决定 obs_only eval 重启 → 核实用正确 checkpoint (`crm_v3_norm/obs_only`) + max_norm=0.1
- obs_only eval 完成（正确版本） → 与 v4-small (perdof) 对比：obs_only ≥ perdof → 核心 claim 需根本重构

### 5. 🎯 战略上下文
**决策链**: D016(state bug fix) → D017(CRM correction 全面拖累) → D018(归一化修复) → D019(归一化不够, 需 clip) → 当前等 v4-small 结果

**核心悬念**: CRM correction 到底能不能超过 baseline？目前所有证据（v2 full=2.5%, v3-norm default=0%, tiny-correction 53% ≈ argmin-only 53%）都指向 CRM correction 的边际贡献接近零或为负。唯一希望是 v4-small (norm=0.1) 的完整 10-task 结果。

**最容易判错的事**:
1. 不要把 bjb2 `/crm_v3/` 和 bjb1 `/crm_v3_norm/` 混淆——前者全部 invalidated
2. 不要把 "training loss 好" 等同于 "eval 会好"——obs_only training loss 最低但 closed-loop 可能不行
3. VLA K=10 mean = 31%，SampleConsensus = 34%，VLA K=1 = 30%——多采样 mean 几乎没提升，argmin selection (53% at 3 tasks) 目前看起来比任何 CRM correction 都强
4. eval-vla-mean-spatial 的 per-task 分布是双峰的：next_to 类 80-100%，精确空间类 0%。评审时注意 "overall rate" 可能被几个容易 task 拉高


---
