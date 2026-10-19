# agent / loop_17.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`9a2d6c5a5f0d45e1807d.json`](../../sessions/9a/9a2d6c5a5f0d45e1807d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-18T00:09:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-47453 GPU 白名单：cuda:0,1,2,3（4× RTX PRO 6000）；bjb1-17606：cuda:0,1（2× A6000）
- factorial_h2_episodeadv_seed1 用的是 westd-47453 cuda:0,1——这两张卡现在空闲，诊断完必须立即重跑或安排其他实验
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不能假设 .venv
- GPU 编号脚本内始终从 0 开始（CUDA_VISIBLE_DEVICES 由框架注入）
- 配置文件名：`_alfworld_factorial_h2_episode_adv`（注意下划线拼写），在 `/root/cost-verify-agent-rl/RAGEN/configs/` 下

### 2. 🖥️ 基础设施快照
- **westd-47453**: 工作目录 `/root/cost-verify-agent-rl/RAGEN`，Python `/root/miniconda3/bin/python`，conda env `base`，ALFWORLD_DATA=`/root/autodl-tmp/alfworld`，磁盘 813G/879G 可用
- **bjb1-17606**: 同结构，磁盘 817G/879G 可用
- **活跃进程**:
  - gsweep_g050_h5_seed1: westd-47453 PID 85798, cuda:2,3, cron 监控中
  - hsweep_h2_seed2: bjb1-17606 PID 945877, cuda:0,1, cron 监控中（含 LOG_PER_SAMPLE_ADV=1 收集 per-window advantage 数据）
- **W&B**: 失败实验 wandb_run_id=jsrvwcfd（factorial_h2_episodeadv_seed1）

### 3. 📊 当前状态
**刚做完**: 收到 factorial_h2_episodeadv_seed1 失败 CRON 回调（EXIT_CODE=1，仅跑 143 秒），已 spawn 诊断 Worker `worker_diagnose_factorial_h2_episodeadv_seed1_20260517T192458`。

**等待中**:
- 诊断 Worker 回调 → 根据根因决定修复+重跑
- gsweep_g050_h5_seed1 完成回调 → 分析 γ=0.5 collapse 速度，链式启动 g080/g095/g100
- hsweep_h2_seed2 完成回调 → 分析 per-window advantage 数据验证 sign misattribution，启动 h=10

**Registry**: RUNNING 2 (gsweep_g050_h5_seed1, hsweep_h2_seed2)，PREPARING 21，DONE 40（success 5, negative 5, failed 19, killed 11）

**尚未向 Director 汇报此次失败**——等诊断结果出来一并汇报（含修复方案 + 资源行）。

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调 → 读诊断报告 → 修复代码/配置 → 在 westd-47453 cuda:0,1 重跑 factorial_h2_episodeadv_seed1 → 汇报 Director
- gsweep_g050_h5_seed1 完成 → 分析 γ=0.5 vs baseline → 链式提交 gsweep_g080_h5_seed1（westd-47453 cuda:2,3）
- hsweep_h2_seed2 完成 → 提取 per-sample advantage 数据 → 验证 sign misattribution 机制 → 释放 bjb1 cuda:0,1 启动 hsweep_h10_seed1
- westd-47453 cuda:0,1 空闲且无 factorial 重跑需求 → 安排 PREPARING 队列中其他实验（如 exp028_prereq_zeroshot_instruct）
- Director 回复 r=0.640 诊断 Q1-Q4 → 据此调整 sign misattribution claim 精度

### 5. 🎯 战略上下文
- **核心方向**: 诊断 step-independent RL 的灾难性崩溃机制，通过 factorial experiment 分离 information loss vs sign misattribution 的贡献
- **Framing (D062)**: 已从 "contrarian/coarser is better" 转为 "mechanistic diagnosis + factorial causal attribution"。GAGPO 93.5% 证明正确的 finer credit IS better，我们的 claim 是诊断 WHY broken step-independent fails
- **factorial_h2_episodeadv_seed1 是最关键的实验**: 它是 2×2 factorial 的关键格子——h=2 truncated context + episode-level advantage。如果 success >> 0%（h=2 step-level），证明 sign misattribution 是主因；如果 ≈ 0%，证明 information loss 足以致崩溃。必须尽快修复重跑
- **易踩的坑**: (1) 这个实验的配置可能需要新建或修改 RAGEN 配置文件以支持 episode-level advantage + step-independent generation 的组合，不是简单改超参 (2) D063 发现 sign misattribution 机制比 binary 假设更复杂（r=0.640），factorial 结果需要结合这个发现解读 (3) 不要把 γ-sweep 和 h-sweep 的结果混为一谈——前者测 discount 影响，后者测 context window 影响


---
