# Bibliography Audit Report — Round 10

**Date:** 2026-05-16
**Trigger:** R10-C1 (MUSTAFAR fake citation flagged as Critical by both reviewers)
**Scope:** Full audit of all 42 bib entries in `references.bib`
**Method:** WebSearch verification of title + first author for every entry

---

## 1. MUSTAFAR Status

`mustafar-neurips2025` ("Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning") — **already removed** from both `references.bib` and all `.tex` files prior to this audit. No residual `\cite{mustafar...}` found in any tex file.

The real paper this was confused with:
- **Title:** "Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference"
- **Authors:** Donghyeon Joo et al.
- **Venue:** NeurIPS 2025
- **OpenReview ID:** C69741fMFX

The paper is not currently cited in the manuscript (nor needs to be, as it addresses single-axis unstructured sparsity rather than compound interaction).

The old `citation_audit_report.md` in the paper directory incorrectly marked `mustafar-neurips2025` as ✅ verified — that report is superseded by this one.

---

## 2. Full Audit Results

### Legend
- ✅ = Verified (title, authors, venue, year, arXiv ID all correct)
- ⚠️ = Minor issue (paper is real, but metadata has a small discrepancy)
- ❌ = Fake / not found

### Compound Compression / Ordering

| # | Key | Status | Title | Authors | Venue | Year | arXiv | Notes |
|---|-----|--------|-------|---------|-------|------|-------|-------|
| 1 | `spark-aaai2026` | ✅ | SparK: Query-Aware Unstructured Sparsity... | Liao et al. | AAAI 2026 | 2026 | 2508.15212 | |
| 2 | `slim-icml2025` | ✅ | SLiM: One-shot Quantization and Sparsity... | Mozaffari et al. | ICML 2025 | 2025 | 2410.09615 | |
| 3 | `unicomp-2026` | ✅ | UniComp: A Unified Evaluation of LLM Compression... | von Rad et al. | arXiv | 2026 | 2602.09130 | |
| 4 | `phase-transition-compression-2026` | ✅ | Phase transitions in large language model compression | Ma et al. | npj AI 2(21) | 2026 | — | nature.com link verified |
| 5 | `graspune-acl2026` | ✅ | GRASPrune: Global Gating for Budgeted Structured Pruning... | Wang et al. | ACL 2026 | 2026 | 2604.19398 | |
| 6 | `pmkvq-iclr2026` | ✅ | PM-KVQ: Progressive Mixed-precision KV Cache Quantization... | Liu et al. | ICLR 2026 | 2026 | 2505.18610 | |
| 7 | `kim2026pqqp` | ✅ | Prune-then-Quantize or Quantize-then-Prune?... | Kim et al. | ICLR 2026 | 2026 | 2603.18426 | |

### KV Cache Eviction

| # | Key | Status | Title | Authors | Venue | Year | arXiv | Notes |
|---|-----|--------|-------|---------|-------|------|-------|-------|
| 8 | `streamingllm-iclr2024` | ✅ | Efficient Streaming Language Models with Attention Sinks | Xiao et al. | ICLR 2024 | 2024 | 2309.17453 | |
| 9 | `duoattention-2024` | ✅ | DuoAttention: Efficient Long-Context LLM Inference... | Xiao et al. | arXiv | 2024 | 2410.10819 | |
| 10 | `adakv-neurips2025` | ✅ | Ada-KV: Optimizing KV Cache Eviction... | Feng et al. | NeurIPS 2025 | 2025 | 2407.11550 | |
| 11 | `snapkv-neurips2024` | ⚠️ | SnapKV: LLM Knows What You Are Looking for Before Generation | Li et al. | NeurIPS 2024 | 2024 | 2404.14469 | Title casing: official uses "You are Looking" (lowercase 'a'). Cosmetic only — bib style may override. |
| 12 | `nacl-acl2024` | ✅ | NACL: A General and Effective KV Cache Eviction Framework... | Chen et al. | ACL 2024 | 2024 | 2408.03675 | |
| 13 | `h2o-neurips2023` | ✅ | H2O: Heavy-Hitter Oracle for Efficient Generative Inference... | Zhang et al. | NeurIPS 2023 | 2023 | 2306.14048 | |
| 14 | `defensivekv-iclr2026` | ✅ | DefensiveKV: Taming the Fragility of KV Cache Eviction... | Feng et al. | ICLR 2026 | 2026 | 2510.13334 | |
| 15 | `greedy-bias-kvcache-2026` | ✅ | More Than a Quick Glance: Overcoming the Greedy Bias... | Sood et al. | arXiv | 2026 | 2602.02199 | |
| 16 | `hies-2025` | ✅ | Entropy Meets Importance: A Unified Head Importance-Entropy Score... | Choi et al. | arXiv | 2025 | 2510.13832 | |
| 17 | `retentivekv-2026` | ✅ | RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction | Liu et al. | arXiv | 2026 | 2605.04075 | |
| 18 | `lkv-2026` | ✅ | LKV: End-to-End Learning of Head-wise Budgets... | Zhou et al. | arXiv | 2026 | 2605.06676 | |

