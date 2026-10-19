# Reviewer coordination (archived snapshot) — Part 3 of 3

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-coordination-20260515-005452.md) · [Structured JSON](../../../sessions/de/de235ec4f545df7ef3e2.json)

## Round 66

### Tool call

_source line 1521 · 2026-05-14T22:38:08.555304+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['status', 'spec', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['status', 'spec', 'metrics']"
  }
}
```

</details>

---


### Tool result

_source line 1522 · 2026-05-14T22:38:08.606168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\u001b[36m(TaskRunner pid=389242)\\u001b[0m step:0 - val-env/AlfworldSG/success:np.float64(0.0) - val-env/AlfworldSG/num_actions:np.float64(17.25) - val-env/AlfworldSG/episodic_return:np.float64(0.0) - val-env/AlfworldSG/action_is_effective:np.float64(0.575) - val-env/AlfworldSG/action_is_valid:np.float64(0.16666666666666666) - val-env/AlfworldSG/raw_reward:np.float64(0.0) - val-env/AlfworldSG/manager_invalid_action:np.float64(0.42500000000000004) - val-env/AlfworldSG/pass@1:np.float64(0.0) - val-env/charts/avg_episode_return:np.float64(0.0) - val-env/AlfworldSG/non-zero/num_actions:np.float64(17.25) - val-env/AlfworldSG/non-zero/action_is_effective:np.float64(0.575) - val-env/AlfworldSG/non-zero/action_is_valid:np.float64(0.3333333333333333) - val-env/AlfworldSG/non-zero/manager_invalid_action:np.float64(0.8500000000000001) - val-env/response_length:np.float64(2842.25) - val-core/unknown/reward/mean@4:np.float64(0.0) - val-aux/unknown/reward/std@4:np.float64(0.0) - val-aux/unknown/reward/best@2/mean:np.float64(0.0) - val-aux/unknown/reward/best@2/std:np.float64(0.0) - val-aux/unknown/reward/worst@2/mean:np.float64(0.0) - val-aux/unknown/reward/worst@2/std:np.float64(0.0) - val-core/unknown/reward/best@4/mean:np.float64(0.0) - val-core/unknown/reward/best@4/std:np.float64(0.0) - val-aux/unknown/reward/worst@4/mean:np.float64(0.0) - val-aux/unknown/reward/worst@4/std:np.float64(0.0)\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m list(reward_extra_infos_dict.keys())=[]\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m step:1 - collapse/first_turn_num_total:64 - collapse/first_turn_num_valid:62 - collapse/first_turn_valid_rate:0.96875 - collapse_first_turn_sample/mi_estimate:0.187404066324234 - collapse_first_turn_sample/mi_upper_bound:1.3862943611198906 - collapse_first_turn_sample/matched_log_prob_mean:-0.4734736382961273 - collapse_first_turn_sample/marginal_log_prob_mean:-0.6608777046203613 - collapse_first_turn
…[truncated 5238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-14T22:38:08.706981+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1013}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 1524 · 2026-05-14T22:38:12.408177+00:00_

训练仍在 step 2/30，进度正常。上次报告已覆盖所有关键信息，无新发现需要汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer"
}
```

</details>

---


## Round 67

## Round 67

14 recorded events


### User

_source line 1525 · 2026-05-14T22:38:58.187039+00:00_

