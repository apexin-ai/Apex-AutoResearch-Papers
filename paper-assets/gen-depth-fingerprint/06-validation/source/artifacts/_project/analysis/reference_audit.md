# Reference Audit — 2026-05-21

## Summary
- Total entries: 66
- Previously audited (2026-05-15): 43 (of which 3 since removed: generator_barrier, intrinsic_dimension, ood_baseline)
- Newly audited: 26
- Errors found and fixed: 4
- Errors found:
  - `attractor_cycles`: **CRITICAL** — 9 completely hallucinated authors + truncated title → replaced with correct 5 authors (Wang Zhilin, Li Yafu, Yan Jianhao, Cheng Yu, Zhang Yue), full title, added arXiv ID 2502.15208
  - `ghostbuster`: wrong last author (Jurafsky, Dan → Klein, Dan) + wrong venue (ACL → NAACL 2024)
  - `qlora`: title "Quantized Language Models" → "Quantized LLMs" (official NeurIPS title)
  - `aaronson_watermark`: author "Kirchner, Hendrik" → "Kirchner, Jan Hendrik" (known fix from prior audit)

## Priority 4 — Detailed Verification

### schaeffer_collapse_position
- Title: ✓ "Position: Model Collapse Does Not Mean What You Think"
- Authors: ✓ Schaeffer, Rylan; Kazdan, Joshua; Arulandu, Alvan Caleb; Koyejo, Sanmi
- Venue: ✓ ICML (Proceedings of the International Conference on Machine Learning)
- Year: ✓ 2025
- arXiv: ✓ 2503.03150

### drayson_detection_prevents_collapse
- Title: ✓ "Machine-Generated Text Detection Prevents Language Model Collapse"
- Authors: ✓ Drayson, George; Yilmaz, Emine; Lampos, Vasileios
- Venue: ✓ EMNLP 2025 (Proceedings of the Conference on Empirical Methods in Natural Language Processing)
- Year: ✓ 2025
- arXiv: ✓ 2502.15654

### seddik_synthetic_data
- Title: ✓ "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
- Authors: ✓ Seddik, Mohamed El Amine; Chen, Suei-Wen; Hayou, Soufiane; Youssef, Pierre; Debbah, Merouane
- Venue: ✓ arXiv preprint arXiv:2404.05090
- Year: ✓ 2024

### attractor_cycles
- Title: ✗ → FIXED. Was "Unveiling Attractor Cycles in {LLM}s", should be "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing"
- Authors: ✗ → FIXED. All 9 authors were hallucinated (Wang Yibo, Li Haotian, Tan Boyu, Liu Yi, Huang Xuming, Chen Hongxia, Li Lei, Huang Xuanjing, Xie Zhongyu). Correct authors: Wang Zhilin, Li Yafu, Yan Jianhao, Cheng Yu, Zhang Yue
- Venue: ✓ ACL 2025 (confirmed via ACL Anthology 2025.acl-long.624)
- Year: ✓ 2025
- arXiv: added 2502.15208 (was missing)

## Batch Verification (22 entries)

| Key | Title | First Author | Year | Venue | Status |
|-----|-------|-------------|------|-------|--------|
| beyond_binary | ✓ | ✓ Cheng, Zihao | ✓ 2025 | ✓ ACM Web Conference | OK |
| beyond_final_actor | ✓ | ✓ Li, Yang | ✓ 2026 | ✓ ACL | OK |
| cohen1988statistical | ✓ | ✓ Cohen, Jacob | ✓ 1988 | ✓ Lawrence Erlbaum | OK |
| coral_ordinal | ✓ | ✓ Cao, Wenzhi | ✓ 2020 | ✓ Pattern Recognition Letters | OK |
| corn_ordinal | ✓ | ✓ Shi, Xintong | ✓ 2023 | ✓ Pattern Analysis and Applications | OK |
| dolma | ✓ | ✓ Soldaini, Luca | ✓ 2024 | ✓ ACL | OK |
| fineweb | ✓ | ✓ Penedo, Guilherme | ✓ 2024 | ✓ NeurIPS D&B | OK |
| frank_hall_ordinal | ✓ | ✓ Frank, Eibe | ✓ 2001 | ✓ ECML | OK |
| ghostbuster | ✗ author, ✗ venue | ✓ Verma, Vivek | ✓ 2024 | ✗ ACL→NAACL | FIXED |
| gutierrez_ordinal_survey | ✓ | ✓ Gutierrez, P.A. | ✓ 2016 | ✓ IEEE TKDE | OK |
| kasa_ordinality_nlp | ✓ | ✓ Kasa, Siva Rajesh | ✓ 2024 | ✓ Findings ACL | OK |
| koike_mia_detection | ✓ | ✓ Koike, Ryuto | ✓ 2025 | ✓ arXiv | OK |
| lakens_equivalence | ✓ | ✓ Lakens, Daniel | ✓ 2017 | ✓ SPPS | OK |
| llama3 | ✓ | ✓ Grattafiori, Aaron | ✓ 2024 | ✓ arXiv | OK |
| mistral7b | ✓ | ✓ Jiang, Albert Q. | ✓ 2023 | ✓ arXiv | OK |
| munir_looking_glass | ✓ | ✓ Munir, Shaoor | ✓ 2021 | ✓ EACL | OK |
| qlora | ✗ title | ✓ Dettmers, Tim | ✓ 2023 | ✓ NeurIPS | FIXED |
| raid | ✓ | ✓ Dugan, Liam | ✓ 2024 | ✓ ACL | OK |
| semeval2024_task8 | ✓ | ✓ Wang, Yuxia | ✓ 2024 | ✓ SemEval | OK |
| strobl_conditional_2008 | ✓ | ✓ Strobl, Carolin | ✓ 2008 | ✓ BMC Bioinformatics | OK |
| two_birds | ✓ | ✓ Rao, Zixin | ✓ 2025 | ✓ arXiv | OK |
| wu_survey_2025 | ✓ | ✓ Wu, Junchao | ✓ 2025 | ✓ Computational Linguistics | OK |

## Known Fix
- `aaronson_watermark`: author "Kirchner, Hendrik" → "Kirchner, Jan Hendrik" (carried over from 2026-05-15 audit finding)

## Verification Method
- Each entry verified via WebSearch for paper title + first author
- Cross-referenced against arXiv, ACL Anthology, publisher pages, and Semantic Scholar
- All 26 new entries individually verified; no entry judged from LLM training data alone
