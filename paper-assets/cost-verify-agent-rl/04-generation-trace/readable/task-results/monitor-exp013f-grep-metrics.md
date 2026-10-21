# monitor exp013f grep metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp013f-grep-metrics_20260514T094629_result.json`
- **Structured JSON:** [`f16c7f50eac48b2c3463.json`](../../sessions/f1/f16c7f50eac48b2c3463.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## exp013f 状态

**进程**: PID 313810 ALIVE, 运行 ~14min
**进度**: Training Progress 20% (6/30), ~289s/step, 预估剩余 ~1.9h

**GPU**:
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 48% | 48GB / 97GB |
| cuda:1 | 100% | 48GB / 97GB |

## Step 5 验证指标（最近完成的 step）

| 指标 | 值 |
|------|-----|
| success | 0.0 |
| pass@1 | 0.0 |
| action_is_valid | 0.6 |
| action_is_effective | 1.0 |
| num_actions | 30.0 |
| raw_reward | 0.0 |
| response_length | 2983.25 |
| reward/mean@4 | 2.70 |
| reward/std@4 | 1.598 |
| reward/best@4/mean | 4.119 |
| reward/worst@4/mean | 1.170 |

## Step 6/7: 尚不可用

- Step 6 PPO 更新正在执行（两个 rank 已调用 `compute_policy_loss`）
- **训练指标（pg_loss, grad_norm, ppo_kl, entropy, clipfrac）未输出到 stdout**——日志中只记录每步的 val 指标（`step:N - val-env/...` 格式），训练指标仅发送到 W&B
- 无 W&B 本地目录（`/root/cost-verify-agent-rl/RAGEN/wandb/` 不存在）

要获取 pg_loss 等训练指标，需要通过 W&B API 查询，或检查代码中是否可以开启 stdout logging。

---
