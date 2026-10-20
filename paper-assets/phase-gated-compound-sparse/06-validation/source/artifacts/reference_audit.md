# Reference Audit

## Summary: 30 entries / 30 cited / 3 issues

All 30 bib entries are cited; all 30 citation keys in tex files have corresponding bib entries. Every entry was verified against arXiv/publisher via web search — **no hallucinated references found**.

## Missing references (cited but not in bib)

None.

## Orphan entries (in bib but never cited)

None.

## Incomplete entries (missing fields)

None. All entries have author, title, year, and venue (booktitle/journal/publisher). `efron1993bootstrap` lacks a URL, which is acceptable for a classic 1993 book.

## Suspicious entries (potential hallucinations)

**None.** All 30 entries verified as real via web search:

| Key | Verified Source |
|-----|----------------|
| adakv-neurips2025 | arXiv:2407.11550, NeurIPS 2025 poster confirmed |
| compression-ordering-2025 | arXiv:2511.19495 confirmed |
| decision-repr-transition-2026 | arXiv:2605.07271 confirmed |
| deepseek-r1 | Nature vol.645 pp.633–638 (2025) confirmed |
| defensivekv-iclr2026 | arXiv:2510.13334, ICLR 2026 confirmed (OpenReview) |
| doing-more-with-less-2026 | arXiv:2604.25098 confirmed |
| efron1993bootstrap | Classic textbook, widely cited |
| graspune-acl2026 | arXiv:2604.19398, ACL 2026 Main confirmed (GitHub) |
| greedy-bias-kvcache-2026 | arXiv:2602.02199 confirmed, authors match |
| h2o2024 | arXiv:2306.14048, NeurIPS 2023 confirmed |
| kwon2023vllm | arXiv:2309.06180, SOSP 2023 confirmed |
| math500 | arXiv:2103.03874, NeurIPS 2021 confirmed |
| michel2019sixteen | arXiv:1905.10650, NeurIPS 2019 confirmed |
| mustafar-neurips2025 | arXiv:2505.22913, NeurIPS 2025 poster confirmed |
| nacl-acl2024 | arXiv:2408.03675, ACL 2024 confirmed |
| obcache-2025 | arXiv:2510.07651 confirmed |
| pagedeviction-eacl2026 | arXiv:2509.04377, EACL 2026 Findings confirmed (ACL Anthology) |
| phase-transition-compression-2026 | Nature npj AI vol.2 no.21 (2026) confirmed |
| pope2023efficiently | arXiv:2211.05102, MLSys 2023 confirmed |
| pyramidkv2024 | arXiv:2406.02069 confirmed |
| qwen2.5 | arXiv:2412.15115 confirmed |
| raas-acl2025 | arXiv:2502.11147, ACL 2025 Findings confirmed (ACL Anthology) |
| retentivekv-2026 | arXiv:2605.04075 confirmed |
| slim-icml2025 | arXiv:2410.09615, ICML 2025 confirmed |
| snapkv-neurips2024 | arXiv:2404.14469, NeurIPS 2024 confirmed |
| spark-aaai2026 | arXiv:2508.15212, AAAI 2026 confirmed (GitHub) |
| sparse-frontier-2025 | arXiv:2504.17768 confirmed |
| thinkv-iclr2026 | arXiv:2510.01290, ICLR 2026 Oral confirmed |
| unicomp-2026 | arXiv:2602.09130 confirmed |
| voita2019heads | arXiv:1905.09418, ACL 2019 confirmed |

## Format issues

### 1. Key naming inconsistency (h2o2024)

`h2o2024`: Key contains "2024" but `year = {2023}` and venue is NeurIPS 2023. Recommend renaming to `h2o-neurips2023` or `h2o2023` to match the actual publication year.

### 2. Mixed key naming conventions

Three conventions are used across the 30 entries:

| Convention | Examples | Count |
|-----------|---------|-------|
| `name-venue-year` | adakv-neurips2025, snapkv-neurips2024, thinkv-iclr2026 | 11 |
| `name-year` | compression-ordering-2025, obcache-2025, unicomp-2026 | 9 |
| `authorYear` | kwon2023vllm, voita2019heads, efron1993bootstrap | 5 |
| Other | deepseek-r1, qwen2.5, math500, h2o2024, pyramidkv2024 | 5 |

Not a correctness issue, but standardizing to one convention (recommend `name-venue-year`) would improve maintainability.

### 3. DeepSeek-R1 title discrepancy

The bib uses the arXiv title: *"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"*

The Nature published title is: *"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning"*

Since the bib entry cites Nature as the journal, the title should match the published version.

---

*Audit date: 2026-05-14. All arXiv IDs and venue claims verified via web search.*
