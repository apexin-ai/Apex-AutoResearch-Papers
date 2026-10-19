# submit westd 34887 dual gpu urgent

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_westd-34887-dual-gpu-urgent_20260518T075011_result.json`
- **Structured JSON:** [`8511ad4df14b61a74598.json`](../../sessions/85/8511ad4df14b61a74598.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡已跑起来：

| GPU | 实验 | PID | 显存 | 利用率 |
|-----|------|-----|------|--------|
| cuda:0 | kl50_s456_eval (wikitext2,arc_c,winogrande,mmlu,gsm8k) | 9003 | 41.7 GB | 100% |
| cuda:1 | c4_ood_kl50_s456 (C4 OOD perplexity) | 9078 | 29.2 GB | 100% |

两个 job 均已进入 TEAL global mask 计算阶段，正常运行。

---
