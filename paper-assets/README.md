**English** | [简体中文](README.zh-CN.md)

# Project materials

[Home](../README.md) · [Highlighted papers](../highlight/README.md) · [Browse by research area](../categories/README.md) · [Full catalogue](../CONTENTS.md)

This directory holds the complete materials for the 36 research projects. Find a paper through the highlighted collection, research areas, or full catalogue, then open that project's `README.md` for links to its materials. Directory names such as `vla-ssd` are project identifiers; the project guide shows the full paper title.

Navigation and project guides have separate English (`README.md`) and Simplified Chinese (`README.zh-CN.md`) editions. Use the language switch at the top of each page. Archived source documents and recorded research conversations retain their original text and language.

## Find the material you need

| Material | Directory inside each project |
|---|---|
| Paper PDF, LaTeX, references, figures, and manuscript versions | `01-manuscript/` |
| Research code, scripts, configurations, and dependencies | `02-code/` |
| Experiment settings, data, results, tables, and analysis outputs | `03-experiments/` |
| Readable conversations and structured generation sessions | `04-generation-trace/` |
| Internal reviews, audits, and checks | `05-validation/` |
| Project notes, provenance, revisions, and maintenance records | `06-maintenance/` |
| File manifests, source paths, checksums, and availability records | `07-index/` |

For a quick read, open the manuscript PDF. To inspect experiments, start with the project guide and its code and experiment directories. To examine how the work was produced, follow the generation trace guide; the file index maps archived materials to their source paths.

## Directory layout

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
