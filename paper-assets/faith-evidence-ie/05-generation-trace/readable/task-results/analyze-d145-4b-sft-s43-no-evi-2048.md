# analyze d145 4b sft s43 no evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d145_4b_sft_s43_no_evi_2048_20260521T182255_result.json`
- **Structured JSON:** [`b6764f023e1d2136f685.json`](../../sessions/b6/b6764f023e1d2136f685.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d145_4b_sft_s43_no_evi_2048 eval 结果

| 指标 | s43 (d145) | s42 (d140_fix) | Δ |
|------|-----------|---------------|------|
| **Ign-F1** | **0.4355** | 0.4016 | **+3.39** |
| F1 | 0.4429 | 0.4095 | +3.34 |
| Precision | 0.4413 | 0.4062 | +3.51 |
| Recall | 0.4445 | 0.4128 | +3.17 |
| Ign-Precision | 0.4205 | 0.3859 | +3.46 |
| Ign-Recall | 0.4516 | 0.4185 | +3.31 |

**补充信息：**
- Evi-F1 = 0（no-evidence 模式，符合预期）
- `no_evidence: true` 已正确设置
- Format OK: 984/985 (99.9%)
- Truncated: 268/985（比 s42 的 178 多，s43 产生了更多 predictions: 32183 vs 25638）
- 推理耗时: 8731.7s (~2h25m)
- 无 W&B run ID
- 无异常/错误，EXIT_CODE=0

s43 比 s42 Ign-F1 高 3.4 个点，提升显著。

---
