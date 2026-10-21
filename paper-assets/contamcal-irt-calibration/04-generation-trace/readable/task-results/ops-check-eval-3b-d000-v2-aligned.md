# ops check eval 3B d000 v2 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-3B-d000-v2-aligned_20260515T002059_result.json`
- **Structured JSON:** [`28aada6db5a9143de4a1.json`](../../sessions/28/28aada6db5a9143de4a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能由触发本次任务的 cron 自身已清理）。

---

**诊断完成。** `exp_001_eval_3B_d000_v2_aligned` 成功，registry 已更新为 DONE。

结果汇总：

| Benchmark | Score | 备注 |
|-----------|-------|------|
| MMLU | 62.95% | |
| GSM8K | 35.25% | **未达目标 50%**，CoT 遗忘未恢复 |
| ARC-Challenge | 81.83% | |
| HumanEval pass@1 | 9.76% | |

关键发现：GSM8K 从 v1 的 11.7% 恢复到 35.25%，但仍远低于 raw baseline 60.5% 和目标 50%。aligned eval format 有改善但不够，CoT catastrophic forgetting 问题持续。

---
