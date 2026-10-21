# research irt data inventory

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_irt-data-inventory_20260516T003209_result.json`
- **Structured JSON:** [`f8b3a96afda81834c25a.json`](../../sessions/f8/f8b3a96afda81834c25a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

盘点完成。结果摘要：

**当前可用 IRT pooling 数据点：N=35**（含 0.5B）/ **N=23**（仅 1.5B+3B）

| Scale | Aligned | Para_aligned | 小计 |
|-------|---------|-------------|------|
| 0.5B  | 8/8 ✅  | 4/8         | 12   |
| 1.5B  | 8/8 ✅  | **8/8 ✅** (NEW) | 16   |
| 3B    | 4/8     | 3/8         | 7    |

关键变化（vs 上次 N=19）：
- **1.5B para_aligned s123 ×4 全部完成**（+4）
- 0.5B 首次纳入计数（+12）
- 3B d000_s42 SFT 重训已完成（今天 08:03），**等待 eval 提交**

3B 瓶颈：s42 全线阻塞（d000 需 eval、d005 重训中、d025 eval 中、d100 SFT 中）。预计 EMNLP 截稿前可达 **N≈38-42**。

---
