# paper final polish

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-polish_20260524T013437_result.json`
- **Structured JSON:** [`1660d64aa626a9dbdcef.json`](../../sessions/16/1660d64aa626a9dbdcef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Final Polish Report

### 1. 编译验证
- Errors: 0
- Undefined refs: 0
- Main text pages: 8 (Limitations starts on page 8, References on page 9)
- Bib warnings: 0

### 2. Caption 检查
- [PASS] Captions are self-contained: model name (Qwen3-8B/LLaMA-3.1-8B), dataset, N, T, seed counts are stated; symbol abbreviations (VC, SJ, FK, LP, EM, MV) are spelled out in tab:scale_comparison, tab:entity_probes, etc.
- [FIXED] First "pp" usage in `introduction.tex` line 6 now expanded as "percentage point (pp)".

### 3. Cross-table 脚注
- [PASS] tab:scale_comparison caption already states: *"F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}"* — no addition needed.

### 4. Abstract word count
- Word count: **185 / 200** (under limit)

### 5. 匿名检查
- [PASS] No GitHub URLs (except anonymous-nlp-2026), no emails, no local paths, no university/department mentions, no "AutoDL", no self-citation markers in references.bib.

### 6. Bib 检查
- Undefined citations: 0
- Duplicate keys: 0
- 60 unique bib entries.

### Additional fixes applied
- **Few-NERD naming**: replaced 10 occurrences of "FewNERD" → "Few-NERD" in `sections/appendix.tex` (caption text and table rows).
- **WNUT-17 naming**: fixed 1 occurrence of bare "WNUT" → "WNUT-17" in training config table.
- **Synced** to anonymous repo (commit f803b24); recompiled successfully (0 errors, 8-page main text preserved).

---
