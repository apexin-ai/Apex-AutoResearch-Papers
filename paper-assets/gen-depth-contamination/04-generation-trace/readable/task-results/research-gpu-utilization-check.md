# research gpu utilization check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gpu_utilization_check_20260512T124716_result.json`
- **Structured JSON:** [`130937684823245b7bd1.json`](../../sessions/13/130937684823245b7bd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/gpu_optimization_report.txt`。核心发现：

**当前状态**: GPU 利用率 45%，显存仅用 3.9GB/24GB (16%)，严重浪费。

**根因**: batch_size=16 (生成) / feat_batch_size=8 (特征提取) 远低于 4090D 能承载的上限。

**推荐参数 (full study)**:
| 阶段 | 当前 | 推荐 |
|------|------|------|
| Step 3 生成 | batch_size=16 | **64** (保守) 或 128 |
| Step 4 特征提取 | feat_batch_size=8 | **24** (保守) 或 32 |

**必须修复**: `tokenizer.padding_side = "left"` — 当前每个 batch 都在报 right-padding 警告，影响生成质量。

**预估节省**: Step 3 ~57min + Step 4 ~17min ≈ **总共节省 ~74 min (38%)**。加上 flash-attn 可能再多 10-15%。

---
