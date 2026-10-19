# reviewer / loop_7.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`bb49cebd213bc3313f48.json`](../../sessions/bb/bb49cebd213bc3313f48.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T10:38:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（C001 约束，`execution.gpu_ids=[0,1]`）。发现进程跑在其他卡上立即 critical
- 验证集最少 16 episodes（C003），val env_groups=16, group_size=1
- 服务器 bjb1-17606 是 AutoDL 容器，cgroup pids.max=20,480——这是 verl-agent 失败的根因（D028），不要再尝试 verl-agent 方案
- Step-independent 模式下 batch 维度会从 episode-level（如32）扩展到 step-level（如1382），rollout_filter 等处理 batch 的代码必须兼容

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606(root)，2× RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/cost-verify-agent-rl`（RAGEN 框架在 `/root/cost-verify-agent-rl/RAGEN/`）
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型 checkpoint：`/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`（SFT 基线）
- 训练输出目录：`/root/autodl-tmp/checkpoints/exp026/`
- 训练日志：`/root/runs/cost-verify-agent-rl/exp026_step_independent_grpo.log`
- 配置文件：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp026_step_independent_grpo.yaml`
- 活跃进程：**无训练进程**。仅 `sleep 1800`（PID 774373, 18:28 启动）+ 系统服务
- W&B：项目名未确认（日志 0 字节未产出 wandb 初始化记录）

### 3. 📊 当前状态
**exp026_step_independent_grpo 启动失败。** Registry 状态仍为 ALLOCATED（10:28:31 UTC 提交），但：
- 日志文件 0 字节，脚本从未执行到
- GPU 0 处于异常状态（100% util, 0 MiB memory, 无进程）——可能是 `ray stop --force` 后挂起
- 已通过 `reviewer_post_to_director` 报告 CRITICAL，建议 Worker 检查 GPU 状态并重新提交

**已完成的审查（本轮 session 共 7 个 worker completion）：**
1. worker_code_cherry_pick_training_config — PASS（配置合规）
2. worker_code_cherry_pick_reward_advantage — WARNING（step_rewards.py 正确，但 core_algos 单 rollout 处理需关注）
3. worker_code_cherry_pick_ctx_manager — CRITICAL（non_tensor_batch 字段缺失，step-level advantage 永远走 fallback）
4. worker_code_cherry_pick_final_fixes_and_test — PASS（修复了 #3 的 critical + is_action_valid 路径 + config key）
5. worker_code_cherry_pick_critical_fix — INFO（已包含在 #4 中，无新问题）
6. worker_ops_exp026_fix_and_dryrun — WARNING（dry run step 0 成功验证 step-level advantage 生效，但 step 1 未完成、anchor_obs 日志 spam 未修）
7. worker_ops_exp026_verify_launch — CRITICAL（训练未启动，GPU 异常）

### 4. 📋 待办
- **exp026 重新提交成功 → 立即核验**：(1) GPU 进程在 cuda:0,1（C001）(2) W&B 连接 (3) 无 `[CRITICAL] step_independent` fallback 警告 (4) val_before_train 16 episodes 结果（C003）(5) 前 5 步 loss/advantage 趋势
- **GPU 0 持续异常 → 升级 critical**：如果 Worker 无法 reset GPU，需提醒 Director 这是 AutoDL 容器限制（可能无 nvidia-smi -r 权限），可能需要重启实例
- **exp026 跑到 step 5+ → 核查 success 指标定义**：dry run 中 val success 报告存在 episode-level（1/4=25%）vs step-level average（0.04）歧义，需统一
- **训练正常推进 → 周期性抽查**：每 ~25 步检查 loss 收敛、advantage 分布、GPU 利用率

### 5. 🎯 战略上下文
- **项目核心**：B-IAVR，训练交互式 agent 进行选择性自验证，用 action change 信号做 reward。Qwen3-1.7B + ALFWorld + GRPO。
- **决策链**：D028 放弃 verl-agent（cgroup pids.max 硬限制）→ Track B cherry-pick：把 step-independent rollout + GiGPO 从 verl-agent 移植回 RAGEN
- **最大风险**：exp026 是 Track B 首次完整训练。如果 step-level advantage 在长训练中不稳定（dry run 只跑了 1 步），整个 cherry-pick 方向可能需要回退
- **易错点 1**：is_action_valid 存在于 `turn['info']['action_is_valid']`（两层嵌套），不是 `turn['is_action_valid']`。之前的 bug 就是读错了路径导致无效动作惩罚失效
- **易错点 2**：step-independent 模式下 batch 从 32 episodes 展开为 ~1382 个 step-level samples，所有处理 batch 维度的代码（rollout_filter、reward_std 广播等）都需要兼容
- **易错点 3**：不要用"人类时间尺度"判断 deadline 风险——150 步 ×21min/步 ≈ 52h wall clock 是合理的，只看 GPU-hours 够不够


---
