# research provenance and stats prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_provenance-and-stats-prep_20260515T173752_result.json`
- **Structured JSON:** [`ae7d5de047abf2b68e17.json`](../../sessions/ae/ae7d5de047abf2b68e17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

**任务 1**: Provenance 补全 36/36。缺失项是 **C177**（"ISR is mathematically sensitive to component count (premise count bias)"），`evidence: []` → 添加了 plan002-additive-b01-s42 和 plan018-additive-random-b01-s42 作为证据（D051 premise-count confound 分析的底层数据来源）。

**任务 2**: 统计量重算 checklist 已写入 `artifacts/stats_recalc_checklist.md` 并注册（art_20260515_2e14c3）。覆盖 5 项统计量：pooled genuine rate、Fisher exact test (两种场景)、Wilson CI、H7/H1/H8 分布汇总、premise-count-matched 1.06x 是否需更新。依赖 s43-r3（RUNNING）和 s44-r2（ALLOCATED）完成后的 eval 数据。

---
