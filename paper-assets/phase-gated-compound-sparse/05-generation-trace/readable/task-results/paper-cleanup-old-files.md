# paper cleanup old files

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_cleanup-old-files_20260514T130953_result.json`
- **Structured JSON:** [`2f2b54a4ec6dc9db96c7.json`](../../sessions/2f/2f2b54a4ec6dc9db96c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。结论：

## 结果

### 旧 tex 文件
**不需要删除任何文件** —— `results_5_1.tex`、`*_fc6d1d.tex`、`*_4cc5f3.tex`、`*_old.tex`、`*_backup.tex` 均不存在。这些文件已经在之前被清理过了。

### Figure 副本目录状态

论文正式使用 `paper/figures/`（通过 `\graphicspath{{figures/}}`），论文中引用了 4 个图：
- `fig1_dose_response.pdf`
- `fig3_crossover.pdf`
- `fig4_bootstrap.pdf`
- `fig5_crossmodel.pdf`

3 个副本目录的状态：

| 目录 | 文件数 | 说明 |
|------|--------|------|
| `figures/` | 26 图 + 3 生成脚本 | 最全的副本，包含所有旧版图（severity_gradient, crossover_heatmap 等）和生成脚本 |
| `paper_figures/` | 10 图 + 1 json | 子集副本，含 `canonical_bf16_stats.json` |
| `analysis/figures/` | 4 图 + 4 脚本 + 4 b64 | 分析脚本的输出目录，含 `.b64` 中间文件 |

这些副本目录未删除（可能有生成脚本依赖它们）。

### paper/ 最终文件树

```
paper/
├── main.tex          # 主文件
├── main.pdf          # 编译产出
├── abstract.tex
├── introduction.tex
├── related_work.tex
├── background.tex
├── methodology.tex
├── results.tex
├── analysis.tex
├── discussion.tex
├── conclusion.tex
├── appendix.tex
├── appendix_results.tex
├── appendix_disc_analysis.tex
├── references.bib
├── acl.sty
├── acl_natbib.bst
├── inconsolata.sty
├── figures/           # 26 图 (pdf+png)
└── _pdf_images/       # 11 页预览 png
```

### 其他可清理内容

`paper/_pdf_images/` 目录（11 张页面截图）是临时预览文件，非论文编译必需，可以考虑删除。是否清理？

---
