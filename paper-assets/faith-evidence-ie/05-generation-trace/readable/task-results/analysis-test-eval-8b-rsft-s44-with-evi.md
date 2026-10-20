# analysis test eval 8b rsft s44 with evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_8b_rsft_s44_with_evi_20260523T104723_result.json`
- **Structured JSON:** [`34753bccfbecc8ccc56f.json`](../../sessions/34/34753bccfbecc8ccc56f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

**s44 with-evi**: ign_f1=0.3329, evi_f1=0.2458, evi_f1_tp=0.5897, edcr=0.809, format_ok=498/500, truncated=29/500

**8B RSFT k1 with-evidence 3-seed 汇总**:

| Seed | ign_f1 |
|------|--------|
| s42  | 0.3353 |
| s43  | 0.3398 |
| s44  | 0.3329 |
| **Mean±Std** | **0.3360±0.0035** |

s44 是三个 seed 中最低的，但三者差异很小（std=0.35pp），variance 控制良好。

日志无 error，唯一 WARNING 是 `train_annotated.json not found, Ign-F1 = F1`，test_revised 评估的正常行为。无 W&B link。

---
