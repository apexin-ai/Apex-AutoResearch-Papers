# ops reference audit

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_reference_audit_20260517T080108_result.json`
- **Structured JSON:** [`66b9c5f68f96ef8261e7.json`](../../sessions/66/66b9c5f68f96ef8261e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。汇总结果：

## Reference Audit 结果

| # | Bib Key | 验证项 | 结果 | 说明 |
|---|---------|--------|------|------|
| 1 | mccullagh1980\_ordinal | 标题/作者/年份/venue/卷号页码 | **PASS** | McCullagh, Peter. JRSS-B, 1980, 42(2):109-142 全部正确 |
| 2 | wenzek2020\_ccnet | 标题/作者/venue/年份 | **PASS** | Wenzek, Lachaux, Conneau, Chaudhary, Guzmán, Joulin, Grave. LREC 2020 正确 |
| 3 | schaeffer2025 | arXiv ID/作者 | **FAIL** | arXiv ID 错误 + 作者列表错误（详见下方） |
| 4 | alemohammad2024\_mad | 作者列表 | **FAIL** | LeJeune 名字错误：bib 写 "Lorenzo"，实际为 "Daniel" |
| 5 | knowledge\_collapse2025 | 存在性/标题/作者/年份 | **PASS** | arXiv:2509.04796，作者 Keisha, Wu, Wang, Koshiyama, Treleaven 正确 |
| 6 | falahati2026\_curated | 存在性/标题/作者/年份 | **PASS** | arXiv:2605.07724, May 2026. Falahati, Mohammadi Amiri, Larson, Golab 正确 |
| 7 | he2021\_deberta\_v3 | 年份 | **PASS** | bib key 写 2021 但 year 字段正确为 2023（ICLR 2023）。内容无误 |
| 8 | frank2001 | 标题/作者/venue/年份 | **PASS** | Frank, Hall. ECML 2001, pp.145-156. Springer LNCS 2167 确认 |
| 9 | rennie2005 | 标题/作者/venue/年份 | **PASS** | Rennie, Srebro. IJCAI Workshop on Advances in Preference Handling, 2005 正确 |
| 10 | c2pa2024 | URL/版本 | **SUSPICIOUS** | v2.1 和 2024 年正确，但 URL 域名已迁移（见下方） |

### 抽样验证（随机5条）

| # | Bib Key | 结果 | 说明 |
|---|---------|------|------|
| S1 | shumailov2024\_nature | **PASS** | Nature 631, 755-759 (2024), DOI 正确 |
| S2 | holtzman2020\_nucleus | **PASS** | ICLR 2020, arXiv:1904.09751, 作者全部正确 |
| S3 | coral2020 | **PASS** | Pattern Recognition Letters, vol.140, pp.325-331, 2020 正确 |
| S4 | dohmatob2024\_tale\_of\_tails | **PASS** | ICML 2024, arXiv:2402.07043, 5位作者全部正确 |
| S5 | binoculars2024 | **PASS** | ICML 2024, arXiv:2401.12070, 8位作者全部正确 |

---

### 需要修正的条目

**1. schaeffer2025 — 两个严重错误**

- **arXiv ID 错误**：bib 写 `arXiv:2502.07087`，但 2502.07087 实际是 "Evaluating the Systematic Reasoning Abilities of Large Language Models through Graph Coloring"（Heyman & Zylberberg），完全不相关的论文。正确 ID 为 **2503.03150**。
- **作者列表错误**：bib 写 `Schaeffer, Rylan and Gerstgrasser, Matthias and Koyejo, Sanmi and Donoho, David L.`，但该论文实际作者为 **Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi**。Gerstgrasser 和 Donoho 不是此论文作者（他们是 arXiv:2404.01413 "Is Model Collapse Inevitable?" 的共同作者，可能是混淆来源）。

正确 bib：
```bibtex
@article{schaeffer2025,
  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
  title     = {{Position: Model Collapse Does Not Mean What You Think}},
  journal   = {arXiv preprint arXiv:2503.03150},
  year      = {2025},
  url       = {https://arxiv.org/abs/2503.03150},
}
```

**2. alemohammad2024\_mad — 作者名字错误**

- bib 第6位作者写 `LeJeune, Lorenzo`，正确为 **`LeJeune, Daniel`**。"Lorenzo" 是第3位作者 Luzi 的名字，可能是复制错误。

修正：将 `LeJeune, Lorenzo` 改为 `LeJeune, Daniel`。

---

### 可疑但无法确认的条目

- **c2pa2024**: bib URL 为 `https://c2pa.org/specifications/specifications/2.1/specs/C2PA_Specification.html`，但当前官方域名已迁移至 `spec.c2pa.org`（搜索结果显示 PDF 在 `https://spec.c2pa.org/specifications/specifications/2.1/specs/_attachments/C2PA_Specification.pdf`）。旧 URL 可能仍重定向有效，但建议更新为当前可访问地址。

---

### 总结

- **2 条 FAIL**（schaeffer2025, alemohammad2024\_mad）— 必须立即修正，否则有 desk reject 风险
- **1 条 SUSPICIOUS**（c2pa2024）— URL 建议更新
- **其余 12 条 PASS**

schaeffer2025 的问题最严重：arXiv ID 指向完全无关的论文 + 2/4 作者是 hallucinated，属于典型的 citation hallucination。

---
