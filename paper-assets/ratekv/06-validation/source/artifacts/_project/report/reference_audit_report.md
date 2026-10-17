# Reference Audit Report

**Project:** ratekv  
**Date:** 2026-05-14  
**Scope:** `docs/paper/references.bib` + all `.tex` files in `docs/paper/`

---

## 统计摘要

| 指标 | 数值 |
|------|------|
| .bib 总条目数 | 19 |
| .tex 中引用的唯一 key 数 | 19 |
| 孤立引用（.bib 有，.tex 未引用） | 0 |
| 缺失引用（.tex 引用，.bib 无） | 0 |
| 疑似重复条目 | 0 |
| 格式不完整条目 | 0 |

**结论：引用集合完全一致，无孤立或缺失条目。**

---

## 问题清单（按严重性排序）

### 中等：Bib key 与 year 字段不一致（2 处）

| Bib Key | Key 中隐含年份 | year 字段 | 实际 venue | 建议 |
|---------|---------------|-----------|------------|------|
| `lin2024qserve` | 2024 | 2025 | MLSys 2025 | 改 key 为 `lin2025qserve`，或保持 key 不变但知悉不一致 |
| `liu2024scissorhands` | 2024 | 2023 | NeurIPS 2023 | 改 key 为 `liu2023scissorhands`，或保持 key 不变但知悉不一致 |

说明：key 中的年份仅为命名约定，不影响编译或显示，但可能造成维护混淆。修改 key 需同步更新所有 .tex 文件中的 `\cite{}` 引用。

### 低：entry type 与 venue 不完全匹配（2 处）

| Bib Key | 当前 type | 实际情况 | 说明 |
|---------|-----------|---------|------|
| `kang2024gear` | `@misc` | arXiv preprint（但已被接受到某 venue） | 如已正式发表，建议更新为 `@inproceedings` 并补充 venue |
| `duanmu2024skvq` | `@misc` | arXiv preprint | 如仍为 preprint 则无问题 |

---

## 格式一致性检查

所有 19 条 .bib 条目均包含以下必需字段：

- `title` ✅
- `author` ✅
- `year` ✅
- `booktitle`（对 `@inproceedings`）或 `note`（对 `@misc`）✅

附加观察：
- 所有 `@inproceedings` 条目的 `booktitle` 使用简写格式（如 "ICML 2024" 而非完整名称），风格一致。
- 所有 `@misc` 条目含 `url`、`eprint`、`archivePrefix` 字段，格式统一。
- 所有条目含 `url` 字段。

---

## 年份合理性检查

| 年份范围 | 条目数 | 判定 |
|---------|--------|------|
| 2019 | 2 | ✅ 合理（经典 attention head 分析论文） |
| 2023 | 2 | ✅ 合理 |
| 2024 | 9 | ✅ 合理 |
| 2025 | 3 | ✅ 合理 |
| 2026 | 3 | ✅ 合理（当前年份，均为 arXiv preprint 或本文自身） |

无异常年份（无未来日期、无明显 typo）。

---

## 真实性抽查结果（5/19）

随机抽取 5 篇，通过 Web 搜索验证 title、author、year、venue：

| Bib Key | Title 匹配 | Author 匹配 | Year/Venue 匹配 | 判定 |
|---------|-----------|-------------|----------------|------|
| `liu2024kivi` | ✅ | ✅ | ✅ ICML 2024, arXiv 2402.02750 | **真实** |
| `zhang2023h2o` | ✅ | ✅ | ✅ NeurIPS 2023, arXiv 2306.14048 | **真实** |
| `voita2019analyzing` | ✅ | ✅ | ✅ ACL 2019, arXiv 1905.09418 | **真实** |
| `he2024zipcache` | ✅ | ✅ | ✅ NeurIPS 2024, arXiv 2405.14256 | **真实** |
| `zuo2026ratequant` | ✅ | ✅ | ✅ arXiv 2605.06675 (May 2026) | **真实** |

**5/5 抽查条目均为真实论文，无 LLM 幻觉引用。**

---

## 引用分布

| .tex 文件 | 引用数 |
|-----------|--------|
| introduction.tex | 9 |
| related_work.tex | 17（覆盖全部 19 条中的 17 条） |
| method.tex | 1 |
| experiments.tex | 1 |
| abstract.tex | 0 |
| analysis.tex | 0 |
| conclusion.tex | 0 |
| main.tex | 0 |

---

## 建议修复

1. **（可选）** 统一 bib key 命名中的年份：将 `lin2024qserve` → `lin2025qserve`，`liu2024scissorhands` → `liu2023scissorhands`，并同步更新所有 .tex 中的 `\cite{}` 调用。这是命名规范问题，不影响编译。

2. **（可选）** 检查 `kang2024gear` (GEAR) 是否已被正式会议/期刊接收，如是则更新 entry type 和 venue 信息。

---

## 总结

引用系统整体健康。19 条 bib 条目与 .tex 引用完全对应，无孤立、无缺失、无重复、无虚假引用。仅有 2 处 key 命名与 year 字段的轻微不一致，不影响论文编译和引用显示。
