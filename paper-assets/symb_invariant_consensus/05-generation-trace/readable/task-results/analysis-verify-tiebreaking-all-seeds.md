# analysis verify tiebreaking all seeds

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify-tiebreaking-all-seeds_20260523T184137_result.json`
- **Structured JSON:** [`a3b30bb0c39f9fdf14b3.json`](../../sessions/a3/a3b30bb0c39f9fdf14b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个实验均使用 **alphabetical tiebreaking**，stored SC 与 alphabetical 重算完全一致。

汇总：

| Model | Seed | 原 SC | Alpha SC | MC SC | 使用的方法 | 需要修正? |
|-------|------|-------|----------|-------|-----------|----------|
| Mistral-7B PW | 123 | 40.83% | 40.83% | 40.50% | ALPHABETICAL | 否 |
| Mistral-7B PW | 456 | 39.83% | 39.83% | 39.50% | ALPHABETICAL | 否 |
| Mistral-7B PW | 789 | 38.83% | 38.83% | 38.33% | ALPHABETICAL | 否 |
| LLaMA-3.1-8B PW | 123 | 71.33% | 71.33% | 69.00% | ALPHABETICAL | 否 |
| LLaMA-3.1-8B PW | 789 | 71.17% | 71.17% | 70.17% | ALPHABETICAL | 否 |
| Qwen2.5-14B PW | 123 | 72.33% | 72.33% | 72.50% | ALPHABETICAL | 否 |
| Qwen2.5-14B PW | 456 | 73.00% | 73.00% | 72.67% | ALPHABETICAL | 否 |
| Qwen2.5-14B PW | 789 | 73.67% | 73.67% | 73.50% | ALPHABETICAL | 否 |

所有 seeds 123/456/789 的实验均已使用正确的 alphabetical tiebreaking (`max(sorted(groups.keys()), key=...)`)，无需修正。seed42 的 Counter.most_common() 问题仅影响旧实验，不影响这批多种子实验。

---
