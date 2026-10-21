# 论文引用审计报告

**项目**: diff_collision_sdf  
**日期**: 2026-05-24  
**bib 文件**: `docs/paper/references.bib`（18 条目）  
**tex 文件扫描范围**: `docs/paper/*.tex` + `artifacts/drafts/*.tex`  
**引用总数**: 39 个唯一 cite key

---

## CRITICAL（必须修复）

### C1. 缺失 bib 条目（21 个 cite key 无对应 bib entry）

以下 cite key 在 tex 文件中被引用，但 `references.bib` 中无对应条目。编译时会产生 `undefined citation` 错误。

| # | cite key | 出现位置 |
|---|----------|----------|
| 1 | `3dcavla2025` | related_work |
| 2 | `augvla3d2026` | related_work |
| 3 | `chen2025samp` | related_work |
| 4 | `chen2026cssdfnet` | related_work |
| 5 | `chen2026dfmvla` | related_work |
| 6 | `depthvla2025` | related_work |
| 7 | `evo02025` | related_work |
| 8 | `evodepth2026` | related_work |
| 9 | `geoaware2025` | related_work |
| 10 | `gstvla2026` | related_work |
| 11 | `jacquet2025neuralnmpc` | related_work |
| 12 | `li2025qdepth` | related_work |
| 13 | `li2025spatialforcing` | related_work |
| 14 | `ruan2025profrobot` | related_work |
| 15 | `savla2026` | related_work |
| 16 | `spatialvla2025` | related_work |
| 17 | `stemvla2026` | related_work |
| 18 | `stvla2026` | related_work |
| 19 | `vasilopoulos2023ramp` | related_work |
| 20 | **`placeholder_goodhart_rl`** | analysis/discussion |
| 21 | **`placeholder_metric_reliability`** | analysis/discussion |

> **特别注意**: `placeholder_goodhart_rl` 和 `placeholder_metric_reliability` 是占位符 key，需替换为真实引用或移除。

### C2. 作者姓名错误

| bib key | bib 中写的 | 实际作者 | 严重性 |
|---------|-----------|---------|--------|
| `yang2025cape` | Yang, **Xinyu** | Yang, **Rui Heng** | ⚠️ 名字完全错误 |
| `spalter2024ikinqp` | Spalter, **Ariel** | Spalter, **Ariana** | ⚠️ 名字拼写错误 |

---

## WARNING（应该修复）

### W1. 年份/venue 不匹配

| bib key | 问题 | 建议 |
|---------|------|------|
| `zhi2021diffco` | bib year=2021，实际 IEEE TRO 正式发表于 **2022**（vol.38, no.5, pp.2668-2685）。arXiv 预印本为 2021，但既然标注为 journal=IEEE TRO，应用发表年份 | 改 year=2022，补 volume={38}, number={5}, pages={2668--2685} |
| `li2024langguided` | cite key 含 "2024" 但 year 字段为 2025（ICRA 2025）。key 与 year 不一致 | 建议改 key 为 `li2025langguided` 或保持现状（不影响编译，仅不规范） |

### W2. 必要字段缺失

| bib key | 类型 | 缺失字段 |
|---------|------|---------|
| `zhi2021diffco` | @article (IEEE TRO) | volume, number, pages |
| `brohan2023rt2` | @article (arXiv) | 实际已发表于 CoRL 2023 (PMLR 229:2165-2183)，建议改为 @inproceedings |

### W3. 作者列表不完整（使用 "and others"）

以下条目用 `and others` 代替完整作者列表。LaTeX 会渲染为 "et al."，功能上可接受，但建议至少列出前 3-5 位作者：

- `hu2025vlsa` — 仅列 1 位作者
- `zhang2025safevla` — 仅列 1 位作者
- `spalter2024ikinqp` — 仅列 1 位作者
- `li2024langguided` — 仅列 1 位作者
- `yang2025cape` — 仅列 1 位作者

---

## INFO（可选修复）

### I1. 无孤立 bib 条目

所有 18 个 bib 条目均在 tex 文件中被引用，无 orphan entry。✓

### I2. 格式不一致

| 问题 | 条目 |
|------|------|
| arXiv 预印本混用 @article 和 @misc | 所有 arXiv 预印本均用 @article，格式统一 ✓ |
| venue 名称风格 | 大多用全称如 "Conference on Robot Learning (CoRL)"，风格统一 ✓ |
| 部分 arXiv 预印本缺 eprint 字段 | 所有 arXiv @article 均通过 journal 字段标注 arXiv ID，可接受 |

### I3. `%[CITE-CHECK]` 注释标记

`artifacts/drafts/related_work_v2.tex` 中有两处 `%[CITE-CHECK]` 注释标记（line 8, line 25），表示作者自己标记了需要核实的引用。建议处理完毕后删除这些标记。

---

## 已验证条目汇总（18/18）

| # | bib key | 真实性 | 标题 ✓ | 作者 ✓ | 年份 ✓ | venue ✓ |
|---|---------|--------|--------|--------|--------|---------|
| 1 | `black2024pi0` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ arXiv 2410.24164 |
| 2 | `kim2024openvla` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ CoRL 2024 |
| 3 | `brohan2023rt2` | ✅ 真实 | ✓ | ✓ | ✓ | ⚠️ 已发表于 CoRL 2023 |
| 4 | `hu2025vlsa` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ arXiv 2512.11891 |
| 5 | `zhang2025safevla` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ NeurIPS 2025 Spotlight |
| 6 | `cofreeevla2026` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ arXiv 2601.21712 |
| 7 | `spalter2024ikinqp` | ✅ 真实 | ✓ | ❌ Ariel→Ariana | ✓ | ✓ arXiv 2409.08233 |
| 8 | `li2024langguided` | ✅ 真实 | ✓ | ✓ | ⚠️ key=2024,year=2025 | ✓ ICRA 2025 |
| 9 | `yang2025cape` | ✅ 真实 | ✓ | ❌ Xinyu→Rui Heng | ✓ | ✓ arXiv 2511.22773 |
| 10 | `park2019deepsdf` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ CVPR 2019 |
| 11 | `ortiz2022isdf` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ RSS 2022 |
| 12 | `zhi2021diffco` | ✅ 真实 | ✓ | ✓ | ⚠️ 2021→2022 | ⚠️ 缺 vol/pages |
| 13 | `huang2023voxposer` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ CoRL 2023 |
| 14 | `liu2023libero` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ NeurIPS 2023 |
| 15 | `lipman2023flow` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ ICLR 2023 |
| 16 | `gururangan2018annotation` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ NAACL 2018 |
| 17 | `karwowski2024goodhart` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ ICLR 2024 |
| 18 | `chi2023diffusionpolicy` | ✅ 真实 | ✓ | ✓ | ✓ | ✓ RSS 2023 |

**无 fake citation。** 所有 18 个现有条目均为真实论文。

---

## 统计摘要

| 类别 | 数量 |
|------|------|
| CRITICAL — 缺失 bib entry | 21 |
| CRITICAL — 作者姓名错误 | 2 |
| WARNING — 年份/venue 问题 | 2 |
| WARNING — 必要字段缺失 | 2 |
| WARNING — 作者列表过短 | 5 |
| INFO — 孤立条目 | 0 |
| Fake citation | 0 |

**最紧迫任务**: 补充 21 个缺失的 bib 条目（其中 2 个是 placeholder，需替换为真实引用或从 tex 中移除）。
