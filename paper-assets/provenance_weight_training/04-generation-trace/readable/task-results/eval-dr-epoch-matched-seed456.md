# eval dr epoch matched seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dr_epoch_matched_seed456_20260522T103227_result.json`
- **Structured JSON:** [`fee3fa344f74d6ab1b5e.json`](../../sessions/fe/fee3fa344f74d6ab1b5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，registry 已更新。

## dr_epoch_matched_seed456 评估结果

| 数据集 | PPL | 预期范围 | 状态 |
|--------|-----|---------|------|
| **Holdout** | 17.66 | 17.6-17.7 | ✓ |
| **OWT** | 18.27 | 18.2-18.4 | ✓ |
| **Wiki** | 15.16 | 15.2-15.4 | ✓ |

三个 seed 的 holdout PPL 一致性好：seed42=17.651, seed123=17.659, seed456=17.660。Registry 已标记 metrics/conclusion=success/status=DONE。

---
