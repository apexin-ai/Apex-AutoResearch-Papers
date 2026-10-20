# ops test eval 1 7b s44 no evi check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_test_eval_1_7b_s44_no_evi_check_20260525T053650_result.json`
- **Structured JSON:** [`6bd74dd9192447f638d4.json`](../../sessions/6b/6bd74dd9192447f638d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## Evidence Tax（1.7B RSFT, seed 44, test_revised）

| Condition | ign_f1 | precision | recall |
|-----------|--------|-----------|--------|
| **With evidence** | 22.46% | 40.07% | 15.76% |
| **No evidence** | 20.19% | 39.71% | 13.53% |
| **Δ (tax)** | **+2.27 pp** | +0.36 pp | +2.23 pp |

**结论**：假设被否定。No-evidence 模型的 ign_f1 反而**低了 2.27 个百分点**，说明 evidence 生成并未构成 performance tax——相反，要求模型输出 evidence 反而略微提升了关系抽取性能（可能因为 evidence reasoning 起到了 chain-of-thought 的作用）。

---
