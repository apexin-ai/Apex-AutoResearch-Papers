# paper fig2 entropy min check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig2-entropy-min-check_20260523T024336_result.json`
- **Structured JSON:** [`9c9620b93c61838f3fb6.json`](../../sessions/9c/9c9620b93c61838f3fb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复确认完成。

**汇报：**

| 项目 | 结果 |
|------|------|
| **entropy_min 原分组** | `C_INTER`（Intermediate，绿色 `#6C8C3C`）— 错误 |
| **需要修复** | 是 |
| **修改内容** | 4 处变更（两份脚本各 4 处）：&lt;br>1. entropy_min 颜色 `C_INTER` → `C_STAT`（蓝色 `#2471A3`）&lt;br>2. entropy_std 与 entropy_min 行序对调（entropy_std 提前至 index 3，entropy_min 下移至 index 4）&lt;br>3. 分组分隔线 `[2.5, 4.5]` → `[2.5, 3.5]`&lt;br>4. group_defs: Intermediate `(3,4)` → `(3,3)`；Stationary → Near-stationary `(4,6)`&lt;br>附加：`pdf.fonttype=42`, `ps.fonttype=42` |
| **Type 3 字体** | 无（全部 CID TrueType） |
| **新 PDF 路径** | `artifacts/_project/paper/figures/fig2_framework.pdf` 及 `docs/chart/`、`docs/paper/figures/`、`docs/paper/chart/`、`docs/paper/`、`artifacts/_project/chart/` 均已同步 |

---
