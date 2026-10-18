# fix bib audit fixes

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bib_audit_fixes_20260528T171451_result.json`
- **Structured JSON:** [`dbcbeb69965576650611.json`](../../sessions/db/dbcbeb69965576650611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项修改均已生效。

## 改动摘要

### Critical — 已修复
1. **`zheng2025xvla`** (line 366): 第一作者 `Zheng, Yifu` → `Zheng, Jinliang`

### Warning — 已修复
2. **`chen2024fastv`** (line 159-167): 作者列表从 `Chen, Liang and others` 补全为 7 位完整作者：Chen, Liang; Zhao, Haozhe; Liu, Tianyu; Bai, Shuai; Lin, Junyang; Zhou, Chang; Chang, Baobao。同时补充了 eprint 字段。

3. **`black2025pi05`** (line 127-138): 从 `@article`(arXiv preprint）转为 `@inproceedings`（CoRL 2025 正式发表），新增 `booktitle`, `series=PMLR`, `volume=305`, `pages=17--40`, `publisher=PMLR`。

### Orphan 条目（26 条，保留未删除）

以下 bib key 在 `references.bib` 中定义但未被任何 `.tex` 文件引用：

`wang2025specprunevla`, `feng2026seewhatmatters`, `zhang2025sparsevlm`, `khaki2025sparsevila`, `jabbour2025dontrun`, `li2024roboflamingo`, `brohan2023rt1`, `jaegle2021perceiver`, `li2024tokenpacker`, `wen2024tinyvla`, `ryoo2021tokenlearner`, `meng2022adavit`, `chen2023sparsevit`, `ye2025fitprune`, `shi2024crossget`, `zhang2024fastervlm`, `liu2024llava15`, `chen2024internvl25`, `gao2024miniinternvl`, `zitkovich2023rt2`, `openxembodiment2024`, `xiao2024streamingllm`, `mees2022calvin`, `chi2023diffusionpolicy`, `bouthillier2024negative`, `oquab2024dinov2`

另外，tex 中引用了 `karl2024negative` 和 `physicalintelligence2025pi05` 两个 key，但 bib 中不存在对应条目——这属于 missing citation，非本次任务范围。

---
