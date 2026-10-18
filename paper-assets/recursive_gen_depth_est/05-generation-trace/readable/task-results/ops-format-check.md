# ops format check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_format-check_20260518T081444_result.json`
- **Structured JSON:** [`5ce6126429d01c1e7713.json`](../../sessions/5c/5ce6126429d01c1e7713.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成，以下是逐项报告。

---

## 1. `\documentclass` 选项

`main.tex:3-4`:
```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}
```
**无问题。** `review` 选项已正确设置，符合 ARR review 版要求。

---

## 2. `references.bib` 格式一致性

### 两个副本一致性
`diff` 输出为空，**两个副本完全一致。**

### 年份字段
所有 entry 均有 `year` 字段。**无问题。**

### 重复 entry
未发现重复。**无问题。**

### Venue 名称不一致

**Findings 系列写法不统一：**
- `references.bib:246` `bevendorff2025_two_paradigms`: `Findings of the Association for Computational Linguistics: ACL 2025`（全称）
- `references.bib:96` `synthetic_eggs2026`: `Findings of ACL`（缩写）
- `references.bib:559` `guo2024curious`: `Findings of NAACL`（缩写）
- `references.bib:122` `drayson2025_detection_prevents_collapse`: `Findings of EMNLP`（缩写）

注：`bevendorff2025_two_paradigms` 实际未被引用（见下），但如将来引用会造成格式不一致。

**Spotlight 标注位置不当：**
- `references.bib:270` `loki2025`: `booktitle = {Proceedings of ICLR (Spotlight)}` — `(Spotlight)` 应放在 `note` 字段而非 `booktitle`。
- `references.bib:107` `shi2025_closer_look`: `note = {Spotlight}` — 这个处理方式是正确的。同一个 bib 文件内两种做法不一致。

**arXiv preprint 格式不统一：**
- `references.bib:432` `liu2019_roberta`: `@article` + `journal = {arXiv preprint arXiv:1907.11692}`
- `references.bib:504` `schaeffer2025`: `@article` + `journal = {arXiv preprint arXiv:2503.03150}`
- 其余 arXiv preprints 用 `@misc` + `howpublished = {arXiv:XXXX.XXXXX}`

### Title 大小写保护

- `references.bib:525` `mccullagh1980_ordinal`: `title={Regression Models for Ordinal Data}` — 单层花括号，BibTeX sentence-case style 会将 "Ordinal Data" 小写化。应改为 `title={{Regression Models for Ordinal Data}}`。
- 其余 entry 均使用 `{{...}}` 双花括号保护，**无问题。**

### 未被引用的 bib entry（6 个）

| Key | 行号 |
|---|---|
| `bevendorff2025_two_paradigms` | 243 |
| `llama3` | 489 |
| `pareek2024understanding` | 589 |
| `penedo2024_fineweb` | 459 |
| `qwen2.5` | 481 |
| `shi2025_closer_look` | 102 |

其中 `llama3`、`qwen2.5`、`penedo2024_fineweb` 在正文中提到了对应模型/数据集（Llama-3.1-8B、Qwen2.5-7B、FineWeb）但未加 `\cite`，大概率是遗漏引用。

### key 与 year 不匹配
- `references.bib:278` `tulchinskii2024_intrinsic_dim`: key 写 2024，实际 `year = {2023}`（NeurIPS 2023）。

---

## 3. Undefined References

### `\ref` vs `\label`
**所有 `\ref{...}` 均有对应 `\label{...}`，无 undefined reference。**

### 未被 `\ref` 引用的 `\label`（24 个）

大部分是结构性 label（`sec:intro`, `sec:method` 等），hyperref 自动使用。以下几个 appendix label 值得注意——如果正文从未引用，可能是遗漏或多余：

| Label | 文件:行号 | 说明 |
|---|---|---|
| `app:calibration` | section_appendix.tex:216 | 正文 Limitations 提到 C4 FPR 数据但未用 `Appendix~\ref{app:calibration}` 引用 |
| `app:downstream` | section_appendix.tex:531 | 下游 fine-tuning probe，正文未引用 |
| `app:mixed_depth` | section_appendix.tex:485 | 混合深度语料实验，正文未引用 |
| `app:compute` | section_appendix.tex:669 | 计算资源，正文未引用 |
| `app:cross_scale_confounds` | section_appendix.tex:393 | 跨规模 confounds，正文未引用 |
| `tab:downstream` | section_appendix.tex:539 | 配套表格，正文未引用 |
| `tab:ref_ablation` | section_appendix.tex:301 | 正文引用的是 `app:ref_ablation` 而非 `tab:ref_ablation` |

---

## 额外发现的格式问题

### 标点错误（`, ;`）
- `conclusion.tex:43`: `...85.9\%), ; the overlap...` — 逗号后多余分号
- `conclusion.tex:50`: `...within-seed avg), ; depth signal...` — 同上

### RF 树数量前后矛盾
- `method.tex:103`: `Random Forest (200 trees, unconstrained depth...)`
- `section_appendix.tex:681`: `scikit-learn defaults (100 trees, Gini criterion, no max depth)`

两处描述的是同一个 primary classifier，但树数量不一致（200 vs 100）。

### `\textsc` vs `\texttt` 混用
- `abstract.tex:4` 和 `section_appendix.tex:9,16,155-156`: 使用 `\textsc{p90\_ppl}`, `\textsc{var\_surprisal}`（小写大写字母）
- `method.tex`, `atlas.tex`, `generalization.tex`: 使用 `\texttt{p90\_ppl}`（等宽字体）

同一特征名在不同位置格式不同。

---
