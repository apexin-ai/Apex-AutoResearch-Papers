# diagnose gsm8k gemma2 exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gsm8k-gemma2-exit_20260520T061751_result.json`
- **Structured JSON:** [`ebb2451e04bf5c889ca5.json`](../../sessions/eb/ebb2451e04bf5c889ca5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断结论：

**结果: FAILED（部分完成）**

| dosage | 状态 | GSM8K accuracy |
|--------|------|---------------|
| d000 | 完成 | **13.87%** (183/1319) |
| d100 | **失败** | 无结果 |

**d100 失败原因**: 进程在 eval 进行到 33% (54/165 batches) 时被静默 kill。日志最后一条记录在 14:19 CST，无任何 Traceback、Killed 或 OOM 错误信息——特征与内核 OOM kill 一致。d100 输出目录为空。

**日志路径**: `/root/runs/contamcal-irt-calibration/gsm8k_gemma2_s42_westd.log`

**关键时间线**:
- 13:32 d000 开始 → 14:07 d000 完成 (exit=0)
- 14:07 d100 开始 → 14:19 日志停止更新（进程死亡）

d100 需要重跑。重跑时可考虑降低 batch-size（当前为 8）以缓解潜在的显存压力。

---
