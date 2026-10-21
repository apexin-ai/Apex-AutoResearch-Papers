# check qwen beam998 done

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen_beam998_done_20260521T053747_result.json`
- **Structured JSON:** [`844f55d1166297b23767.json`](../../sessions/84/844f55d1166297b23767.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**r14_qwen_docred_beam4_998 结果摘要：**

| 指标 | 值 |
|------|-----|
| E_F1 | 58.19 |
| R_F1 | 8.72 |
| DR_pct | **0.0%** |
| RV_pct | **0.0%** |
| ET_pct | **0.0%** |
| CF_pct | 4.94% |
| parse_fail | 3.51% (35/998) |

**关键发现：**
- Beam-4 约束解码**完全消除**了 DR/RV/ET 三类违规，schema 合规性达 100%
- E_F1=58.19 对 ZS Qwen DocRED 合理
- R_F1=8.72 极低，relation_fp=15754 远超 relation_tp=1273 — 模型生成大量不匹配 gold 的关系。这是 ZS baseline 本身的问题（无 finetuning），非约束解码导致的退化
- CF_pct=4.94% 仍有残留（cross-field consistency 不受 grammar 约束）

---
