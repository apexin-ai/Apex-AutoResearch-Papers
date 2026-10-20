# analysis r3 intervention threshold sensitivity

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r3_intervention_threshold_sensitivity_20260520T155337_result.json`
- **Structured JSON:** [`151981961ce29d4159ab.json`](../../sessions/15/151981961ce29d4159ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/intervention_threshold_sensitivity.json`。

核心结论：**结论对 threshold 不敏感。**

- α=1.0 时 gen 1 的 entropy drop = 40.7%，远超所有 5 个 threshold（5%-25%），因此 5 个 threshold 全部在 gen 1 触发，产生完全相同的干预轨迹（peak PPL 57.0 → final PPL 21.3，vs 无干预 collapse 到 15,024）
- 跨 α 分析：threshold 10%-20% 功能等价（检测 α≥0.50，零误报）；25% 稍保守（漏掉 α=0.50）；5% 过敏（在 null 数据上误报）
- 15% threshold 位于 [10%, 22%] 安全操作区间的中心，不是 fragile post-hoc 选择而是一个 broad plateau 上的稳健选取

---
