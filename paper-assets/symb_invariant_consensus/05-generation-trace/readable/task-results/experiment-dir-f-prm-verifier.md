# experiment dir f prm verifier

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-f-prm-verifier_20260520T155425_result.json`
- **Structured JSON:** [`96c739fc90073f264111.json`](../../sessions/96/96c739fc90073f264111.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 方法 | 准确率 | 正确数/总数 |
|------|--------|-----------|
| Standard SC | 53.33% | 16/30 |
| **Filtered SC** | **56.67%** | **17/30** |
| Weighted SC | 53.33% | 16/30 |
| Min-Filtered SC | 53.33% | 16/30 |

**Filtered SC 比 Standard SC 提升 +3.33% (+1题)**，具体是 folio_6 和 folio_21 被 Filtered SC 纠正（从 Unknown→True），但 folio_1 被 Filtered SC 搞错（从 True→Unknown）。净增 1 题。

局限性：使用同一 Mistral-7B 做生成+评估（self-eval），评分区分度有限。用独立 reward model（如 DeBERTa-NLI 或专用 PRM）预期能获得更好的区分效果，但本次因 AutoDL 网络问题无法下载。

结果已写入 `/root/symb_invariant_consensus/results/dir_f_prm_verifier_pilot/results.json`。

---
