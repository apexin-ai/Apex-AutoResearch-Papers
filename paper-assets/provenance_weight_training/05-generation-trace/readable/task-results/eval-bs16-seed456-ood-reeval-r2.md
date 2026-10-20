# eval bs16 seed456 ood reeval r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bs16_seed456_ood_reeval_r2_20260522T084756_result.json`
- **Structured JSON:** [`11e539166a2d29b1d692.json`](../../sessions/11/11e539166a2d29b1d692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成——re-eval 之前已经跑完，registry 也已更新。验证如下：

**旧 eval（参数不对，tokens 偏少）：**

| | OWT ppl | OWT tokens | Wiki ppl | Wiki tokens |
|---|---|---|---|---|
| adaptive seed456 | 17.807 | 5,000,859 | 14.713 | 5,009,907 |

**新 eval（已修正，参数与 seed42/123 一致）：**

| | OWT ppl | OWT tokens | Wiki ppl | Wiki tokens |
|---|---|---|---|---|
| adaptive seed456 | **18.313** | 6,767,242 ✓ | **15.296** | 27,000,339 ✓ |
| uniform seed456 | **18.390** | 6,767,242 ✓ | **15.363** | 27,000,339 ✓ |

**对比 seed42/123 参考范围：**

| | OWT ppl | Wiki ppl |
|---|---|---|
| adaptive seed42 | 18.309 | 15.286 |
| adaptive seed123_r2 | 18.325 | 15.348 |
| **adaptive seed456** | **18.313** ✓ | **15.296** ✓ |
| uniform seed42 | 18.364 | 15.337 |
| uniform seed123 | 18.369 | 15.381 |
| **uniform seed456** | **18.390** ✓ | **15.363** ✓ |

Token 数量与参考一致（OWT 6,767,242 / Wiki 27,000,339），PPL 均在预期范围内。Registry 中两个实验的 metrics 已是修正后的值，无需额外操作。

---