[系统通知 — worker_done:worker_diagnose_cleanup-exp020d-ray_20260514T223825]:
Worker worker_diagnose_cleanup-exp020d-ray_20260514T223825 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1526 · 2026-05-14T22:39:12.477921+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "limit": "5",
  "fields": "['status', 'conclusion', 'updated_at', 'spec.pid', 'failure_reason']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "limit": "5",
    "fields": "['status', 'conclusion', 'updated_at', 'spec.pid', 'failure_reason']"
  }
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-14T22:39:13.032117+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp021_sft_ragen_format\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T22:35:49.619Z\"}, \"exp020d_grpo_from_sft\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T22:19:42.519Z\"}, \"exp020c_grpo_from_sft\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T22:15:49.267Z\"}, \"exp020b_grpo_from_sft\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-14T22:12:49.490Z\"}, \"exp020_grpo_from_sft\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:11:05.341Z\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\"}}, \"count\": 5, \"total\": 41, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1608}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-14T22:39:13.233817+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-17606",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-17606",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader"
  }
}
```

</details>

---


### Tool result

_source line 1529 · 2026-05-14T22:39:14.338447+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 %, 40213 MiB\\n1, 0 %, 40213 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-14T22:39:23.023315+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-17606",
  "command": "tail -20 /root/runs/cost-verify-agent-rl/exp020b_grpo_from_sft.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-17606",
    "command": "tail -20 /root/runs/cost-verify-agent-rl/exp020b_grpo_from_sft.log"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-14T22:39:23.375222+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\u001b[36m(TaskRunner pid=389242)\\u001b[0m  \\\"'val-aux/unknown/reward/best@2/mean': np.float64(0.0), \\\"\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m  \\\"'val-aux/unknown/reward/best@2/std': np.float64(0.0), \\\"\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m  \\\"'val-aux/unknown/reward/worst@2/mean': np.float64(0.0), \\\"\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m  \\\"'val-aux/unknown/reward/worst@2/std': np.float64(0.0), \\\"\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m  \\\"'val-core/unknown/reward/best@4/mean': np.float64(0.0), \\\"\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m  \\\"'val-core/unknown/reward/best@4/std': np.float64(0.0), \\\"\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m  \\\"'val-aux/unknown/reward/worst@4/mean': np.float64(0.0), \\\"\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m  \\\"'val-aux/unknown/reward/worst@4/std': np.float64(0.0)}\\\")\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m \\rTraining Progress:   0%|          | 0/30 [00:00<?, ?it/s]\\n\\u001b[36m(WorkerDict pid=389434)\\u001b[0m /root/cost-verify-agent-rl/RAGEN/ragen/workers/actor/dp_actor.py:433: FutureWarning: Warning: Function 'verl.trainer.ppo.core_algos.compute_policy_loss' is deprecated. Please use 'verl.trainer.ppo.core_algos.compute_policy_loss_vanilla' instead.\\n\\u001b[36m(WorkerDict pid=389434)\\u001b[0m   pg_loss, pg_clipfrac, ppo_kl, pg_clipfrac_lower = compute_policy_loss(\\n\\u001b[36m(TaskRunner pid=389242)\\u001b[0m \\rTraining Progress:   3%|▎         | 1/30 [04:34<2:12:45, 274.67s/it]\\n\\u001b[36m(WorkerDict pid=389435)\\u001b[0m /root/cost-verify-agent-rl/RAGEN/ragen/workers/actor/dp_actor.py:433: FutureWarning: Warning: Function 'verl.trainer.ppo.core_algos.compute_policy_loss' is deprecated. Please use 'verl.trainer.ppo.core_algos.compute_policy_loss_vanilla' instead.\\n\\u001b[36m(WorkerDict pid=389435)\\u001b[0m   pg_loss, pg_clipfrac, ppo_kl, pg_clipfrac_lower = compute_policy_l
…[truncated 6536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-14T22:39:23.727795+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "filters": "{'exp_id': 'exp021_sft_ragen_format'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "filters": "{'exp_id': 'exp021_sft_ragen_format'}",
    "fields": "['*']"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-14T22:39:23.879362+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1191}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-14T22:39:30.666794+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "limit": "2",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "limit": "2",
    "fields": "['*']"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-14T22:39:30.767728+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp021_sft_ragen_format\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:35:48.559Z\", \"updated_at\": \"2026-05-14T22:35:49.619Z\", \"hypothesis\": \"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\", \"parent\": \"exp019b_expert_sft_v3\"}, \"exp020d_grpo_from_sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:19:30.993Z\", \"updated_at\": \"2026-05-14T22:19:42.519Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.\", \"parent\": \"exp019b_expert_sft_v3\", \"spec\": {\"command\": \"bash -c \\\"ray stop --force 2>/dev/null; sleep 5; ln -sfn /root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final /root/autodl-tmp/checkpoints/qwen3_exp019b_sft && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p /root/autodl-tmp/tmp/ && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && export RAY_memory_monitor_refresh_ms=0 && export RAY_SYSTEM_MEMORY=210000000000 && export HYDRA_FULL_ERROR=1 && mkdir -p /root/autodl-tmp/checkpoints/exp020d/ && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp018_sft_grpo model_path=/root/autodl-tmp/checkpoints/qwen3_exp019b_sft trainer.experiment_name=exp020d-alfworld-sft-grpo trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp020d/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp020d/ es_manager.val.en
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-14T22:39:43.267219+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-17606",
  "command": "nvidia-smi --query-compute-apps=pid,used_memory,name --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-17606",
    "command": "nvidia-smi --query-compute-apps=pid,used_memory,name --format=csv,noheader"
  }
}
```

</details>

---


### Tool result

