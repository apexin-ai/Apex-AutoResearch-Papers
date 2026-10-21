# analysis p0 training metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p0-training-metrics_20260514T210338_result.json`
- **Structured JSON:** [`8d70a966fe016bcb6a83.json`](../../sessions/8d/8d70a966fe016bcb6a83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，当前训练在 step 45/200。

## P0 训练趋势 (grpo-s3-ced-lr5e6-r1, step 5–40)

| Step | reward | f1_reward | ced_reward | format_reward | reward_std | frac_zero_std | KL | grad_norm | loss |
|------|--------|-----------|------------|---------------|------------|---------------|-----|-----------|------|
| 5 | 0.087 | 0.0185 | 0.0114 | 0.057 | 0.139 | 0.2 | **2.4e9** | 0.224 | **2.4e7** |
| 10 | 0.068 | **0.0** | 0.0 | 0.068 | 0.110 | 0.1 | 0.002 | 0.187 | -0.002 |
| 15 | 0.155 | 0.011 | 0.004 | 0.141 | 0.167 | 0.2 | 0.002 | 0.393 | 0.048 |
| 20 | 0.101 | 0.0 | 0.0 | 0.101 | 0.121 | 0.2 | 1.374 | 0.115 | 0.046 |
| 25 | 0.176 | 0.0 | 0.0 | 0.176 | 0.137 | 0.2 | 0.004 | 0.445 | 0.029 |
| 30 | 0.131 | 0.002 | 0.002 | 0.128 | 0.140 | 0.1 | **7.0e13** | 0.250 | **9.9e11** |
| 35 | 0.194 | 0.010 | 0.015 | 0.168 | 0.188 | 0.1 | 0.157 | 0.190 | 0.053 |
| 40 | 0.318 | **0.038** | **0.079** | 0.201 | 0.345 | 0.3 | 0.006 | 0.137 | 0.023 |

当前进度：step 45/200，~1.4 hr elapsed，预计总时长 ~6.5 hr。

## 关键判断

- **f1_reward 趋势**：前 25 步基本为零，step 35 起才出现信号，step 40 跃升到 0.038。**极慢启动**，但最新方向是上升。Step 10 的 f1_reward = 0.0（Director 关注点）。
- **ced_reward**：与 f1 同步，step 40 首次出现有意义值 (0.079)。CED reward 比 f1 稍高，符合预期（CED 更宽松）。
- **frac_zero_std**：0.1–0.3 范围，**暂无 mode collapse 迹象**。
- **KL 异常飙升**：step 5 (2.4e9) 和 step 30 (7.0e13) 出现巨大 KL spike + loss spike，训练之后自行恢复。这是严重的数值不稳定信号——可能是 QLoRA + GRPO 的已知问题，或 vLLM reference model 与 training model 之间的 logprob 不同步导致。
- **整体 reward**：从 ~0.07 缓慢爬升到 0.32，但主要由 format_reward 贡献。任务奖励（f1+ced）到 step 40 才真正开始学习。
- **风险评估**：KL spike 可能导致后续训练崩溃。如果 step 45–50 的 KL 再次飙升，建议降低 lr 或加 KL penalty clip。

---
