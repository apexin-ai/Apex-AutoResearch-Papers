# analysis roc auc baselines

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_roc-auc-baselines_20260518T000939_result.json`
- **Structured JSON:** [`fbdcbbd3226aa4ee9781.json`](../../sessions/fb/fbdcbbd3226aa4ee9781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Method | Binary F1 | ROC-AUC | 95% CI |
| --- | --- | --- | --- |
| FastDetectGPT | 0.5805 | 0.5796 | [0.5717, 0.5873] |
| Binoculars | 0.5327 | 0.6203 | [0.6133, 0.6271] |
| AvgLogProb | 0.6785 | 0.7844 | [0.7780, 0.7906] |
| LD-Score | 0.6758 | 0.7507 | [0.7422, 0.7584] |
| 4-Det Ensemble | 0.6983 | 0.8175 | [0.8116, 0.8234] |
| 7-Feature (Ours) | 0.6935 | 0.8111 | [0.8050, 0.8169] |
| Combined (4-Det + 7-Feature) | 0.7127 | **0.8304** | [0.8248, 0.8358] |

7-Feature (Ours) 的 AUC 0.811 与 4-Det Ensemble 的 0.818 差距很小（CI 重叠），且不依赖外部检测器分数。Combined 达到最优 0.830。

输出已保存：
- 远程：`results/roc_auc_baselines.json`
- 本地：`artifacts/_project/analysis/roc_auc_baselines.md`

---
