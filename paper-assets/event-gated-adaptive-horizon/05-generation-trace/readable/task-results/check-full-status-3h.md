# check full status 3h

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_status_3h_20260523T133053_result.json`
- **Structured JSON:** [`b1e6b5b42bf600da749b.json`](../../sessions/b1/b1e6b5b42bf600da749b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手，汇总如下：

---

```
=== bjb1-45299 进程状态 ===
PID 123495 (exp_053): ALIVE, GPU显存 643+2758 MiB
PID 133956 (exp_054): ALIVE, GPU显存 2849×2 MiB

=== exp_053 PegInsertion frozen s0 ===
train_step: 185.2K / 210K (88%)

ve_ratio 完整趋势:
  step    | ve_ratio | eval_return
  2,500   |    —     |   0.56
  12,500  |  0.160   |  10.89
  22,500  |  1.613   |   5.67
  32,500  |  1.258   |  13.01
  42,500  |  1.898   |  10.08
  52,500  |  8.100   |   2.41  ← primary burst
  62,500  |  2.211   |   7.93
  72,500  |  3.934   |   3.84
  82,500  |  1.819   |   7.32
  92,500  |  1.314   |   8.68
  102,500 |  1.646   |   5.67
  112,500 |  1.569   |   4.73
  122,500 |  0.704   |   8.80
  132,500 |  0.724   |   7.37
  142,500 |  0.577   |   7.67
  152,500 |  0.741   |   4.81
  162,500 |  0.477   |   6.47
  172,500 |  0.311   |   8.90
  182,500 |  0.438   |   5.89

secondary burst 检查: 无。102.5K 之后 ve_ratio 持续下降（1.65→0.44），无第二次 burst。

=== exp_054 PickCube frozen s0 ===
train_step: 126.4K / 210K (60%)

ve_ratio 完整趋势:
  step    | ve_ratio | eval_return
  2,500   |    —     |   2.41
  12,500  |  0.150   |  20.97
  22,500  |  1.520   |  11.59
  32,500  |  4.912   |   5.35
  42,500  |  5.764   |   3.50
  52,500  |  4.498   |   3.33
  62,500  |  8.810   |   1.22  ← primary burst
  72,500  |  0.547   |  16.32  ← burst 后恢复
  82,500  |  0.944   |   8.72
  92,500  |  0.620   |  13.20
  102,500 |  0.514   |  16.01
  112,500 |  0.773   |   9.75
  122,500 |  0.588   |  11.32

vs trained baseline @52.5K: frozen=3.33, trained=5.66 → frozen 落后
但 72.5K 后 frozen 恢复至 11-16 区间，已明显优于 trained baseline

=== bjb1-40020 进程状态 ===
PID 345223 (exp_055): ALIVE, GPU显存 2575×2 MiB
PID 346430 (exp_056): ALIVE, GPU显存 435+2528 MiB

=== exp_055 PegInsertion trained s1 ===
train_step: 76.6K / 210K (36%)

ve_ratio 趋势:
  step    | ve_ratio | eval_return
  2,500   |    —     |   2.01
  12,500  |  0.190   |  10.12
  22,500  |  0.807   |  11.47
  32,500  |  1.354   |  12.01
  42,500  |  2.001   |  10.13
  52,500  |  2.386   |  10.31
  62,500  |  2.851   |   9.02
  72,500  |  2.281   |  10.07

ve_ratio onset: 22.5K 突破 0.8，持续爬升至 62.5K 的 2.85 后回落。
尚未出现 burst（所有值 <3），eval_return 稳定在 9-12 区间。

=== exp_056 PegInsertion frozen s1 ===
train_step: 71.0K / 210K (34%)

ve_ratio 趋势:
  step    | ve_ratio | eval_return
  2,500   |    —     |   2.01
  12,500  |  0.316   |   5.75
  22,500  |  0.975   |   9.30
  32,500  |  1.839   |   9.23
  42,500  |  1.966   |  12.30
  52,500  |  5.422   |   5.90  ← 初现 burst 迹象
  62,500  |  4.047   |   9.98
```

---
