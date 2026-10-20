# verify spider sql data quality

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_spider_sql_data_quality_20260520T221659_result.json`
- **Structured JSON:** [`e319b152e85d507a8574.json`](../../sessions/e3/e319b152e85d507a8574.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：数据可靠，论文可用

### 时间线确认

| 事件 | 时间 (UTC) |
|------|-----------|
| 代码最后修改（含 Bug 1/Bug 2 fix） | 20:47:22 |
| checkpoint.jsonl 创建 | 20:47:52 |
| checkpoint.jsonl 最后写入 | 21:38:13 |

数据在 bugfix 之后 30 秒开始生成。代码中明确标注了 `Bug 1 fix: failure modes aligned with NER cascade`（L484）和 `Bug 2 fix: degeneracy on EXECUTION RESULTS, not SQL text`（L467）。

### 一致性验证

用当前 `classify_failure_mode()` 逻辑对 196 条 valid 记录重算：**零 mismatch**。嵌入值与重算值完全一致。

### F1-F4 分布（论文可用）

| Mode | Count | Rate |
|------|-------|------|
| F1 degeneracy | 171 | 87.2% |
| F2 low agreement | 0 | 0.0% |
| F3 high agreement wrong | 16 | 8.2% |
| F4 selection gap | 0 | 0.0% |
| OK (no failure) | 9 | 4.6% |

### 附注

1. **F2=0**：所有非退化实例的 agreement 都 >= 0.5，说明 SQL 执行结果的一致性很高——要么退化（F1），要么高共识。
2. **F4 是死代码**：`classify_failure_mode()` 中 F4 检查 `greedy_correct and not mv_correct` 永远不会触发，因为 F3 已经捕获了所有 `not mv_correct` 的情况。当前数据中也确实没有 F4 候选（0 个 greedy 正确但 MV 错误的非退化高共识实例）。
3. **跨任务对齐**：SQL 用 `agreement < 0.5` 划分 F2/F3；RE 用 `kappa < 0.3`；NER frontier 实验没有逐实例 cascade 分类器（只有聚合诊断）。SQL 的定义自洽，但与 RE 的阈值不同——论文中需要注明各任务的阈值选择。

---
