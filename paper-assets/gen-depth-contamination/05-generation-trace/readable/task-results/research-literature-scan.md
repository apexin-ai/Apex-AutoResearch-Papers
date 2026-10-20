# research literature scan

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260514T061524_result.json`
- **Structured JSON:** [`4a4d2e27147332ce9176.json`](../../sessions/4a/4a4d2e27147332ce9176.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`literature_map.yaml` 已更新，新增 3 篇论文：

| ID | 标题 | 日期 | 类别 | 角色 |
|---|---|---|---|---|
| `falahati2026curated` | Curated Synthetic Data Doesn't Have to Collapse | 2026-05-08 | model-collapse | background |
| `mady2026feataugmented` | Feature-Augmented Transformers for Robust AI-Text Detection | 2026-05-05 | detection | method-component |
| `pu2026generator` | Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection | 2026-04-15 | detection | method-component |

**K\*=2 universality 相关性**：本轮扫描未发现直接挑战或支持 K\*=2 claim 的论文。三篇新论文均为 binary detection 或 collapse prevention，无一涉及多代深度估计或代际可区分性饱和边界。该领域目前仍无竞品直接做 ordinal depth estimation。

**值得关注**：
- Falahati et al. 的 pluralistic curation 与我们的 depth-based graduated filtering 正交且可能互补
- Pu et al. 的 disentangled representation（分离语义 vs generator artifact）架构思路可迁移至 depth encoder 设计

---
