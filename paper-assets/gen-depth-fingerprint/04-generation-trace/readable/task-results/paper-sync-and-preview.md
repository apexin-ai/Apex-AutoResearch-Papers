# paper sync and preview

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_sync-and-preview_20260525T080200_result.json`
- **Structured JSON:** [`83b5a64b320f348b5c88.json`](../../sessions/83/83b5a64b320f348b5c88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

同步完成。汇报如下：

### 已同步的文件（8 个 tex，两份副本均已更新）

| 文件 | 关键变化 |
|------|---------|
| `main.tex` | appendix 章节重排（Confusion Matrix 和 Classifier Sensitivity 顺序互换等）；新增若干 `\FloatBarrier` |
| `introduction.tex` | 全段加 `\looseness=-1` 压缩行距；entropy 注脚从 inline 改为 `\footnote{}`；QLoRA 加 `\cite{qlora}` 和 "(within-model 5-fold CV)"；图 caption 颜色描述从 "blue/amber" 改为 "red/blue"；匿名 repo URL 更新 |
| `related_work.tex` | 微调措辞（"novel OOD framing" 简化）；段落加 `\looseness=-1` |
| `method.tex` | 特征表 caption 精简；feature 名加 `\textit{\scriptsize(NLL)}` 标注；新增 **fig2_framework** 图；生成链段落加 `\looseness=-1`；Classifier 段新增 hyperparameter sensitivity 说明；CI 展开为 "confidence intervals" |
| `results.tex` | 转移矩阵图 caption 大幅精简；新增 **Error analysis** 段落（错误率按深度递减分析）；baseline 表 caption 精简；所有段落加 `\looseness=-1`；图 caption 颜色从 blue/amber/wine → red/blue/purple；"SD" → "std. dev."；TOST 展开为 "two one-sided tests" |
| `discussion.tex` | 重写为更紧凑结构：原 "DDR reflects..." 改为假设性表述（shape stability 可能源于 architectural constraints）；新增 **Temperature sensitivity** 段；Error structure 段大幅压缩；Robustness 段重组为 **Scope and applications**；新增 5-class resolution limit 结论 |
| `conclusion.tex` | 加 `\vspace{-1mm}`；措辞精简 |
| `limitations.tex` | 微调措辞（QLoRA 加 "within-model"） |

### PDF 预览图
路径：`artifacts/_project/paper/_pdf_images/main_p{1-8}.png`（8 页，200dpi）

---
