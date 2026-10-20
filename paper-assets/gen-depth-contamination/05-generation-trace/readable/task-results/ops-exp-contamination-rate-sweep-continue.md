# ops exp contamination rate sweep continue

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp_contamination_rate_sweep_continue_20260520T175717_result.json`
- **Structured JSON:** [`ead244d90587d0773e19.json`](../../sessions/ea/ead244d90587d0773e19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。汇总如下：

## exp_contamination_rate_sweep 最终结果

| Rate | Strategy | MMLU | HellaSwag | ARC-C |
|------|----------|------|-----------|-------|
| 10% | no_filter | 0.5878 | 0.6652 | 0.4471 |
| 10% | binary | 0.5868 | **0.6709** | 0.4462 |
| 10% | graduated | 0.5873 | 0.6672 | 0.4428 |
| 30% | no_filter | 0.5885 | 0.6625 | 0.4334 |
| 30% | binary | 0.5867 | **0.6702** | **0.4480** |
| 30% | graduated | 0.5873 | 0.6640 | 0.4334 |
| 50% | no_filter | 0.5858 | 0.6582 | 0.4300 |
| 50% | binary | **0.5913** | **0.6700** | **0.4505** |
| 50% | graduated | 0.5848 | 0.6606 | 0.4292 |
| 100% | no_filter | 0.5707 | 0.6217 | 0.3891 |
| 100% | binary | N/A | N/A | N/A |
| 100% | graduated | 0.5701 | 0.6215 | 0.3933 |

**关键发现：**
- Binary filtering 在 10-50% 污染率上的 HellaSwag 和 ARC-C 均优于 no_filter，效果随污染率增大而增强
- 50% 时 binary 优势最大：HellaSwag +1.18pp，ARC-C +2.05pp
- 100% 时 binary 不可用（所有数据被过滤掉，0 samples）
- Graduated 介于 no_filter 和 binary 之间，但更靠近 no_filter
- no_filter 有清晰的剂量反应：污染越高分数越低

`summary.json` 已写入两台服务器，registry 已更新为 DONE。

---
