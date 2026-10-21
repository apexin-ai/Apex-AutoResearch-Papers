# train d129 1 7b random b01 s43 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_d129-1_7b-random-b01-s43-r2_20260517T235136_result.json`
- **Structured JSON:** [`3b47fe4e2118823ca02d.json`](../../sessions/3b/3b47fe4e2118823ca02d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功重启并注册监控。

**总结：**
- tmux session: `d129-random-b01-s43-r2`
- PID: `66669`
- GPU: cuda:0，占用 39294 MiB
- reward_mode: `additive_random` ✓（日志中出现 `random=0.441` 确认）
- 预估训练时间: ~12s/step × 500 steps ≈ **1.7 小时**

注：第一次失败原因是任务描述中的项目路径 `/root/autodl-tmp/solver-trace-ablation/` 不存在，实际路径为 `/root/solver-trace-ablation`。已用正确路径重启。

---
