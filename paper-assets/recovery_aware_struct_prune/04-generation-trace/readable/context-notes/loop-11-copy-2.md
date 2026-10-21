# agent / loop_11.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`e59f5487493105629068.json`](../../sessions/e5/e59f5487493105629068.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-16T01:43:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb cuda:0/1, westd cuda:0/1。**没有其他可用 GPU**
- westb 数据盘上次查 89% 满（29GB free），checkpoint save 可能失败——任何新实验前先 `df -h /root/autodl-tmp/`
- Standard GRPO v8 已确认 step 60 collapse，checkpoint-50 是唯一可用恢复点，**禁止删除** `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50`
- RASP GRPO v9 save_steps=5, save_total_limit=5——checkpoint 会自动轮转，peak checkpoint（可能是 step 5 或 10）可能被覆盖。**v9 完成后第一件事是确认哪些 checkpoint 还在**
- GRPO v8 配置导致所有模型最终 collapse（包括 unpruned），**不能声称 collapse 是 pruning 特有的**，只能说 pruning 加速了 collapse
- EMNLP ARR 截止 2026-05-25，距今 9 天

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× ~98GB GPU
  - 工作目录: `/root/recovery_aware_struct_prune`（代码）, `/root/autodl-tmp/recovery_aware_struct_prune/`（模型/数据/checkpoint）
  - Python: `/root/miniconda3/bin/python`（conda base，不是 venv）
  - cuda:0 → RASP GRPO v9 (PID 566666, tmux, wandb mrikafz3, max_steps=30)
  - cuda:1 → Standard GRPO v8 (PID 534667, tmux, wandb q34vz8j2, max_steps=100, 已 collapse step 60)
  - 关键模型路径: `sft_rasp_20`, `sft_standard_20`, `grpo_stage2_standard_20_v8/checkpoint-50` 均在 `/root/autodl-tmp/recovery_aware_struct_prune/`
- **westd-11672**: 2× ~95GB GPU
  - 同样 conda base，类似目录结构
  - cuda:0 → eval_sft_unpruned_full (PID 74129, N=1319 GSM8K eval)
  - cuda:1 → 空闲（α ablation sweep 已完成）
  - Unpruned SFT model: `/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline`
- **Cron 活跃**: grpo_stage2_standard_20_v8, grpo_stage2_rasp_20_v9（reconcile 确认双在跑）
- **W&B project**: recovery_aware_struct_prune

### 3. 📊 当前状态
**刚做完**: D044 major narrative pivot——从 "RASP enables better recovery" 转向 "GRPO fails on pruned models + Redundancy-Stability Tradeoff"。Standard GRPO step-50 full eval 已出：58.91%（vs SFT 59.29%，Δ=-0.38pp，零收益）。α ablation sweep (cal=512) 完成，确认 U-shape。paper_framing.md 已全面更新。

**正在跑的 3 个实验**:
| exp_id | 服务器 | GPU | 估计剩余 | 说明 |
|--------|--------|-----|---------|------|
| grpo_stage2_standard_20_v8 | westb | cuda:1 | 数小时 | 已 collapse step 60，跑到 100 步收集完整曲线 |
| grpo_stage2_rasp_20_v9 | westb | cuda:0 | 数小时 | max_steps=30, save_steps=5, 核心实验——捕获 collapse 前 peak |
| eval_sft_unpruned_full | westd | cuda:0 | 1-2小时 | N=1319 unpruned SFT baseline |

**等待中**:
- 2 个 cron 回调（上述 GRPO 完成时触发）
- eval_sft_unpruned_full 无 cron，需手动检查或 Worker 轮询
- Worker 池 = 0（全在等实验完成）

### 4. 📋 待办（条件触发式）
- **grpo_stage2_rasp_20_v9 cron 回调** → 立即 SSH 确认存活的 checkpoint 列表 → eval peak checkpoint（step 5 或 10，哪个 reward 最高）on GSM8K N=1319 → 对比 Standard step-50 的 58.91%
- **grpo_stage2_standard_20_v8 cron 回调** → 标记 DONE，记录完整 collapse 曲线（step 40 peak → step 60 collapse → step 100 终态）
- **eval_sft_unpruned_full 完成** → 记录 unpruned SFT baseline（预期 ~70-75%？）→ 更新三方对比表 → 准备 unpruned GRPO 实验（如果时间允许）
- **RASP v9 eval 出结果** → 判定：|RASP_peak - Standard_step50| 决定 paper story 强度。>15pp = 强 claim; 5-15pp = moderate; <5pp = 核心假设弱
- **westd cuda:1 空闲** → 可以立即用于 eval_sft_grasp_20_westd（GraSP full eval）或其他排队实验
- **所有 GRPO 完成** → 综合分析 → 大规模 paper writing push（9 天 DDL）

### 5. 🎯 战略上下文
**核心结论链**: Post-prune RASP vs Standard 差异不显著 (D027, 4pp p=0.54) → Post-SFT 也不显著 (D029, 2.2pp p=0.25) → Standard GRPO step-50 零收益 (D043, 58.91% ≈ SFT 59.29%) → Unpruned 也 collapse (D039) → **Narrative pivot to Redundancy-Stability Tradeoff (D044)**: 论文不是关于 RASP 更好，而是关于 GRPO 在 pruned model 上根本失败 + pruning 方法决定 collapse 速度。

**最容易判断错的事**:
1. **不要以为 unpruned collapse 削弱了论文**——恰恰相反，三者都 collapse 但速度不同（RASP step10 < Standard step60 < Unpruned step80）是 Redundancy-Stability Tradeoff 的核心证据
2. **RASP v9 可能也是零 accuracy gain**——如果 peak checkpoint eval ≈ SFT baseline，这其实**支持** Claim 1（GRPO 在 pruned model 上 reward hacking），不是坏消息
3. **不要开 unpruned GRPO 新实验除非 DDL 时间够**——已有 unpruned GRPO 数据（grpo_unpruned_baseline, step80 collapse），但该实验缺 SFT 步骤（D041 判定无效）。如果要做有效的 unpruned GRPO，需要先跑 unpruned SFT → GRPO，至少 2-3 天
4. **westb 磁盘紧张**——v9 的 5 个 checkpoint（每个 ~18GB）可能挤爆磁盘，save_total_limit=5 理论上会自动清理旧的，但要确认
5. **paper_framing.md 是最新 truth source**——所有 claim 和 evidence 都已在 D044 后更新，按它写论文


---
