# analysis reeval ced s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reeval_ced_s42_20260516T072811_result.json`
- **Structured JSON:** [`8f47aeb42afe36633574.json`](../../sessions/8f/8f47aeb42afe36633574.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## reeval_ced_s42 结果

日志无 error/traceback，EXIT_CODE=0，正常完成。

### 核心指标

```
F1:        0.4517
Ign-F1:    0.4423
Precision: 0.4657
Recall:    0.4385
Evi-F1:    0.8174
EDCR:      0.6569
```

### 三 seed 对比（统一协议，checkpoint-510, lora_alpha=128）

| 指标 | s42 | s43 | s45 | 均值 | 标准差 |
|------|-----|-----|-----|------|--------|
| **F1** | 0.4517 | **0.4601** | 0.4514 | 0.4544 | 0.0050 |
| **Ign-F1** | 0.4423 | **0.4512** | 0.4416 | 0.4450 | 0.0054 |
| **Evi-F1** | **0.8174** | 0.8063 | **0.8174** | 0.8137 | 0.0064 |
| **EDCR** | **0.6569** | 0.6542 | 0.6550 | 0.6554 | 0.0014 |
| Evi-F1-Joint | 0.3518 | **0.3605** | 0.3558 | 0.3560 | 0.0044 |
| Precision | 0.4657 | 0.4696 | **0.4718** | 0.4690 | 0.0031 |
| Recall | 0.4385 | **0.4509** | 0.4326 | 0.4407 | 0.0093 |
| Truncated | 214 | 184 | 206 | 201 | — |
| Predictions | 15436 | 15051 | 15307 | 15265 | — |

**结论**：s42 与 s43/s45 高度一致，三 seed 标准差极小（F1 σ=0.005, Evi-F1 σ=0.006）。s43 的 F1/Ign-F1 略高（+0.8pp），主要来自更高的 recall（0.4509 vs 0.4385/0.4326）。Evi-F1 和 EDCR 三 seed 几乎无差异。

Artifact 已注册：`art_20260516_ee2f95`。

---
