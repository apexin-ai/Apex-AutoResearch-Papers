# research paper data aggregation

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-data-aggregation_20260525T202620_result.json`
- **Structured JSON:** [`8498ae67eb6c6381988c.json`](../../sessions/84/8498ae67eb6c6381988c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成 `factorial_data_summary.md` 并注册为 artifact。关键发现：

**V2 已完成数据**：
- Cell 2 (Full OCC LN): 3 seeds, CAR=0.743±0.024, TSR=0.897±0.032
- Cell 4 (Detach LN): 3 seeds, CAR=0.765±0.023, TSR=0.901±0.016
- Cell 1 (Full OCC BN): 仅 1 seed (CAR=0.746)
- Cell 3 (Detach BN): 0 seeds (3 个在跑)

**最大瓶颈**: Cell 1 (Full OCC BN) 当前 RUNNING 全部完成后也只有 2 seeds，不够 3-seed 平衡 ANOVA。需要再安排 1 个 seed (~17h)。

**初步观察** (v2 已有数据): Full OCC LN CAR(0.743) ≈ Full OCC BN CAR(0.746)，Detach LN CAR(0.765) 反而最高——gradient OFF + LN 组合在 v2 下表现最好，与 v1 时代的叙事相反。不过 Cell 1 仅 1 seed，需更多数据确认。

---
