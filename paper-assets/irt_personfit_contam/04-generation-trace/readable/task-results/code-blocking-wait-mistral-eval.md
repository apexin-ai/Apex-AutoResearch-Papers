# code blocking wait mistral eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_blocking-wait-mistral-eval_20260521T152852_result.json`
- **Structured JSON:** [`9bf543d652ed9b921b45.json`](../../sessions/9b/9bf543d652ed9b921b45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 seed 的 Mistral clean eval 结果：

| Condition | accuracy | lz_star | theta_mle | n_items | n_seen | n_unseen |
|-----------|----------|---------|-----------|---------|--------|----------|
| **clean_s8** | 0.5162 | 5.7996 | -1.1457 | 14042 | 0 | 14042 |
| **clean_s9** | 0.5165 | 3.5214 | -1.1240 | 14042 | 0 | 14042 |
| **clean_s10** | 0.5347 | 3.4159 | -1.0286 | 14042 | 0 | 14042 |

所有 clean seed 均无 seen items（n_seen=0），acc_seen 和 lz_seen 为 None。lz_star 均为正值（3.4–5.8），theta_mle 在 -1.03 到 -1.15 之间。

---
