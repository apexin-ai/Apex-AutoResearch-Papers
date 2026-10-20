# check cls4b seed123 ckpt800 val5120 result

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cls4b-seed123-ckpt800-val5120-result_20260514T222616_result.json`
- **Structured JSON:** [`e4f63d2f47842fc5ed6b.json`](../../sessions/e4/e4f63d2f47842fc5ed6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron，可能已在之前的 session 中删除或未创建。

---

**CLS 4B seed123 ckpt-800 val@5120 eval 结果（success）**

| 指标 | 值 |
|------|-----|
| **accuracy** | 87.92% |
| **f1_macro** | 81.95 |
| **f1_fail** | 71.57 |
| **f1_pass** | 92.33 |
| **precision_fail** | 82.75 |
| **precision_pass** | 89.08 |
| **recall_fail** | 63.06 |
| **recall_pass** | 95.82 |
| **unparseable_rate** | 0% |
| **total samples** | 9,335 |
| **n_truncated** | 234 |
| **majority baseline** | 75.88% |
| **gap vs majority** | +12.04pp |

Registry 已更新：status=DONE, conclusion=success, metrics 已写入。

home cuda:0 已释放，可以启动 4B v5 val@5120 sweep。

---