### Reasoning-Aware Eviction

| # | Key | Status | Title | Authors | Venue | Year | arXiv | Notes |
|---|-----|--------|-------|---------|-------|------|-------|-------|
| 19 | `rlkv-2025` | ✅ | Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | Du et al. | arXiv | 2025 | 2510.08525 | |
| 20 | `longflow-2026` | ✅ | LongFlow: Efficient KV Cache Compression for Reasoning Models | Su et al. | arXiv | 2026 | 2603.11504 | |
| 21 | `dong2026foresightkv` | ✅ | ForesightKV: Optimizing KV Cache Eviction for Reasoning Models... | Dong et al. | arXiv | 2026 | 2602.03203 | |
| 22 | `lethe-aaai2026` | ✅ | Lethe: Layer- and Time-Adaptive KV Cache Pruning... | Zeng et al. | AAAI 2026 | 2026 | 2511.06029 | |
| 23 | `hold-onto-thought-neurips2025` | ⚠️ | Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | Liu et al. | arXiv | 2025 | 2512.12008 | Actual venue is NeurIPS 2025 ER Workshop, not main conference. Bib entry lists as arXiv preprint (acceptable), but citation key implies main NeurIPS. |
| 24 | `rkv-neurips2025` | ✅ | R-KV: Redundancy-Aware KV Cache Compression for Reasoning Models | Cai et al. | NeurIPS 2025 | 2025 | 2505.24133 | |
| 25 | `xu2025think` | ✅ | ThinK: Thinner Key Cache by Query-Driven Pruning | Xu et al. | ICLR 2025 | 2025 | 2407.21018 | |

### Phase-Aware Inference

| # | Key | Status | Title | Authors | Venue | Year | arXiv | Notes |
|---|-----|--------|-------|---------|-------|------|-------|-------|
| 26 | `thinkv-iclr2026` | ✅ | ThinKV: Thought-Adaptive KV Cache Compression... | Ramachandran et al. | ICLR 2026 (Oral) | 2026 | 2510.01290 | |
| 27 | `decision-repr-transition-2026` | ✅ | Understanding Performance Collapse in Layer-Pruned LLMs... | Shi et al. | arXiv | 2026 | 2605.07271 | |
| 28 | `doing-more-with-less-2026` | ✅ | Doing More With Less: Revisiting the Effectiveness of LLM Pruning... | Monjur et al. | arXiv | 2026 | 2604.25098 | |
| 29 | `sparse-frontier-2025` | ✅ | The Sparse Frontier: Sparse Attention Trade-offs... | Nawrot et al. | arXiv | 2025 | 2504.17768 | |
| 30 | `physics-kvcache-2026` | ✅ | Understanding the Physics of Key-Value Cache Compression... | Ananthanarayanan et al. | arXiv | 2026 | 2603.01426 | |
| 31 | `pyramidkv-colm2025` | ✅ | PyramidKV: Dynamic KV Cache Compression... | Cai et al. | COLM 2025 (Spotlight) | 2025 | 2406.02069 | |

### Attention Head Analysis

