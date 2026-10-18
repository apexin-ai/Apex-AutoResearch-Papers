# ops llama3 status urgent

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3_status_urgent_20260516T101159_result.json`
- **Structured JSON:** [`23249d1528e76b1e3748.json`](../../sessions/23/23249d1528e76b1e3748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cross_scale_llama3_8b_003 状态：已完成 ✓

Pipeline 于 **17:25 CST** 正常结束，GPU 已释放（0MiB / 0%）。

### 关键指标

| 指标 | 值 |
|------|-----|
| **4-class acc** | **0.702** [0.683, 0.724] |
| **6-class acc** | **0.554** [0.536, 0.571] |
| **EDD estimate** | **>5** |

### Pairwise AUC（consecutive binary）

| 对比 | Acc | AUC |
|------|-----|-----|
| d0v1 | 0.885 | 0.949 |
| d1v2 | 0.810 | 0.877 |
| d2v3 | 0.698 | 0.771 |
| d3v4 | 0.656 | 0.716 |
| d4v5 | 0.583 | 0.618 |

模型：Meta-Llama-3.1-8B-Instruct，策略：nucleus_p0.95，每深度 500 样本。AUC 随深度递增单调下降，符合预期。cuda:0 当前空闲可用。

---
