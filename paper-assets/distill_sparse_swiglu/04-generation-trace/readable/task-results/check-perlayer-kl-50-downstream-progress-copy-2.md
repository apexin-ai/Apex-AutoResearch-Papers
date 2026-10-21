# check perlayer kl 50 downstream progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_perlayer_kl_50_downstream_progress_20260522T080436_result.json`
- **Structured JSON:** [`b101a2c1571349a88bb7.json`](../../sessions/b1/b101a2c1571349a88bb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成，总耗时 4291.9s（~71.5 分钟）。6 个 task 全部跑完，结果：

| Task | Metric | Score |
|------|--------|-------|
| arc_challenge | acc / acc_norm | 24.15% / 27.05% |
| winogrande | acc | 51.54% |
| mmlu | acc | 26.58% |
| gsm8k | exact_match | 1.74% |
| hellaswag | acc / acc_norm | 31.02% / 38.18% |
| piqa | acc / acc_norm | 63.98% / 62.79% |

结果已保存到 `/root/distill_sparse_swiglu/results/benchmark/perlayer_kl_50_s42_downstream/results.json`。进程已正常退出（EXIT_CODE=0）。

---
