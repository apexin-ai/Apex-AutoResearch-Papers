# agent / loop_12.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`4959e1499b1ae3bc118f.json`](../../sessions/49/4959e1499b1ae3bc118f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-15T23:27:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 bjb1-17606 的 cuda:0 和 cuda:1（2× RTX PRO 6000 Blackwell 98GB），Director 指令也不能越过此限制
- exp028c_selfguide_recipe 正在跑（PID 824675），**不要 kill 它**——这是 D050 决策后的全面 Self-Guide recipe 对齐实验，是当前唯一活跃实验
- 禁止 WANDB_MODE=disabled（D033 教训：cron 无法监控导致误标 DONE(failed)）
- submit_training_job 必须自带环境激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不要假设 .venv 存在
- B-IAVR 代码已实现但 Phase B 前必须解决两个前置（D031）：&lt;VERIFY> special token 注册 + a_pre 推理开销量化

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606（root@），工作目录 `/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`，conda base 环境（不是 venv）
- SFT checkpoint：`/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/`（exp021，RAGEN 格式 SFT，success=6.25%）
- 数据：`/root/autodl-tmp/alfworld/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：exp028c_selfguide_recipe PID=824675，W&B run=4yu6qz1m
- Cron：1 个活跃（exp028c），间隔 ~300s 监控 PID 存活

### 3. 📊 当前状态
exp028c_selfguide_recipe 正在训练（RUNNING）。这是 D050 后的全面 Self-Guide recipe 对齐实验，9 项参数变更 vs exp027：ppo_mini_batch_size 128、total_steps 100、LR 1e-6、KL 0.01、env_groups 16、group_size 8、entropy 0.001、history_length 2、loss_agg token-mean。从 exp021 SFT checkpoint 出发。

**没有活跃 Worker（0/0）。** 没有等待中的 Worker 回调或 Director 决策。

Registry 摘要：35 个实验，3 success / 5 negative / 18 failed / 1 RUNNING / 多个 PREPARING（绝大部分已废弃或 killed）。

### 4. 📋 待办（条件触发式）
- exp028c cron 回调到达 → spawn worker 读 W&B/日志分析训练曲线（success trend、KL、entropy、pass@16），按三层阈值判定（D037/D040）
- exp028c val success ≥ 20% → MVP 通过，`complete_mvp()`，向 Director 汇报，启动 Phase B（B-IAVR selective verification）
- exp028c val success < 20% 但 train 有上升趋势 → 评估是否继续到 100 步或调参
- exp028c fail/collapse → 汇报 Director，recipe gap 仍未解决，需决策：(1) 向 Director 申请更多 GPU 跑 verl-agent 原版，或 (2) 重评项目
- 空闲时（exp028c 等待期）→ 可并行做：文献更新 literature_map.yaml、引用审计修复（AgentPRM/Huang2024/DAPO/CFGM 有错）、B-IAVR Phase B 代码准备

### 5. 🎯 战略上下文
**核心问题**：52 个实验只解决了"能跑起来"的工程问题，核心 B-IAVR 选择性验证机制零实验。62pp baseline gap（Self-Guide 72.7% vs 我们最好 ~13% train / 6.25% val）是最大瓶颈。

**决策链关键节点**：
- D039: cost-efficiency framing 锁定，baseline 必须 ≥50% 才有论文意义
- D044: Recipe gap 三大根因——SFT毒药(❌D047否定) + 零梯度(❌D050否定，penalty已在exp027生效) + mini-batch过小(✅唯一未验证)
- D050: 单变量策略连续失败，转为全面对齐 Self-Guide recipe → 即 exp028c

**易判断错的事**：
- 不要把 eval_sft_fast 的指标（exp019b 20%）和 RAGEN val 的指标（exp021 6.25%）混淆——两个评估框架结果完全不同，RAGEN val 是 truth
- RAGEN 框架内 SFT baseline 是 6.25%（不是 20%），GRPO 从未在 val 上超过 SFT baseline
- exp027 的 invalid_action_penalty=0.1 已经默认生效了（step_rewards.py），不要重复添加
- Qwen3-1.7B 本身就是 instruct 模型（无独立 -Instruct 变体），零样本 0% success
- B-IAVR 代码已实现（52 tests pass），但 &lt;VERIFY> token 和 a_pre 开销两个前置还没做（D031）


---
