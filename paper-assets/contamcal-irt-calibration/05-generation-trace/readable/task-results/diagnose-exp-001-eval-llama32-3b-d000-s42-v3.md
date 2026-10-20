# diagnose exp 001 eval llama32 3B d000 s42 v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_llama32_3B_d000_s42_v3_20260516T182511_result.json`
- **Structured JSON:** [`4fb85b88c2f1936cc5aa.json`](../../sessions/4f/4fb85b88c2f1936cc5aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diagnose_exp001_eval_3B_d000_s42_v3.md`。

**结论：监控误报，实验实际已成功完成。**

- 输出目录有 `.done` 和全部 7 个结果文件（mmlu/gsm8k/arc/humaneval/eval_results/item_responses/correctness_matrix）
- 进程经历了 v2 OOM kill (exit 137) → v3 attempt 1 跑到 GSM8K 33% 死亡 → v3 attempt 2 最终在 May 17 02:13 完成
- 失败原因是 `/tmp/agent-ml-exit/` 里没有 v3 的 exit sentinel，监控 5 次检查 PID 均已死亡就自动标 failed
- 无需重跑，应更正实验状态为 completed

---