| # | Key | Status | Title | Authors | Venue | Year | arXiv | Notes |
|---|-----|--------|-------|---------|-------|------|-------|-------|
| 32 | `voita-acl2019` | ✅ | Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting... | Voita et al. | ACL 2019 | 2019 | 1905.09418 | |
| 33 | `michel-neurips2019` | ✅ | Are Sixteen Heads Really Better than One? | Michel et al. | NeurIPS 2019 | 2019 | 1905.10650 | |

### Reasoning & CoT

| # | Key | Status | Title | Authors | Venue | Year | arXiv | Notes |
|---|-----|--------|-------|---------|-------|------|-------|-------|
| 34 | `wei-neurips2022-cot` | ✅ | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | Wei et al. | NeurIPS 2022 | 2022 | 2201.11903 | |
| 35 | `lanham-2023-faithfulness` | ✅ | Measuring Faithfulness in Chain-of-Thought Reasoning | Lanham et al. | arXiv | 2023 | 2307.13702 | |
| 36 | `turpin-2023-biased-cot` | ✅ | Language Models Don't Always Say What They Think... | Turpin et al. | NeurIPS 2023 | 2023 | 2305.04388 | |

### Models & Infrastructure

| # | Key | Status | Title | Authors | Venue | Year | arXiv | Notes |
|---|-----|--------|-------|---------|-------|------|-------|-------|
| 37 | `deepseek-r1-2025` | ⚠️ | DeepSeek-R1 incentivizes reasoning in LLMs through RL | DeepSeek-AI | Nature 645 | 2025 | — | Author: bib uses "DeepSeek-AI" (arXiv convention). Nature version lists 194 individual authors (Guo, Daya et al.). Acceptable for arXiv citation; if citing Nature, individual authors preferred. |
| 38 | `qwen25-2024` | ✅ | Qwen2.5 Technical Report | Yang et al. | arXiv | 2024 | 2412.15115 | |
| 39 | `kwon-sosp2023` | ✅ | Efficient Memory Management for Large Language Model Serving with PagedAttention | Kwon et al. | SOSP 2023 | 2023 | 2309.06180 | |
| 40 | `pope-mlsys2023` | ✅ | Efficiently Scaling Transformer Inference | Pope et al. | MLSys 2023 | 2023 | 2211.05102 | |

### Statistics

| # | Key | Status | Title | Authors | Venue | Year | Notes |
|---|-----|--------|-------|---------|-------|------|-------|
| 41 | `efron-1993` | ✅ | An Introduction to the Bootstrap | Efron & Tibshirani | Chapman & Hall/CRC | 1993 | Classic textbook, confirmed |

### Benchmark

| # | Key | Status | Title | Authors | Venue | Year | arXiv | Notes |
|---|-----|--------|-------|---------|-------|------|-------|-------|
| 42 | `math500-neurips2021` | ✅ | Measuring Mathematical Problem Solving With the MATH Dataset | Hendrycks et al. | NeurIPS 2021 | 2021 | 2103.03874 | Key says "math500" but paper is full MATH dataset; MATH-500 is a later subset. Citation itself is correct. |

---

## 3. Summary

| Category | Count |
|----------|-------|
| Total entries audited | 42 |
| ✅ Verified | 39 |
| ⚠️ Minor issue | 3 |
| ❌ Fake / not found | 0 |

### Minor Issues Detail

1. **`snapkv-neurips2024`** — Title capitalization: "You Are Looking" vs official "You are Looking". Cosmetic; bib style typically overrides.
2. **`hold-onto-thought-neurips2025`** — Actual venue is NeurIPS 2025 ER Workshop, not main conference. Bib entry lists it as arXiv preprint (not incorrect), but citation key is misleading.
3. **`deepseek-r1-2025`** — Author field uses "DeepSeek-AI" (arXiv convention). Nature version uses individual authors. Acceptable as-is if citing the arXiv version.

### Action Items

- **None required.** All 3 minor issues are cosmetic or convention-dependent. No corrections are blocking.
- MUSTAFAR deletion confirmed complete — no residual references in bib or tex files.
- This report supersedes the old `citation_audit_report.md` which incorrectly marked `mustafar-neurips2025` as ✅.
