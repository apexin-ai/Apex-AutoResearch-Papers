# diagnose exp 006 graduated filtering v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_006_graduated_filtering_v2_20260514T213308_result.json`
- **Structured JSON:** [`0525a0fc39d066cad2d1.json`](../../sessions/05/0525a0fc39d066cad2d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 失败原因：**假警报（cron 监控了错误的日志文件）**

实验实际上**正在正常运行中**。问题是：
- cron 监控的是旧日志 `exp_006_graduated_filtering.log`，其中仍残留第一次运行的 `EXIT_CODE=124`
- resume 运行写入的是新日志 `exp_006_resumed.log`
- cron 读到旧文件的 EXIT_CODE=124，误报为"第二次失败"

### 2. 当前进度：**33/50 runs**（32 完成 + 1 正在训练）

| 策略 | 状态 |
|------|------|
| no-filter (5 seeds) | ✅ 全部完成 |
| binary-ours (5 seeds) | ✅ 全部完成 |
| binary-drayson (5 seeds) | ✅ 全部完成 |
| graduated α=0.1 (5 seeds) | ✅ 全部完成 |
| graduated α=0.3 (5 seeds) | ✅ 全部完成 |
| graduated α=0.5 (5 seeds) | ✅ 全部完成 |
| graduated α=0.7 (5 seeds) | ✅ s42, s123 完成；**s456 正在训练 (step 1856/2814, 66%)** |
| graduated α=0.9 (5 seeds) | ⏳ 未开始 |
| surprisal (5 seeds) | ⏳ 未开始 |
| dsir (5 seeds) | ⏳ 未开始 |

### 3. 未完成 runs（18 个）

| # | Run | 状态 |
|---|-----|------|
| 33 | graduated_a0.7_s456 | 🔄 训练中 66% |
| 34 | graduated_a0.7_s789 | 待跑 |
| 35 | graduated_a0.7_s1024 | 待跑 |
| 36 | graduated_a0.9_s42 | 待跑 |
| 37 | graduated_a0.9_s123 | 待跑 |
| 38 | graduated_a0.9_s456 | 待跑 |
| 39 | graduated_a0.9_s789 | 待跑 |
| 40 | graduated_a0.9_s1024 | 待跑 |
| 41 | surprisal_s42 | 待跑 |
| 42 | surprisal_s123 | 待跑 |
| 43 | surprisal_s456 | 待跑 |
| 44 | surprisal_s789 | 待跑 |
| 45 | surprisal_s1024 | 待跑 |
| 46 | dsir_s42 | 待跑 |
| 47 | dsir_s123 | 待跑 |
| 48 | dsir_s456 | 待跑 |
| 49 | dsir_s789 | 待跑 |
| 50 | dsir_s1024 | 待跑 |

### 4. 是否需要干预：**不需要**

实验在 tmux session `exp_006_graduated_filtering` 中正常跑着，GPU 83% 利用率，磁盘 22%，无 OOM/error。只需让它继续跑完即可。

需要修的是 cron 监控——让它指向正确的日志文件 `exp_006_resumed.log`，或者干脆不管它（实验会自然完成）。

### 5. 预估剩余时间

- 当前 run 剩余：~13 min 训练 + ~10 min eval ≈ 23 min
- 剩余 17 个完整 run × ~25 min/run ≈ 425 min
- **总计：约 7.5 小时**（预计完成时间 ~13:00 今天）

---
