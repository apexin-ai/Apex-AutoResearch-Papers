# analysis 018v2 civo decomposition

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_018v2-civo-decomposition_20260516T172145_result.json`
- **Structured JSON:** [`89ce2172a5fae09c4e61.json`](../../sessions/89/89ce2172a5fae09c4e61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**exp_018v2_full_sgs_walker_s1 — SUCCESS (C5 confirmed)**

| Metric | 008d (collapsed) | 018v2 (Full-SGS) | Baseline |
|--------|-----------------|-------------------|----------|
| eval@105K | 131.08 | **448.34** | 915.67 |
| NVE final | 1.57 | **1.34** | ~0.66 |
| NVE peak | 4.12@55K | 4.01@25K | N/A |
| vs baseline | -85.7% | -51.0% | — |

**CIVO Decomposition:**
- 008d 总退化: 85.7% (vs baseline)
- CIVO 贡献: **40.4%** 的退化归因于 CIVO（被 Full-SGS 恢复）
- 固有成本: **59.6%** 为 gate 机制本身的开销

**结论:** Full-SGS 成功消除了 sustained CIVO collapse（final NVE 1.34 < 1.5 阈值），eval 从 131→448（+242%）。但 gate 机制本身仍有 ~51% 的 inherent performance cost vs baseline。C5 假设确认：stop-gradient on reward head eliminates value-critic-induced collapse。

Artifact 已注册: `art_20260516_32da8b`

---
