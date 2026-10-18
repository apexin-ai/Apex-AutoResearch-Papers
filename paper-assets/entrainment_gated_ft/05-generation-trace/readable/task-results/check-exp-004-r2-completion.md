# check exp 004 r2 completion

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp-004-r2-completion_20260519T171608_result.json`
- **Structured JSON:** [`1b1eec37ff24d26fb981.json`](../../sessions/1b/1b1eec37ff24d26fb981.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron 监控任务，无需清除。

---

**exp-004-r2 总结**：

| 项目 | 状态 |
|------|------|
| **状态** | DONE (success) |
| **耗时** | ~30 min（00:45 → 01:14 CST） |
| **输出** | 3×.pt (~126MB each) + 3×.csv (~59MB each) + 3 分析文件 |
| **GPU** | 空闲（0% util），可释放给 exp-007 |

**核心发现**：假设被否定——attention entropy **无法**区分 helped 与 hurt 样本（三个架构的差异均 <0.02）。Per-example effect 不体现在 attention pattern 层面。

**跨架构相似度**有意思：GDN 和 RetNet 全层高度相似（>0.9），HGRN2 在浅层（L2）与另外两者差异大（cos sim ~0.2），但深层收敛到 >0.94。这意味着三个架构在深层学到了相似的 attention pattern，分化主要在浅层。

---
