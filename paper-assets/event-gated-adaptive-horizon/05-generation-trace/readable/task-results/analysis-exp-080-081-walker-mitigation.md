# analysis exp 080 081 walker mitigation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_080_081_walker_mitigation_20260525T154527_result.json`
- **Structured JSON:** [`5fa6eabfeb1a677ded89.json`](../../sessions/5f/5fa6eabfeb1a677ded89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**exp_080 (seed=1): SUCCESS** — eval 876.7 (94.3% baseline), NVE=0.6
**exp_081 (seed=2): NEGATIVE** — eval 597.1 (64.2% baseline), NVE=0.5

**CIVO 抑制：3/3 seeds 验证通过**（NVE 全程 0.5-0.6，远低于 1.5 阈值）。dt=1 imagination 下 trained dt_emb 不触发 CIVO 的假设成立。

**任务性能：2/3 seeds 达标**。Seed 2 学习显著偏慢（25-55K 步出现平台期），105K 时仅 597，但仍在上升中（112K train return ~580-630）。3-seed 均值 781.2 ± 159.5 (84% baseline)，高方差由 seed 2 单独拉低。

报告已注册：`art_20260525_ac9ea8`。

---
