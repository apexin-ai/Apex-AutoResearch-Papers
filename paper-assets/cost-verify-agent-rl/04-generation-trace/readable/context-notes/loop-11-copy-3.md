# reviewer / loop_11.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`0467f5c864f21a074eb1.json`](../../sessions/04/0467f5c864f21a074eb1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-16T12:22:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（仅 2 张卡，bjb1-17606 只有这两张 RTX PRO 6000 Blackwell 98GB）
- 训练进程必须用 CUDA_VISIBLE_DEVICES=0,1，越界即 critical
- alfworld_memory.py 有格式冲突（format_prompt 用 `&lt;answer>` tags vs AlfworldSG env_instruction 无 `&lt;answer>` tags）——D051 P1 项，exp029 启动前必须确认解析器兼容性
- W&B entity/project 未配置在项目 config 中，fetch_wandb_metrics 会失败——跳过 W&B 交叉验证

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606(root)，工作目录 /root/cost-verify-agent-rl
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4（SFT checkpoint，Qwen3-1.7B）
- 数据：ALFWORLD_DATA=/root/autodl-tmp/alfworld
- Checkpoints：/root/autodl-tmp/checkpoints/exp028c/（global_step_5, global_step_10）
- 训练日志：~/runs/cost-verify-agent-rl/
- 活跃进程：**无**（exp028c 已终止，GPU 空闲）
- exp029 配置就绪：RAGEN/config/_alfworld_exp029_episode_level.yaml + scripts/run_exp029_episode_level.sh

### 3. 📊 当前状态
刚审完 worker_fix_exp029_config_and_dryrun。关键修正：gpu_memory_utilization 0.92→0.5，max_model_len 16384→20480。**Dryrun 未执行**（日志文件不存在）。

Registry:
- exp029_episode_level: **PENDING**（配置就绪，未启动）
- exp028c_selfguide_recipe: DONE/failed（灾难性崩溃，step_10_val=0%）
- 其余 54 个实验均 DONE

等待中：Director 决策是否启动 exp029（我已 post 了 3 个 warning：gpu_mem 已修、registry notes 描述过时说 0.92、格式冲突未修）。

### 4. 📋 待办
- exp029 启动通知到来 → 立即 ssh_read_only 确认 PID 在 cuda:0/1、日志开始写入、初始 val 是否正常（期望 val success ≈ 6.25% = baseline）
- step_5_val 出来 → 这是第一个决策点。若 ≥10% 说明 episode-level 有效；若仍 6.25% 则可能有代码路径问题（full 模式可能未真正生效——检查日志中 batch_size 是否 =128 而非 ~3200）
- 若 OOM 出现 → 检查是 rollout 阶段还是 training 阶段，建议调 gpu_memory_utilization 或 ppo_max_token_len_per_gpu
- 格式冲突问题若未修 → 观察 step_0_val action_is_valid 是否骤降（若从 74.5% 暴跌说明格式 mismatch 导致 reward parsing 失败）

### 5. 🎯 战略上下文
- 决策链：D037(MVP≥20%) → D044(SFT有用) → D045(exp027 failed) → D050(recipe gap) → D051(exp028c 非有效 Self-Guide 复现) → D052(终止 exp028c, 灾难性崩溃)
- exp029 是 **唯一活跃的 MVP 路径**。若 episode-level 也失败，项目可能需要更根本的方向调整（D051 还有 P1: self-guidance reward 缺失）
- 核心判断标准：full 模式下 batch_size 应 = 128（episode 数），不是 ~3200（step 数）。如果日志显示 batch_size >> 128，说明代码仍走了 step_independent 路径
- exp028c 的教训：train success 振荡不代表学习，val 才是真信号。best@k 改善但 pass@1 停滞 = 高方差无策略
- 易错点：registry notes 说 gpu_memory_utilization=0.92 但实际 config 已改为 0.5——不要被 notes 误导


---
