# diagnose threshold q03 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_threshold_q03_seed42_20260516T103210_result.json`
- **Structured JSON:** [`676dccbfbe3b6f9377e1.json`](../../sessions/67/676dccbfbe3b6f9377e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：根分区磁盘满（30G 用满，0 bytes 剩余）**

根分区被三个大目录撑爆：miniconda3 (12G) + data (11G) + models (8.8G) = 32.2G > 30G 限制。虽然 checkpoint 已正确 symlink 到 autodl-tmp 数据盘，但训练数据和基础模型仍在根分区。

三个实验失败模式完全一致：进度条正常推进后突然中断，无任何 Traceback 或错误信息——磁盘满时连错误日志都写不出来。

**紧急提醒**：`rho02_uniform_seed42` 目前还在 GPU 1 上跑（PID 316988），下次 checkpoint save 时同样会挂。

**修复**：将 `data/` 和 `models/` 迁移到 autodl-tmp 并创建 symlink，可释放 ~19.8G。报告已写入 `artifacts/diagnosis_threshold_q03_seed42.md`。

---
