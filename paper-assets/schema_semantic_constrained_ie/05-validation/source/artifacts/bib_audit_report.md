# Bib Audit Report

**Date:** 2026-05-22
**File:** `artifacts/_project/paper/relwork_new_entries.bib`
**Total entries:** 60
**Verified via:** WebSearch (arXiv, ACL Anthology, OpenReview, DBLP, Semantic Scholar)

## Summary

- ✅ Correct: 54
- ⚠️ Minor issue (no fix needed): 4
- ❌ Fixed: 4

## Fixes Applied

| bib_key | Issue | Severity | Fix |
|---------|-------|----------|-----|
| `paolini2021tanl` | Authors fabricated: "Akyürek, Ben", "Akyürek, Ekin", "Oğuz, Barlas" are NOT authors. Real authors: Paolini, Athiwaratkun, Krone, Ma, Achille, Anubhai, Nogueira dos Santos, Xiang, Soatto (all AWS) | ❌ serious | Replaced full author list |
| `boostcd2025` | 2 fabricated authors: Geng, Saibo and Josifoski, Martin added incorrectly (they co-authored `geng2023gcd`, not this paper). Real authors: Sakota, Marija and West, Robert only | ❌ serious | Removed fabricated authors |
| `ugare2024syncode` | Wrong venue: listed as ICML 2024 (PMLR v235), actual venue is TMLR 2024 | ⚠️ moderate | Changed from @inproceedings to @article, updated journal to TMLR |
| `ugare2025itergen` | Wrong author: "Banerjee, Debangshu" is NOT an author. Correct author: "Gumaste, Rohan" | ⚠️ moderate | Replaced author, corrected author order |

## Minor Issues (not fixed, no action needed)

| bib_key | Note |
|---------|------|
| `synchromesh_iclr2022` | Author "Oleksandr Polozov" — arXiv uses this form; ICLR proceedings use "Alex Polozov". Both are correct. |
| `mgd_neurips2023` | Middle initials "K." on Lahiri/Rajamani present in DBLP but absent from NeurIPS proceedings page. Cosmetic. |
| `cabot2021rebel` | ACL Anthology title has lowercase "generation" vs bib's "Generation". Cosmetic. |
| `zhou2026ontologytools` | Author surname "Bulter" (not "Butler") — matches arXiv listing; likely a typo in the paper itself. |

## Full Verification Table

