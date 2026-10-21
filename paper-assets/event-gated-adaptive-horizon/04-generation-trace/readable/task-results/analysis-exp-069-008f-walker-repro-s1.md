# analysis exp 069 008f walker repro s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_069_008f_walker_repro_s1_20260525T071818_result.json`
- **Structured JSON:** [`350a2b19477768157803.json`](../../sessions/35/350a2b19477768157803.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结论：SUCCESS** — C2 因果控制实验验证通过。

核心发现：
- **训练正常完成**（EXIT_CODE=0），112K env steps
- **eval_return**：peak 390.1 @ 95K，final 237.8 @ 105K
- **ve_ratio 始终 < 0.5**（max 0.447），远低于 1.5x CIVO 阈值，civo/alert 从未触发
- **gate_dt 固定 2.0**（100% dt_2_frac，entropy=0）——确认无 dt_embedding 配置生效
- **value_mean ≈ target_mean**（106.3 vs 106.4）——无 value overestimation
- 105K 的 eval 下降是正常 Walker Walk 方差（与 exp_047 模式一致），非 CIVO 驱动

该 seed=1 结果与 parent（seed=0）行为模式一致，进一步强化了 dt_embedding 是 CIVO 触发必要条件的因果证据。

已更新 registry（DONE/success）并注册分析报告 `art_20260525_2cdbf0`。

---
