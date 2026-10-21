# ssh 5090c check n16 data exists

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_check_n16_data_exists_20260521T144452_result.json`
- **Structured JSON:** [`ba75dbeba105b9502d4c.json`](../../sessions/ba/ba75dbeba105b9502d4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. FewNERD N=16 s456

**autodl-5090-c** — **存在** ✓

| 项 | 值 |
|---|---|
| 路径 | `output/fewnerd_n16_seed456_v2/` |
| samples.jsonl | 1.28 GB, 37648 行, May 21 19:01 |
| report.json | 1.6 KB, May 21 19:02 |
| greedy_f1 | 0.7883 |
| oracle_f1 | 0.9058 |
| soft_jaccard rho (full) | 0.2851 |
| verdict | FAIL |

**autodl-5090** — 不存在（无 fewnerd n16 s456 匹配）

### 2. SciERC N=16 s42

**autodl-5090-c** — **存在** ✓

| 项 | 值 |
|---|---|
| 路径 | `output/scierc_n16_s42/` |
| samples.jsonl | 37.3 MB, 551 行, May 21 19:46 |
| report.json | 1.7 KB, May 21 19:46 |
| greedy_f1 | 0.6631 |
| oracle_f1 | 0.8086 |
| soft_jaccard rho (full) | 0.3695 |
| verdict | MARGINAL |

**autodl-5090** — 不存在（无 scierc n16 s42 匹配；有 `scierc_n16_s456` 是另一个 seed）

### 结论

两个实验数据**都在 autodl-5090-c 上完好存在**，不需要重跑。附带注意：`fewnerd_n16_s123` 目录在 autodl-5090-c 上是空的（仅创建了目录，无文件）。

---
