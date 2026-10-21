# writing related work audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-audit_20260514T045022_result.json`
- **Structured JSON:** [`e99ae4b182d76dc1ee3b.json`](../../sessions/e9/e99ae4b182d76dc1ee3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成，结果已写入 `artifacts/drafts/related_work_audit.md`。

核心发现：

| 类别 | 状态 |
|------|------|
| Model collapse | 充分（8篇） |
| Binary detection | 充分（8篇） |
| Data selection | 充分（4篇） |
| Watermarking | 充分 |
| Ordinal classification | 偏薄（仅 CORAL 1篇） |
| **Probing classifiers** | **缺失** |

**最高优先级缺口**：neural probe 实验在 discussion.tex 和 conclusion.tex 中大量讨论，但 Related Work 完全没有 probing classifiers 文献支撑。建议新增段落引用 Alain & Bengio (2017)、Conneau et al. (2018)、Belinkov (2022)。

次优先级：补 Frank & Hall (2001) 加强 ordinal classification 段落，可选补 Fast-DetectGPT 和 Gerstgrasser et al. (2024)。详细建议文本和插入位置见审查文件。

---
