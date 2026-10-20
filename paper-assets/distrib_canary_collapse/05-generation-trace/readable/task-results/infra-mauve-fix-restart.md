# infra mauve fix restart

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mauve-fix-restart_20260514T062820_result.json`
- **Structured JSON:** [`196c9dc595a2fbf9b06a.json`](../../sessions/19/196c9dc595a2fbf9b06a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`rep_42` 和 `rep_43` 已删除。剩下 `rep_42_v1_partial` 和 `rep_43_v1_partial` 是之前的旧数据，不在清理范围内。

### 汇报

| 项目 | 状态 |
|------|------|
| metrics.py 修复 | 第 248 行 `compute_mauve` 的 `max_samples=500` → `2000`，`compute_distinct_n`(第92行) 保持 500 不变 |
| 进程 kill | 无残留 python/train 进程，ALL_CLEAN |
| GPU | 空闲，无占用 |
| 输出目录清理 | `results/mvp/rep_42` 和 `rep_43` 已删除（`rep_42_v1_partial`、`rep_43_v1_partial` 为旧数据，保留） |

**可以安全重启实验。**

---
