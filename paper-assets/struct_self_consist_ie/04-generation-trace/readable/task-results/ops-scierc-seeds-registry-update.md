# ops scierc seeds registry update

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scierc-seeds-registry-update_20260522T182548_result.json`
- **Structured JSON:** [`6645de177d35b6fab0ba.json`](../../sessions/66/6645de177d35b6fab0ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。两个实验摘要：

| | exp_scierc_n8_s2024 | exp_scierc_n8_s3141 |
|---|---|---|
| **status** | DONE (success) | DONE (success) |
| **greedy_f1** | 0.6641 | 0.6609 |
| **oracle_f1** | 0.7914 | 0.7645 |
| **ρ(SJ,F1) full** | 0.337 | 0.348 |
| **ρ(κ,F1) full** | 0.236 | 0.207 |
| **structural > surface** | YES (+0.101) | YES (+0.140) |
| **logprob ρ full** | 0.183 | 0.193 |
| **verdict** | MARGINAL | MARGINAL |
| **wall_clock** | ~1.9 GPU-hrs | ~1.9 GPU-hrs |

两个 seed 均确认 structural consistency (SJ) 优于 surface consistency (kappa)，与之前 3 个 seed 一致。现在 SciERC 有 5 个 seed (42, 123, 456, 2024, 3141)，可用于 Holm-Bonferroni 校正。

---
