# check urgent all 4 final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent_all_4_final_20260523T232518_result.json`
- **Structured JSON:** [`08139a004c0c46361b67.json`](../../sessions/08/08139a004c0c46361b67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## bjb1-45299

### === exp_057 Walker frozen s2 ===
```
进程: DEAD (PID 157775 已退出)
步数: 224K / 210K ✅ 已完成（超额完成）
ve_ratio_max (NVE peak): 1.2826 @step 115K
ve_ratio_final: 0.1774 @step 215K
NVE 分类: clean (<1.5)
eval_final: 无 eval/return 指标，仅 train_return
train_return_peak: 290.20
train_return_final: 114.05 @step 224K
checkpoint: latest.pt, checkpoint_225000.pt 等 6 个

完整 ve_ratio 趋势:
15K:0.020 → 25K:0.137 → 35K:0.495 → 45K:0.615 → 55K:0.747 → 
65K:0.715 → 75K:0.619 → 85K:0.606 → 95K:0.636 → 105K:0.544 → 
115K:1.283↑ → 125K:0.732 → 135K:1.069 → 145K:1.163 → 155K:0.452 → 
165K:0.272 → 175K:0.146 → 185K:0.120 → 195K:0.108 → 205K:0.107 → 
215K:0.177
趋势: 前半段攀升，115K 处 peak，之后持续下降至 0.1 附近，收敛干净
```

### === exp_058 Cheetah frozen s1 ===
```
进程: ALIVE (PID 164830, 运行 5h16m, GPU 3257 MiB)
步数: 195K / 210K (93%)
ve_ratio_max: 0.2314 @step 45K
ve_ratio_current: 0.1112 @step 195K
NVE 分类: clean (<1.5，极低)
eval_final: 无 eval/return 指标
train_return_peak: 273.99
train_return_current: 65.78

完整 ve_ratio 趋势:
15K:0.011 → 25K:0.030 → 35K:0.054 → 45K:0.231↑ → 55K:0.081 → 
65K:0.127 → 75K:0.139 → 85K:0.188 → 95K:0.223 → 105K:0.166 → 
115K:0.138 → 125K:0.102 → 135K:0.129 → 145K:0.103 → 155K:0.103 → 
165K:0.127 → 175K:0.113 → 185K:0.143 → 195K:0.111
趋势: 全程极低 (<0.25)，基本无 novelty event 触发
```

## bjb1-40020

### === exp_055 PegInsertion trained s1 ===
```
进程: ALIVE (PID 345223, 运行 14h39m, GPU 2577 MiB)
步数: 221.6K / 210K ✅ 超额运行中
ve_ratio_max: 3.0775 @step 92.5K
ve_ratio_current: 0.4983 @step 212.5K
NVE 分类: transient (1.5 < 3.08 < 5)
eval_final: 无 eval/return 指标
train_return_peak: ≥26.07 (可能更高，中间数据被截断)
train_return_current: 19.97 @step 221.6K
checkpoint: latest.pt, checkpoint_202500.pt 等 9 个

完整 ve_ratio 趋势:
12.5K:0.190 → 22.5K:0.807 → 32.5K:1.354 → 42.5K:2.001 → 52.5K:2.386 → 
62.5K:2.851 → 72.5K:2.281 → 82.5K:2.478 → 92.5K:3.078↑ → 102.5K:2.514 → 
112.5K:0.908 → 122.5K:1.211 → 132.5K:1.355 → 142.5K:0.745 → 152.5K:0.546 → 
162.5K:1.173 → 172.5K:0.963 → 182.5K:0.941 → 192.5K:0.900 → 202.5K:0.727 → 
212.5K:0.498
趋势: 前半段明显 transient burst (peak 3.08 @92.5K)，112.5K 后快速衰减，后半段在 0.5-1.2 间波动
```

### === exp_056 PegInsertion frozen s1 ===
```
进程: ALIVE (PID 346430, 运行 14h24m, GPU 2528 MiB)
步数: 214K / 210K ✅ 超额运行中
ve_ratio_max: 11.321 @step 82.5K
ve_ratio_current: 1.1934 @step 212.5K (⚠️ alert=1.0 已触发)
NVE 分类: burst (>5，严重)
eval_final: 无 eval/return 指标
train_return_peak: ≥35.25 (中间截断)
train_return_current: 5.11 @step 214K
checkpoint: latest.pt, checkpoint_202500.pt 等 9 个

完整 ve_ratio 趋势:
12.5K:0.316 → 22.5K:0.975 → 32.5K:1.839 → 42.5K:1.966 → 52.5K:5.422 → 
62.5K:4.047 → 72.5K:8.408 → 82.5K:11.321↑↑ → 92.5K:3.724 → 102.5K:3.034 → 
112.5K:2.204 → 122.5K:2.425 → 132.5K:0.842 → 142.5K:2.194 → 152.5K:2.203 → 
162.5K:0.651 → 172.5K:1.085 → 182.5K:1.070 → 192.5K:0.467 → 202.5K:0.708 → 
212.5K:1.193⚠️
趋势: 前半段严重 burst (72.5K-82.5K 飙到 8-11)，后缓慢下降但仍不稳定，最近一个点又回升触发 alert
```

---

**关键观察**:
- 4 个实验均无 `eval/return`，只有 `train_return`
- 4 个实验的 `gate_dt` 全锁在 dt=2（gate_dt_2_frac=1.0），包括 exp_055（trained）—— gate 未学到有效切换
- exp_057 已完成，NVE clean；exp_058 还有约 15K 步，预计 ~1.5h 完成
- exp_055/056 已超 210K 目标仍在跑
- exp_056 的 burst NVE（peak 11.3）和低 train_return（5.11）值得关注

---
