# ssh p4 entity independence

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p4-entity-independence_20260520T140839_result.json`
- **Structured JSON:** [`cc12dfb8062f2538cd0a.json`](../../sessions/cc/cc12dfb8062f2538cd0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。产出文件：

- `artifacts/r25_response/entity_independence.json` — 完整数值结果
- `artifacts/r25_response/entity_independence_paragraph.tex` — 论文可用段落

**核心结论**：entity 间存在轻微正相关（mean ratio ~1.33-1.38），但不构成对 construction 方法的威胁：

| | FewNERD | CoNLL | SciERC |
|---|---|---|---|
| 总 entity pairs | 22,404 | 6,783 | 2,531 |
| 不可测（确定性）pairs | 67.6% | 77.9% | 80.4% |
| 可测 pairs 中 Fisher 显著 | 12.1% | 44.0% | 12.7% |
| 正依赖 vs 负依赖 | 12.0% vs 0.1% | 44.0% vs 0.1% | 12.5% vs 0.2% |
| All-present obs/exp | 1.11 | 1.02 | 1.05 |
| MC null baseline (N=8) | 0.35% FPR | — | — |

三点缓解论证：(1) 依赖几乎全部是正向的（co-appear, 不是 compete），有利于 voting；(2) all-or-nothing ratio 接近 1.0（仅 2-11% 偏移）；(3) construction 基于 marginal frequency 投票，正相关不改变相对排序。

---
