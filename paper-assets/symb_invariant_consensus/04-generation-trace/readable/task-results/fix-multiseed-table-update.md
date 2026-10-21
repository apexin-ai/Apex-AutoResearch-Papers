# fix multiseed table update

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_multiseed-table-update_20260522T233652_result.json`
- **Structured JSON:** [`1710a0944619f1882dca.json`](../../sessions/17/1710a0944619f1882dca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，27页，无错误。

### 产出汇总

**appendix.tex — 多种子表 (tab:multi-seed)**

新增两组数据，表格现为 4 个条件：

| 条件 | 新增行 |
|------|--------|
| Mistral-7B × PW-D5 (n=600) | 4 seeds (42/123/456/789), Mean Δ = −2.38±1.12, 4/4 Δ≤0 |
| LLaMA-3.1-8B × FOLIO (n=204) | 3 seeds (123/456/789), Mean Δ = −0.98±2.25 |

表格标题更新为：*"Three of four conditions show consistent Δ≤0 across all seeds; Mistral-7B × FOLIO is the exception (+0.16±2.70 pp)."*

**experiments.tex — 叙事（L57）**

旧：*"Three-seed replication on Mistral-7B confirms seed-level noise: two of three seeds produce null or negative Δ (mean +0.16±2.70 pp; Table)"*

新：*"Four-seed replication on Mistral-7B × ProofWriter (Δ̄=−2.38±1.12 pp, 4/4 seeds Δ≤0) and three-seed replication on LLaMA-3.1-8B × FOLIO (Δ̄=−0.98±2.25 pp) confirm that the SICA≤SC pattern is stable across seeds, models, and datasets (Table)"*

Qwen2.5-14B × FOLIO 四种子句保持不变。

---
