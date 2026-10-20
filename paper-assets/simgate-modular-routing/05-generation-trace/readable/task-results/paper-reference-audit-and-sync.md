# paper reference audit and sync

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit-and-sync_20260514T144920_result.json`
- **Structured JSON:** [`b1f2956e59a818a059eb.json`](../../sessions/b1/b1f2956e59a818a059eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。在执行同步前，需要先报告一个重要发现。

---

## 1. 引用审计报告

### 引用完整性

| 检查项 | 结果 |
|--------|------|
| ❌ 论文中 cite 了但 bib 中不存在的 | **无** — 所有 12 个被引用的 key 均存在于 bib 中 |
| ⚠️ bib 中存在但论文中未 cite 的 | **`dagger-2011`** (Ross et al., 2011, DAgger) |

被引用的 12 个 key: `scienceworld-2022`, `toolformer-2024`, `art-2023`, `chameleon-2024`, `retool-2026`, `react-2023`, `cogrouter-2026`, `ares-2026`, `mixture-of-recursions-2025`, `itp-2026`, `dynathink-2025`, `mtrouter-2026`

### Bib entry 质量问题

**Key 与 year 字段不匹配（3 个）：**
| Key | key 中的年份 | year 字段 |
|-----|------------|-----------|
| `toolformer-2024` | 2024 | 2023 |
| `chameleon-2024` | 2024 | 2023 |
| `retool-2026` | 2026 | 2025 |

**Entry type 错误（8 个）：** 以下 arXiv 预印本使用了 `@inproceedings` + `booktitle`，应改为 `@article` + `journal`：
`art-2023`, `retool-2026`, `cogrouter-2026`, `ares-2026`, `mixture-of-recursions-2025`, `itp-2026`, `dynathink-2025`, `mtrouter-2026`

**缺失字段：** 无。所有 entry 均有 title, author, year。

---

## 2. 同步：重要警告

**逐文件 diff 显示 `docs/paper/` 很可能是更新的版本，`artifacts/_project/paper/latex/` 是旧版本。** 具体证据：

| 文件 | artifacts (主) | docs (副) | 差异 |
|------|---------------|-----------|------|
| `abstract.tex` | 更短，约 3 行 | 更详细，含具体数值 | docs 更完整 |
| `introduction.tex` | 枚举式 contributions | 压缩为 1 段 + 引用 §rule | docs 增加了 keyword baseline 引用 |
| `method.tex` | 3 小节 | 4 小节（多了 Rule-Based Baseline §rule） | docs 新增内容 |
| `experiments.tex` | 有独立 Setup 小节；router 分析简略 | Setup 移走；增加 classification head / implicit router / cross-seed / end-to-end / labeling quality 段落 | docs 大幅扩充 |
| `conclusion.tex` | 1 段 | 3 段（含 labeling quality + limitations） | docs 大幅扩充 |
| `main.tex` | 含 `\input{discussion}` + Limitations + Ethics 节 | 不含 discussion；限制移入 conclusion | 结构不同 |
| `related_work.tex` | 分段引用，较松散 | 合并压缩，更紧凑 | docs 更精炼 |
| `references.bib` | @inproceedings 用于 arXiv | 已修正为 @article + venue 缩写 | docs 质量更高 |
| `discussion.tex` | 存在 | **缺失** | 需要复制 |

**如果按原计划用 artifacts 覆盖 docs，会丢失 docs 中的大量改进（实验分析扩充、bib 修正、结构重组等）。**

### 建议

反向同步更合理：以 `docs/paper/` 为准更新 `artifacts/_project/paper/latex/`，并将 `discussion.tex` 复制到 docs。

是否按原计划执行（artifacts → docs 覆盖），还是反向同步（docs → artifacts + 补 discussion.tex）？

---