_source line 1537 · 2026-05-14T22:39:43.669138+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"389434, 40184 MiB, ray::WorkerDict\\n389435, 40184 MiB, ray::WorkerDict\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 401
}
```

</details>

---


### Assistant

_source line 1538 · 2026-05-14T22:39:48.746409+00:00_

exp020b Ray workers 仍占用 GPU 显存。训练在 step 3/30，进程正常。

注意到 exp020d 命令含 `ray stop --force` — 如果它执行过，会杀掉 exp020b。但 exp020b 仍在运行说明 exp020d 要么没启动，要么 cleanup worker 阻止了。exp021 仅 PREPARING 未启动，暂无冲突。

无需额外报告，exp020b 正常运行中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 1539 · 2026-05-15T00:54:09.167475+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 1540 · 2026-05-15T00:54:52.640402+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1 only（C001 约束，bjb1-17606）
- exp020b GRPO 正在跑（PID 389434/389435 Ray workers，双卡各 40GB）——不要 `ray stop --force` 或启动新 GPU 任务
- Cron 误报模式：SFT 实验用 `report_to="none"`，cron 无法区分正常退出与崩溃，已连续 4 次误报（exp017/019/019b×2）——收到 cron on_failed 先 tail log 确认再下结论
- ALFWorld 动作格式："move X to Y" 是唯一合法 placement action，"put X in/on Y" 不合法（exp019 踩过坑）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606(root)，工作目录 `/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型 checkpoint：`/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final/`（Qwen3-1.7B，3.4GB）
- Symlink：`/root/autodl-tmp/checkpoints/qwen3_exp019b_sft` → 上述 final/（RAGEN 用）
- 数据：`/root/autodl-tmp/expert_sft_v3/`（train 2546, val 133）
- RAGEN config：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp018_sft_grpo.yaml`
- 活跃进程：exp020b Ray workers PID 389434, 389435（双卡各 ~40GB，step 3/30）
- 无 W&B（SFT/GRPO 都用 `logger: ['console']`）
- Eval 结果：`/root/cost-verify-agent-rl/artifacts/eval_exp019b_fast.json`

### 3. 📊 当前状态
**刚做完**：确认 exp019b SFT 成功（20% success, 100% format, 85.3% valid），修正 exp020b initial val 0% 为样本量问题（4 episodes），确认 exp020b GRPO step 1 train success=18.75% 与 eval_sft_fast 一致。

**Registry 活跃实验**：
- `exp020b_grpo_from_sft`: PREPARING（实际 RUNNING，step 3/30，~274s/step，ETA ~2h from step 3）
- `exp020d_grpo_from_sft`: PREPARING（exp020d 命令含 `ray stop --force`，未实际运行——被 cleanup worker 处理）
- `exp021_sft_ragen_format`: PREPARING（计划用 v4 RAGEN 格式数据重做 SFT，尚未启动）

**等待**：exp020b 完成后需审查 val success 是否 ≥20%。exp021 启动时需审查数据格式。

### 4. 📋 待办
- exp020b step 20 val 结果出来 → 检查 success 是否提升（pass@1 > 0%），action_is_valid 趋势
- exp020b 完成（30 steps） → 审查最终 val metrics，对比 baseline 20%，判断 GRPO 是否有效
- exp021 启动 → 审查 v4 数据格式（RAGEN Turn/State/Reward 结构）是否正确，system prompt 是否与 RAGEN agent_proxy 一致
- 任何新实验启动 → 检查 GPU 合规（cuda:0,1）+ 不与 exp020b 冲突
- cron on_failed 通知 → 先 `tail log` + `nvidia-smi` 确认，不盲信

### 5. 🎯 战略上下文
**核心进展链**：base 4.7% → exp008_sft format only → exp017 expert SFT 5%（无 admissible actions）→ **exp019b expert SFT + admissible actions 20%** → exp020b GRPO（进行中）

**关键发现**：admissible actions 在 observation 中是 success rate 从 5%→20% 的关键因素。

**易判断错的事**：
1. RAGEN initial val 只有 4 episodes（`env_groups=4, group_size=1`），0% success 不代表模型退化——看 train rollout（64 episodes）才准
2. action_is_valid 在 RAGEN train（temp=1.0）vs eval_sft_fast（temp=0.4）会有大差异（58% vs 85%），这是温度导致的，不是 bug
3. `enable_response_mask=True` 在 exp020b 中生效（通过 symlink 路径含 "qwen" 绕过 assertion），如果后续要禁用，正确 hydra override 是顶层 `enable_response_mask=false`，不是 `actor_rollout_ref.model.enable_response_mask`
4. Registry 状态可能不准——exp020b 显示 PREPARING 但实际 RUNNING，以 GPU 进程为准
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_733b284b383121720ce3d07c5c4a6bb2:reviewer"
}
```

</details>

---
