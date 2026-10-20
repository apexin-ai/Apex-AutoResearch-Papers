# analysis exp 006 collapse mechanism

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_006_collapse_mechanism_20260514T011010_result.json`
- **Structured JSON:** [`dc8b39eccfd816f6b8ab.json`](../../sessions/dc/dc8b39eccfd816f6b8ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**崩塌时序**：actor_loss → 0 是首发信号（35K 开始加速衰减），eval_return 滞后 ~10K 步跟降。actor_entropy / critic_loss / world model losses 在崩塌期间均无异常。

**机制**：
1. 固定 dt=2 让每步 imagination rollout 跨 2 物理步，15 步想象 = 30 步物理时间，compounding error 指数放大
2. Actor 优化"想象中的最优策略"，与现实 diverge → 实际 return 下降
3. 但 critic 的 value_mean 仍基于乐观的想象训练，从 151→362 单调上升，即使实际 return 从 485 崩到 133
4. advantage (target - value) 从 6.6 缩到 0.4 → actor 梯度枯竭 → 策略固化 → 不可恢复的死循环

**dt=4 同模式但更快**：actor_loss 在 35K 就归零（vs dt=2 的 65K），dt 越大 compounding error 越大，崩塌越快。

**世界模型本身健康**——model_loss/reward_loss/dyn_loss 全部平稳下降，问题纯粹在 policy optimization 侧。

报告已保存到 `artifacts/exp_006_fixed_dt2/analysis/collapse_mechanism.md`。

---
