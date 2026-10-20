# analysis eval sft baseline noquant

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_sft_baseline_noquant_20260515T194506_result.json`
- **Structured JSON:** [`595a3e359cfa2119c317.json`](../../sessions/59/595a3e359cfa2119c317.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（hook 已自动填充了大部分字段）。

## 新旧 Baseline 对比

| 指标 | 量化 (旧) | 无量化 (新) | Delta |
|------|----------|------------|-------|
| **rel_f1** | 0.4057 | 0.4106 | **+0.49pp** |
| **evi_f1** | 0.7979 | 0.8013 | +0.34pp |
| **edcr** | — | 0.7039 | — |
| **format_ok_rate** | — | 99.8% | — |
| 推理时间 | 6139s | 3678s | **-40%** |

**结论**：量化 confound 不显著（rel_f1 差异 <1pp）。所有基于量化 baseline 的对比结论仍成立。无量化版反而更快，因为不做量化/反量化直接用满 GPU 显存。

---
