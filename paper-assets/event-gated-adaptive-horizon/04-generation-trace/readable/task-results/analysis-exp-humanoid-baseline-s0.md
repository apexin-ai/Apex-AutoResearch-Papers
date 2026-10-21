# analysis exp humanoid baseline s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_humanoid_baseline_s0_20260529T043619_result.json`
- **Structured JSON:** [`fe1cbfb9afb5a0d27dcf.json`](../../sessions/fe/fe1cbfb9afb5a0d27dcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## exp_humanoid_baseline_s0 结果摘要

| 指标 | 值 |
|------|-----|
| 训练完成 | 212K steps, EXIT_CODE=0 |
| eval_return (last 5 mean±std) | **1.48 ± 0.36** |
| NVE_max (≥35K) | **12.97×** @ 105K step |
| NVE_final (205K) | **12.22×** |
| NVE_mean (≥35K) | **7.64×** |
| value_mean_final | 15.18 (实际 return 仅 ~1.2) |
| actor_entropy | -17.8 (坍塌) |
| CIVO alerts | 3次 (55K, 105K, 195K) |

**结论: NEGATIVE** — 假设被证伪。DreamerV3-S baseline 在 Humanoid Walk (21-DoF) 上即使 dt=1 也存在严重 value overestimation (NVE 12.97×, 远超 τ=2.0)，且几乎没有学到有效行为。与 Walker (~950) / Cheetah (~430) 的 baseline (NVE < 2.0) 形成鲜明对比——说明高维动作空间本身就是 value overestimation 的温床，Humanoid 是 CIVO gating 的天然压力测试环境。

Registry 已更新为 DONE/negative，报告已注册为 artifact。

---
