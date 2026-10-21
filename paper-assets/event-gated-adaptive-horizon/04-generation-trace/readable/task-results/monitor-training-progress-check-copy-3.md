# monitor training progress check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260526T063748_result.json`
- **Structured JSON:** [`c8d24718bf1f5368a9d9.json`](../../sessions/c8/c8d24718bf1f5368a9d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度摘要

### exp_097_cheetah_008d_s3 (cuda:0)

| 指标 | 值 |
|---|---|
| 当前 step | **76,000** / 105,000 (72.4%) |
| 速率 | ~380 steps/min (fps≈10) |
| 剩余 | ~29,000 steps → **预计 ~1h16m 后完成** |

**Eval return 趋势:**
```
 5k:   8.7
15k: 216.6  ← 初始峰值
25k: 139.4
35k: 105.3
45k:  23.4  ← 谷底
55k:  68.2
65k: 182.5  ← 恢复
75k: 192.5  ← 缓慢上升中
```

**ve_ratio 趋势（CIVO 检测）:**
```
15k: 0.009  (delta=0.0)
25k: 0.120  (delta=+0.11)
35k: 0.350  (delta=+0.23)  ← 峰值
65k: 0.232  (delta=-0.53)
75k: 0.173  (delta=-0.06)  ← 持续下降
```
- **无 CIVO onset** — alert=0, gate_dt 锁定在 2.0 (100% dt_2_frac), empirical entropy=0
- ve_ratio 从 35k 的 0.35 峰值持续下降到 0.17，value error 在缩小，model 在变好

---

### exp_100_walker_008a_s1 (cuda:1)

| 指标 | 值 |
|---|---|
| 当前 step | **68,000** / 105,000 (64.8%) |
| 速率 | ~378 steps/min (fps≈10.7) |
| 剩余 | ~37,000 steps → **预计 ~1h38m 后完成** |

**Eval return 趋势:**
```
 5k:  31.0
15k: 168.8
25k: 158.0
35k: 202.9
45k: 306.0
55k: 457.3
65k: 628.8  ← 强劲单调上升
```
- 每 10k 步 eval return 增幅稳定在 ~100-170，学习曲线健康
- ve_ratio: 55k=0.248, 65k=0.234, 缓降中，alert=0，**无 CIVO onset**
- gate_dt 同样锁定在 2.0

---

### GPU 状态

| GPU | 温度 | 功耗 | 显存 | 利用率 |
|-----|------|------|------|--------|
| 0 (exp_097) | 40°C | 118W/600W | 52.4/97.9 GB | 22% |
| 1 (exp_100) | 40°C | 143W/600W | 4.7/97.9 GB | 36% |

两卡温度低、功耗低，运行正常。

---

**总结:** 两个实验都在正常训练，无异常。exp_097 预计 ~15:54、exp_100 预计 ~16:16 (服务器时间) 完成。两个实验的 gate 均锁死在 dt=2，未触发 CIVO onset——exp_097 的 ve_ratio 已从峰值 0.35 回落到 0.17，exp_100 的 eval return 单调递增表现很好。

---
