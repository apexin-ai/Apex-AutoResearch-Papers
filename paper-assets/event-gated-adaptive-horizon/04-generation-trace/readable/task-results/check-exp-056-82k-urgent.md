# check exp 056 82k urgent

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_056_82k_urgent_20260523T142048_result.json`
- **Structured JSON:** [`21454ed582e7b73ce9c9.json`](../../sessions/21/21454ed582e7b73ce9c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp_056 PegInsertion frozen s1 ===
当前步数: 83.2K
82.5K ve_ratio: 11.32 ✓ 已到

完整 ve_ratio 趋势:
  12.5K → 0.32
  22.5K → 0.98
  32.5K → 1.84
  42.5K → 1.97
  52.5K → 5.42
  62.5K → 4.05
  72.5K → 8.41
  82.5K → 11.32

=== exp_055 PegInsertion trained s1 ===
当前步数: 89.2K
92.5K ve_ratio: 未到（还差 ~3.3K 步）

完整 ve_ratio 趋势:
  12.5K → 0.19
  22.5K → 0.81
  32.5K → 1.35
  42.5K → 2.00
  52.5K → 2.39
  62.5K → 2.85
  72.5K → 2.28
  82.5K → 2.48
```

exp_056 frozen 的 ve_ratio 在 82.5K 达到 **11.32**，远超 exp_055 trained 的 2.48。frozen 变体持续攀升，trained 变体在 52.5K 后基本平台化（2.3-2.9 区间徘徊）。

exp_055 当前 89.2K，按 ~4.2 fps 估算约 13 分钟后到 92.5K eval 点。

---
