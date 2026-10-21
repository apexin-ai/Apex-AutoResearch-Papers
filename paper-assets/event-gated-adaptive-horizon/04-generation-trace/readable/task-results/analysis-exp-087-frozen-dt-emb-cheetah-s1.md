# analysis exp 087 frozen dt emb cheetah s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_087_frozen_dt_emb_cheetah_s1_20260525T184359_result.json`
- **Structured JSON:** [`45c10f131ae63a628ff5.json`](../../sessions/45/45c10f131ae63a628ff5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

**exp_087 结果：NVE = 0.33×，no_civo，hypothesis confirmed (success)**

关键发现：
- ve_ratio 全程趋近零（peak 仅 0.2 at 95K），远低于 baseline（0.6）
- civo/alert 从未触发
- gate_dt 恒定为 2（frozen embedding 无法适应）
- eval_return peak=310.1，远低于 baseline 444.0（符合预期：无自适应 gating 收益）

这与 exp_078（trained dt_emb, NVE=4.1×, CIVO 触发）形成鲜明对照，确认 **dt_embedding 的梯度训练是 CIVO 的必要条件**。C2 claim 现已有 Cheetah seed=1 的交叉验证支撑。等 exp_086（frozen s0）完成后将有完整 2-seed 证据。

---
