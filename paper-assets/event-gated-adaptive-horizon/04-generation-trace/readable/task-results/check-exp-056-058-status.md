# check exp 056 058 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_056_058_status_20260523T233801_result.json`
- **Structured JSON:** [`5c7a5bd2d897c06f60c5.json`](../../sessions/5c/5c7a5bd2d897c06f60c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。汇总如下：

---

## exp_056 PegInsertion frozen s1（bjb1-40020）

| 项目 | 值 |
|------|-----|
| **进程状态** | 运行中（PID 346430, elapsed 14h 36m） |
| **当前 step** | 212500 / 目标 210000（已过目标，预计跑到 ~222K） |
| **ve_ratio_peak** | **11.321 @ step 82500** |
| **ve_ratio_final** | 1.193 @ step 212500 |
| **eval_return_peak** | **24.42 @ step 132500** |
| **eval_return_final** | 4.37 @ step 212500 |
| **NVE 分类** | **burst**（peak 11.321 > 5）— 60K-90K 区间爆发，后半段回落 |
| **最后 checkpoint** | `logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt` |

**ve_ratio 轨迹：**
```
 12.5K: 0.316 | 22.5K: 0.975 | 32.5K: 1.839 | 42.5K: 1.966
 52.5K: 5.422 | 62.5K: 4.047 | 72.5K: 8.408 | 82.5K: 11.321 ← peak
 92.5K: 3.724 |102.5K: 3.034 |112.5K: 2.204 |122.5K: 2.425
132.5K: 0.842 |142.5K: 2.194 |152.5K: 2.203 |162.5K: 0.651
172.5K: 1.085 |182.5K: 1.070 |192.5K: 0.467 |202.5K: 0.708
212.5K: 1.193
```

---

## exp_058 Cheetah frozen s1（bjb1-45299）

| 项目 | 值 |
|------|-----|
| **进程状态** | 运行中（PID 164830, elapsed 5h 29m） |
| **当前 step** | ~195000 / 目标 210000（尚未完成） |
| **ve_ratio_peak** | **0.231 @ step 45000** |
| **ve_ratio_final** | 0.111 @ step 195000 |
| **eval_return_peak** | **191.74 @ step 25000** |
| **eval_return_final** | 82.54 @ step 195000 |
| **NVE 分类** | **clean**（peak 0.231 < 1.5）— ve_ratio 全程极低 |
| **最后 checkpoint** | `logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_175000.pt` |

**ve_ratio 轨迹：**
```
 15K: 0.011 | 25K: 0.030 | 35K: 0.054 | 45K: 0.231 ← peak
 55K: 0.081 | 65K: 0.127 | 75K: 0.139 | 85K: 0.188
 95K: 0.223 |105K: 0.166 |115K: 0.138 |125K: 0.102
135K: 0.129 |145K: 0.103 |155K: 0.103 |165K: 0.127
175K: 0.113 |185K: 0.142 |195K: 0.111
```

---

**两个实验均未完成，仍在运行。** exp_056 已过 210K 目标步数，接近尾声；exp_058 还差约 15K 步。

---
