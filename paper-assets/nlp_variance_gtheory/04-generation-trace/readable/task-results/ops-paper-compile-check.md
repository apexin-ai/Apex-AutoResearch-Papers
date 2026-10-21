# ops paper compile check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_paper_compile_check_20260523T150422_result.json`
- **Structured JSON:** [`4d227650f8b9a491b37b.json`](../../sessions/4d/4d227650f8b9a491b37b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 编译检查报告

### 1. 编译状态
**成功** — 0 errors，PDF 生成正常（551KB）。

BibTeX 1 warning：`gao2024lmeval` 的 entry type 未在 bst 中定义（references.bib:496）。

### 2. 页数
| 区域 | 页码 | 页数 |
|------|------|------|
| 主文（Abstract → Conclusion） | 1–8 | **~7.5 页** |
| Limitations | 8 (下半) | ~0.5 页 |
| References | 9–11 | 3 页 |
| Appendix | 12–17 | 6 页 |
| **总计** | | **17 页** |

**主文 ≤ 8 页 ✅**（Conclusion 和 Limitations 都在第 8 页，Limitations 不计入页数限制）

Abstract：156 words ✅（限制 200 words）

### 3. Warning 统计
| 类型 | 数量 | 说明 |
|------|------|------|
| Underfull \hbox | 61 | 大部分 badness 10000，集中在 appendix 的 prompt 模板 |
| Underfull \vbox | 3 | 排版松散页 |
| Overfull \hbox | 5 | 见下 |
| Float specifier `h`→`ht` | 3 | 无害 |

### 4. Undefined citation/reference
**无** ✅ — 所有引用和标签均已解析。

### 5. Critical Warnings

**主文 Overfull hbox（1 处）：**
- `method.tex` lines 36–51：**37.2pt too wide**（page 4）— 可能是公式或表格溢出，建议检查

**Appendix Overfull hbox（4 处，优先级低）：**
- 82.0pt, 26.7pt, 13.1pt, 6.1pt — 均在 prompt 模板区域，monospace 文本难以自动断行

**BibTeX：** `gao2024lmeval` entry type 非标准（可能用了 `@software` 或自定义类型），建议改为 `@misc`。

---
