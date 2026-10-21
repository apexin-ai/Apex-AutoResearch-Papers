# ops exp027 urgent status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp027_urgent_status_check_20260515T152743_result.json`
- **Structured JSON:** [`208422de7ce4a5e14b70.json`](../../sessions/20/208422de7ce4a5e14b70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp027 状态检查报告

---

### 1. 进程存活 ✅

```
PID     ELAPSED CMD
789790    55:01 python train.py --config-name _alfworld_exp027_stable_grpo
```

**进程存活**，已运行 55 分钟。

---

### 2. tmux 输出

tmux 命令在 read-only 模式下被阻止，无法获取。

---

### 3. 训练日志 & 指标

**当前训练步数：step 0（初始验证刚完成，尚未进入第一个训练步）**

主日志 (`exp027_stable_grpo.log`) 中无 `global_step` 或 `step:` 记录——所有实质输出在 Ray worker log 中。

Worker log 中唯一的 step 记录是 **step:0 初始验证**（`val_before_train=True`）：

| 指标 | 值 |
|------|-----|
| val-env/AlfworldSG/**success** | **6.25%** |
| val-env/AlfworldSG/pass@1 | 6.25% |
| val-env/AlfworldSG/action_is_valid | 63.125% |
| val-env/AlfworldSG/action_is_effective | 87.875% |
| val-env/AlfworldSG/num_actions | 42.375 |
| val-env/response_length | 114.67 |
| val-core/unknown/reward/mean@775 | 0.3226 |
| validation generation time | 502.57 秒 |

**尚无训练指标（KL / entropy / pg_loss）**——初始验证后进入第一个训练 step 的 rollout 阶段。主日志末尾（23:00:18）全是 TaskRunner 的 rollout warnings（`Skipping non-numeric metric 'anchor_obs'`），说明 step 1 的环境交互正在进行中。

Worker `WorkerDict pid=793233` 输出了 `compute_policy_loss` 的 FutureWarning，表明 policy update 计算已开始执行。

---

### 4. Checkpoint ❌

```
/root/autodl-tmp/checkpoints/exp027/
total 4
drwxr-xr-x  2 root root   10 May 15 22:33 .
drwxr-xr-x 10 root root 4096 May 15 22:33 ..
```

**目录为空，无 checkpoint 产出。** 符合预期——训练还未完成任何 step。

---

### 5. W&B 状态 ✅

W&B run: `run-20260515_223406-y7jiibqk`

```
files/
  output.log    855933 bytes  (最后更新 23:16)
  requirements.txt
  wandb-metadata.json
  media/
```

`wandb-summary.json` **尚未生成**（正常——第一个训练 step 未完成时不会写 summary）。

`output.log` 持续在更新（855KB，最后更新 23:16），**W&B 正在上报日志**。output.log 末尾内容与主日志一致——rollout warnings。

---

### 总结

| 检查项 | 状态 |
|--------|------|
| 进程存活 | ✅ PID 789790，运行 55 分钟 |
| 当前步数 | step 0 完成（初始验证），step 1 rollout 进行中 |
| 训练指标 | 尚无（KL/entropy/pg_loss 需等 step 1 完成） |
| 初始 val success | 6.25%（16 episodes） |
| Checkpoint | ❌ 无（预期之中） |
| W&B 上报 | ✅ output.log 持续更新 |

训练正常运行中。初始验证耗时 ~8.4 分钟，之后进入 step 1 的 rollout 阶段。鉴于 Alfworld 环境交互较慢，第一个完整训练 step 尚需时间。

---
