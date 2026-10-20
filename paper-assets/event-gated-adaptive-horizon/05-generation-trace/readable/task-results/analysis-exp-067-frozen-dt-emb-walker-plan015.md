# analysis exp 067 frozen dt emb walker plan015

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_067_frozen_dt_emb_walker_plan015_20260525T065640_result.json`
- **Structured JSON:** [`6035f27bef49c429f5a6.json`](../../sessions/60/6035f27bef49c429f5a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**exp_067_frozen_dt_emb_walker_plan015 → conclusion: success**

| 指标 | exp_042 (parent) | exp_067 |
|------|------------------|---------|
| eval_final | 612.45 | 281.5 |
| eval_peak | 682.38 | 334.1 |
| nve_peak | 0.194 | 0.4 |
| CIVO triggered | No | No |

NVE peak=0.4 远低于 1.5x 阈值，civo_alert 全程为 0。Frozen dt_embedding 确实不触发 CIVO，验证了 **dt_emb 的梯度训练是 CIVO 触发的必要条件**，而非 dt_emb 的存在本身。

性能方面 exp_067 仅为 exp_042 的约一半，因为 frozen embedding 使 gate 完全锁死在 dt=2（entropy=0），丧失了自适应能力。

Registry 已更新为 DONE/success，analysis 已注册为 artifact。

---
