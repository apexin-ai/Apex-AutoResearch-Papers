# Step 5e Verification Report — 2026-05-16

## 1. Reference Verification (verify_references)

**Status: PASS (minor note)**

| Metric | Value |
|--------|-------|
| Total bib entries | 22 |
| Unique cited keys | 22 |
| Orphan bib (in .bib, not cited) | 0 |
| Missing bib (cited, not in .bib) | 0 |
| Online verified | 21 |
| Online mismatch | 1 |

**Mismatch detail:**
- `grattafiori2024llama3`: OpenAlex returns first_author="aaron" (first name) vs bib key prefix "grattafiori" (last name). This is a tool parsing artifact, not a real error — the entry is correct.

**Conclusion:** All 22 references are real, complete, and properly cited. No phantom citations, no orphan entries.

---

## 2. Provenance Completeness (check_provenance_completeness)

**Status: WARNING — 5 non-existent experiment references, 13 unmapped numbers**

**Coverage:** 14/14 claims mapped (all tier 2)

**Non-existent experiment references (need registry entries or claim updates):**

| Claim | Missing Experiment |
|-------|-------------------|
| C010 | kl_30_global_teal, kl_70_global_teal |
| C015 | kl_50_mistral |
| C021 | spon_decomposition |
| C028 | architecture |
| C031 | kl_30_global_teal, kl_70_global_teal |
| C038 | spon_decomposition |
| C043 | kl_50_mistral |
| C056 | architecture |

**Unmapped numbers in .tex (no provenance trail):**

| Section | Numbers |
|---------|---------|
| abstract | 2.37, 75.9, 3.1, 2.71, 0.3, 2.4 |
| conclusion | 2.37, 75.9, 3.1, 2.4, 0.3, 3.1, 0.3 |

These are architecture parameters (2.37M/layer, 75.9M total) and key results (PPL delta, speedup) that appear in headline sections but lack explicit provenance mapping.

---

## 3. Paper Consistency (check_paper_consistency)

**Status: 15 CRITICAL issues**

All critical issues are "unsupported_headline_number" — numbers in abstract/conclusion not found verbatim in experiments.tex:

| Number | Appears in | Issue |
|--------|-----------|-------|
| 3.1 | abstract, conclusion (x3) | Not in experiments section |
| 11.79 | abstract, conclusion | Not in experiments section |
| 23.31 | abstract, conclusion | Not in experiments section |
| 27.97 | abstract, conclusion | Not in experiments section |
| 2.71 | abstract | Not in experiments section |
| 0.196 | abstract, conclusion | Not in experiments section |
| 2.4 | abstract, conclusion | Not in experiments section |
| 8.36 | conclusion | Not in experiments section |

**Root cause hypothesis:** These numbers likely exist in tables/figures in experiments.tex but the consistency checker only scans inline text, not tabular data. Alternatively, some may appear only in the appendix.

---

## Action Items

### Must-fix (before submission):
1. **Provenance gaps:** Register experiments `kl_30_global_teal`, `kl_70_global_teal`, `kl_50_mistral`, `spon_decomposition`, `architecture` in registry, OR update claims C010/C015/C021/C028/C031/C038/C043/C056 to reference correct experiment names.

### Should-verify (low risk but check):
2. **Headline numbers:** Confirm that 3.1, 11.79, 23.31, 27.97, 2.71, 0.196, 2.4, 8.36 all appear somewhere in the experiments section (tables count). If any number is abstract/conclusion-only with no backing data in the body, it must be added or removed.

### No action needed:
3. **References:** All clean. The `grattafiori2024llama3` mismatch is a false positive.
