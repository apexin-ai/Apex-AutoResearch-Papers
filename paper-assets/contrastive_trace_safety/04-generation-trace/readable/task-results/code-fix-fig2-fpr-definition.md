# code fix fig2 fpr definition

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_fig2_fpr_definition_20260517T011624_result.json`
- **Structured JSON:** [`d99b3ff768b1d20578c5.json`](../../sessions/d9/d99b3ff768b1d20578c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成修正。所有 `precp_fpr` 现在统一为 step-level：

| 模型 | 修改前 (trace) | 修改后 (step) |
|------|---------------|---------------|
| r1_8b_hs W=1 | 0.1037 | **0.0965** |
| r1_8b_hs W=5 | 0.0913 | **0.0809** |
| r1_8b_hs W=10 | 0.0865 | **0.0761** |
| r1_8b_hs W=15 | 0.0701 | **0.0639** |
| r1_8b_hs W=25 | 0.0545 | **0.0483** |
| r1_32b_best | 0.1891 | **0.2340** |
| qwq_32b_best | 0.1795 | **0.2168** |

`r1_8b_text` 保持不变（已是 step-level）。

---
