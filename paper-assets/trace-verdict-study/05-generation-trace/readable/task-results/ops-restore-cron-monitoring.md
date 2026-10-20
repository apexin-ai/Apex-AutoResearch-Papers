# ops restore cron monitoring

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restore-cron-monitoring_20260515T210107_result.json`
- **Structured JSON:** [`16e2a90dcd896afbc4be.json`](../../sessions/16/16e2a90dcd896afbc4be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. deepseek_exception_only_seed456 — **RUNNING** ✓
- **PID**: 160932，tmux session: `deepseek_exception_only_seed456`
- **GPU**: cuda:0 (GPU 0)，占用 22414 MiB，GPU利用率 100%
- **进度**: 165/444 steps (~37%)，~13-14s/it
- **Checkpoint**: `checkpoint-148` 已保存
- **预估剩余**: ~1h 左右

### 2. deepseek_full_trace_seed42_v3 — **RUNNING** ✓
- **PID**: 163109，在 pts/1 终端中（非 tmux，用 tee 输出日志）
- **GPU**: cuda:1 (GPU 1)，占用 22386 MiB，GPU利用率 100%
- **进度**: 11/444 steps (~2%)，刚启动不久，~16.7s/it
- **Checkpoint**: 尚无（只有 runs/ 目录）
- **预估剩余**: ~2h

### 3. vota_seed456_v2 — **COMPLETED** ✓
- **PID 146592**: 已结束
- **Checkpoint**: `final/` + `checkpoint-444` + `checkpoint-296` + `checkpoint-148` 全部保存
- **Eval 结果**:
  - **Accuracy: 99.08%** (baseline 71.5%, lift +27.6%)
  - Pass: precision 1.000, recall 0.987, F1 0.993
  - Fail: precision 0.969, recall 1.000, F1 0.984

三个实验均正常：2个在跑，1个已成功完成。GPU 0 显存占用较高（71.6GB/97.9GB），可能有其他缓存占用，但不影响训练。

---
