# Project materials · 项目资料

[Home / 首页](../README.md) · [精选论文](../highlight/README.md) · [Browse by area / 按方向浏览](../categories/README.md) · [Full catalogue / 完整目录](../CONTENTS.md)

This directory holds the complete materials for the 36 research projects. Find a paper through the highlighted collection, research areas, or full catalogue, then open that project's `README.md` for links to its materials. Directory names such as `vla-ssd` are project identifiers; the project guide shows the full paper title.

本目录存放 36 个研究项目的完整资料。先通过精选论文、研究方向或完整目录找到论文，再打开项目的 `README.md` 查看材料入口。`vla-ssd` 等目录名是项目标识，完整论文标题见对应项目说明。

## Find the material you need · 按需查找

| Material / 材料 | Directory inside each project / 项目内目录 |
|---|---|
| Paper PDF, LaTeX, references, figures, and manuscript versions / 论文、LaTeX、参考文献、图表和版本 | `01-manuscript/` |
| Research code, scripts, configurations, and dependencies / 代码、脚本、配置和依赖记录 | `02-code/` |
| Experiment settings, data, results, tables, and analysis outputs / 实验设置、数据、结果和分析 | `03-experiments/` |
| Readable conversations and structured generation sessions / 可读对话和结构化生成记录 | `04-generation-trace/` |
| Internal reviews, audits, and checks / 内部评审、审计和检查记录 | `05-validation/` |
| Project notes, provenance, revisions, and maintenance records / 项目说明、来源、修订和维护记录 | `06-maintenance/` |
| File manifests, source paths, checksums, and availability records / 文件清单、来源路径、校验和可用性记录 | `07-index/` |

For a quick read, open the manuscript PDF. To inspect experiments, start with the project guide and its code and experiment directories. To examine how the work was produced, follow the generation trace guide; the file index maps archived materials to their source paths.

快速阅读可直接打开论文 PDF；查看实验时，从项目说明进入代码和实验目录；了解研究生成过程时，打开生成记录指南。文件索引用于核对归档材料及其来源路径。

## Directory layout · 目录结构

```text
paper-assets/
└── <project-id>/
    ├── README.md
    ├── 01-manuscript/
    ├── 02-code/
    ├── 03-experiments/
    ├── 04-generation-trace/
    ├── 05-validation/
    ├── 06-maintenance/
    └── 07-index/
```

The five PDFs in `highlight/` are copies of the corresponding manuscripts here. Original papers and project materials remain at their existing paths.

`highlight/` 中的 5 份 PDF 是本目录对应论文的副本。原论文和项目资料保留在原有路径。
