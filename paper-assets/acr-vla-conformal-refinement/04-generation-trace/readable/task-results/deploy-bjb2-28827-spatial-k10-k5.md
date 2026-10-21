# deploy bjb2 28827 spatial k10 k5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-spatial-k10-k5_20260519T152123_result.json`
- **Structured JSON:** [`96541ba054d8e31530bb.json`](../../sessions/96/96541ba054d8e31530bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 状态有问题，需要汇报：

| GPU | Utilization | Memory Used | 状态 |
|-----|------------|-------------|------|
| cuda:0 | 19% | 2861 MiB | **未空闲** |
| cuda:1 | 17% | 1906 MiB | - |
| cuda:2 | 99% | 3931 MiB | **繁忙** |
| cuda:3 | 0% | 1 MiB | 空闲 ✓ |
| cuda:4 | 17% | 1972 MiB | - |
| cuda:5 | 24% | 2559 MiB | **未空闲** |

目标 GPU 中只有 **cuda:3 空闲**。cuda:0 (19%), cuda:2 (99%), cuda:5 (24%) 均有负载，超过 10% 阈值。

是否继续在这些 GPU 上部署？还是需要先排查占用进程？

---
