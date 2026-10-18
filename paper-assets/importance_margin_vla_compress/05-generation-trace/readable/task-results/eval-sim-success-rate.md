# eval sim success rate

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sim_success_rate_20260516T072610_result.json`
- **Structured JSON:** [`ad3f7e2f25d1196e35e5.json`](../../sessions/ad/ad3f7e2f25d1196e35e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## aloha_sim_insertion Rollout 评估结果 (50 episodes, seed=42)

| Mode | Success Rate | 95% Wilson CI | Mean Ep Length | Mean Reward |
|------|-------------|---------------|----------------|-------------|
| **baseline** | 0/50 (0.0%) | [0.0%, 7.1%] | 300 (all truncated) | **0.1600** |
| **acis_prune** | 0/50 (0.0%) | [0.0%, 7.1%] | 300 (all truncated) | 0.0000 |
| **bypass** | 0/50 (0.0%) | [0.0%, 7.1%] | 300 (all truncated) | 0.0000 |

关键观察：
- **三个模式均 0% 成功率**，所有 episode 都跑满 300 步（env 硬上限）后截断
- **baseline 有非零 reward (0.16)**，说明策略有一定程度的任务进展（部分接近目标），但不足以完成插入
- **acis_prune 和 bypass（IMM checkpoint）reward 为 0**，说明 IMM two-stage 训练的 checkpoint 在 rollout 推理上表现更差——虽然它在 offline action loss 上通过了所有 gate，但这个优势没有转移到 closed-loop 控制

这与 offline evaluation (action loss) 的结论形成对比：v8b_twostage 的 offline loss 优于 baseline，但 rollout success rate 均为 0。可能原因包括训练数据量不足（仅 scripted 数据）、sim 环境的 closed-loop error compounding、或模型容量/训练步数不够。

---
