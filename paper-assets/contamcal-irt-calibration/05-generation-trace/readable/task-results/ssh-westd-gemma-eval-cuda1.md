# ssh westd gemma eval cuda1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-gemma-eval-cuda1_20260519T085900_result.json`
- **Structured JSON:** [`0720c0cd5814e3fcc54c.json`](../../sessions/07/0720c0cd5814e3fcc54c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。cuda:1 上 d000/d005/d025 的 Gemma-2-9B 评估结果汇总：

| Dosage | MMLU | ARC-Challenge |
|--------|------|---------------|
| d000 | 0.6571 (9227/14042) | 0.7867 (922/1172) |
| d005 | 0.6520 (9156/14042) | 0.2295 (269/1172) |
| d025 | 0.6585 (9247/14042) | 0.8532 (1000/1172) |

注意 d005 的 ARC-Challenge 结果异常低 (0.2295)，远低于 d000 baseline (0.7867)，而 d025 反而升到了 0.8532。MMLU 三组差异不大（0.6520-0.6585）。d005 ARC 这个数字值得关注，可能是 contamination dosage 5% 引发了某种灾难性干扰，或者 adapter 加载有问题。

---
