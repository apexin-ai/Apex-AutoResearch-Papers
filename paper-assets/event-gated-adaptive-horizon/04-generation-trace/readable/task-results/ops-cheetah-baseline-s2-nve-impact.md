# ops cheetah baseline s2 nve impact

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cheetah-baseline-s2-nve-impact_20260519T001414_result.json`
- **Structured JSON:** [`93cfac6b310e53ef4a3c.json`](../../sessions/93/93cfac6b310e53ef4a3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_021_cheetah_sgs doesn't exist. Now computing the full analysis.

**S2 ve_ratio sequence:**
| step | s2_ve_ratio |
|------|------------|
| 35K | 0.145204 |
| 45K | 0.248134 |
| 55K | 0.514221 |
| 65K | 0.392063 |
| 75K | 0.417086 |
| 85K | 0.525493 |
| 95K | 0.650478 |
| 105K | 0.680481 |
| 115K | 0.587358 |
| 125K | 0.885724 |
| 135K | 0.732496 |
| 145K | 1.274663 |
| 155K | 0.666779 |
| 165K | 0.629038 |
| 175K | 0.635802 |
| 185K | 1.238133 |
| 195K | 0.605085 |
| 205K | 0.606175 |

---

```
Cheetah baseline comparison (35K-105K):
step  | old_avg(s0,s1) | s2_ve    | new_avg(s0,s1,s2) | delta%
------|----------------|----------|--------------------|---------
35K   | 0.109623       | 0.145204 | 0.121483           | +10.82%
45K   | 0.196562       | 0.248134 | 0.213753           | +8.75%
55K   | 0.342713       | 0.514221 | 0.399882           | +16.68%
65K   | 0.385000       | 0.392063 | 0.387355           | +0.61%
75K   | 0.408752       | 0.417086 | 0.411530           | +0.68%
85K   | 0.614197       | 0.525493 | 0.584629           | -4.81%
95K   | 0.509839       | 0.650478 | 0.556719           | +9.19%
105K  | 0.650991       | 0.680481 | 0.660821           | +1.51%

S2 pulls baseline UP at most steps (especially 55K: +16.7%), except 85K where s2 was lower.

Per-experiment NVE impact (NVE = exp_ve_ratio / baseline_ve_ratio):
exp_id     | old_peak_NVE | new_peak_NVE | old_nve@105K | new_nve@105K | peak_chg% | 105K_chg%
-----------|-------------|-------------|-------------|-------------|-----------|----------
010b       |  8.267 @65K |  8.217 @65K |   1.055     |   1.039     |   -0.61%  |  -1.49%
010b_s0    | 108.52 @105K| 106.90 @105K|  108.52     |  106.90     |   -1.49%  |  -1.49%
008a_ch_s0 |  1.078 @35K |  0.973 @35K |   0.490     |   0.483     |   -9.76%  |  -1.49%
008a_ch_s1 |  1.290 @35K |  1.164 @35K |   0.478     |   0.471     |   -9.76%  |  -1.51%
```

要点：
- S2 加入后 baseline 整体上移，NVE 全部下降（实验表现相对变好）
- @105K 变化统一约 -1.5%，因为该步 baseline 仅涨 1.51%
- 35K 处影响最大（baseline +10.82%），导致 008a 两个 seed 的 peak NVE 从 >1 降到接近/低于 1
- 010b 的极端 peak（65K 的 8.27）几乎不变，因为 65K baseline 仅涨 0.61%
- 010b_s0 的 105K 崩溃（NVE≈107）仍然极端，s2 无法实质性改变结论

---
