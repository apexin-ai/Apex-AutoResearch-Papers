# extract openvla spatial trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_openvla_spatial_trained_20260522T090157_result.json`
- **Structured JSON:** [`c02565c9dd5c2eb4b7b8.json`](../../sessions/c0/c02565c9dd5c2eb4b7b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**OpenVLA Spatial Trained (standardized_v1, 4/5 phases)**:

| 指标 | 值 |
|------|-----|
| R² peak | L14 = 0.845 |
| R² exit (L31) | 0.735 |
| Δ | **0.110** — exit collapse 确认 |
| L1 attention | 24/32 instruction-dominant, 8 mixed |
| Cross-instr classification | L1 起 100% 完美 |
| RSA best (last_preaction) | L0 = 0.579 (无明显 mid-layer peak) |

矩阵行已从旧的 `0.696 peak (L13), exit N/A` 更新为 `0.845→0.735, Δ=0.110`。L1 从缺失更新为 24/32。CF 列保留 legacy 数据并标注来源（‡‡）。

报告写入 `artifacts/openvla_spatial_trained_extraction.md`。

---
