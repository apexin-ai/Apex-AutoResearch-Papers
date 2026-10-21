# check full status 2 5h

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_status_2_5h_20260523T180126_result.json`
- **Structured JSON:** [`c5a14bf5c06ed1d8398e.json`](../../sessions/c5/c5a14bf5c06ed1d8398e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== bjb1-45299 进程 ===
PID 133956 (exp_054): ALIVE, uptime 10h16m, GPU 2849 MiB
PID 157775 (exp_057): ALIVE, uptime 2h37m, GPU 3257 MiB

=== exp_054 PickCube frozen s0 ===
状态: running (已超 210K 目标，仍在跑)
当前步数: 220.4K
VE_RATIO 趋势:
  12.5K: 0.15  |  22.5K: 1.52  |  32.5K: 4.91  |  42.5K: 5.76
  52.5K: 4.50  |  62.5K: 8.81  ← 峰值
  72.5K: 0.55  |  82.5K: 0.94  |  92.5K: 0.62  | 102.5K: 0.51
 112.5K: 0.77  | 122.5K: 0.59  | 132.5K: 0.50  | 142.5K: 0.37
 152.5K: 0.42  | 162.5K: 0.45  | 172.5K: 0.61  | 182.5K: 0.51
 192.5K: 0.58  | 202.5K: 0.35  | 212.5K: 0.58
VE_RATIO_FINAL: 0.583 @ 212.5K
eval_return: 无数据（未记录该指标）
特征: 62.5K 后 ve_ratio 塌缩到 <1 区间，稳定在 0.35-0.61，无回升迹象

=== exp_057 Walker frozen s2 ===
当前步数: 105K
VE_RATIO 趋势:
  15K: 0.02  |  25K: 0.14  |  35K: 0.49  |  45K: 0.61
  55K: 0.75  |  65K: 0.72  |  75K: 0.62  |  85K: 0.61
  95K: 0.64  | 105K: 0.54
特征: 55K 后稳定在 0.54-0.75 区间，从未突破 1.0

=== bjb1-40020 进程 ===
PID 345223 (exp_055): ALIVE, uptime 9h15m, GPU 2575 MiB
PID 346430 (exp_056): ALIVE, uptime 9h00m, GPU ~2963 MiB

=== exp_055 PegInsertion trained s1 ===
当前步数: 142.5K
VE_RATIO 趋势:
  12.5K: 0.19  |  22.5K: 0.81  |  32.5K: 1.35  |  42.5K: 2.00
  52.5K: 2.39  |  62.5K: 2.85  |  72.5K: 2.28  |  82.5K: 2.48
  92.5K: 3.08  ← 峰值  | 102.5K: 2.51
 112.5K: 0.91  | 122.5K: 1.21  | 132.5K: 1.35  | 142.5K: 0.75
102.5K 后 eval 点: 2.51 → 0.91 → 1.21 → 1.35 → 0.75
⚠️ 112.5K 起断崖下跌，142.5K 跌至 0.75

=== exp_056 PegInsertion frozen s1 ===
当前步数: 136.2K
VE_RATIO 趋势:
  12.5K: 0.32  |  22.5K: 0.98  |  32.5K: 1.84  |  42.5K: 1.97
  52.5K: 5.42  |  62.5K: 4.05  |  72.5K: 8.41  |  82.5K: 11.32 ← 峰值
  92.5K: 3.72  | 102.5K: 3.03
 112.5K: 2.20  | 122.5K: 2.43  | 132.5K: 0.84
102.5K 后 eval 点: 3.03 → 2.20 → 2.43 → 0.84
⚠️ 132.5K 已跌破 2，降至 0.84
```

---
