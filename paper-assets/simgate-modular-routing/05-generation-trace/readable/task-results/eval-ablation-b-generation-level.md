# eval ablation b generation level

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ablation-b-generation-level_20260514T083613_result.json`
- **Structured JSON:** [`cc2e1b2069a69e20e362.json`](../../sessions/cc/cc2e1b2069a69e20e362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

## ablation-b Generation-Level Eval 结果

**结论：ablation-b 通过验证，generation-level internal_recall = 51.52% > 30% 阈值。**

| Metric | 值 |
|--------|---|
| Accuracy | 65.36% |
| Balanced Accuracy | 59.27% |
| Internal Recall | **51.52%** |
| Deterministic Recall | 67.03% |
| Logit-Generation Gap | **0.0** |

**核心发现**：ablation-b 的 generation-level 和 logit-level 结果完全一致（confusion matrix [[17,16],[90,183]] 相同），是项目中唯一没有 logit-generation gap 的模型。

| 模型 | logit internal_recall | gen internal_recall | gap |
|------|----------------------|--------------------|----|
| **ablation-b** | **51.52%** | **51.52%** | **0.0** |
| v5 | 84.85% | 26.7% | 58.15 |
| generative-v1 | 51.85% | 16.67% | 35.18 |

**对 C2 claim 的影响**：项目有一个有效的 generation-level router (ablation-b)。ablation-b 与失败模型的训练差异（`upsample_minority=true` + `gradient_accumulation_steps=1`）可能是避免 logit-generation gap 的关键因素。

Registry 和 artifact 已更新。

---
