# check status and registry align

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_status_and_registry_align_20260523T141209_result.json`
- **Structured JSON:** [`1f3b1d5224e3354a393d.json`](../../sessions/1f/1f3b1d5224e3354a393d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== bjb1-45299 进程 ===
PID 123495: ALIVE (GPU: 643+2758 MiB)
PID 133956: ALIVE (GPU: 2849 MiB)

=== exp_053 PegInsertion frozen s0 (PID 123495, cuda:1) ===
状态: running
当前步数: 199.4K / 210K (95%)
ve_ratio 趋势:
  step=12.5K   ve=0.160
  step=22.5K   ve=1.613
  step=32.5K   ve=1.258
  step=42.5K   ve=1.898
  step=52.5K   ve=8.100  ← peak
  step=62.5K   ve=2.211
  step=72.5K   ve=3.934
  step=82.5K   ve=1.819
  step=92.5K   ve=1.314
  step=102.5K  ve=1.646
  step=112.5K  ve=1.569
  step=122.5K  ve=0.704
  step=132.5K  ve=0.724
  step=142.5K  ve=0.577
  step=152.5K  ve=0.741
  step=162.5K  ve=0.477
  step=172.5K  ve=0.311
  step=182.5K  ve=0.438
  step=192.5K  ve=0.271
趋势: 52.5K peak 后持续下降，后半程稳定在 0.3–0.7。即将完成。

=== exp_054 PickCube frozen s0 (PID 133956, cuda:0) ===
状态: running
当前步数: 141.8K / 210K (68%)
ve_ratio 趋势:
  step=12.5K   ve=0.150
  step=22.5K   ve=1.520
  step=32.5K   ve=4.912
  step=42.5K   ve=5.764
  step=52.5K   ve=4.498
  step=62.5K   ve=8.811  ← peak
  step=72.5K   ve=0.547
  step=82.5K   ve=0.944
  step=92.5K   ve=0.620
  step=102.5K  ve=0.514
  step=112.5K  ve=0.773
  step=122.5K  ve=0.588
  step=132.5K  ve=0.503
趋势: 62.5K peak 后骤降并稳定在 0.5–0.9。

=== bjb1-40020 进程 ===
PID 345223: ALIVE (GPU: 2575 MiB)
PID 346430: ALIVE (GPU: 435+2528 MiB)

=== exp_055 PegInsertion trained s1 (PID 345223, cuda:0) ===
状态: running
当前步数: 87.2K / 210K (42%)
ve_ratio 趋势:
  step=12.5K   ve=0.190
  step=22.5K   ve=0.807
  step=32.5K   ve=1.354
  step=42.5K   ve=2.001
  step=52.5K   ve=2.386
  step=62.5K   ve=2.851
  step=72.5K   ve=2.281
  step=82.5K   ve=2.478  ← 82.5K 关键点
趋势: 持续上升中，82.5K 的 ve=2.48 远低于 exp_050 s0 在 82.5K 的 10.05 burst。trained gate 在 s1 上没有复现 s0 的爆发。

=== exp_056 PegInsertion frozen s1 (PID 346430, cuda:1) ===
状态: running
当前步数: 81.4K / 210K (39%)
ve_ratio 趋势:
  step=12.5K   ve=0.316
  step=22.5K   ve=0.975
  step=32.5K   ve=1.839
  step=42.5K   ve=1.966
  step=52.5K   ve=5.422
  step=62.5K   ve=4.047
  step=72.5K   ve=8.408  ← 72.5K 已出现大 spike
趋势: frozen gate 在 s1 上 72.5K 已爆发到 8.41，比 trained gate (exp_055) 在同阶段高得多。frozen 更早、更强地触发 ve spike。
```

---
