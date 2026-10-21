# fix algo1 and bib

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_algo1-and-bib_20260514T085846_result.json`
- **Structured JSON:** [`d85cdbfb82100f79e48a.json`](../../sessions/d8/d85cdbfb82100f79e48a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处改动完成：

1. **method.tex L118** — Algorithm 1 伪代码从按结构数量比例 `bottom-⌊s·|H|⌋` 改为按参数量预算贪心：`structures with lowest S(h) s.t. Σ params(h) ≥ s·|θ|`，与 prune.py 实际逻辑一致。

2. **references.bib `lachance2024cka`** — year: `2022` → `2024`

3. **references.bib `paser2025`** — 添加 `note={Under review}`

---
