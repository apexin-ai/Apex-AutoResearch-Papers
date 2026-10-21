# fix multi candidate rate

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_multi-candidate-rate_20260517T132002_result.json`
- **Structured JSON:** [`ddf5fb53c982723e1a16.json`](../../sessions/dd/ddf5fb53c982723e1a16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。验证结果：

| Experiment | 旧值 | 新值 (from data) | 状态 |
|---|---|---|---|
| **exp-010-mistral-v3** | 0.0667 | **0.5** (30/60) | 已修正 |
| **exp-018-arc-v2** | 0.0833 | **0.05** (3/60) | 已修正 |
| **exp-019-llama8b-strategyqa-200** | (缺失) | **0.41** (82/200) | 已补充 |
| **sica_expanded_14b** | (缺失) | **0.3818** (307/804) | 已补充 |
| exp-011-llama8b-v3 | 0.6167 | 0.6167 | 无需修改 |
| exp-017-strategyqa-v3 | 0.1 | 0.1 | 无需修改 |
| exp-020-llama8b-folio-204 | 0.618 | 0.6176 | 无需修改 (rounding) |
| sica_d012_14b | 0.5333 | 0.5333 | 无需修改 |

exp-010-mistral-v3 的旧值 0.0667 (4/60) 确实是 discordant rate 而非 multi_candidate_rate，实际有 30/60 题存在多候选答案。exp-018-arc-v2 的旧值 0.0833 (5/60) 也有误，实际只有 3/60 题有多候选。

---
