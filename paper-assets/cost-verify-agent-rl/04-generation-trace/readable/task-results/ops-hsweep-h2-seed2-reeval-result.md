# ops hsweep h2 seed2 reeval result

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_hsweep-h2-seed2-reeval-result_20260518T050912_result.json`
- **Structured JSON:** [`c200e9735bafba6605c6.json`](../../sessions/c2/c200e9735bafba6605c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被自动清理）。

**汇总：**

| Metric | Value |
|---|---|
| OOD success rate | **3.73%** (5/134) |
| action_is_valid | 99.4% |
| action_is_effective | 100% |
| pass@1 | 3.73% |
| num_actions | 48.53 |
| response_length | 8501 |

hsweep_h2_seed2 的 OOD 表现极差（3.73%），对比 exp029 reeval 的 23.88% 差距巨大。Registry 已更新为 DONE/success（假设确认：collapse 是真实的）。

GPU cuda:0,1 现在空闲，可用。

---
