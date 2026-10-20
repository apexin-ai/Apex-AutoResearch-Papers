# ops exp 027 s1 final analysis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp_027_s1_final_analysis_20260520T124427_result.json`
- **Structured JSON:** [`3728a32272bde068542c.json`](../../sessions/37/3728a32272bde068542c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（status=DONE, conclusion=negative 已在之前设置）。

```
=== exp_027_tcn_walker_s1 FINAL ===
total_steps: 215000
eval_return 完整轨迹:
  5K=31.0, 15K=140.5, 25K=163.6, 35K=153.0, 45K=136.8, 55K=158.3,
  65K=298.5, 75K=364.9, 85K=134.0, 95K=94.6, 105K=216.7, 115K=318.9,
  125K=309.1, 135K=216.1, 145K=175.4, 155K=171.0, 165K=209.5, 175K=120.4,
  185K=355.4, 195K=183.3, 205K=240.2, 215K=350.8
ve_ratio 完整轨迹:
  15K=0.0246, 25K=0.1416, 35K=0.3585, 45K=0.6101, 55K=0.7092, 65K=0.4875,
  75K=0.4902, 85K=1.4104, 95K=1.6367, 105K=0.6444, 115K=0.4021, 125K=0.3800,
  135K=0.5078, 145K=0.8469, 155K=0.8568, 165K=0.5393, 175K=0.7355, 185K=0.2110,
  195K=0.3513, 205K=0.2376, 215K=0.1476
汇总: eval_peak=364.9@75K, eval_last10_mean=233.1, nve_max=1.6367@95K, nve_final=0.1476
checkpoint: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/latest.pt
log: ~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log
Registry 更新: DONE/negative
```

与 s0 对比：s1 的 eval_peak 仅 364.9（s0 约 900+），NVE 在 85K-95K 出现严重飙升（1.41→1.64）后虽回落至 0.15，但 eval 始终在 100-365 区间剧烈震荡，远低于 baseline ~900。gate 全程锁定 dt=2（entropy=0），σ=0.5 TCN 噪声未能触发任何自适应行为。

---