| bib_key | arXiv/DOI | Title Match | Author Match | Status |
|---------|-----------|-------------|--------------|--------|
| `synchromesh_iclr2022` | arXiv:2201.11227 | ✅ | ⚠️ Oleksandr/Alex | ✅ |
| `mgd_neurips2023` | NeurIPS 2023 | ✅ | ⚠️ middle initials | ✅ |
| `pldi2025_type_constrained_codegen` | DOI:10.1145/3729274 | ✅ | ✅ | ✅ |
| `roth_yih_2004` | ACL W04-2401 | ✅ | ✅ | ✅ |
| `adakgc_emnlp2023` | ACL 2023.findings-emnlp.425 | ✅ | ✅ | ✅ |
| `knowcoder_acl2024` | ACL 2024.acl-long.475 | ✅ | ✅ | ✅ |
| `spires_2024` | DOI:10.1093/bioinformatics/btae104 | ✅ | ✅ | ✅ |
| `ontologx_2025` | arXiv:2510.01409 | ✅ | ✅ | ✅ |
| `ekaw2024_ontology_beam` | arXiv:2411.15666 | ✅ | ✅ | ✅ |
| `scholak2021picard` | ACL 2021.emnlp-main.779 | ✅ | ✅ | ✅ |
| `olasunkanmi2025relate` | arXiv:2509.19057 | ✅ | ✅ | ✅ |
| `zhou2026ontologytools` | arXiv:2602.03439 | ✅ | ⚠️ "Bulter" matches arXiv | ✅ |
| `eberts2020spert` | arXiv:1909.07755 | ✅ | ✅ | ✅ |
| `yan2021pfn` | ACL 2021.emnlp-main.17 | ✅ | ✅ | ✅ |
| `zhong2021frustratingly` | ACL 2021.naacl-main.5 | ✅ | ✅ | ✅ |
| `ye2022packed` | ACL 2022.acl-long.337 | ✅ | ✅ | ✅ |
| `zhou2026snowballing` | arXiv:2604.06066 | ✅ | ✅ | ✅ |
| `dong2025xgrammar` | arXiv:2411.15100 | ✅ | ✅ | ✅ |
| `willard2023outlines` | arXiv:2307.09702 | ✅ | ✅ | ✅ |
| `beurer-kellner2023lmql` | DOI:10.1145/3591300 | ✅ | ✅ | ✅ |
| `beurer-kellner2024domino` | PMLR v235 | ✅ | ✅ | ✅ |
| `park2024grammar` | arXiv:2405.21047 | ✅ | ✅ | ✅ |
| `decao2021genre` | OpenReview 5k8F6UU39V | ✅ | ✅ | ✅ |
| `josifoski2022genie` | ACL 2022.naacl-main.342 | ✅ | ✅ | ✅ |
| `geng2023gcd` | ACL 2023.emnlp-main.674 | ✅ | ✅ | ✅ |
| `lu2021neurologic` | ACL 2021.naacl-main.339 | ✅ | ✅ | ✅ |
| `lu2022uie` | ACL 2022.acl-long.395 | ✅ | ✅ | ✅ |
| `sainz2024gollie` | OpenReview Y3wpuxd7u9 | ✅ | ✅ | ✅ |
| `li2023codeie` | ACL 2023.acl-long.855 | ✅ | ✅ | ✅ |
| `qi2024adelie` | ACL 2024.emnlp-main.419 | ✅ | ✅ | ✅ |
| `zaratiana2024enrico` | arXiv:2404.12493 | ✅ | ✅ | ✅ |
| `khorshidi2025odke` | arXiv:2509.04696 | ✅ | ✅ | ✅ |
| `upadhyay2023openie` | ACL 2023.findings-eacl.95 | ✅ | ✅ | ✅ |
| `regino2025kgcurator` | ACL 2025.genaik-1.10 | ✅ | ✅ | ✅ |
| `tam2024letmespeak` | ACL 2024.emnlp-industry.91 | ✅ | ✅ | ✅ |
| `banerjee2025crane` | PMLR v267 | ✅ | ✅ | ✅ |
| `schall2025hiddencost` | ACL 2025.ranlp-1.124 | ✅ | ✅ | ✅ |
| `cabot2021rebel` | ACL 2021.findings-emnlp.204 | ⚠️ capitalization | ✅ | ✅ |
| `ugare2024syncode` | arXiv:2403.01632 | ✅ | ✅ | ❌→✅ FIXED (venue) |
| `ugare2025itergen` | arXiv:2410.07295 | ✅ | ❌→✅ | ❌→✅ FIXED (author) |
| `boostcd2025` | ACL 2025.emnlp-main.926 | ✅ | ❌→✅ | ❌→✅ FIXED (authors) |
| `luan2018scierc` | ACL D18-1360 | ✅ | ✅ | ✅ |
| `yao2019docred` | ACL P19-1074 | ✅ | ✅ | ✅ |
| `wei2023zeroshot` | arXiv:2302.10205 | ✅ | ✅ | ✅ |
| `qwen2025qwen3` | arXiv:2505.09388 | ✅ | ✅ | ✅ |
| `zheng2024sglang` | arXiv:2312.07104 | ✅ | ✅ | ✅ |
| `li2021document` | ACL 2021.naacl-main.69 | ✅ | ✅ | ✅ |
| `formattax2026` | arXiv:2604.03616 | ✅ | ✅ | ✅ |
| `dccd2026` | arXiv:2603.03305 | ✅ | ✅ | ✅ |
| `guidex2025` | ACL 2025.findings-acl.1245 | ✅ | ✅ | ✅ |
| `jsonschemabench2025` | arXiv:2501.10868 | ✅ | ✅ | ✅ |
| `wang2023instructuie` | arXiv:2304.08085 | ✅ | ✅ | ✅ |
| `wang2022deepstruct` | ACL 2022.findings-acl.67 | ✅ | ✅ | ✅ |
| `zhou2024universalner` | OpenReview r65xfUb76p | ✅ | ✅ | ✅ |
| `lou2023usm` | DOI:10.1609/aaai.v37i11.26563 | ✅ | ✅ | ✅ |
| `wadhwa2023revisiting` | ACL 2023.acl-long.868 | ✅ | ✅ | ✅ |
| `paolini2021tanl` | OpenReview US-TP-xnXI | ✅ | ❌→✅ | ❌→✅ FIXED (authors) |
| `fei2022lasuie` | arXiv:2304.06248 | ✅ | ✅ | ✅ |
| `riedel2010modeling` | ECML-PKDD 2010 | ✅ | ✅ | ✅ |
| `anderson2017guided` | ACL D17-1098 | ✅ | ✅ | ✅ |
