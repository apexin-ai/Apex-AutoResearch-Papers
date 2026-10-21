# analysis exp cheetah 008a s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_cheetah_008a_s1_20260527T141828_result.json`
- **Structured JSON:** [`b189daeea3d61bc73f0d.json`](../../sessions/b1/b189daeea3d61bc73f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成，status=DONE。

---

## 结果汇总

| 指标 | 值 |
|------|-----|
| **eval_return_105K** | **281.24** |
| **NVE_105K** | **0.584** (< τ=2.0, no CIVO) |
| **value_mean_105K** | 164.29 |
| **ve_ratio_105K** | 0.584 |
| **conclusion** | **success** |
| **vs_baseline_105K** | **-36.7%** (baseline s1=444) |

## 完整 Eval Trajectory

| Step | eval_return | value_mean | NVE |
|------|------------|------------|-----|
| 5K   | 13.48      | 0.001      | ~0  |
| 15K  | 21.22      | 1.94       | 0.091 |
| 25K  | 178.88     | 10.83      | 0.061 |
| 35K  | 265.67     | 28.16      | 0.106 |
| 45K  | 391.72     | 51.43      | 0.131 |
| 55K  | 446.50     | ~75.3      | 0.169 |
| 65K  | 459.79     | 98.89      | 0.215 |
| 75K  | 519.56     | 120.76     | 0.232 |
| 85K  | 411.18     | 138.35     | 0.336 |
| 95K  | 415.49     | 151.31     | 0.364 |
| 105K | 281.24     | 164.29     | 0.584 |

## 分析报告路径
`projects/event-gated-adaptive-horizon/artifacts/exp_cheetah_008a_s1/report/analysis_c5f89a.md` (artifact ID: art_20260527_c5f89a)

C3 claim 在 Cheetah Run seed=1 得到确认：untrained dt=2 embedding 导致 value growth suppression，NVE 全程远低于 2.0，pattern 与 Walker 008a 一致。

---
