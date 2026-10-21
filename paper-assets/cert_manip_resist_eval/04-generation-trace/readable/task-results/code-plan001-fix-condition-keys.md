# code plan001 fix condition keys

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-fix-condition-keys_20260522T082358_result.json`
- **Structured JSON:** [`c17c26d1b0a42c799930.json`](../../sessions/c1/c17c26d1b0a42c799930.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。修改汇总：

| 脚本 | 行号 | 旧格式 | 新格式 |
|------|------|--------|--------|
| `step4_panel_regression.py` | 398 | `f"{ds}×{atk}"` | `f"{ds}__{atk}"` |
| `step5_random_fault.py` | 302 | `f"{ds}x{atk}"` | `f"{ds}__{atk}"` |
| `confound_diagnosis.py` | 229, 395 | `f"{ds}×{attack}"` | `f"{ds}__{attack}"` |
| `step3_mi_matrix.py` | — | 无 condition key | 无需改 |

4 个脚本 syntax check 全部 OK。

---
