# check session restore full status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_session_restore_full_status_20260523T180535_result.json`
- **Structured JSON:** [`5a05af8d48e2dcd97320.json`](../../sessions/5a/5a05af8d48e2dcd97320.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## 全量状态汇报

### 进程状态
| 服务器 | PID | GPU 显存 | 运行时间 | 状态 |
|--------|-----|----------|----------|------|
| bjb1-45299 | 133956 (exp_054) | 2849 MiB cuda:0 | 10h20m | alive |
| bjb1-45299 | 157775 (exp_057) | 3257 MiB cuda:1 | 2h41m | alive |
| bjb1-40020 | 345223 (exp_055) | 2575 MiB cuda:0 | 9h19m | alive |
| bjb1-40020 | 346430 (exp_056) | 2528 MiB cuda:1 | 9h05m | alive |

---

### 实验汇总

```
exp_054 | 222.4K/210K | ve=0.583@212.5K | eval_return=10.26@212.5K | running (已超 210K，仍在跑)
exp_057 | 108K/210K   | ve=0.544@105K   | eval_return=81.85@105K   | running (51%)
exp_055 | 143.6K/210K | ve=0.745@142.5K | eval_return=20.44@142.5K | running (68%)
exp_056 | 137.4K/210K | ve=0.842@132.5K | eval_return=24.42@132.5K | running (65%)
```

---

### ve_ratio 趋势

**exp_054 PickCube frozen s0** — 早期飙升后快速回落，100K 后稳定在 0.35~0.62：
```
12.5K→0.15 | 22.5K→1.52 | 32.5K→4.91 | 42.5K→5.76 | 52.5K→4.50 | 62.5K→8.81
72.5K→0.55 | 82.5K→0.94 | 92.5K→0.62 | 102.5K→0.51 | 112.5K→0.77 | 122.5K→0.59
132.5K→0.50 | 142.5K→0.37 | 152.5K→0.42 | 162.5K→0.45 | 172.5K→0.61 | 182.5K→0.51
192.5K→0.58 | 202.5K→0.35 | 212.5K→0.58
```

**exp_057 Walker frozen s2** — 缓慢爬升到 0.75 后开始回落：
```
15K→0.02 | 25K→0.14 | 35K→0.49 | 45K→0.61 | 55K→0.75
65K→0.72 | 75K→0.62 | 85K→0.61 | 95K→0.64 | 105K→0.54
```

**exp_055 PegInsertion trained s1** — 升到 3.08 后 112.5K 处骤降，回落到 0.75：
```
12.5K→0.19 | 22.5K→0.81 | 32.5K→1.35 | 42.5K→2.00 | 52.5K→2.39 | 62.5K→2.85
72.5K→2.28 | 82.5K→2.48 | 92.5K→3.08 | 102.5K→2.51 | 112.5K→0.91 | 122.5K→1.21
132.5K→1.35 | 142.5K→0.75
```

**exp_056 PegInsertion frozen s1** — 82.5K 处达峰 11.32，之后快速回落：
```
12.5K→0.32 | 22.5K→0.98 | 32.5K→1.84 | 42.5K→1.97 | 52.5K→5.42 | 62.5K→4.05
72.5K→8.41 | 82.5K→11.32 | 92.5K→3.72 | 102.5K→3.03 | 112.5K→2.20 | 122.5K→2.43
132.5K→0.84
```

### eval_return 趋势

**exp_054** — 波动剧烈，最佳 20.97@12.5K，近期 10~17 区间震荡：
```
2.5K→2.41 | 12.5K→20.97 | 22.5K→11.59 | 32.5K→5.35 | 42.5K→3.50 | 52.5K→3.33
62.5K→1.22 | 72.5K→16.32 | 82.5K→8.72 | 92.5K→13.20 | 102.5K→16.01 | 112.5K→9.75
122.5K→11.32 | 132.5K→12.49 | 142.5K→16.13 | 152.5K→15.03 | 162.5K→13.67 | 172.5K→10.03
182.5K→12.07 | 192.5K→10.73 | 202.5K→17.44 | 212.5K→10.26
```

**exp_057** — 25K 达峰 184.07，之后缓慢下降到 75~82：
```
5K→39.27 | 15K→181.97 | 25K→184.07 | 35K→94.98 | 45K→106.39
55K→110.73 | 65K→103.36 | 75K→93.78 | 85K→83.76 | 95K→75.52 | 105K→81.85
```

**exp_055** — 前期 10 附近平稳，112.5K 跳到 24.05，近期 13~20：
```
2.5K→2.01 | 12.5K→10.12 | 22.5K→11.47 | 32.5K→12.01 | 42.5K→10.13 | 52.5K→10.31
62.5K→9.02 | 72.5K→10.07 | 82.5K→8.78 | 92.5K→7.24 | 102.5K→9.20
112.5K→24.05 | 122.5K→16.46 | 132.5K→13.15 | 142.5K→20.44
```

**exp_056** — 132.5K 跳到 24.42（与 ve_ratio 回落时间吻合），前期 3~12：
```
2.5K→2.01 | 12.5K→5.75 | 22.5K→9.30 | 32.5K→9.23 | 42.5K→12.30 | 52.5K→5.90
62.5K→9.98 | 72.5K→5.41 | 82.5K→3.57 | 92.5K→8.68 | 102.5K→9.60
112.5K→12.33 | 122.5K→10.13 | 132.5K→24.42
```

---

### 关键观察

1. **exp_054 已超 210K（222.4K）**，但进程仍在跑。可能配置的 total_steps 大于 210K，或没有自动停止。
2. **exp_055 和 exp_056** 都在 ve_ratio 从高峰回落的阶段出现 eval_return 跳升——ve_ratio 下降与性能提升正相关，符合 "frozen event gate 学会收敛后策略改善" 的预期。
3. **exp_057 Walker** 进度最慢（51%），eval_return 呈持续下降趋势，需关注后续是否企稳。

---
