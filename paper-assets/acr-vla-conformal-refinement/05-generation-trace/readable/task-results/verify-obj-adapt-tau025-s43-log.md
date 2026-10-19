# verify obj adapt tau025 s43 log

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_obj-adapt-tau025-s43-log_20260523T124024_result.json`
- **Structured JSON:** [`84d8c2075a243e3b3d2e.json`](../../sessions/84/84d8c2075a243e3b3d2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志和 JSON 均完整，参数确认无误：

| 项目 | 日志值 | 预期值 | 匹配 |
|------|--------|--------|------|
| `conformal_threshold` | **0.25** | 0.25 | ✓ |
| `benchmark` | **object** | object | ✓ |
| `seed` | **43** | 43 | ✓ |
| `mode` | **adaptive_conformal_crm** | adaptive_conformal_crm | ✓ |
| Overall SR | **77.5%** (155/200) | 77.5% | ✓ |
| trigger_rate | **3.67%** (1312/35796 steps) | 3.67% | ✓ |
| mean_uncertainty | 0.1103 | — | — |
| tau (JSON) | 0.25 | 0.25 | ✓ |

**结论：τ=0.25 实验结果已确认正确。** 日志路径：`/root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-object-s43.log`，JSON 结果：`logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json`。Registry 记录的 SR=77.5%, trigger_rate=3.67% 与日志完全一致。

---
