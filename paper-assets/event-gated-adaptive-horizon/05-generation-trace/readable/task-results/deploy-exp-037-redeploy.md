# deploy exp 037 redeploy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp_037_redeploy_20260521T122042_result.json`
- **Structured JSON:** [`54e7ed13c5128278adf0.json`](../../sessions/54/54e7ed13c5128278adf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_037_wide_critic_cheetah 实际上正在运行。** 无需重新部署。

诊断结果：

| 项目 | 状态 |
|------|------|
| PID 14487 | **存活**，已运行 2 分 27 秒 |
| GPU 1 | RTX PRO 6000 Blackwell，23% 利用率，2973 MiB / 97887 MiB |
| 训练进度 | 已完成 prefill，step 5000 开始训练，eval_return=8.3 |
| 日志 | 正常输出 model_loss=13.0, wide_critic 参数已加载 (value_opt 2886911 vars) |

训练刚启动不久（2.5 分钟），GPU 利用率和显存偏低是因为刚开始训练、batch 还没跑满。gate_dt_mean=2.0 / wide_critic=True 均已生效。

当前无需任何操作，实验正在正常推进。

---
