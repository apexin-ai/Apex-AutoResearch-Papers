# diagnose c2 qw n500

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_c2_qw_n500_20260514T143651_result.json`
- **Structured JSON:** [`340d4cb7e77e67f118e4.json`](../../sessions/34/340d4cb7e77e67f118e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cron 已经不存在了（可能之前已被清除）。

---

## 诊断结论：still_running

**结论**：进程仍在运行，这是 cron 第 3 次 false positive。

**关键发现**：
- **PID 131864** (SCREEN `c2_qw_gpu2`, importance): 正在跑 s015 condition，进度 93/500，100% CPU
- **PID 132002** (SCREEN `c2_qw_gpu3`, random): 正在跑 s015 condition，进度 98/500，100% CPU
- 实验用的是 **SCREEN sessions**（不是 tmux），运行 `python`（不是 `python3`）
- 当前只在第 1 个 condition (s015)，总共 8 conditions（imp/rand × s015/s020/s025/s030），预计还需数小时
- 无结果文件产出——正常，profiling 输出在全部完成后才写盘

**误判原因**：profiling 实验不产生 W&B 数据也不写 sentinel 文件，cron 检测不到活跃信号就判定为进程退出。

**已执行**：
- Registry 状态已从 DONE/failed 修正回 RUNNING
- cron 已不存在，不会再误触发

---
