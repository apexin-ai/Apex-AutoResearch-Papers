# check exp 053 054 055 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_053_054_055_progress_20260523T085705_result.json`
- **Structured JSON:** [`c9ee874fd56bd0182e79.json`](../../sessions/c9/c9ee874fd56bd0182e79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集，汇总如下：

---

## exp_053_peginsertion_frozen_s0 (bjb1-45299)
```
status:      running (uptime 4h36m, PID 123495)
train_step:  96.2K / 210K
eval_return: 8.68 @92.5K
gate_dt:     fixed=2 (frozen, 100% dt=2)
```

**ve_ratio 完整趋势（civo/ve_ratio）：**
| step | ve_ratio | 备注 |
|------|----------|------|
| 12.5K | 0.16 | 初始低位 |
| 22.5K | 1.61 | |
| 32.5K | 1.26 | |
| 42.5K | 1.90 | |
| 52.5K | **8.10** | spike |
| 62.5K | 2.21 | 回落 |
| 72.5K | 3.93 | 二次上升 |
| 82.5K | 1.82 | 回落 |
| 92.5K | **1.31** | 继续下降 ✓ |

**结论：92.5K 的 ve_ratio=1.31，从 72.5K 的 3.93 持续下降（82.5K=1.82→92.5K=1.31）。PegInsertion 的 ve_ratio spike（52.5K 峰值 8.10）确认是 transient，已回归正常范围。**

---

## exp_054_pickcube_frozen_s0 (bjb1-45299)
```
status:      running (uptime 1h11m, PID 133956)
train_step:  28.4K / 210K
eval_return: 11.59 @22.5K (下一次 eval 在 32.5K)
ve_ratio:    0.15 @12.5K → 1.52 @22.5K
gate_dt:     fixed=2 (frozen, 100% dt=2)
```

---

## exp_055_peginsertion_civo_trigger_s1 (bjb1-40020)
```
status:      running (uptime 10m38s, PID 345223)
train_step:  4.8K / 210K (刚启动，仍在 prefill 后的早期训练)
eval_return: 2.01 @2.5K
ve_ratio:    尚无（首次 CIVO eval 在 12.5K）
gate_dt:     fixed=2 (非 frozen，dt_emb_freeze 未设置)
```

---
