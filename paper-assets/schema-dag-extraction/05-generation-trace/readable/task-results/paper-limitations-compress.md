# paper limitations compress

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_limitations_compress_20260522T073005_result.json`
- **Structured JSON:** [`ae56ff7e902822ecb91f.json`](../../sessions/ae/ae56ff7e902822ecb91f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Main body (Discussion/Conclusion + Limitations start) is on page 8. Limitations continues onto page 9 but that's fine — Limitations doesn't count toward the 8-page limit per EMNLP rules. The body content is within 8 pages. Compilation: 0 errors, 0 undefined refs.

---

**压缩前后对比：**

| | 压缩前 | 压缩后 |
|---|---|---|
| 结构 | 5 条 enumerate + 2 段 paragraph | 1 段，3 个编号点 |
| 行数（.tex） | ~35 行 | ~15 行 |
| 覆盖点 | 5 条 + 2 段 = 7 个独立主题 | 3 个核心点 |

**保留的 3 点：**
1. Model & statistical scope — 单一 LLM family、TOST logit-scale inconclusive、greedy decoding uncertainty、correlational evidence
2. DocRED VIF confounding — VIF=50.9、semipartial R²=5.6% directional only
3. Experimental scope — 4 datasets zero-shot only、RE vs NER asymmetry、Bonferroni robustness

**合并/删除：**
- 原 Item 1 的 Gemini leave-one-out 细节、error taxonomy cross-model 细节 → 删除
- 原 Item 2 的 SCS variance fraction、DocRED 5-batch 细节 → 删除
- 原 Item 3 的 format independence、NER 3-model table ref → 删除
- 原 Item 4 (Causal mechanism) → 半句并入 Point 1 ("All evidence is correlational...")
- 原 Item 4 的 contamination/renaming 细节 → 删除
- 原 Item 5 (Domain/language) → 并入 Point 3
- Across-batch correlation 段 → 半句并入 Point 3
- Multiple comparisons 段 → 半句并入 Point 3 (Bonferroni + Rothman citation)
- 删除 `\citep{card-2020-power}` (随 multiple comparisons 段压缩)

---
