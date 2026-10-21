# fix appendix degen consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_appendix_degen_consistency_20260519T143858_result.json`
- **Structured JSON:** [`7d7e03d820ce041cc4b5.json`](../../sessions/7d/7d7e03d820ce041cc4b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diff 摘要：

| 行 | 修改 | 原值 | 新值 |
|---|---|---|---|
| L360 | 表头 CoNLL 8B 列 N 值 | `$N{=}16$` | `$N{=}8$` |
| L687 | 正文 Qwen valid fraction | `41\%` | `38\%` (匹配 100% − 61.7% 3-seed 均值) |
| L693 | within_rho 表 caption | — | 末尾追加 "Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates." |

一致性确认：
- L360 三列表头现在全部为 N=8
- L687 的 38% 与 L362 的 degeneracy 61.7% 互补（100−61.7≈38）
- L702-703 表格数据不变（仍为 seed 42 实际计算值 41%/11%），caption 已注明数据来源
- LLaMA 11% 无需改动（LLaMA 只有单种子推理数据，与 3-seed 均值无矛盾）

---
