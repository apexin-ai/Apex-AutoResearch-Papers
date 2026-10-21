# research citation verification r26

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-verification-r26_20260520T145252_result.json`
- **Structured JSON:** [`100bb5a0c85a113a504d.json`](../../sessions/10/100bb5a0c85a113a504d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。96 条 bib entry 全部检查，结果：

**93 条验证通过，0 条 fabricated，3 条 mismatch，17 条 orphan。**

### 3 条需修复的 mismatch

| Key | 严重性 | 问题 |
|-----|--------|------|
| `chen2025twofailures` | **CRITICAL** | URL 指向完全无关的论文 (arXiv:2410.23123 = "On Memorization of LLMs")；authors 编造 (David Dohan/David So)；year 应为 2024；venue 应为 TMLR 而非 ICLR 2025；正确 arXiv: 2305.14279 |
| `wen2025abstention` | HIGH | 9 个作者全部错误 (bib: Zhenting Wen 等 → 实际: Bingbing Wen, Jihan Yao, Shangbin Feng 等 7 人)；DOI 可能也错 |
| `liu2025uqcc` | HIGH | 10 个作者中 9 个编造，仅第一作者 Xiaoou Liu 正确；实际只有 6 位作者 |

### hobelsberger2025systematic: NOT fabricated
arXiv:2510.20460 确实存在，标题/作者/年份全部匹配。

### 17 条 orphan entries (bib 中有但 tex 未引用)
`venktesh2025trust`, `ho2023reasoning`, `min2022rethinking`, `suzgun2023crowd`, `stechly2024chain`, `setlur2025rewarding`, `kuleshov2018accurate`, `openai2024o1`, `ashok2023promptner`, `wang2025gptner`, `wei2023chatie`, `sagi2018ensemble`, `lakshminarayanan2017ensembles`, `welling2011sgld`, `deng2023rad`, `keraghel2024ner`, `xu2024llmie`

产出已写入 `artifacts/r26_response/citation_verification.json` 并注册 (art_20260520_09f198)。

---
