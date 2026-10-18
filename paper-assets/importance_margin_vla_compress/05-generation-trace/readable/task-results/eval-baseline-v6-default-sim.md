# eval baseline v6 default sim

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline_v6_default_sim_20260516T122005_result.json`
- **Structured JSON:** [`01228f94f0c9fdb60a68.json`](../../sessions/01/01228f94f0c9fdb60a68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

50 episodes 完成。结果：

## baseline_v6_alpha16 Sim Rollout 结果

| 指标 | 值 |
|------|-----|
| **Success Rate** | **0/50 (0.0%)** |
| **95% Wilson CI** | [0.0%, 7.1%] |
| Mean episode length | 400.0 (全部跑满) |
| Mean reward | 0.0000 |
| Wall clock per episode | ~3.4s |
| 总耗时（不含加载） | ~170s |

**所有 50 个 episode 均 FAIL，reward=0，跑满 400 步。** 模型在 sim 中完全无法完成 peg insertion 任务。

这说明 baseline_v6_alpha16 (LoRA rank=32, alpha=16, step 29999) 在默认 ODE (temperature=1.0, Euler 10 steps) 下的 sim 表现为零。每 episode 仅 3.4s 完成 400 步（因为 action_horizon=50，所以每 episode 只做 8 次推理），时间合理。

---
