# ops extract gen4 urgent

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract-gen4-urgent_20260518T163209_result.json`
- **Structured JSON:** [`908dd19dabcca930d70c.json`](../../sessions/90/908dd19dabcca930d70c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验各有 gen0-gen3（共 4 代），**没有 Gen 4 数据**（每个文件只有 4 条记录，generation 0-3）。

### exp_007 (r=0.2)

| gen | log_det | eff_rank | ppl | d4 |
|-----|---------|----------|-----|-----|
| 0 | 2366.68 | 417.55 | 9.55 | 0.741 |
| 1 | 2367.46 | 476.73 | 10.28 | 0.674 |
| 2 | 2358.31 | 481.62 | 10.74 | 0.498 |
| 3 | 2362.52 | 486.54 | 11.14 | 0.467 |

### exp_008 (r=0.3)

| gen | log_det | eff_rank | ppl | d4 |
|-----|---------|----------|-----|-----|
| 0 | 2366.68 | 417.55 | 9.55 | 0.741 |
| 1 | 2366.13 | 476.91 | 10.19 | 0.689 |
| 2 | 2372.45 | 484.17 | 10.59 | 0.489 |
| 3 | 2386.72 | 489.48 | 10.90 | 0.465 |

两个实验最新数据只到 **gen3**，Gen 4 尚未生成。两者 gen0 完全一致（同一 base model），之后 r=0.3 的 log_det 在 gen3 出现上升趋势（2386.72 vs 2362.52），ppl 略低于 r=0.2（10.90 vs 11.14），d4 相近。

---
