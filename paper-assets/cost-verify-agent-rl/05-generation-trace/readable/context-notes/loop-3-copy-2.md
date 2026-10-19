# agent / loop_3.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`8445036815a49f307d81.json`](../../sessions/84/8445036815a49f307d81.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T09:01:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 bjb1-17606 的 cuda:0, cuda:1（project config 未列 gpu_ids 字段，但所有历史实验均用这两张卡，其他卡未被分配）
- 训练入口必须是 `python train.py --config-name=&lt;cfg>`，**禁用** `python -m ragen.llm_agent.agent_proxy` 启动训练（exp012 踩过，vLLM 参数不兼容）
- 启动命令必须带 `export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR`（exp007/exp010 两次 /tmp 满崩溃）
- ALFWorld score 是纯二值 0/1（PddlEnv 不支持 intermediate_reward），任何"进度奖励"方案的前提不成立
- 同一 checkpoint 目录不可被多个实验同时写入（exp009 教训）

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-17606，2× RTX PRO 6000 Blackwell 94GB，cgroup 内存限制 220GB
- **工作目录**: `/root/cost-verify-agent-rl/RAGEN/`
- **Python**: `/root/miniconda3/bin/python`，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型**: Qwen3-1.7B base → SFT checkpoint `/root/autodl-tmp/checkpoints/exp008_sft/final`（symlink `qwen3_sft_final`）
- **GRPO checkpoint**: `/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/`（exp013 系列的恢复起点）
- **数据**: ALFWorld `/root/autodl-tmp/alfworld/`（3553 train games），SFT 数据 `/root/autodl-tmp/sft_data/alfworld_sft_ragen.jsonl`（1200 条）
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **活跃进程**: 无。0 个 cron，0 个 RUNNING 实验，两张 GPU 空闲

### 3. 📊 当前状态
**刚做完**: exp013d 失败（Ray OOM）。这是 dense reward shaping 的第 3 次基础设施重试。

**问题链**: exp013b 验证了 dense reward shaping 算法有效（reward_std=1.608>0, pg_loss≠0），但 step 6 rollout 时 Ray Plasma mmap ENOMEM 崩溃。原因: cgroup 220GB 限制下，128 并发 ALFWorld 游戏（8 env_groups × 16 group_size）内存超限。exp013c 被预防性 kill。exp013d 将 env_groups 降到 4（64 并发）并设 `RAY_object_store_memory=30GB` 环境变量，但 **env var 未生效**——Ray 仍分配 70.36GB object store（默认值），Raylet 被 cgroup OOM killer SIGKILL。

**已诊断的修复方案**（exp013d notes 中记录）: 用 Hydra config override `ray_kwargs.ray_init.object_store_memory=32212254720` 显式传给 `ray.init()`，而非依赖环境变量。

**Registry**: 23 个实验，1 success (exp008_sft)，其余全 failed/killed/PREPARING。无 RUNNING。

**等待中**: 无 Worker 回调，无 Cron，无 Director 待决策。两张 GPU 空闲 = 失职状态。

### 4. 📋 待办（条件触发式）
- **立即（无条件）** → 提交 exp013e: 用 Hydra override 修复 Ray object_store_memory，其余配置同 exp013d（env_groups=4, valid_action_bonus=0.15, kl_loss_coef=0.01, 从 step 5 恢复）。需要 Director 审批或基于 D011 授权直接提交
- exp013e step 1-2 出结果 → 检查 reward_std>0 且 pg_loss≠0（kill/go 标准）
- exp013e step 10 success≥20% → Phase A PASS，启动 FSDP→HF 转换 + Phase B
- exp013e step 10 success=0 + valid 不涨 → Phase A 需要 pivot，向 Director 汇报备选方案（expert trajectory SFT 加强 warmup / 换更大模型 / 换环境）
- Phase A 出 checkpoint → 跑 FSDP→HF 转换脚本 → 更新 `_alfworld_phase_b.yaml` → 提交 Phase B (B-IAVR)
- **并行可做**: Phase B FSDP→HF 转换脚本可以提前写好（CPU 任务，不占 GPU）

### 5. 🎯 战略上下文
- **项目核心**: 训练 agent 学会"何时验证"（B-IAVR），但 Phase A（always-on self-guidance 基线）卡在 reward sparsity 冷启动问题
- **关键进展**: dense reward shaping（valid_action_bonus=0.15）已被 exp013b 验证有效（非零梯度 + 非零 reward_std），但连续 3 次因 Ray 内存管理崩溃未能跑完
- **决策链**: D006(SFT warmup) → D007/D008(reward shaping 问题确认) → D010/D011(dense reward shaping 方案, MVP 标准降至 20%)
- **易错点 1**: `RAY_object_store_memory` 环境变量对 RAGEN 的 Ray 初始化无效，必须通过 Hydra config override 传入 `ray.init()` 参数
- **易错点 2**: cgroup 内存限制是 220GB（不是物理内存），env_groups=4（64 并发）时峰值约 158GB 理论可行，但 Ray object_store 默认 70GB 仍会超限
- **易错点 3**: valid_action_bonus 从最初的 0.5 降到了 0.15（D011 决策），不要用旧值
- **Phase B 状态**: 代码就绪（68 tests pass），被 Phase A checkpoint 阻塞。一旦 Phase A 出 checkpoint，转换 + 启动可在 1h 内完成


---
