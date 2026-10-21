# check 70b scierc done

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_70b_scierc_done_20260521T065916_result.json`
- **Structured JSON:** [`95766139016991ffad7c.json`](../../sessions/95/95766139016991ffad7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 r16_70b_scierc_zs_s1 完成，registry 已更新为 DONE/success。

**结果摘要：**

| | Unconstrained | S1 Constrained | Δ |
|---|---|---|---|
| **E_F1** | 35.21 | 35.19 | -0.02 |
| **R_F1** | 11.15 | 11.24 | +0.09 |
| **DR%** | 6.41% | **0.00%** | -6.41pp |
| **RV%** | 0.61% | **0.00%** | -0.61pp |
| **CF%** | 0.00% | 3.50% | +3.50pp |
| **Parse fail** | 0% | 0% | — |

**vs 8B Qwen ZS S1：** 70B E_F1 35.19 vs 31.45 (+3.74)，R_F1 11.24 vs 8.38 (+2.86)，DR 0% vs 0.93%。70B 在 F1 和约束遵守上均优于 8B。

S1 constrained 成功消除所有 DR/RV 违规，F1 无损失。CF 从 0→3.50% 是因为 constrained 模式下 cross-field 检测更严格。

---
