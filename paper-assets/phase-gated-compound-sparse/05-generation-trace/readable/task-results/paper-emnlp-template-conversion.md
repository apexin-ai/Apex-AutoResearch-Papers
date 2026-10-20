# paper emnlp template conversion

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_emnlp-template-conversion_20260514T104702_result.json`
- **Structured JSON:** [`a1982b8a6ae8f4b5e0ff.json`](../../sessions/a1/a1982b8a6ae8f4b5e0ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's the summary:

---

## 完成情况

### 已完成
1. **ACL style files** — 从 GitHub 下载 `acl.sty` + `acl_natbib.bst` 到 paper 目录
2. **main.tex 改造** — `\usepackage[review]{acl}` (anonymous)，移除冗余包（geometry/natbib/hyperref/xcolor 由 acl.sty 提供），移除重复的 `\bibliographystyle`
3. **Appendix 创建** — `appendix.tex` 包含 `\label{app:multiplicative-null}` 和 `\label{app:bootstrap-details}`，解决了所有 `??` 引用
4. **表格适配** — Table 2 (main-results, 7列) 和 Table 5 (cohens-d) 改为 `table*` 跨双栏；Table 3 (cross-model) 缩短模型名
5. **旧文件清理** — 删除 `_archive/results_5_1.tex`
6. **编译验证** — 服务器上 4 次编译（pdflatex + bibtex + 2×pdflatex）成功，**零 Warning、零未定义引用**

### 编译结果
- PDF: `/root/autodl-tmp/pacs/paper/main.pdf` (westd-22162)
- **17 页**，双栏，带行号 (review mode)
- 1 个 Overfull hbox (4.19pt，可忽略)

### 页数问题 (需要处理)

**Main body ≈ 15 页，超出 8 页限制约 7 页。** 建议可移到 appendix 的内容（按优先级排序）：

| 内容 | 预估节省 | 说明 |
|------|---------|------|
| §7 Discussion 中的 Limitations (§7.1) | ~2 页 | 5 个 limitation 段落很长，可精简后保留 1 段在 main body |
| §5.6 Statistical Validation（permutation test + effect size 细节）| ~1.5 页 | 主文保留结论句，表格移到 appendix |
| §5.5 Cross-Model Replication 细节 | ~1 页 | 主文保留 "qualitatively replicates" 总结句 |
| §6 Analysis 中 Entropy Redistribution (§6.2) | ~1 页 | Qwen-specific entropy 分析可移到 appendix |
| §4 Methodology 细节（phase segmentation、metrics 定义）| ~1 页 | 已在 §3 Background 定义过，有重复 |
| §5.1 Experimental Overview | ~0.5 页 | 与 §4 部分重叠 |

以上合计可释放 ~7 页，刚好满足 8 页限制。但这需要重写文本结构，**我未自行删减任何内容**。

---
