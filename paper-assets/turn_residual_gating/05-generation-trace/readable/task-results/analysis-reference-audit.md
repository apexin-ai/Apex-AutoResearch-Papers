# analysis reference audit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reference_audit_20260522T042955_result.json`
- **Structured JSON:** [`c9bd5eedd4bc127d8411.json`](../../sessions/c9/c9bd5eedd4bc127d8411.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。下面是审计报告。

---

## 引用审计报告

**总数**: 46 条 bib 条目（22 条被引用，24 条 orphan）  
**真实性**: 22/22 被引用条目均为真实论文  
**格式问题**: 5 条需修复  
**结构问题**: 1 个重复 bib 文件

---

### A. 真实性验证

所有 22 条被引用条目通过 WebSearch 验证为真实论文，无幻觉引用。

OpenAlex 报告 3 条 `not_found`，均为索引问题而非真实性问题：

| Key | 原因 |
|-----|------|
| `fan2020layerdrop` | Fan, Grave, Joulin. ICLR 2020. OpenAlex 索引缺失，论文真实 |
| `luo2025flexidepth` | Xuan Luo et al. arXiv 2503.23798. OpenAlex 未收录，论文真实 |
| `elhage2021framework` | Elhage et al. Anthropic blog post，非正式论文，不在 OpenAlex 中 |

---

### B. 需修复的错误（5 条）

**1. [severity: critical] `levy2025lost` — 第一作者错误**
- bib 写 `Levy and others`，实际第一作者是 **Philippe Laban**
- 修复: `author = {Laban and others}`

**2. [severity: critical] `ko2024found` — 第一作者错误**
- bib 写 `Ko and others`，实际第一作者是 **Cheng-Yu Hsieh**
- 修复: `author = {Hsieh and others}`

**3. [severity: warning] `anonymous2024reassessing` — 应使用真实作者**
- 论文已公开，第一作者是 Yao Lu
- 修复: `author = {Lu and others}`

**4. [severity: warning] `anonymous2025style` — 应使用真实作者**
- 论文已公开，第一作者是 Yu-Xiang Lin
- 修复: `author = {Lin and others}`

**5. [severity: warning] `grattafiori2024llama3` — author 字段异常 + 缺 URL**
- `author = {Grattafiori and 1 others}` 中 `1 others` 非标准
- 修复: `author = {Grattafiori and others}`, 补 `url = {https://arxiv.org/abs/2407.21783}`

---

### C. 格式一致性

**Author 格式不统一**：部分条目列全部作者（如 `Bengio and Vinyals and Jaitly and Shazeer`），部分用 `Last and others`。建议统一为其中一种风格。当前引用的 22 条中：
- 全部作者列表: bengio2015scheduled, ranzato2016sequence, lamb2016professor, leblond2018searnn, he2019exposure, yu2020pcgrad, chen2018gradnorm, liu2021cagrad, navon2022nash, bachlechner2021rezero, dongre2026attention
- `and others` 缩写: 其余 11 条

**`he2019exposure` arXiv 标题变更**：arXiv 1905.10617 最新版标题改为 "Exposure Bias versus Self-Recovery..."，bib 中使用 v1 标题。如论文引用的是 v1 内容则可保留，否则建议更新。

---

### D. 完整性

**Missing（引用了但 bib 没有）**: 0 条

**Orphan（bib 有但未引用）**: 24 条

| 分类 | 条目 |
|------|------|
| Layer Importance | gromov2024deeper, men2024shortgpt, sun2025curse, anonymous2024reassessing |
| Multi-Turn | liu2023lost, anonymous2025style |
| Residual Gating | wang2018skipnet, lawson2025skip |
| Attention Manipulation | press2022alibi, chen2023positional, peng2024yarn, han2024lminfinite |
| Theoretical | elhage2021framework, elhage2022superposition, belrose2023tuned, yu2023residual, makkuva2025markov, ildiz2024markov |
| Benchmarks | zheng2023mtbench, chiang2024arena, dubois2024alpacaeval, lin2024wildbench, sirdeshmukh2025multichallenge |
| Residual Scaling | zhang2019fixup |

建议：删除 orphan 条目，或在正文中补充引用。

**重复 bib 文件**: `paper/sections/references.bib` 是 `paper/references.bib` 的副本。`main.tex` 只引用后者。建议删除 `paper/sections/references.bib` 以避免维护不一致。

---

### E. 修复优先级

1. **立即修复**: `levy2025lost` 和 `ko2024found` 的第一作者错误（reviewer 一查即发现）
2. **应修复**: anonymous 条目替换为真实作者、`grattafiori2024llama3` 格式修正
3. **建议修复**: 清理 24 条 orphan 条目、统一 author 格式、删除重复 bib 文件

---
