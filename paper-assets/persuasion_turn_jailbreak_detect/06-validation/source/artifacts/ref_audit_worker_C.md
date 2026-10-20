# Reference Audit Report — Worker C

**Date**: 2026-05-26
**Auditor**: Worker C (independent verification)
**File**: `docs/paper/references.bib`

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total .bib entries | 91 |
| Verified correct (✓) | 62 |
| P0 — Critical errors | 8 |
| P1 — Significant errors | 8 |
| P2 — Minor issues | 5 |
| Duplicate entries | 2 pairs (4 entries) |
| Uncited entries | 18 |
| Entries with any issue | 25 |

---

## P0 — Critical Errors (must fix before submission)

### P0-1: `hsu2024improved` — FABRICATED AUTHORS
- **Issue**: arXiv 2412.01547 is authored by **Erick Galinkin and Martin Sablotny**, NOT "Hsu, Erick and Hsu, Ikuya and Chung, Paul". The listed authors are entirely fabricated. Title is also slightly wrong: actual title is "Improved **Large Language Model** Jailbreak Detection via Pretrained Embeddings" (not "Improved LLM Jailbreak Detection").
- **Also**: Duplicate of `galinkin2024improved` (entry 91), which has the correct authors. Neither entry is cited in any .tex file.
- **Fix**: Delete `hsu2024improved` entirely. If needed, cite `galinkin2024improved` instead.
- **Source**: [arXiv:2412.01547](https://arxiv.org/abs/2412.01547)

### P0-2: `li2025m2s` — WRONG TITLE AND AUTHORS
- **Issue**: arXiv 2503.04856 is titled **"M2S: Multi-turn to Single-turn jailbreak in Red Teaming for LLMs"** and authored by **Junwoo Ha, Hyunjun Kim, Sangyoon Yu, Haon Park, Ashkan Yousefpour, Yuna Park, Suhyun Kim**. The bib entry lists completely wrong authors (Li, Minxuan; Liu, Yue; Chen, Siyuan; etc.) and a fabricated subtitle ("Converting Multi-Turn Jailbreak Attacks to Single-Turn for Enhanced Safety Guardrails").
- **Not cited** in any .tex file.
- **Fix**: Replace title and entire author list. Or delete if unused.
- **Source**: [arXiv:2503.04856](https://arxiv.org/abs/2503.04856), [ACL Anthology](https://aclanthology.org/2025.acl-long.805/)

### P0-3: `wang2026trajguard` — WRONG TITLE AND AUTHORS
- **Issue**: arXiv 2604.07727 is titled **"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense"** and authored by **Cheng Liu, Xiaolei Liu, Xingyu Li, Bangzhou Xin, Kangyi Ding**. The bib entry lists "Wang, Yifan and others" as authors and a fabricated subtitle ("Trajectory-Based Hidden-State Detection of Multi-Turn Jailbreak Attacks").
- **Not cited** in any .tex file.
- **Fix**: Replace title and entire author list. Or delete if unused.
- **Source**: [arXiv:2604.07727](https://arxiv.org/abs/2604.07727)

### P0-4: `marchiori2025jdapt` — WRONG TITLE AND AUTHOR NAME
- **Issue**: arXiv 2509.23281 is titled **"Preventing Robotic Jailbreaking via Multimodal Domain Adaptation"** (NOT "J-DAPT: CORAL-Based Domain Adaptation with Cross-Modal Fusion for Multimodal Robotic Jailbreak Detection"). First author is **Francesco Marchiori** (NOT "Andrea"). Full authors: Francesco Marchiori, Rohan Sinha, Christopher Agia, Alexander Robey, George J. Pappas, Mauro Conti, Marco Pavone.
- **Not cited** in any .tex file.
- **Fix**: Correct title, author first name, and full author list. Or delete if unused.
- **Source**: [arXiv:2509.23281](https://arxiv.org/abs/2509.23281)

### P0-5: `phute2023selfdefense` — WRONG AUTHORS
- **Issue**: arXiv 2308.07308 actual authors are **Mansi Phute, Alec Helbling, Matthew Hull, ShengYun Peng, Sebastian Szyller, Cory Cornelius, Duen Horng Chau**. The bib entry has multiple errors: "Helber" → **Helbling**; "ShiNung Peng" → **ShengYun Peng**; "Szyber" → **Szyller**; "Caliskan, Aylin" and "Khashabi, Daniel" are **NOT authors** of this paper; missing authors **Cory Cornelius** and **Duen Horng Chau**.
- **Not cited** in any .tex file.
- **Fix**: Replace entire author list. Or delete if unused.
- **Source**: [arXiv:2308.07308](https://arxiv.org/abs/2308.07308)

### P0-6: `ren2024actorattack` — WRONG TITLE AND VENUE
- **Issue**: The paper at arXiv 2410.10700 is titled **"LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts"**, NOT "ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory". "ActorAttack" (also called ActorBreaker) is the method name, not the paper title. Venue is **ACL 2025 Main Conference**, NOT ICLR 2025.
- **Cited** in tex files.
- **Fix**: Correct title to "LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts"; change booktitle to ACL 2025; add arXiv ID 2410.10700.
- **Source**: [arXiv:2410.10700](https://arxiv.org/abs/2410.10700), [ACL Anthology](https://aclanthology.org/2025.acl-long.1207/)

### P0-7: `mehrotra2024tap` — WRONG TITLE
- **Issue**: Actual title is **"Tree of Attacks: Jailbreaking Black-Box LLMs Automatically"**, NOT "Tree of Attacks: Jailbreaking Black-Box LLMs with the Pruning of Candidate Outputs". The subtitle is fabricated.
- **Cited** in tex files.
- **Fix**: Change title to "Tree of Attacks: Jailbreaking Black-Box LLMs Automatically".
- **Source**: [NeurIPS 2024 proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/70702e8cbb4890b4a467b984ae59828a-Abstract-Conference.html)

### P0-8: `anthropic2025constitutional` — WRONG AUTHOR
- **Issue**: "Korbak, Tomek" is **NOT** an author on arXiv 2501.18837. The actual authors are Mrinank Sharma, Meg Tong, Jesse Mu, Jerry Wei, Jorrit Kruthoff, Scott Goodfriend, Euan Ong, Alwin Peng, and many others (~40 total). Tomasz Korbak does not appear.
- **Cited** in tex files.
- **Fix**: Remove "Korbak, Tomek" from author list; consider replacing with accurate key authors or using "and others" more carefully.
- **Source**: [arXiv:2501.18837](https://arxiv.org/abs/2501.18837)

---

## P1 — Significant Errors (should fix)

### P1-1: `robey2024smoothllm` — WRONG VENUE
- **Issue**: Entry says `booktitle = {Proceedings of the 41st International Conference on Machine Learning}` (= ICML 2024). Paper was **NOT** published at ICML 2024. It appeared at the ICLR 2024 Workshop on Reliable and Responsible Foundation Models. No evidence of main conference acceptance at ICML.
- **Cited** in tex files.
- **Fix**: Change venue. Either cite as arXiv preprint or as ICLR 2024 Workshop.
- **Source**: [arXiv:2310.03684](https://arxiv.org/abs/2310.03684), [OpenReview (ICLR 2024 Workshop)](https://openreview.net/pdf?id=ZnTpF6Vf68)

### P1-2: `gguard2025` — TITLE MISMATCH
- **Issue**: Entry title "An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs". Actual arXiv title is **"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak"** (no leading "An"; "Defense" not "Defender"; different word order at end).
- **Cited** in tex files.
- **Fix**: Correct title to match arXiv.
- **Source**: [arXiv:2507.07146](https://arxiv.org/abs/2507.07146)

### P1-3: `fitd2024` — MISSING AUTHOR
- **Issue**: Missing author **"Francis Song"** (3rd author). Full author list: Wang, Zhenhua; Xie, Wei; **Song, Francis**; Wang, Baosheng; Wang, Enze; Gui, Zhiwen; Ma, Shuoyoucheng; Chen, Kai.
- **Cited** in tex files.
- **Fix**: Add "Song, Francis" as 3rd author.
- **Source**: [arXiv:2402.15690](https://arxiv.org/abs/2402.15690)

### P1-4: `qwen3_2025` — WRONG NAMED AUTHORS
- **Issue**: The entry lists "Wang, Binyuan" but no such author exists on the paper (should be **Binyuan Hui**); "Li, Bo" should be **Bo Zheng**; "Lin, Bowen" should be **Bowen Yu**. The first names were incorrectly paired with wrong surnames.
- **Cited** in tex files.
- **Fix**: Replace with `{Qwen Team}` or correct the named authors to match [arXiv:2505.09388](https://arxiv.org/abs/2505.09388).
- **Source**: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

### P1-5: `chao2024jailbreakbench` — INCOMPLETE AUTHORS, MISSING VENUE
- **Issue**: Only 6 of 12 authors listed. Missing: Edoardo Debenedetti, Maksym Andriushchenko, Francesco Croce, Vikash Sehwag, Nicolas Flammarion, Florian Tramèr. Also, paper was published at **NeurIPS 2024 Datasets & Benchmarks Track** but entry only cites arXiv.
- **Cited** in tex files.
- **Fix**: Add missing authors; change to `@inproceedings` with `booktitle = {NeurIPS}` and `year = {2024}`.
- **Source**: [arXiv:2404.01318](https://arxiv.org/abs/2404.01318), [NeurIPS 2024](https://dl.acm.org/doi/10.5555/3737916.3739661)

### P1-6: `jiang2024redqueen` — WRONG YEAR, MISSING VENUE
- **Issue**: Paper was published at **Findings of ACL 2025** (year=2025), not just arXiv 2024. Entry has `year = {2024}` and no booktitle. 
- **Cited** in tex files.
- **Fix**: Change `year` to 2025; add `booktitle = {Findings of the Association for Computational Linguistics: ACL 2025}`.
- **Source**: [ACL Anthology](https://aclanthology.org/2025.findings-acl.1311/)

### P1-7: `mann1988rst` — WRONG JOURNAL NAME
- **Issue**: Journal is listed as "Text & Talk". The journal was renamed to "Text & Talk" in 2008. In 1988, the journal was simply **"Text"** (full: *Text — Interdisciplinary Journal for the Study of Discourse*).
- **Cited** in tex files.
- **Fix**: Change `journal` to `Text` or `Text --- Interdisciplinary Journal for the Study of Discourse`.

### P1-8: `lu2025xboundary` — TITLE MISMATCH WITH PUBLISHED VERSION
- **Issue**: Entry title includes "Multi-Turn Jailbreaks" but the published ACL Anthology title is **"X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Jailbreak Attacks without Compromising Usability"** (drops "Multi-Turn"). The arXiv version has "Multi-Turn" but the official published version does not.
- **Cited** in tex files.
- **Fix**: Update title to match the published Findings of EMNLP 2025 version.
- **Source**: [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.282/)

---

## P2 — Minor Issues (nice to fix)

### P2-1: `metallamaguard3_2024` — INFORMAL CITATION
- **Issue**: No standalone paper titled "Llama Guard 3" exists. It was released as a model card with Llama 3.1 (July 2024). Citing as `@misc` with `howpublished` is acceptable but non-standard. The Llama 3.1 herd paper (arXiv:2407.21783) is the closest formal citation.
- **Cited** in tex files.

### P2-2: `han2024wildguard` — MINOR CAPITALIZATION
- **Issue**: Title has "One-Stop" (capital S); the official title uses "One-stop" (lowercase s).
- **Cited** in tex files.
- **Source**: [arXiv:2406.18495](https://arxiv.org/abs/2406.18495)

### P2-3: `zeng2024pap` — GENERIC BOOKTITLE
- **Issue**: `booktitle = {Proceedings of the Association for Computational Linguistics}` is too generic. Should be "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics" or "ACL 2024".
- **Cited** in tex files.

### P2-4: `beltagy2019scibert` — VENUE ABBREVIATION
- **Issue**: The 2019 event was a joint conference: EMNLP-IJCNLP 2019. Entry lists only "EMNLP". Standard practice often shortens this, so it's borderline acceptable.
- **Cited** in tex files.

### P2-5: `song2026multibreak` — UNVERIFIED VENUE, POSSIBLE TITLE VARIANT
- **Issue**: Listed as ICML 2026, but acceptance cannot be independently verified yet (conference not concluded). OpenReview version has slightly different subtitle ("Stress-testing" vs "Evaluating LLM Safety").
- **Cited** in tex files.
- **Source**: [arXiv:2605.01687](https://arxiv.org/abs/2605.01687)

---

## Duplicate Entries (2 pairs)

### DUP-1: `shen2025antidote` (entry 81) ↔ `shen2024jailbreakantidote` (entry 88)
- **Same paper**: arXiv 2410.02298, same title, same authors.
- Entry 81: `@inproceedings`, year=2025, booktitle=ICLR — correctly formatted for venue.
- Entry 88: `@article`, year=2024, note="ICLR 2025" — preprint-style formatting.
- **`shen2024jailbreakantidote` is cited** in tex; `shen2025antidote` is NOT cited.
- **Fix**: Keep one entry. Prefer the `@inproceedings` format (entry 81) with booktitle=ICLR 2025. Update all `\cite{shen2024jailbreakantidote}` to the kept key.

### DUP-2: `hsu2024improved` (entry 82) ↔ `galinkin2024improved` (entry 91)
- **Same arXiv ID**: 2412.01547.
- Entry 82 has **fabricated authors** (Hsu/Hsu/Chung) — see P0-1.
- Entry 91 has correct authors (Galinkin, Sablotny).
- **Neither is cited** in tex.
- **Fix**: Delete `hsu2024improved`. Keep `galinkin2024improved` if needed, or delete both if unused.

---

## Uncited Entries (18 total)

Entries present in .bib but not referenced by any `\cite`/`\citep`/`\citet` in any .tex file:

| # | Key | Status | Note |
|---|-----|--------|------|
| 1 | `zou2023gcg` | ✓ Correct | Well-known GCG paper; consider citing or removing |
| 2 | `he2021deberta` | ✓ Correct | DeBERTa v1; v3 (`he2023debertav3`) is cited |
| 3 | `devlin2019bert` | ✓ Correct | Foundational BERT paper |
| 4 | `chen2020simclr` | ✓ Correct | SimCLR; contrastive learning |
| 5 | `grill2020byol` | ✓ Correct | BYOL; self-supervised learning |
| 6 | `marchiori2025jdapt` | ✗ P0 errors | Wrong title + author name (see P0-4) |
| 7 | `wang2026trajguard` | ✗ P0 errors | Wrong title + authors (see P0-3) |
| 8 | `templeton2024saemitigators` | ✓ Correct | SAE / monosemanticity paper |
| 9 | `alon2023perplexity` | ✓ Correct | Perplexity-based attack detection |
| 10 | `phute2023selfdefense` | ✗ P0 errors | Wrong authors (see P0-5) |
| 11 | `nian2025jaildam` | ✓ Correct | JailDAM, COLM 2025 |
| 12 | `anil2024manyshot` | ✓ Correct | Many-shot jailbreaking, NeurIPS 2024 |
| 13 | `jain2023baseline` | ✓ Correct | Baseline defenses |
| 14 | `li2025m2s` | ✗ P0 errors | Wrong title + authors (see P0-2) |
| 15 | `li2025repejailbreak` | ✓ Correct | COLING 2025, representation engineering |
| 16 | `shen2025antidote` | Duplicate | Same as cited `shen2024jailbreakantidote` (see DUP-1) |
| 17 | `hsu2024improved` | ✗ P0 + Dup | Fabricated authors + duplicate of `galinkin2024improved` (see P0-1, DUP-2) |
| 18 | `galinkin2024improved` | Duplicate | Correct entry but duplicate of `hsu2024improved` (see DUP-2) |

---

## Full Entry-by-Entry Verification (91 entries)

### Category 1: Production Multi-Turn Safety Systems

**1. `inan2023llamaguard`** ✓
- Title: Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations — correct
- Authors: all 11 authors verified correct
- Year: 2023 — correct
- arXiv: 2312.06674 — correct
- Source: [arXiv:2312.06674](https://arxiv.org/abs/2312.06674)

**2. `metallamaguard3_2024`** ✓ (P2 — informal)
- No standalone arXiv paper; model card released with Llama 3.1 (July 2024). Acceptable as informal citation.
- Source: Meta AI Llama 3.1 release

**3. `zeng2024shieldgemma`** ✓
- Title, all 12 authors, year 2024, arXiv 2407.21772 — all correct
- Source: [arXiv:2407.21772](https://arxiv.org/abs/2407.21772)

**4. `han2024wildguard`** ✓ (P2 — capitalization)
- Title: "One-Stop" should be "One-stop" (lowercase s)
- Authors, year, venue (NeurIPS 2024) — correct
- Source: [arXiv:2406.18495](https://arxiv.org/abs/2406.18495)

**5. `anthropic2025constitutional`** ✗ (P0)
- "Korbak, Tomek" is NOT an author. See P0-8.
- Source: [arXiv:2501.18837](https://arxiv.org/abs/2501.18837)

### Category 2: Multi-Turn Jailbreak Defenses

**6. `deepcontext2026`** ✓
- Title, authors (Albrethsen, Datta, Kumar, Rajasekar), year 2026, arXiv 2602.16935 — all correct
- Source: [arXiv:2602.16935](https://arxiv.org/abs/2602.16935)

**7. `tong2025biid`** ✓
- Title, all 7 authors, year 2025, arXiv 2509.22732 — all correct
- Source: [arXiv:2509.22732](https://arxiv.org/abs/2509.22732)

**8. `gguard2025`** ✗ (P1)
- Title mismatch. See P1-2.
- Authors, year 2025, arXiv 2507.07146 — correct
- Source: [arXiv:2507.07146](https://arxiv.org/abs/2507.07146)

**9. `safedream2026`** ✓
- Title, authors (Yan, Lin, Zhu, Wang), year 2026, arXiv 2604.16824 — all correct
- Source: [arXiv:2604.16824](https://arxiv.org/abs/2604.16824)

**10. `bullwinkel2025repeng`** ✓
- Title, all 11 authors, year 2025, arXiv 2507.02956 — all correct
- Source: [arXiv:2507.02956](https://arxiv.org/abs/2507.02956)

### Category 3: Discourse Analysis in NLP

**11. `mann1988rst`** ✗ (P1)
- Journal name wrong: "Text & Talk" → should be "Text". See P1-7.
- Title, authors, year, volume/number/pages — correct

**12. `prasad2008pdtb`** ✓
- Title, all 7 authors, year 2008, venue LREC — all correct
- Source: ACL Anthology L08-1093

**13. `stolcke2000dialogueact`** ✓
- Title, all 10 authors, year 2000, journal/volume/pages — all correct
- Source: ACL Anthology J00-3003

**14. `austin1962speechacts`** ✓
- Title, author, year, publisher — all correct

**15. `searle1969speechacts`** ✓
- Title, author, year, publisher — all correct

### Category 4: Computational Persuasion Detection

**16. `cialdini2001influence`** ✓
- Title, author, year, publisher, edition — all correct

### Category 5: Jailbreak Attacks & Taxonomies

**17. `zeng2024pap`** ✓ (P2 — generic booktitle)
- Title, all 6 authors, year 2024 — correct. Booktitle is generic. See P2-3.
- Source: ACL 2024

**18. `russinovich2024crescendo`** ✓
- Title, authors (Russinovich, Salem, Eldan), arXiv 2404.01833 — correct
- Year: 2025 (USENIX Security 2025) — correct for published venue
- Source: [arXiv:2404.01833](https://arxiv.org/abs/2404.01833)

**19. `chao2023pair`** ✓
- Title, all 6 authors, arXiv 2310.08419 — correct
- Year: 2025 (IEEE SaTML 2025) — correct for published venue
- Source: [arXiv:2310.08419](https://arxiv.org/abs/2310.08419)

**20. `wei2023jailbroken`** ✓
- Title, all 3 authors, year 2023, venue NeurIPS — all correct
- Source: NeurIPS 2023 proceedings

**21. `hagendorff2026reasoning`** ✓
- Title, authors, year 2026, Nature Communications vol. 17, p. 1435, DOI — all correct
- Source: doi:10.1038/s41467-026-69010-1

**22. `fitd2024`** ✗ (P1)
- Missing author "Francis Song" (3rd author). See P1-3.
- Title, year, arXiv 2402.15690 — correct
- Source: [arXiv:2402.15690](https://arxiv.org/abs/2402.15690)

**23. `deceptivedelight2024`** ✓
- Published as tech report by Palo Alto Networks Unit 42 (2024). No arXiv. Acceptable.

**24. `ren2024actorattack`** ✗ (P0)
- Wrong title and venue. See P0-6.
- Source: [arXiv:2410.10700](https://arxiv.org/abs/2410.10700), [ACL Anthology](https://aclanthology.org/2025.acl-long.1207/)

**25. `zou2023gcg`** ✓ (UNCITED)
- Title, all 6 authors, year 2023, arXiv 2307.15043 — all correct
- Source: [arXiv:2307.15043](https://arxiv.org/abs/2307.15043)

### Category 5b: Human Jailbreak Datasets

**26. `lin2023toxicchat`** ✓
- Title, all 7 authors, year 2023, venue Findings EMNLP 2023, pages — all correct
- Source: ACL Anthology

### Category 6: Red-Teaming

**27. `li2024mhj`** ✓
- Title, all 9 authors, year 2024, arXiv 2408.15221 — all correct
- Source: [arXiv:2408.15221](https://arxiv.org/abs/2408.15221)

### Category 7: Annotation Artifacts & Dataset Biases

**28. `gururangan2018artifacts`** ✓
- Title, all 6 authors, year 2018, venue NAACL — all correct
- Source: ACL Anthology N18-2017

**29. `niven2019probing`** ✓
- Title, authors, year 2019, venue ACL — all correct
- Source: ACL Anthology P19-1459

### Category 8: Adaptive Attacks on Classifiers

**30. `nasr2025attackermovessecond`** ✓
- Title, authors (Nasr, Carlini, Sitawarin + others), year 2025, arXiv 2510.09023 — all correct
- Source: [arXiv:2510.09023](https://arxiv.org/abs/2510.09023)

**31. `andriushchenko2024adaptive`** ✓
- Title, authors (Andriushchenko, Croce, Flammarion), year 2025 (ICLR 2025) — all correct
- Source: ICLR 2025

### Technical Foundation

**32. `he2021deberta`** ✓ (UNCITED)
- Title, authors, year 2021, venue ICLR — all correct

**33. `he2023debertav3`** ✓
- Title, authors, year 2023, venue ICLR — all correct

**34. `kopf2023openassistant`** ✓
- Title, authors, year 2023, venue NeurIPS vol. 36 — all correct
- Source: [arXiv:2304.07327](https://arxiv.org/abs/2304.07327)

**35. `kornblith2019cka`** ✓
- Title, all 4 authors, year 2019, venue ICML, pages — all correct
- Source: PMLR vol. 97

**36. `qwen3_2025`** ✗ (P1)
- Named authors are incorrectly paired with wrong surnames. See P1-4.
- arXiv 2505.09388, year 2025 — correct
- Source: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

### Domain-Adaptive Pretraining & Multi-Task Learning

**37. `gururangan2020dontstop`** ✓
- Title, all 7 authors, year 2020, venue ACL, pages — all correct

**38. `caruana1997multitask`** ✓
- Title, author, year, journal, volume/number/pages — all correct

**39. `phang2018stilts`** ✓
- Title, authors, year 2018, arXiv 1811.01088 — all correct

**40. `liu2019mtdnn`** ✓
- Title, authors, year 2019, venue ACL, pages — all correct

**41. `howard2018ulmfit`** ✓
- Title, authors, year 2018, venue ACL, pages — all correct
- Source: ACL Anthology P18-1031

### Propaganda Detection

**42. `dasanmartino2020semeval`** ✓
- Title, authors, year 2020, venue SemEval, pages — all correct
- Source: ACL Anthology 2020.semeval-1.186

**43. `dasanmartino2019fine`** ✓
- Title, authors, year 2019, venue EMNLP, pages — all correct
- Source: ACL Anthology D19-1565

### Adversarial NLP

**44. `jin2020textfooler`** ✓
- Title, authors, year 2020, venue AAAI vol. 34, pages — all correct

**45. `li2020bertattack`** ✓
- Title, authors, year 2020, venue EMNLP, pages — all correct
- Source: ACL Anthology 2020.emnlp-main.500

### Probing Classifiers

**46. `devlin2019bert`** ✓ (UNCITED)
- Title, authors, year 2019, venue NAACL-HLT, pages — all correct
- Source: ACL Anthology N19-1423

**47. `conneau2018probing`** ✓
- Title, authors, year 2018, venue ACL, pages — all correct
- Source: ACL Anthology P18-1198

**48. `hewitt2019structural`** ✓
- Title, authors, year 2019, venue NAACL, pages — all correct
- Source: ACL Anthology N19-1419

**49. `liu2019roberta`** ✓
- Title, all 10 authors, year 2019, arXiv 1907.11692 — all correct (arXiv-only)

**50. `wang2019persuasion`** ✓
- Title, all 7 authors, year 2019, venue ACL, pages — all correct
- Source: ACL Anthology P19-1566

### Safety Defenses

**51. `robey2024smoothllm`** ✗ (P1)
- Wrong venue: not ICML 2024. See P1-1.
- Source: [arXiv:2310.03684](https://arxiv.org/abs/2310.03684)

**52. `mehrotra2024tap`** ✗ (P0)
- Wrong title subtitle. See P0-7.
- Source: [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/70702e8cbb4890b4a467b984ae59828a-Abstract-Conference.html)

**53. `chao2024jailbreakbench`** ✗ (P1)
- Incomplete authors, missing venue. See P1-5.
- Source: [arXiv:2404.01318](https://arxiv.org/abs/2404.01318)

**54. `mazeika2024harmbench`** ✓
- Title, authors, year 2024, venue ICML (PMLR 235) — all correct
- Source: [PMLR](https://proceedings.mlr.press/v235/mazeika24a.html)

**55. `lu2025xboundary`** ✗ (P1)
- Title mismatch with published version. See P1-8.
- Source: [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.282/)

**56. `kadali2026trace`** ✓
- Title, authors, year 2026, arXiv 2602.11495 — all correct
- Source: [arXiv:2602.11495](https://arxiv.org/abs/2602.11495)

**57. `hua2026rcs`** ✓
- Title, authors, year 2026, arXiv 2512.12069, venue ACL 2026 — plausible (confirmed by GitHub repo)
- Source: [arXiv:2512.12069](https://arxiv.org/abs/2512.12069)

**58. `jiang2024redqueen`** ✗ (P1)
- Wrong year, missing venue. See P1-6.
- Source: [ACL Anthology](https://aclanthology.org/2025.findings-acl.1311/)

**59. `song2026multibreak`** ✓ (P2 — unverified venue)
- Title/venue may differ between arXiv and OpenReview. See P2-5.
- Source: [arXiv:2605.01687](https://arxiv.org/abs/2605.01687)

**60. `xie2024gradsafe`** ✓
- Title, authors, year 2024, venue ACL, pages 507-518 — all correct
- Source: [ACL Anthology](https://aclanthology.org/2024.acl-long.30/)

**61. `xu2024safedecoding`** ✓
- Title, authors, year 2024, venue ACL — all correct
- Source: ACL Anthology 2024.acl-long.303

**62. `zou2024circuitbreakers`** ✓
- Title, all 10 authors, year 2024, venue NeurIPS — all correct

**63. `zhang2025jbshield`** ✓
- Title, all 10 authors, year 2025, venue USENIX Security, arXiv 2502.07557 — all correct
- Source: [arXiv:2502.07557](https://arxiv.org/abs/2502.07557)

**64. `perez2022redteaming`** ✓
- Title, all 9 authors, year 2022, venue EMNLP, pages — all correct
- Source: ACL Anthology 2022.emnlp-main.225

**65. `kulkarni2026latentadversarial`** ✓
- Title, author, year 2026, arXiv 2604.28129 — all correct (posted April 30, 2026)

**66. `derya2026revisitingjbshield`** ✓
- Title, authors (Derya, Sunar), year 2026, arXiv 2605.03095 — all correct (posted May 4, 2026)
- Source: [arXiv:2605.03095](https://arxiv.org/abs/2605.03095)

### Domain-Adaptive & Contrastive Learning

**67. `lee2020biobert`** ✓
- Title, authors, year 2020, journal Bioinformatics, vol/num/pages — all correct

**68. `beltagy2019scibert`** ✓ (P2)
- Venue should technically be EMNLP-IJCNLP 2019. See P2-4.

**69. `chen2020simclr`** ✓ (UNCITED)
- Title, authors, year 2020, venue ICML, pages — all correct

**70. `grill2020byol`** ✓ (UNCITED)
- Title, lead authors, year 2020, venue NeurIPS — all correct

### Generalization Theory

**71. `zhang2021understanding`** ✓
- Title, authors, year 2021, journal CACM, vol/num/pages, DOI — all correct

**72. `maennel2020random`** ✓
- Title, all 7 authors, year 2020, venue NeurIPS — all correct

### Additional Entries

**73. `marchiori2025jdapt`** ✗ (P0, UNCITED)
- Wrong title and author name. See P0-4.
- Source: [arXiv:2509.23281](https://arxiv.org/abs/2509.23281)

**74. `wang2026trajguard`** ✗ (P0, UNCITED)
- Wrong title and authors entirely. See P0-3.
- Source: [arXiv:2604.07727](https://arxiv.org/abs/2604.07727)

**75. `templeton2024saemitigators`** ✓ (UNCITED)
- Title, authors, year 2024, venue Transformer Circuits Thread — all correct

**76. `alon2023perplexity`** ✓ (UNCITED)
- Title, authors, year 2023, arXiv 2308.14132 — all correct

**77. `phute2023selfdefense`** ✗ (P0, UNCITED)
- Multiple author errors. See P0-5.
- Source: [arXiv:2308.07308](https://arxiv.org/abs/2308.07308)

**78. `nian2025jaildam`** ✓ (UNCITED)
- Title, authors, year 2025, venue COLM, arXiv 2504.03770 — all correct

**79. `anil2024manyshot`** ✓ (UNCITED)
- Title, lead authors, year 2024, venue NeurIPS — all correct

**80. `jain2023baseline`** ✓ (UNCITED)
- Title, authors, year 2023, arXiv 2309.00614 — all correct

**81. `shen2025antidote`** DUPLICATE (UNCITED)
- Same as entry 88. See DUP-1.

**82. `hsu2024improved`** ✗ (P0, DUPLICATE, UNCITED)
- Fabricated authors. See P0-1 and DUP-2.

**83. `li2025m2s`** ✗ (P0, UNCITED)
- Wrong title and authors. See P0-2.
- Source: [arXiv:2503.04856](https://arxiv.org/abs/2503.04856)

**84. `li2025repejailbreak`** ✓ (UNCITED)
- Title, all 9 authors, year 2025, venue COLING, arXiv 2401.06824 — all correct
- Source: [ACL Anthology](https://aclanthology.org/2025.coling-main.212/)

**85. `kadali2025internallayers`** ✓
- Title, authors, year 2025, arXiv 2510.06594 — all correct

**86. `markov2023holistic`** ✓
- Title, all 8 authors, year 2023, venue AAAI vol. 37, pages — all correct

**87. `wu2025safeint`** ✓
- Title, authors, year 2025, arXiv 2502.15594 — all correct
- Also published: Findings of EMNLP 2025
- Source: [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.450/)

**88. `shen2024jailbreakantidote`** DUPLICATE
- Same as entry 81. See DUP-1. This entry IS cited in tex.

**89. `alobaid2026echochamber`** ✓
- Title, lead author (Alobaid, Ahmad), year 2026, arXiv 2601.05742 — correct
- Source: [arXiv:2601.05742](https://arxiv.org/abs/2601.05742)

**90. `yousefpour2025repbend`** ✓
- Title, lead author (Yousefpour, Ashkan), year 2025, arXiv 2504.01550 — correct
- Also published: ACL 2025
- Source: [ACL Anthology](https://aclanthology.org/2025.acl-long.1173/)

**91. `galinkin2024improved`** DUPLICATE (UNCITED)
- Correct version of arXiv 2412.01547 (vs fabricated `hsu2024improved`). See DUP-2.
- Source: [arXiv:2412.01547](https://arxiv.org/abs/2412.01547)

---

## Recommended Actions (Priority Order)

### Immediate (P0 — blocks submission)
1. **Delete** `hsu2024improved` — fabricated authors, duplicate
2. **Fix** `ren2024actorattack` — correct title to "LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts"; venue to ACL 2025
3. **Fix** `mehrotra2024tap` — correct title to "Tree of Attacks: Jailbreaking Black-Box LLMs Automatically"
4. **Fix** `anthropic2025constitutional` — remove "Korbak, Tomek" from authors
5. **Fix or delete** `li2025m2s`, `wang2026trajguard`, `marchiori2025jdapt`, `phute2023selfdefense` — all have wrong titles/authors and are uncited

### Before camera-ready (P1)
6. **Fix** `robey2024smoothllm` venue
7. **Fix** `jiang2024redqueen` year (→2025) and add booktitle (Findings of ACL 2025)
8. **Fix** `gguard2025` title to match arXiv
9. **Fix** `chao2024jailbreakbench` author list and add NeurIPS venue
10. **Resolve** duplicate pairs (DUP-1, DUP-2)
11. **Fix** `qwen3_2025` authors, `fitd2024` missing author, `mann1988rst` journal, `lu2025xboundary` title

### Cleanup
12. **Remove** 11+ uncited entries that have no P0/P1 issues, or add citations if intended
13. **Fix** P2 minor issues (capitalization, generic booktitle)
