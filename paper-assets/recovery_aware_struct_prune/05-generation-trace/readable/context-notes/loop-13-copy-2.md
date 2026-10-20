# agent / loop_13.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`77995f1e1b57e8c0abdf.json`](../../sessions/77/77995f1e1b57e8c0abdf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-16T12:01:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westb-23072:cuda:0/1, westd-11672:cuda:0/1。其他 GPU 一律不能用
- westb 用 conda 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不存在 .venv
- GRPO v9 RASP 已确认 collapse（step 10 永久 collapse），不要再尝试 RASP GRPO 恢复
- 论文 narrative 已 pivot 到 "Pruning for Plasticity"（D037/D038/D044）——不再是 "RASP enables better RLVR recovery"
- eval 脚本在 `/root/recovery_aware_struct_prune/`，模型和 checkpoint 在 `/root/autodl-tmp/recovery_aware_struct_prune/`

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2×~98GB GPU | 工作目录 `/root/recovery_aware_struct_prune/` | 数据盘 `/root/autodl-tmp/`
  - Python: `/root/miniconda3/bin/python`
  - HF cache: `/root/autodl-tmp/.hf_cache`
  - GRPO v9 checkpoints: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-{10,15,20,25,30}`
  - Standard v8 checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50`
  - Unpruned GRPO checkpoints: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-{90,95,100}`
- **westd-11672**: 2×~95GB GPU | 同结构路径
  - SFT models: `sft_rasp_20_westd/`, `sft_standard_20_westd/`, `sft_rasp_25/`, `sft_standard_25/`
- W&B entity: `xiaoyucorynne-` / project: `recovery_aware_struct_prune`
- 活跃 Worker: `worker_analyze_eval_grpo_rasp_v9_step10_20260516T075918`（正在读取 eval 结果）

### 3. 📊 当前状态
**刚收到 cron 回调**: `eval_grpo_rasp_v9_step10` 进程正常退出，状态 ANALYZING。已派 Worker 去 westb-23072 读最终 accuracy。中间指标 acc_at_200=0.68。

**RUNNING 实验**:
- `eval_sft_standard_25` — westb, Standard 25% post-SFT GSM8K N=1319 eval
- `eval_sft_rasp_25` — westd, RASP 25% post-SFT GSM8K N=1319 eval

**PREPARING 实验（重要）**:
- `eval_postprune_25` — 25% post-prune accuracy (N=100)
- `eval_sft_standard_20_n1319` — Standard 20% full eval (替代之前 failed 的)
- `eval_sft_rasp_20_full` — RASP 20% full eval
- `grpo_standard_20_v8` / `grpo_rasp_20_v8` — 旧 placeholder，已被 v8 实际实验取代

**等待中**:
- Worker 回调：eval_grpo_rasp_v9_step10 结果读取
- eval_sft_standard_25 和 eval_sft_rasp_25 的 cron 完成回调

### 4. 📋 待办（条件触发式）
- Worker 回调带回 eval_grpo_rasp_v9_step10 最终 accuracy → update_registry(DONE) + 与 step-5 (60.65%) 和 Standard step-50 (58.91%) 对比 → 汇报 Director
- eval_sft_standard_25 cron 回调 → 读结果 + 与 eval_sft_rasp_25 配对分析 25% sparsity SFT recovery
- eval_sft_rasp_25 cron 回调 → 同上，两个都到了做 RASP vs Standard @25% 对比
- 两个 25% eval 都完成 → 汇总 20%+25% multi-sparsity 表格，汇报 Director
- GPU 空出来后 → 优先跑 eval_sft_standard_20_n1319 和 eval_sft_rasp_20_full（补 Table 1 的 tight CI）

### 5. 🎯 战略上下文
**核心发现（D044 narrative pivot）**:
- 三模型 GRPO collapse severity gradient: RASP step~10 (永久) > Standard step~60 (transient recovery) > Unpruned 无 collapse
- 原假设 "RASP enables better RLVR recovery" 已失败——RASP GRPO 反而最快 collapse
- 新 narrative: "Pruning for Plasticity" — pruning 创造 reward-accuracy decoupling 现象，CKA-guided pruning 影响 collapse dynamics
- **Unpruned GRPO v2 step-100 eval = 81.27%** 是关键对照（无 collapse + 高 accuracy）
- Standard GRPO step-50 eval = 58.91%（Δ=-0.38pp vs SFT，GRPO 未提升 accuracy）
- RASP step-5 eval = 60.65%（collapse 前仍保留 SFT 水平）

**易错点**:
- 不要把 westb 和 westd 的 SFT eval 直接合并——westd RASP=61.49% vs westb RASP≈57%，有 cross-server variance
- 论文 Table 1 用 N=1319 full eval 数据，N=100 只做 pilot
- DDL: EMNLP 2026 ARR May 25（距今 9 天），GRPO narrative pivot 后需要重新构建实验矩阵
- eval_grpo_rasp_v9_step10 的 acc_at_200=0.68 暗示最终可能在 ~65% 左右（比 step-5 的 60.65% 高），如果确认则 step-10 collapse onset 时 accuracy 仍在上升——这支持 "reward-accuracy decoupling" narrative


---
