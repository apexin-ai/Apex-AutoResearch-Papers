# paper experiments sync to docs

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiments-sync-to-docs_20260515T150400_result.json`
- **Structured JSON:** [`5ca734d3d4f03bf3afbe.json`](../../sessions/5c/5ca734d3d4f03bf3afbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都没有旧引用 key，这项检查通过。

对比两个文件后，**docs/paper 版本实际上比 artifacts 版本更完整**，不建议直接用 artifacts 覆盖：

| 方面 | artifacts 版本 | docs/paper 版本 |
|------|---------------|----------------|
| LaTeX 宏 | 不用（直接写 CLS/CWM） | 用 `\cls{}`, `\cwm{}`, `\pp{}`, `\fone{}` 等宏 |
| Analysis 段落 | 6 段 | 8 段（多了 relaxed matching, variance compression, precision/recall, majority voting） |
| 表格格式 | 简单 | `\resizebox` + per-seed 列 |
| Repo-level | 无 limitations 段 | 有 limitations 段 |
| Scaling 表 | 只有 Mean | 含 s42/s123/s456 列 |
| Label 命名 | `\label{ssec:...}` | `\label{sec:...}` |
| 引用命令 | `\citep` | `\cite` |
| lr 值 | 正确 | 正确 |

两个文件 lr 值都已经是正确的（$2{\times}10^{-4}$ function / $5{\times}10^{-5}$ repo），citation keys 也没问题。

**结论：docs/paper/experiments.tex 已经是更完整、格式更正确的版本，不需要从 artifacts 同步。** 覆盖反而会丢失内容并破坏编译。是否跳过这次同步？

---
