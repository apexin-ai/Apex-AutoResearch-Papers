# verify rebuttal q5 numbers

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017_result.json`
- **Structured JSON:** [`ba0c36f09e9d9e67b1d0.json`](../../sessions/ba/ba0c36f09e9d9e67b1d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry agent 完成。结果确认了上述分析：

- **Obs-decoder SGS 1/6**: Registry 中 exp_025_obs_sgs_walker_s2 的 NVE 为 0.8-1.4（< 1.5× 阈值），符合论文 prevention 标准，registry 标记为 "negative" 是因为 eval 仅 66-90%。这就是论文中 1/6 的那个成功。
- **TCN**: Registry 有 12 个 TCN 实验（论文只用了 11 个，排除了 PickCube σ=0.5）。exp_029c (σ=0.1, NVE transient) 和 exp_030c (σ=1.0, NVE≤0.30) 在 registry 标记为 "negative"（因为 eval 差），但在论文中按 NVE<1.5× 标准算作 prevented。
- **Dual-critic**: Registry 确认 wide dual 3-4/4 Walker 成功 + Cheetah/PickCube 失败，与论文 3/4 一致。

Registry 数据与论文表格一致，进一步证实 **Q5 的数字有误**。上述 4 个不一致点成立。

---
