# ACL 模板对齐审计

**日期**: 2026-05-25
**官方模板来源**: https://github.com/acl-org/acl-style-files (latest commit)
**我们的论文**: `/tmp/anon_repo_check/paper/` (匿名仓库)

---

## (a) 差异列表

| # | 文件 | 差异描述 | 官方 | 我们 |
|---|------|----------|------|------|
| 1 | `acl.sty` | 无差异 | — | 与官方完全一致 |
| 2 | `acl_natbib.bst` | 无差异 | — | 与官方完全一致 |
| 3 | `main.tex` | `inconsolata` 包被注释掉 | `\usepackage{inconsolata}` | `% \usepackage{inconsolata} % unavailable locally; re-enable for submission` |
| 4 | `main.tex` | 额外包: `booktabs` | 无 | `\usepackage{booktabs}` |
| 5 | `main.tex` | 额外包: `amsmath,amssymb` | 无 | `\usepackage{amsmath,amssymb}` |
| 6 | `main.tex` | 额外包: `xcolor` | 无（acl.sty 内部已加载） | `\usepackage{xcolor}`（重复但无害） |
| 7 | `main.tex` | 额外包: `subcaption` | 无 | `\usepackage{subcaption}` |
| 8 | `main.tex` | 额外包: `tikz` + `arrows.meta,positioning` | 无 | `\usepackage{tikz}` + `\usetikzlibrary{arrows.meta,positioning}` |
| 9 | `main.tex` | `\documentclass` 选项 | `[11pt]{article}` | `[11pt]{article}` — 一致 |
| 10 | `main.tex` | `\usepackage[review]{acl}` | `[review]{acl}` | `[review]{acl}` — 一致 |
| 11 | `main.tex` | `\usepackage{times}` | 有 | 有 — 一致 |
| 12 | `main.tex` | `\usepackage{latexsym}` | 有 | 有 — 一致 |
| 13 | `main.tex` | `\usepackage[T1]{fontenc}` | 有 | 有 — 一致 |
| 14 | `main.tex` | `\usepackage[utf8]{inputenc}` | 有 | 有 — 一致 |
| 15 | `main.tex` | `\usepackage{microtype}` | 有 | 有 — 一致 |
| 16 | `main.tex` | `\usepackage{graphicx}` | 有 | 有 — 一致 |

## (b) 修复方式

| # | 处理 | 原因（如保留） |
|---|------|----------------|
| 1 | 无需修复 | acl.sty 与官方一致 |
| 2 | 无需修复 | acl_natbib.bst 与官方一致 |
| 3 | **已修复**: 取消注释，启用 `\usepackage{inconsolata}` | 对齐官方模板 |
| 4 | 保留 | 论文表格使用 `\toprule`/`\midrule`/`\bottomrule`，为内容必需包 |
| 5 | 保留 | 论文使用数学公式（OR、p值等），为内容必需包 |
| 6 | 保留 | 虽然 acl.sty 内部已加载 xcolor，显式声明不产生冲突（LaTeX 自动跳过重复加载），且论文中使用了 `\textcolor` 等命令 |
| 7 | 保留 | 论文使用 `\subcaption` 环境排列子图，为内容必需包 |
| 8 | 保留 | 论文使用 TikZ 绘制 DAG 因果图（Figure 2），为内容必需包 |

## (c) 页数

- **对齐前正文页数**: 8（Conclusion 在第 8 页右栏结束）
- **对齐后正文页数**: 8（Conclusion 在第 8 页右栏结束）
- **调整措施**: 无需调整。添加 inconsolata 仅影响等宽字体渲染，不改变排版间距。
- **总页数**: 20（正文 8 页 + Limitations 在第 8 页底部 + References 第 9-10 页 + Appendix 第 10-20 页）
- **Limitations 位置**: 第 8 页右栏底部（不计入正文页数）

## (d) 编译状态

- **error 数量**: 0
- **warning 数量**: 10
  - 8 个 `'h' float specifier changed to 'ht'`（标准浮动位置调整，无害）
  - 2 个 `hyperref: Token not allowed in a PDF string (Unicode): removing 'math shift'`（Appendix 标题含 `$` 符号导致 PDF 书签警告，无害）
- **undefined reference**: 无
- **undefined citation**: 无

## (e) 修改文件清单

| 文件 | 修改内容 |
|------|----------|
| `main.tex` | 第 10 行: `% \usepackage{inconsolata}` → `\usepackage{inconsolata}` |
| `acl.sty` | 无修改（与官方一致） |
| `acl_natbib.bst` | 无修改（与官方一致） |

## (f) 结论

模板文件（acl.sty、acl_natbib.bst）与 ACL 官方仓库完全一致，无任何差异。main.tex preamble 唯一偏差是 `inconsolata` 包被注释掉，已修复。其余额外包（booktabs、amsmath、xcolor、subcaption、tikz）均为论文内容所需，属于合理添加。正文恰好 8 页，符合 EMNLP 2026 页数限制。
