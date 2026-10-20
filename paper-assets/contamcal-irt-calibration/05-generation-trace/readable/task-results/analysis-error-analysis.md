# analysis error analysis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-analysis_20260520T025332_result.json`
- **Structured JSON:** [`f57573ae6494e692a5cd.json`](../../sessions/f5/f57573ae6494e692a5cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。

**核心发现**：105 条失败实验的 3 大系统性根因占 51%：
- **GPU 进程冲突 + CUDA 绑定失败** (21 条, 20%)：`submit_training_job` 无 GPU 锁，多 Worker 并发提交到同一 GPU
- **实验废弃/设计变更** (20 条, 19%)：alpha 标准化和 IRT 设计迭代产生的自然废弃
- **Cron/监控误报** (16 条, 15%)：基于 tmux session 的进程检测不可靠，多次将存活进程误标为 failed

**最高 ROI 修复**：在 `submit_training_job` 加 GPU 占用检查 + 改用 PID 文件做进程检测，可预防 ~37 条 (35%) 失败。

---
