# ops fix 15B signals cuda0 cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_15B_signals_cuda0_cuda2_20260516T125351_result.json`
- **Structured JSON:** [`009b969f9147586c7728.json`](../../sessions/00/009b969f9147586c7728.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**两个实验都实际成功完成，无需重新启动。**

### cuda:0 — `exp_002_signals_15B_s123_batch`
- **根因**：脚本 `run_15B_s123_signals.sh` 有 shell 语法错误（line 39-40 `continue`/`fi` outside loop），导致 exit code=2。监控系统看到非零退出码误判为失败。
- **实际状态**：4 doses × 3 benchmarks × 3 signals = 36 个任务全部计算完成，所有 `signals_merged_*.json` 已生成。
- faiss 错误是非致命 warning（60 次出现但未阻断执行）。

### cuda:2 — `exp_002_signals_15B_d100_s123_cuda2`
- **根因**：进程在 sentinel 检查前退出（`reconcile_crons` 5× 检测到 process dead）。实际是任务已完成但退出太快，cron 来不及捕获 sentinel。
- **实际状态**：9/9 全部完成，日志有 `===BATCH_COMPLETE_15B_d100_s123_cuda2===` sentinel，所有输出文件完整。

### 已完成
- Registry 两个实验 conclusion 已更新为 `success`
- **不需要重跑任何任务**

### 当前 GPU 状态
| GPU | 状态 | 用途 |
|-----|------|------|
| cuda:0 | 占用 (7269 MiB) | PID 780943 — 3B d000_s123_a32 signals |
| cuda:1 | 占用 (1897 MiB) | PID 780591 |
| cuda:2 | **空闲** | 可用 |
| cuda:3 | 占用 (6619 MiB) | PID 764460 |
| cuda:4-5 | **空闲** | 可用 |

---
