# ops s1 baseline ve profile

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s1-baseline-ve-profile_20260519T182204_result.json`
- **Structured JSON:** [`5ae244d16d4d33a747af.json`](../../sessions/5a/5ae244d16d4d33a747af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提取完成，51 个数据点（5K–505K，每 10K 一个 eval 点）。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| **@105K** | eval_return=**915.67**, value_mean=**601.06**, ve_ratio=**0.6564** |
| **Peak eval_return** | step=**505K**, eval_return=**970.41**, value_mean=665.27, ve_ratio=0.6856 |

**ve_ratio profile 特征：**
- 0–75K 快速攀升（0→0.72），value 追赶 return
- 75K–105K 回落至 ~0.65（eval_return 从 596→916 急涨，value 跟不上）
- 105K–165K 缓慢回升至 ~0.73
- 165K+ 收敛振荡在 **0.69–0.73** 区间，value_mean 饱和在 ~665

CSV 已保存到本地 `artifacts/exp_001_baseline_s1_ve_profile_full.csv`。

---
