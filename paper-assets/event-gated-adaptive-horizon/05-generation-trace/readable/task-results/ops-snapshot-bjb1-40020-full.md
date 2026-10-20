# ops snapshot bjb1 40020 full

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_snapshot_bjb1_40020_full_20260520T161734_result.json`
- **Structured JSON:** [`85c9700ce2dd64f21430.json`](../../sessions/85/85c9700ce2dd64f21430.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。注意 exp_029a 已经跑到 215K（超过 210K target），已完成/接近完成。

```
=== exp_029a (σ=0.2 s1) — PID 50924 ===
PID 50924: running (elapsed 07:45:09)
当前 step: 215K (target 210K, 已超额完成)

eval_return 完整:
  5K=36.7, 15K=137.7, 25K=180.9, 35K=124.0, 45K=124.2, 55K=133.9
  65K=169.7, 75K=171.2, 85K=151.8, 95K=180.3, 105K=319.4, 115K=345.5
  125K=401.0★, 135K=307.8, 145K=380.8, 155K=307.3, 165K=320.3
  175K=159.0, 185K=278.2, 195K=301.2, 205K=204.6, 215K=161.3

ve_ratio 完整:
  15K=0.0248, 25K=0.1165, 35K=0.3574, 45K=0.5147, 55K=0.6428★
  65K=0.4777, 75K=0.3980, 85K=0.4033, 95K=0.3007
  105K=0.1554, 115K=0.1348, 125K=0.1160, 135K=0.1449, 145K=0.1088
  155K=0.1287, 165K=0.1142, 175K=0.2138, 185K=0.1210, 195K=0.1075
  205K=0.1503, 215K=0.1864

P0 窗口 85-95K: ve_ratio=0.4033→0.3007 (远低于 s0 的 peak 0.908)
Peak NVE: 55K=0.6428, 之后持续下降到 ~0.11-0.19 区间
Peak return: 125K=401.0, 后半程回落严重 (175K=159, 215K=161)

=== exp_029c (σ=0.1 s0) — PID 59395 ===
PID 59395: running (elapsed 04:34:57)
当前 step: 135K

eval_return 完整:
  5K=35.6, 15K=99.1, 25K=140.7, 35K=155.7, 45K=160.9, 55K=254.8
  65K=268.7, 75K=295.5★, 85K=220.8, 95K=188.6, 105K=204.7
  115K=296.4, 125K=232.3, 135K=247.4

ve_ratio 完整:
  15K=0.0306, 25K=0.1606, 35K=0.3162, 45K=0.4807, 55K=0.4368
  65K=0.5432, 75K=0.6211, 85K=0.9533, 95K=1.0218★, 105K=0.7610
  115K=0.4514, 125K=0.4899, 135K=0.3995

P0 窗口 85-95K: ve_ratio=0.9533→1.0218★ (超过 s0 σ=0.2 的 0.908 peak!)
Peak NVE: 95K=1.0218 (NVE>1.0 表明 variance-explained 极高)
Peak return: 75K=295.5, 115K=296.4

=== GPU ===
cuda:0: 2% util, 3564/24564 MiB — PID 59400 (3025 MiB) [exp_029c]
cuda:1: 20% util, 2523/24564 MiB — PID 50924 (2514 MiB) [exp_029a]
```

**关键发现**：exp_029c (σ=0.1) 在 85-95K 窗口 NVE 达到 1.0218，**超越了 σ=0.2 s0 的 peak 0.908**。σ=0.1 的 TCN 噪声在该窗口表现更强。但 exp_029a (σ=0.2 s1) 同窗口仅 0.40-0.30，seed 间差异显著。

---
