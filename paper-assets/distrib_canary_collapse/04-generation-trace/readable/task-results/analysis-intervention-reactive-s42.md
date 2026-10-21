# analysis intervention reactive s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_intervention_reactive_s42_20260518T145214_result.json`
- **Structured JSON:** [`e94d4fc86f84278f1edb.json`](../../sessions/e9/e94d4fc86f84278f1edb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果总结：

**Reactive intervention 成功阻止了 model collapse。**

| 关键事件 | 数值 |
|---------|------|
| 触发时机 | Gen 2（distinct_1 下降 15.58%） |
| 峰值损伤 | ppl=157.09（基线 5.8x），entropy 从 3.23→1.48 |
| 恢复时间 | 2 代（gen 4 完全恢复） |
| 最终 distinct_1 | 0.0844（-14.1% drift），vs 无干预 0.0704（-28.3%） |
| 最终 ppl | 21.24（-21.2% drift），vs 无干预 1003.73（+3624.6%） |

**关键发现**：干预后模型收敛到 α=0.0（纯真实数据）baseline，两者差异 <1%。说明 2 代 α=1.0 污染未造成永久性损伤，但 reactive 方式的局限在于：
1. distinct_1 是**滞后指标**（gen 1 entropy 已跌 41%，但 distinct_1 仅跌 0.7%）
2. 模型在触发前已经历严重瞬时损伤（ppl 飙到 157）
3. 最终等价于完全不用合成数据

这为 predictive（canary-based）干预提供了对比基线：如果 canary 能在 gen 1 甚至更早触发，就可以避免 ppl=157 的瞬时损伤。

报告已注册，registry 已更新为 DONE/success。

---
