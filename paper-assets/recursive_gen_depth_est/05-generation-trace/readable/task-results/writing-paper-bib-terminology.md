# writing paper bib terminology

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-bib-terminology_20260515T145355_result.json`
- **Structured JSON:** [`f204777d759cc274bf04.json`](../../sessions/f2/f204777d759cc274bf04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改已验证正确。

---

## 汇总报告

### 任务 1: Bibliography 扩充

| 指标 | 值 |
|------|-----|
| 修改前条目数 | 38 |
| 修改后条目数 | **40** |
| 新增 | `liang2023helm` (HELM, TMLR 2023), `hendrycks2021mmlu` (MMLU, ICLR 2021) |
| Orphan entries | **0**（修改前后均无） |
| 必需子领域覆盖 | 全部 10 类 ✓ |

新引用在 `related_work.tex` Adjacent Tasks 段落中引用，定位为 benchmark 方法论先例。

### 任务 2: 术语一致性

| 变体 | 统一为 | 文件 | 替换数 |
|------|--------|------|--------|
| "recursion depth" | "generation depth" | related_work.tex:6 | 1 |
| "recursive depth signals" | "generation depth signals" | related_work.tex:30 | 1 |
| "recursive depth itself" | "generation depth itself" | related_work.tex:35 | 1 |
| "hand-crafted features" | "statistical features" | section_appendix.tex:22 | 1 |
| "sampling methods" | "decoding strategies" | method.tex:24 | 1 |

**无需修改的术语**（已全文一致）：
- "model family" — 唯一用法，无 "model architecture" 变体
- "GPT-2 XL" / "GPT-2~XL" — 仅 `~` vs 空格差异，渲染结果相同
- "nucleus sampling" — 无 "top-p sampling" 变体
- "temperature sampling" — 无 "temperature scaling" 变体
- "decoding strategy" — 已为主导术语（修复了 method.tex 1 处 "sampling methods"）
- "AUC" / "pairwise AUC" — 语义不同，前者泛指后者特指 EDD 计算，无冲突

---
