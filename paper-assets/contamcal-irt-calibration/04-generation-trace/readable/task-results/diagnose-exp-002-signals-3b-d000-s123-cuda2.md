# diagnose exp 002 signals 3B d000 s123 cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_3B_d000_s123_cuda2_20260516T141348_result.json`
- **Structured JSON:** [`e483c9c3e99a8eb37143.json`](../../sessions/e4/e483c9c3e99a8eb37143.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**这是一次误报（false positive）**，进程实际正常运行中。

**根因**：提交时声明 cuda:2，但未显式设置 `CUDA_VISIBLE_DEVICES=2`，进程实际落在 GPU 0。日志写入 `/tmp/3B_d000_s123_signals.log`（不含 `_cuda2` 后缀），导致监控系统找不到期望的 sentinel 文件 → 5 次 poll 后自动标 failed。

**当前进程状态**：PID 780943 在 GPU 0 正常运行，已完成 8/9 任务（s1/s2/s4 × mmlu/gsm8k/arc_challenge），正在处理最后的 s4_selfcritique_mmlu 分块。输出目录已有 9 个信号文件。

**建议**：无需重提交，将实验状态从 failed 改为 running。这是又一次 C004 违规（声明 GPU 与实际不符）。

---
