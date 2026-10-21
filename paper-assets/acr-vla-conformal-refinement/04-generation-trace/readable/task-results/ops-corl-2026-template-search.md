# ops corl 2026 template search

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_corl-2026-template-search_20260518T104403_result.json`
- **Structured JSON:** [`0daf16c926c4d1daa52a.json`](../../sessions/0d/0daf16c926c4d1daa52a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## CoRL 2026 LaTeX 模板搜索结果

### 模板来源
- **官方页面**: https://www.corl.org/contributions/instruction-for-authors
- **Review 模板**: [Google Drive](https://drive.google.com/file/d/1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ/view?usp=drive_link)
- **Camera-ready 模板**: [Google Drive](https://drive.google.com/file/d/19xt72-5YaVqhWRO-ErqRQZ2SPZef8FFe/view?usp=drive_link)

### documentclass 设置
- `\documentclass{article}` + `\usepackage{corl_2026}`
- 三种模式：
  - **Review（默认）**: `\usepackage{corl_2026}` — 匿名 + 行号 + 底部显示 "Submitted to CoRL 2026"
  - **Camera-ready**: `\usepackage[final]{corl_2026}` — 显示作者 + 去行号
  - **Preprint**: `\usepackage[preprint]{corl_2026}` — 显示作者 + 去行号 + 去 CoRL 脚注

### Page limit
- **Initial submission**: 8 页正文
- **Camera-ready**: 9 页正文
- Acknowledgments、References、Appendix 不计入页数

### Anonymous / 行号
- Review 阶段：**双盲匿名**（作者自动显示为 "Anonymous Author(s)"），**自动开启行号**（`\linenumbers`）
- Camera-ready：显示作者，行号关闭

### 字体和 margin
- 正文字体：10pt（Times Roman `ptm`，sans-serif `phv`）
- 页面：letterpaper，textheight=9in，textwidth=5.5in，top=1in

### 必需 section
- **Limitations section**（计入 8 页限制）
- **Keywords**（Abstract 之后）
- **Acknowledgments**（仅 final/preprint 版本显示）
- 无明确要求 Checklist / Ethics Statement / Broader Impact

### 其他要求
- 引用格式：natbib + `corlabbrvnat.bst`（按出现顺序编号 [1][2]...）
- 补充材料：视频 <= 250MB, <= 3min；通过 OpenReview 提交单个 zip
- 投稿截止：**2026-05-29**
- 投稿平台：OpenReview

### 模板文件保存路径
```
docs/paper/
├── corl2026_review_template.zip
├── corl2026_camera_ready_template.zip
├── review_template/corl_2026_template_submission/
│   ├── corl_2026.sty
│   ├── corlabbrvnat.bst
│   ├── example.tex
│   └── example.bib
└── camera_ready_template/corl_2026_template_cameraready/
    ├── corl_2026.sty
    ├── corlabbrvnat.bst
    ├── example.tex
    └── example.bib
```

Sources:
- [CoRL 2026 - Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Official Website](https://www.corl.org/)

---
