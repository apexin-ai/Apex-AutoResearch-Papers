# analysis exp 001 eval 3B d000 s42 a32 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_3B_d000_s42_a32_batch_20260516T060402_result.json`
- **Structured JSON:** [`8bea80bfd2fefc37f563.json`](../../sessions/8b/8bea80bfd2fefc37f563.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新（conclusion=success, metrics, checkpoint_path, log_path），summary 已注册为 artifact `art_20260516_ae736c`。

**汇总：**

| Benchmark | Aligned | Para-aligned |
|-----------|---------|-------------|
| MMLU | 63.07% | 64.31% |
| GSM8K | 14.10% | 5.26% |
| ARC | 82.42% | 81.06% |
| HumanEval | 14.02% | 19.23% |

**结论：success。** 所有指标与 d000_s123 baseline 一致（MMLU 差 0.25pp, ARC 差 0.86pp, GSM8K 差 4pp 在 seed 方差内）。GSM8K 绝对值低（14%）是 d000 SFT 的预期行为——d000_s123 也只有 18%，而 d100 达到 71%，说明 GSM8K 是 dose-response 最强判别器（+57pp 跨度）。无 W&B run。

---
