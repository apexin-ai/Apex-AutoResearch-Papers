# analysis entity token lp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_entity_token_lp_20260518T152501_result.json`
- **Structured JSON:** [`7bf78bff72723722a1cc.json`](../../sessions/7b/7bf78bff72723722a1cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

| LP Variant | Within-ρ | Global-ρ | AUROC | Sel.F1 |
|---|---|---|---|---|
| full (baseline) | 0.30 | 0.30 | 0.64 | **0.6465** |
| **entity-text-type** | **0.38** | **0.44** | **0.72** | 0.6357 |
| entity-span | 0.00 | 0.00 | 0.51 | 0.5923 |

**Entity text+type LP 是更强的质量信号**（ρ/AUROC 全面超越 full-sequence LP），证实了 full-sequence LP 被 schema token 噪声稀释的假设。但 full-sequence LP 仍在 selection F1 上胜出（0.6465 vs 0.6357），因为 172 tokens 平均比 15 tokens 估计方差更低 — 经典的 bias-variance tradeoff。

其他发现：
- Entity-span LP（start/end 数字）信号为零（ρ≈0, AUROC≈0.50）
- Entity-all LP 反而比子集差，因为 span tokens 稀释了 text+type 信号
- 暗示加权 LP（upweight entity text+type）可能同时获得高相关性和低方差

---
