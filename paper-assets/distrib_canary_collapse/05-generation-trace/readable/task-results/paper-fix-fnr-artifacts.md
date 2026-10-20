# paper fix fnr artifacts

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_fnr_artifacts_20260516T002749_result.json`
- **Structured JSON:** [`c4a55926a75c1c9273f7.json`](../../sessions/c4/c4a55926a75c1c9273f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All remaining 25% instances are about TY significance rate (4/16 = 25.0%) or other method statistics — none are about TY FNR. No further fixes needed.

**修改报告：**

| 位置 | 修改 |
|------|------|
| `experiments.tex:173` | TY FNR 25% → 33.3%（正文描述） |
| `experiments.tex:191` | TY FNR 25% → 33.3%（Table 1 数据） |

**确认无需修改：**
- `experiments.tex:55, 78` — 25% 指的是 TY 显著性率（4/16），不是 FNR
- `method.tex:100` — 已经是 33.3%
- `discussion.tex:27` — 已经是 33.3%
- 其他文件中的 25% 均为方法显著性率，与 FNR 无关

---
