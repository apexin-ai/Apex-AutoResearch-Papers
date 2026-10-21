# diag cuda2 deep diagnosis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cuda2_deep_diagnosis_20260514T151505_result.json`
- **Structured JSON:** [`3a12785c88eeb14acf33.json`](../../sessions/3a/3a12785c88eeb14acf33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 进程实际运行时间

计算 starttime: uptime=14984426s, starttime=1498263825 ticks (HZ=100) → 进程启动距今 **~30 分钟**，**不是 24+ 小时**。输出目录在 21:51 创建（可能是启动脚本先创建），进程本身约 22:46 启动。

### 进程状态

| 指标 | 值 | 判读 |
|------|-----|------|
| State | R (running) | 活跃 |
| CPU time (utime) | 1740s / ~1800s wall | ~97% CPU，活跃计算 |
| GPU util | 37%, 95W, 3686 MiB | 正在做推理 |
| Threads | 323 | 正常（PyTorch 线程池） |
| VmRSS | 1.9 GB | 正常（0.5B 模型） |
| Disk writes | 4096 bytes | 几乎没写过文件 |
| Output dir | 完全空 | 无任何 benchmark 完成 |

### 核心问题

1. **stdout/stderr → `/dev/pts/5`（死掉的 tmux）**：无法看到任何进度
2. **没有日志文件**：这次 aligned eval 没有重定向到 `/root/runs/` 下的 log
3. **30 分钟无输出**：aligned 格式（生成式评测）可能比 logprob 方式慢 10-100x，MMLU 14042 题可能需要数小时，但无法确认是否卡住

### 建议：Kill 并重跑

理由：
- 进程仅跑了 ~30 分钟，损失小
- 无日志可观测，无法判断是正常慢还是卡死
- 重跑时必须将 stdout/stderr 重定向到日志文件

是否执行 kill？

---
