# fix c0 definition rollback

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c0-definition-rollback_20260517T133946_result.json`
- **Structured JSON:** [`10df7b6fdcc2fa95f533.json`](../../sessions/10/10df7b6fdcc2fa95f533.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

**Bug**: `c0_multi_candidate_rate` 被错误定义为 `sica_answer != sc_answer`（SICA-SC 分歧率），而非真实多候选率。

**Fix**: 改为 `len(sc_vote_distribution) > 1`（K 条 trace 投票中有 >1 个不同答案），并将原指标保留为 `c0_disagree_rate`。

**验证结果**:

| 实验 | 旧值(disagree) | 新值(multi) | registry |
|------|----:|----:|----:|
| exp011 (LLaMA-8B) | 0.1167 | **0.6167** | 0.6167 ✓ |
| exp017 (StrategyQA) | 0.0333 | **0.1000** | 0.1 ✓ |
| exp020 (FOLIO) | 0.0637 | **0.6176** | 0.618 ✓ |
| exp010 (Mistral) | 0.0667 | **0.5000** | registry 值本身有误 |
| extraction_rate | 全部 ≤ 1.0 ✓ | | |

`c0_disagree_rate` 在所有实验中均远小于 `c0_multi_candidate_rate`，符合预期。

---
