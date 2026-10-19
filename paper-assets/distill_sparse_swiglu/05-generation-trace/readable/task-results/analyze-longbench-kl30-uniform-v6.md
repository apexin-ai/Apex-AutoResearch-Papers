# analyze longbench kl30 uniform v6

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_longbench_kl30_uniform_v6_20260516T184421_result.json`
- **Structured JSON:** [`2a791419a6f42cc62463.json`](../../sessions/2a/2a791419a6f42cc62463.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No W&B run. Here are the results:

```
METRICS:
- longbench_narrativeqa: 4.12 (dense baseline: 7.3, Δ = -3.18)
- longbench_qasper: 6.23 (dense baseline: 13.4, Δ = -7.17)
- longbench_gov_report: 16.97 (dense baseline: 30.5, Δ = -13.53)
- longbench_multi_news: 18.01 (dense baseline: 2.5, Δ = +15.51)

WANDB_RUN_ID: N/A
EXIT_STATUS: clean (EXIT_CODE=0, completed in 6156.6s)
CONCLUSION: negative — sparse KL30 uniform 在 3/4 任务上显著低于 dense baseline
ANALYSIS: 30% uniform sparsity 在长文本生成任务上造成严重退化（narrativeqa -44%, qasper -54%, gov_report -44%），唯一例外是 multi_news 大幅超越 baseline（+620%），但 dense baseline 本身得分极低(2.5)，可能是评估噪声而非真实提升。整体看 uniform allocation 在 LongBench 上不如 dense，uniform 策略未能保护长上下文关键层。
```

---
