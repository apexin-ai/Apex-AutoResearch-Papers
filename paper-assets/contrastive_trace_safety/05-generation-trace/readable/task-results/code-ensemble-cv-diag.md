# code ensemble cv diag

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ensemble_cv_diag_20260522T054323_result.json`
- **Structured JSON:** [`ea039484d8a987ecce68.json`](../../sessions/ea/ea039484d8a987ecce68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 进程状态
- **PID 4049 正常运行中** — `State: R (running)`
- 命令: `python scripts/n7_ensemble_loocv.py`
- 231 线程, VmRSS ~3.4 GB, 大量 CPU 使用（多核并行 lbfgs）
- 未被 OOM kill, 无异常

### 结果文件
- `artifacts/ensemble_cv_results.json` **不存在** — 脚本在两个模型全部跑完后才写入
- `/tmp` 下也无 ensemble 相关临时文件

### 日志文件
- `/root/runs/contrastive_trace_safety/ensemble_cv_7_8b.log` 存在但 **0 bytes**
- **原因**: stdout/stderr 都重定向到了该文件（已通过 `/proc/4049/fd/1` 和 `/fd/2` 确认），但 Python 在非 tty 模式下使用 block buffering，print 输出尚未 flush
- 这不是异常 — 输出会在缓冲区满或进程结束时一次性写入

### 磁盘
- `/root/autodl-tmp/`: 18G/250G used (7%) — 无磁盘压力

### 超时原因分析
脚本做 LOO-CV，计算量远超预估：
- **R1-8B**: 209 folds × 13 layers × (inner split + outer eval) ≈ 5,434 次 LogisticRegression fit（4096 维）
- **OT-7B**: 228 folds × 28 layers × (inner split + outer eval) ≈ 12,768 次 LogisticRegression fit（3584 维）
- 总计 ~18,000 次高维 LR 训练，60 分钟估计偏乐观

### 结论
**进程健康，仍在正常计算中，只是 LOO-CV 计算量大导致耗时超预期。** 无需干预，等待完成即可。结果 JSON 和日志内容会在进程结束后出现。

---
