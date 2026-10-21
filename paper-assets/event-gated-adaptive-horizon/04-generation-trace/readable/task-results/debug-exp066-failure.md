# debug exp066 failure

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_exp066-failure_20260524T223008_result.json`
- **Structured JSON:** [`45341bdd1f011e652bc6.json`](../../sessions/45/45341bdd1f011e652bc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**诊断结果**：原始命令中 `cd /root/dreamerv3-torch` 路径不存在，实际代码在 `/root/autodl-tmp/event-gated-adaptive-horizon`。

**已修复并重新提交**：
- 修正 cd 路径，通过 tmux session `exp_066_timeseries_rssm_fidelity` 重新启动
- 训练已正常运行，日志显示已完成 prefill 并到达 step 5000 开始 evaluation
- Registry 已更新为 RUNNING，spec 中记录了修正后的命令
- 服务器 bjb1-40020, GPU cuda:1, 60K steps, checkpoint_every=5000

---
