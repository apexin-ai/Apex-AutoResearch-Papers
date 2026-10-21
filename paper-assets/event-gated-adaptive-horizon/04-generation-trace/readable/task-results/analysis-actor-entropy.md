# analysis actor entropy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_actor-entropy_20260524T181302_result.json`
- **Structured JSON:** [`da3359b4c006786f65cd.json`](../../sessions/da/da3359b4c006786f65cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

1. **Collapsed 配置 entropy 爆炸**：EG v4 从 -5.21 升至 +3.22（40K steps，+2.1 nats/10K），EG v5 从 -5.11 升至 +1.03（+1.14 nats/10K）。exp_045 延长训练也持续升高到 -0.14。

2. **Healthy baseline entropy 漂移慢 10-20 倍**：+0.07 到 +0.22 nats/10K，且 return 维持 900+，不影响性能。

3. **时序因果**：Return 先崩（60-80K），entropy 后升（95K+），符合 "delusional critic → bad actor gradients → policy confusion" 的因果链。

4. **短跑 collapsed 实验**（006、008d）在 entropy 爆炸前就被停掉了，但 008d_civo_s3/s4 和 059 已显示早期 entropy 上升信号（+0.3-0.8 nats）。

报告已注册：`art_20260524_1053a6`

---
