# research corl2026 template

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_corl2026_template_20260518T172947_result.json`
- **Structured JSON:** [`e1b1f3bd5bf40557e5a5.json`](../../sessions/e1/e1b1f3bd5bf40557e5a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模板文件已完整获取。以下是结果汇总：

---

## CoRL 2026 官方 LaTeX 模板

### 模板来源
- **官方页面**: [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- **Initial Submission 模板**: [Google Drive 下载](https://drive.google.com/file/d/1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ/view?usp=drive_link)
- **Camera-Ready 模板**: [Google Drive 下载](https://drive.google.com/file/d/19xt72-5YaVqhWRO-ErqRQZ2SPZef8FFe/view?usp=drive_link)

### 模板类型
**CoRL 自定义 .sty**（基于 NeurIPS/ICML/ICLR 风格修改），不是 .cls 文件。

模板文件清单：
- `corl_2026.sty` — 主样式文件
- `example.tex` — 模板主文件
- `example.bib` — 参考文献示例
- `corlabbrvnat.bst` — 引用排序样式（按出现顺序）

### documentclass 选项

```latex
\documentclass{article}

\usepackage{corl_2026}            % 初始投稿（匿名、带行号）
% \usepackage[final]{corl_2026}   % Camera-ready（显示作者、去行号）
% \usepackage[preprint]{corl_2026} % Preprint/arXiv（显示作者、去 CoRL 脚注）
```

可用选项：`final`, `preprint`, `nonatbib`, `nohyperref`

### 关键格式规范
- **页数**: 正文 8 页（camera-ready 9 页），References 和 Appendix 不计入
- **匿名**: 默认 double-blind，作者显示为 "Anonymous Author(s)"
- **行号**: submission 版自动启用（`\linenumbers`），final/preprint 版无行号
- **投稿平台**: [OpenReview](https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)
- **会议信息**: 第 10 届 CoRL，Austin TX, USA

### 已下载位置
模板已解压到：
```
artifacts/corl_template/corl_2026_template_submission/
```

**当前项目的 12 行 placeholder `corl_2026.cls` 应替换为这个官方 `corl_2026.sty`，并将 `\documentclass` 改为 `\documentclass{article}` + `\usepackage{corl_2026}`。**

Sources:
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Homepage](https://www.corl.org/)

---
