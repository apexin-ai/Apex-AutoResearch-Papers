# ops check v3 status

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_v3_status_20260512T225743_result.json`
- **Structured JSON:** [`ad885e862b1168e85c22.json`](../../sessions/ad/ad885e862b1168e85c22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v3 实验状态报告

| 项目 | 状态 |
|------|------|
| **进程** | 存活，已运行 5h21m |
| **GPU 5** | 利用率 100%，显存 9311/24564 MiB |
| **当前阶段** | Phase B → ACDC 方法，τ=0.01（第 1/5 个阈值） |
| **ACDC 进度** | 20399/32491 edges（62.8%），~5.5 it/s |
| **当前 τ ETA** | ~36 min |

**已完成**：
- Phase A: EAP-IG（32491 edges scored，已缓存）
- Phase B: edge_pruning（32491 edges scored，已缓存）

**剩余工作**：当前 τ=0.01 还需 ~36 min，之后还有 4 个 τ 值要跑。若每个 τ 耗时相近（~70 min），ACDC 总计还需约 **5 小时**。

**状态**：正常运行，无异常。

---
