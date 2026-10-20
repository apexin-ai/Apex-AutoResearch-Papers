# ssh westd gemma d000 v2 must complete

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-gemma-d000-v2-must-complete_20260519T113101_result.json`
- **Structured JSON:** [`88fb2c8ef1dd525c3288.json`](../../sessions/88/88fb2c8ef1dd525c3288.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Gemma-2 d000 eval 完成。**

### 结果

**gemma2_d000:**
- MMLU: **0.6186** (61.86%)
- ARC Challenge: **0.8601** (86.01%)

文件确认存在：`eval_results_v2/gemma2_d000/eval_results.json`

### eval_results_v2 完整状态

| Model | MMLU | ARC | Status |
|-------|------|-----|--------|
| gemma2_d000 | 0.6186 | 0.8601 | DONE |
| gemma2_d005 | 0.6342 | 0.7782 | DONE |
| gemma2_d025 | 0.6456 | 0.8737 | DONE |
| gemma2_d050 | 0.6401 | 0.7108 | DONE |
| gemma2_d100 | — | — | INCOMPLETE |
| phi4_d000 | 0.7644 | 0.9206 | DONE |
| phi4_d005 | 0.7636 | 0.9181 | DONE |
| phi4_d025 | 0.7698 | 0.9232 | DONE |
| phi4_d050 | — | — | INCOMPLETE |
| qwen14b_d000 | 0.6944 | 0.9104 | DONE |
| qwen14b_d005 | 0.6901 | 0.9036 | DONE |
| qwen14b_d025 | 0.6204 | 0.8891 | DONE |
| qwen14b_d050 | — | — | INCOMPLETE |
| qwen7b_d000 | 0.6611 | 0.8788 | DONE |
| qwen7b_d005 | 0.6474 | 0.8609 | DONE |
| qwen7b_d025 | 0.6298 | 0.8404 | DONE |
| qwen7b_d050 | 0.6307 | 0.8456 | DONE |
| qwen7b_d100 | 0.6433 | 0.8498 | DONE |

3 个 INCOMPLETE（gemma2_d100, phi4_d050, qwen14b_d050）仍在其他 GPU 上运行。

---
