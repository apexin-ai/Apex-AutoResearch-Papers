# design bernoulli st pessimism

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_design_bernoulli_st_pessimism_20260514T033956_result.json`
- **Structured JSON:** [`18819306c3e54dbffb89.json`](../../sessions/18/18819306c3e54dbffb89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入 `artifacts/bernoulli_st_pessimism_designs.md`。

核心发现：现有代码是**单 critic**（`self.value` + `_slow_value` EMA target），无 ensemble。方案 A 需要从零加第二个 critic。

三方案摘要：
- **A (Twin Critic)**: 改动最大但理论最稳，加 `value2` MLP，`_compute_target` 取 `min(v1,v2) - β|v1-v2|`，β=0.5
- **B (Reward Discount)**: 最简单，`_compute_target` 里对 step>K 的 reward 乘 0.95^(t-K)，仅一处改动
- **C (Partial Freeze)**: 最新颖，冻结 `_dt_embedding.weight[1]`（dt=2），用随机 embedding 作为内置悲观源，RSSM 对 dt=2 转移预测不精确 → value 自然偏低

推荐：A 首选实现（理论扎实），C 作为论文亮点探索（新颖性高），B 作为消融对照。

---
