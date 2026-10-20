# ops read kl001 ckpt30 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-kl001-ckpt30-results_20260514T212719_result.json`
- **Structured JSON:** [`bb6386495f3216ac51bb.json`](../../sessions/bb/bb6386495f3216ac51bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**kl001_r4 ckpt-30 评估结果：**

| 指标 | ckpt-30 |
|------|---------|
| **Rel-F1** | **0.0338** |
| Precision | 0.0459 |
| Recall | 0.0267 |
| **Evi-F1** | **0.5889** |
| **EDCR** | **0.9798** |
| pred_count | 7085 (n_predictions=8127) |
| truncated | 1/985 |
| format_compliance | 100% |
| 推理耗时 | 3462s |

**与已知 kl001 checkpoint 对比：**

| checkpoint | Rel-F1 | Evi-F1 | EDCR | pred_count |
|-----------|--------|--------|------|------------|
| ckpt-10 | 0.003 | 0.720 | 0.998 | 11621 |
| **ckpt-30** | **0.034** | **0.589** | **0.980** | 7085 |
| ckpt-50 | 0.156 | — | — | — |
| ckpt-100 | 0.217 | — | — | — |
| SFT baseline | 0.406 | 0.798 | 0.712 | — |

ckpt-30 的 Rel-F1 从 ckpt-10 的 0.003 提升到 0.034，有进步但仍然很低。Evi-F1 反而从 0.720 下降到 0.589。EDCR 保持高位(0.98)说明模型仍在大量引用 distractor 文档。整体趋势：关系抽取能力在缓慢恢复，但到 ckpt-100 也只有 0.217，远低于 SFT baseline 的 0.406。

---
