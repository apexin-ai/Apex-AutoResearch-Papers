# check harvest zs docred s1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_harvest-zs-docred-s1_20260523T022708_result.json`
- **Structured JSON:** [`4179074611a7ef3862c2.json`](../../sessions/41/4179074611a7ef3862c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job，无需删除（可能在之前的 session 中已清理）。

---

## 实验结果：eval_70b_zs_docred_200_full_s1 ✓ SUCCESS

| 指标 | Full S1 | Unconstrained | Grammar-only | Semantic-only |
|------|---------|---------------|--------------|---------------|
| **DR%** | **0.00** | 14.98 | 17.03 | 1.66 |
| **RV%** | **0.00** | — | — | — |
| **ET%** | **0.00** | — | — | — |
| **CF%** | 5.34 | — | — | — |
| **E-F1** | 70.05 | — | — | — |
| **R-F1** | **13.25** | 13.25 | 12.73 | 13.61 |
| **PF%** | 0.00 | — | — | — |

**Hypothesis 完美验证：**
- DR 从 unconstrained 的 14.98% 降至 **0.00%**（优于 semantic_only 的 1.66%，完全消除了 domain-range 违规）
- R-F1 = **13.25**，与 unconstrained 完全一致，零性能损失
- 200/200 样本全部成功，无 parse failure

Registry 已更新为 DONE (success)。

---
