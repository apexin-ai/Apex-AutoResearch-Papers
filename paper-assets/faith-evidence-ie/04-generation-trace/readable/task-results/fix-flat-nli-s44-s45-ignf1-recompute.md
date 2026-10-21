# fix flat nli s44 s45 ignf1 recompute

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_flat_nli_s44_s45_ignf1_recompute_20260516T034724_result.json`
- **Structured JSON:** [`f83cb421efb9f31b4ddf.json`](../../sessions/f8/f83cb421efb9f31b4ddf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重算完成，metrics_v2.json 已写入。汇总：

## rsft_flat_nli_s44

| 指标 | 值 |
|------|------|
| rel_f1 | 0.461506 |
| **ign_f1** | **0.452126** |
| evi_f1 | 0.813123 |
| edcr | 0.645808 |
| evi_f1_joint | 0.359673 |
| Δ(ign_f1 - rel_f1) | **-0.0094** |

## rsft_flat_nli_s45

| 指标 | 值 |
|------|------|
| rel_f1 | 0.455052 |
| **ign_f1** | **0.446181** |
| evi_f1 | 0.815399 |
| edcr | 0.652133 |
| evi_f1_joint | 0.355612 |
| Δ(ign_f1 - rel_f1) | **-0.0089** |

两个实验的 ign_f1 现在均低于 rel_f1 约 0.9pp，符合预期（train facts 被正确排除）。rel_f1 / evi_f1 / edcr 均未变。

---
