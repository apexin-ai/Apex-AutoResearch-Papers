# ops pilot log investigation

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pilot-log-investigation_20260521T105920_result.json`
- **Structured JSON:** [`f9509a35c9d87197cd70.json`](../../sessions/f9/f9509a35c9d87197cd70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。汇报如下：

---

## 调查结论

### 状态：两个进程都在正常计算，不是卡住

| | CKA (PID 78996) | CaCLR highdim (PID 79164) |
|---|---|---|
| 状态 | R (running) | R (running) |
| CPU 使用 | 3798%（~38核） | 4884%（~49核） |
| 累计 CPU 时间 | 441 分钟 | 554 分钟 |
| RSS | 1.2 GB | 4.2 GB |
| 线程数 | 128 | 173 |
| CWD | `/root/autodl-tmp/xling_calib_direction` | 同左 |

### 日志为空的原因：Python stdout block buffering

两个脚本都用 `print()` 输出，**没有** `flush=True`。stdout 重定向到文件时 Python 使用 **8KB block buffer**。脚本前几行 print 输出不到 200 字节，远未填满缓冲区。在脚本完成或缓冲区满之前，日志文件保持 0 字节。

### 输出目录为空的原因：脚本只在计算全部完成后才写文件

两个脚本都是在 `main()` 末尾才 `json.dump` 和写 `report.txt`。计算未结束，文件不会出现。

### 计算量分析

**CKA**: 8 层 × 5 语言 = 40 对，每对 100 次 bootstrap CKA（矩阵大小 14042×3584）= 4,000 次 CKA 计算。

**CaCLR highdim**: 3 alignment 方法 × 5 conditions × 16 超参组合（4α × 4β）× 8 层 = **640 次神经网络训练**（每次最多 100 epochs，patience=10）。这是 CPU 上的重计算。

### 建议

1. **不需要干预**——进程正在正常推进
2. **下次启动时**用 `python -u`（unbuffered）或 `PYTHONUNBUFFERED=1` 避免日志缓冲问题
3. 如果想立刻看到已有输出，可以 `kill -USR1` 或直接等完成；Python 进程正常退出时会 flush 缓冲区

---
