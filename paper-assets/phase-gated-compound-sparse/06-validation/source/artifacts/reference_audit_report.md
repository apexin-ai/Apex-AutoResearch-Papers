# Reference Audit Report — Phase-Gated Compound Sparse

**Date**: 2026-05-14
**Paper**: "Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models"
**Bib file**: `artifacts/_project/paper/references.bib`
**Tex files**: 14 files in `artifacts/_project/paper/`

---

## Summary

| Metric | Count |
|--------|-------|
| Bib entries | 31 |
| Unique citation keys used in .tex | 26 |
| Orphan entries (bib only, not cited) | 5 |
| Missing entries (cited but not in bib) | 0 |
| WebSearch-verified references | 8 |
| Issues found | 7 |

---

## Issues

### Critical (1)

#### 1. `deepseek-r1-2025` — Wrong DOI

**Current bib**: `doi = {10.1038/s41586-025-08636-z}`
**Correct DOI**: `10.1038/s41586-025-09422-z`

The DOI in the bib file does not resolve to the DeepSeek-R1 Nature article. The correct DOI is confirmed via Nature, PubMed (PMID 40962978), and RePEc.

**Action**: Replace DOI with `10.1038/s41586-025-09422-z`.

---

### Warning (3)

#### 2. `deepseek-r1-2025` — Title mismatch (arXiv vs Nature)

**Current bib title**: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
**Nature published title**: "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning"

Since the bib cites the Nature version (journal = Nature, volume = 645, pages = 633–638), the title should match the published version.

**Action**: Update title to Nature published version, or keep arXiv title and add a note. Recommended: use Nature title since journal/volume/pages point to Nature.

#### 3. `deepseek-r1-2025` — Author field

**Current**: `author = {{DeepSeek-AI}}`
**Nature version**: Individual authors listed (Guo, D., Yang, D., Zhang, H., et al.)

Using the collective name is common for arXiv versions but Nature lists individual authors. Since journal=Nature, consider using individual authors.

**Action**: Update to individual author list per the Nature publication, or keep `{DeepSeek-AI}` if brevity is preferred (acceptable but non-standard for Nature citations).

#### 4. Five orphan bib entries (not cited in any .tex file)

| Key | Title |
|-----|-------|
| `compression-ordering-2025` | A Systematic Study of Compression Ordering for Large Language Models |
| `mustafar-neurips2025` | Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning |
| `obcache-2025` | OBCache: Optimal Brain KV Cache Pruning |
| `pagedeviction-eacl2026` | PagedEviction: Structured Block-wise KV Cache Pruning |
| `raas-acl2025` | RaaS: Reasoning-Aware Attention Sparsity |

These entries exist in `references.bib` but are not referenced by any `\cite{}` in the paper. They will not appear in the bibliography but add clutter.

**Action**: Remove orphan entries, or cite them in Related Work if relevant.

---

### Info (3)

#### 5. `pyramidkv-2024` — Potentially published but listed as arXiv

The bib lists PyramidKV as `@article` (arXiv preprint, 2024). OpenReview submissions exist (IDs: `jZVNmDiU86`, `ayi7qezU87`), suggesting it may have been accepted at a venue. No confirmed acceptance found in search results as of May 2026.

**Action**: Verify whether PyramidKV has been formally published; if so, update entry type and venue.

#### 6. Papers mentioned in `paper_framing.md` but absent from bib/tex

The paper framing document (RC5, RC6 sections) identifies the following papers as important for positioning but they are **not** cited in the current paper:

| Paper | arXiv ID | Relevance per framing |
|-------|----------|----------------------|
| Physics of KV Cache Compression | 2603.01426 | Single-axis phase transition vs our phase-dependent gradient |
| HIES (importance score collapse) | 2510.13832 | Independent evidence for discrimination collapse mechanism |
| R-KV (reasoning KV compression) | 2505.24133 | Task-specific method, different goal (optimization vs understanding) |

These are listed in the framing as positioning references for anticipated reviewer concerns RC5 and RC6, but the Related Work section does not include them.

**Action**: Consider adding these to Related Work §2 if the framing analysis is still current, especially HIES (supports the discrimination collapse mechanism) and Physics of KV Cache Compression (closest related work per framing).

#### 7. DOI field inconsistency

Only `deepseek-r1-2025` has a `doi` field. Other published-at-venue entries (e.g., `h2o-neurips2023`, `snapkv-neurips2024`, `slim-icml2025`) lack DOI. This is minor — arXiv URLs are generally sufficient — but adding DOIs for published proceedings would improve discoverability.

**Action**: Optional. Add DOI for published venue papers if available.

---

## WebSearch Verification Results

| Bib Key | Claimed Venue | Verified | Notes |
|---------|---------------|----------|-------|
| `spark-aaai2026` | AAAI 2026 | **Yes** | GitHub confirms "[AAAI 2026]" |
| `thinkv-iclr2026` | ICLR 2026 | **Yes** | ICLR 2026 Oral confirmed |
| `deepseek-r1-2025` | Nature 645, 633–638 | **Yes** | Volume/pages match; DOI incorrect (see #1) |
| `lethe-aaai2026` | AAAI 2026 | **Yes** | AAAI proceedings link confirmed |
| `phase-transition-compression-2026` | npj AI 2026 | **Yes** | Nature.com article confirmed |
| `retentivekv-2026` | arXiv 2605.04075 | **Yes** | arXiv page exists |
| `graspune-acl2026` | ACL 2026 | **Yes** | GitHub confirms "ACL 2026 Main" |
| `slim-icml2025` | ICML 2025 | **Yes** | ICML poster page + NVIDIA Research confirmed |

No hallucinated references detected. All 8 sampled references are real papers with matching titles and authors.

---

## Cross-Reference Matrix

All 26 citation keys used in .tex files have corresponding bib entries:

| Citation Key | Used In |
|-------------|---------|
| `kwon-sosp2023` | introduction |
| `pope-mlsys2023` | introduction |
| `voita-acl2019` | introduction, background, appendix |
| `michel-neurips2019` | introduction, background, appendix |
| `snapkv-neurips2024` | introduction, related_work, discussion |
| `adakv-neurips2025` | introduction, related_work |
| `spark-aaai2026` | introduction, related_work, background, appendix |
| `slim-icml2025` | introduction, related_work |
| `unicomp-2026` | introduction, related_work |
| `phase-transition-compression-2026` | introduction, related_work |
| `decision-repr-transition-2026` | introduction, related_work |
| `sparse-frontier-2025` | introduction, related_work |
| `thinkv-iclr2026` | introduction, related_work, background |
| `greedy-bias-kvcache-2026` | introduction, related_work |
| `retentivekv-2026` | introduction, related_work |
| `lethe-aaai2026` | introduction, related_work |
| `graspune-acl2026` | related_work, background |
| `defensivekv-iclr2026` | related_work, background, appendix |
| `nacl-acl2024` | related_work, background |
| `doing-more-with-less-2026` | related_work |
| `deepseek-r1-2025` | methodology |
| `qwen25-2024` | methodology |
| `math500-neurips2021` | methodology |
| `efron-1993` | methodology |
| `h2o-neurips2023` | discussion |
| `pyramidkv-2024` | discussion |

---

## Bib Entry Completeness

All 31 bib entries have: title, author, year. Format breakdown:

| Type | Count | Required fields present |
|------|-------|------------------------|
| @inproceedings | 18 | All have booktitle |
| @article | 12 | All have journal |
| @book | 1 | Has publisher |

No entries are missing critical fields (title, author, year, venue).
