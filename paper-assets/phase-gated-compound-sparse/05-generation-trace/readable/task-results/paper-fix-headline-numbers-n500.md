# paper fix headline numbers n500

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_headline_numbers_n500_20260516T035841_result.json`
- **Structured JSON:** [`0979ce4087ab0e7ea3fb.json`](../../sessions/09/0979ce4087ab0e7ea3fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

abstract.tex、introduction.tex、conclusion.tex、results 表格中的数字一致。

## 修改清单

### abstract.tex
| 行 | 原文 | 新文 |
|---|------|------|
| 4 | `$0.32$` ... `$9.94$` | `$0.39$` ... `$8.48$` |
| 6 | `$0.048 \to 2.619$` | `$0.07 \to 3.16$` |

### introduction.tex
| 行 | 原文 | 新文 |
|---|------|------|
| 14 | `$0.32$` ... `$9.94$` | `$0.39$` ... `$8.48$` |
| 15 | `$0.048 \to 2.619$` | `$0.07 \to 3.16$` |
| 23 | `$0.32 \to 9.94$` | `$0.39 \to 8.48$` |
| 24 | `$0.048 \to 2.619$` | `$0.07 \to 3.16$` |

### paper_framing.md
| 位置 | 原文 | 新文 |
|------|------|------|
| Header (L3) | `DS median_diff 恢复 0.32/1.15/3.97/9.94` | `DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16` |
| Core Insight (L7) | `DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619` | `DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16` |
| Narrative Arc (L13) | `0.32→9.94` | `0.39→8.48` |
| C2 (L25) | `0.32→1.15→3.97→9.94` | `0.39→1.21→3.99→8.48` |
| Paper Positioning (L85) | `0.32→9.94` | `0.39→8.48` |

### 未修改（正确上下文）
- `conclusion.tex` — 已有 n=500 数字
- `results.tex` — 表格为 n=500 数据
- `appendix_*.tex` — n=500 表格或明确标注 n=50 spot check 的独立实验
- `discussion.tex` — 无 headline 数字

---
