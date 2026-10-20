# diagnose exp 002 signals 05B s123 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_05B_s123_batch_20260516T020115_result.json`
- **Structured JSON:** [`e563e9428069b4bc37eb.json`](../../sessions/e5/e563e9428069b4bc37eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因**：提交命令引用的脚本 `run_05B_s123_signals.sh` 不存在，实际文件名是 `run_signals_05B.sh`（文件名拼写不同）。

**日志关键错误**：
```
bash: run_05B_s123_signals.sh: No such file or directory
EXIT_CODE=127
```

**修复建议**：重新提交时使用正确的脚本名 `run_signals_05B.sh`，或根据 seed=123 的需求基于 `run_signals_05B.sh` 创建 `run_05B_s123_signals.sh`（如果需要不同参数配置）。

---
