# Compilation Setup

## ACL Style File

This paper uses `acl_natbib` bibliography style and is formatted for ACL submission. To compile with the official ACL 2023 template:

1. Download the ACL 2023 style files from https://github.com/acl-org/acl-style-files
2. Place `acl.sty`, `acl_natbib.bst`, and related files in this directory
3. Change `\documentclass[11pt]{article}` to `\documentclass[11pt]{article}` with `\usepackage{acl}` (and remove the `geometry`/`times` fallback lines)

## Figures

Place `fig1_daf_scatter.pdf` in a `figures/` subdirectory. The figure is referenced as `figures/fig1_daf_scatter.pdf` in `experiments.tex`.

## Build

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```
