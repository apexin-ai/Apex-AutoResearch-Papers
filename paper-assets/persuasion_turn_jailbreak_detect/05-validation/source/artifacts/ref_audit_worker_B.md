# Reference Audit Report — Worker B

**Date**: 2026-05-26
**Auditor**: Worker B (independent verification)
**File**: `references.bib` (91 entries)

## Summary

| Metric | Count |
|--------|-------|
| Total .bib entries | 91 |
| Passed (✓) | 68 |
| P0 — Serious errors | 10 entries (9 distinct issues) |
| P1 — Should fix | 9 entries |
| P2 — Cleanup/cosmetic | 4 entries |
| Uncited entries | 18 |
| Cited keys in .tex | 73 unique |

---

## P0 — Serious (factual errors; reviewers will flag)

### P0-1. `hsu2024improved` — FABRICATED AUTHORS + WRONG TITLE ✗
- **Bib claims**: "Improved LLM Jailbreak Detection via Pretrained Embeddings" by Hsu, Erick and Hsu, Ikuya and Chung, Paul
- **Actual (arXiv 2412.01547)**: "Improved **Large** Language Model Jailbreak Detection via Pretrained Embeddings" by **Erick Galinkin and Martin Sablotny** (NVIDIA)
- **Impact**: No paper by "Hsu, Hsu, Chung" exists at this arXiv ID. Entry appears fabricated or mis-assigned.
- **Status**: UNCITED — delete entirely. `galinkin2024improved` is the correct entry for this arXiv ID.
- **Source**: https://arxiv.org/abs/2412.01547

### P0-2. `li2025m2s` — WRONG AUTHORS + WRONG TITLE ✗
- **Bib claims**: Authors "Li, Minxuan and Liu, Yue and Chen, Siyuan and Sun, Fangzhao and Ren, Hao and Liu, Zhengyi and Wu, Chengming and Xie, Xing"; title "M2S: Multi-Turn to Single-Turn -- Converting Multi-Turn Jailbreak Attacks to Single-Turn for Enhanced Safety Guardrails"
- **Actual (arXiv 2503.04856)**: Authors **Junwoo Ha, Hyunjun Kim, Sangyoon Yu, Haon Park, Ashkan Yousefpour, Yuna Park, Suhyun Kim**; title "**M2S: Multi-turn to Single-turn jailbreak in Red Teaming for LLMs**"
- **Impact**: Completely wrong authors and substantially wrong title.
- **Status**: UNCITED — delete or replace with correct metadata.
- **Source**: https://arxiv.org/abs/2503.04856

### P0-3. `ren2024actorattack` — WRONG VENUE ✗
- **Bib claims**: `booktitle={International Conference on Learning Representations}` (ICLR 2025)
- **Actual**: Published at **ACL 2025** (Main Conference), not ICLR 2025.
- **Fix**: Change booktitle to `Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics`
- **Status**: CITED (introduction, experiments, related_work)
- **Source**: https://arxiv.org/abs/2410.10700

### P0-4. `jiang2024redqueen` — WRONG TITLE + WRONG VENUE + WRONG YEAR ✗
- **Bib claims**: title "RED QUEEN: Safeguarding Large Language Models against Concealed Multi-Turn Jailbreaking", year 2024, no venue (arXiv preprint)
- **Actual**: Published title is "**Red Queen: Exposing Latent Multi-Turn Risks in Large Language Models**" at **ACL 2025 Findings**, year **2025**
- **Fix**: Update title, add `booktitle={Findings of the Association for Computational Linguistics: ACL 2025}`, change year to 2025
- **Status**: CITED (related_work)
- **Source**: https://aclanthology.org/2025.findings-acl.1311/

### P0-5. `mehrotra2024tap` — WRONG TITLE ✗
- **Bib claims**: "Tree of Attacks: Jailbreaking Black-Box LLMs **with the Pruning of Candidate Outputs**"
- **Actual (NeurIPS 2024)**: "Tree of Attacks: Jailbreaking Black-Box LLMs **Automatically**"
- **Fix**: Replace subtitle
- **Status**: CITED (related_work)
- **Source**: https://neurips.cc/virtual/2024/poster/95078

### P0-6. `robey2024smoothllm` — WRONG VENUE ✗
- **Bib claims**: `booktitle={Proceedings of the 41st International Conference on Machine Learning}` (ICML 2024)
- **Actual**: Published in **Transactions on Machine Learning Research (TMLR)**, not ICML 2024. The paper was arXiv 2310.03684 (Oct 2023), presented at ICLR 2024 Workshop on Reliable and Responsible Foundation Models, and journal-published in TMLR.
- **Fix**: Change to `@article` with `journal={Transactions on Machine Learning Research}`
- **Status**: CITED (related_work)
- **Source**: https://www.semanticscholar.org/paper/SmoothLLM:-Defending-Large-Language-Models-Against-Robey-Wong/8cf9b49698fdb1b754df2556576412a7b44929f6

### P0-7. `shen2025antidote` + `shen2024jailbreakantidote` — DUPLICATE ENTRIES ✗
- Both entries have identical arXiv ID **2410.02298**, identical title, identical authors.
- `shen2025antidote`: `@inproceedings`, ICLR 2025 — **correct venue**
- `shen2024jailbreakantidote`: `@article`, arXiv 2024 — pre-publication form
- **Fix**: Delete `shen2024jailbreakantidote` (uncited entry that would cause confusion). Keep `shen2025antidote` and update all citations from `shen2024jailbreakantidote` → `shen2025antidote`.
- **Status**: `shen2024jailbreakantidote` is CITED; `shen2025antidote` is NOT CITED. Need to swap citation keys.
- **Source**: https://arxiv.org/abs/2410.02298

### P0-8. `wang2026trajguard` — WRONG TITLE + WRONG AUTHOR ✗
- **Bib claims**: title "TrajGuard: Trajectory-Based Hidden-State Detection of Multi-Turn Jailbreak Attacks", author "Wang, Yifan and others"
- **Actual (arXiv 2604.07727)**: title "**TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense**", first author **Cheng Liu** (not Wang)
- **Status**: UNCITED — delete or fix metadata
- **Source**: https://arxiv.org/abs/2604.07727

### P0-9. `marchiori2025jdapt` — WRONG TITLE ✗
- **Bib claims**: "J-DAPT: CORAL-Based Domain Adaptation with Cross-Modal Fusion for Multimodal Robotic Jailbreak Detection"
- **Actual (arXiv 2509.23281)**: "**Preventing Robotic Jailbreaking via Multimodal Domain Adaptation**" (J-DAPT is the framework name within the paper, not the paper title)
- **Status**: UNCITED — delete or fix title
- **Source**: https://arxiv.org/abs/2509.23281

---

## P1 — Should Fix (inaccurate metadata)

### P1-1. `metallamaguard3_2024` — UNDER-SPECIFIED CITATION ✗
- No standalone paper titled "Llama Guard 3" exists. Llama Guard 3 was introduced as part of "The Llama 3 Herd of Models" (arXiv 2407.21783).
- **Fix**: Cite arXiv 2407.21783 with proper author list (Llama Team / Meta AI) or reference the model card directly.
- **Status**: CITED (experiments)
- **Source**: https://arxiv.org/abs/2407.21783

### P1-2. `gguard2025` — TITLE MISMATCH ✗
- **Bib title**: "An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs"
- **Canonical arXiv title**: "**Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak**"
- **Fix**: Align with the canonical abs page title
- **Status**: CITED (introduction, related_work)
- **Source**: https://arxiv.org/abs/2507.07146

### P1-3. `lu2025xboundary` — PUBLISHED TITLE DIFFERS FROM BIB ✗
- **Bib title** (from arXiv): "...Shield LLMs from **Multi-Turn Jailbreaks** without..."
- **Published title** (EMNLP 2025 Findings): "...Shield LLMs from **Jailbreak Attacks** without..." (drops "Multi-Turn")
- **Fix**: Use published ACL Anthology title since venue is EMNLP 2025 Findings
- **Status**: CITED (related_work)
- **Source**: https://aclanthology.org/2025.findings-emnlp.282/

### P1-4. `chao2024jailbreakbench` — MISSING VENUE ✗
- Listed as `@article` / arXiv preprint, but actually published at **NeurIPS 2024 Datasets & Benchmarks Track**.
- **Fix**: Change to `@inproceedings` with `booktitle={Advances in Neural Information Processing Systems}`
- **Status**: CITED (related_work)
- **Source**: https://proceedings.neurips.cc/paper_files/paper/2024/file/63092d79154adebd7305dfd498cbff70-Paper-Datasets_and_Benchmarks_Track.pdf

### P1-5. `mann1988rst` — WRONG JOURNAL NAME ✗
- **Bib claims**: `journal={Text \& Talk}`
- **Actual**: In 1988 the journal was titled **"Text"** (full: *Text — Interdisciplinary Journal for the Study of Discourse*). It was renamed "Text & Talk" only in 2008.
- **Fix**: Change to `journal={Text}`
- **Status**: CITED (related_work)
- **Source**: https://www.degruyterbrill.com/document/doi/10.1515/text.1.1988.8.3.243/html

### P1-6. `song2026multibreak` — PREMATURE VENUE CLAIM ✗
- Listed as `booktitle={International Conference on Machine Learning}` (ICML 2026)
- arXiv posted May 2026 — ICML 2026 acceptance decisions likely not publicly announced yet.
- **Fix**: If not yet accepted, change to `@article` / arXiv preprint. Verify acceptance before claiming venue.
- **Status**: CITED (related_work)
- **Source**: https://arxiv.org/abs/2605.01687

### P1-7. `yousefpour2025repbend` — MISSING VENUE ✗
- Listed as `@article` / arXiv preprint, but published at **ACL 2025** (Main Conference).
- **Fix**: Change to `@inproceedings` with `booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics}`
- **Status**: CITED (related_work)
- **Source**: https://aclanthology.org/2025.acl-long.1173/

### P1-8. `wu2025safeint` — MISSING VENUE UPDATE ✗
- Listed as `@article` / arXiv preprint, but also published at **EMNLP 2025 Findings**.
- **Fix**: Change to `@inproceedings` with `booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025}`
- **Status**: CITED (related_work)
- **Source**: https://arxiv.org/abs/2502.15594

### P1-9. `deceptivedelight2024` — NON-STANDARD SOURCE ✗
- This is a blog post / technical report from Palo Alto Networks Unit 42 website, not a peer-reviewed paper.
- Bib type `@techreport` is acceptable. Author listed as `{Palo Alto Networks Unit 42}` is OK for organizational authorship.
- **Fix**: Consider adding `howpublished` or URL field for traceability
- **Status**: CITED (introduction, experiments, appendix, related_work)
- **Source**: https://unit42.paloaltonetworks.com/jailbreak-llms-through-camouflage-distraction/

---

## P2 — Cleanup (cosmetic / minor)

### P2-1. `han2024wildguard` — Minor capitalization
- Bib: "One-Stop" vs official proceedings: "One-stop". Very minor.
- **Status**: CITED

### P2-2. `templeton2024saemitigators` — Misleading bib key + non-peer-reviewed
- Key name "saemitigators" doesn't match paper content (paper is about scaling monosemanticity, extracting features). Venue "Transformer Circuits Thread" is a blog, not peer-reviewed.
- **Status**: UNCITED

### P2-3. `qwen3_2025` — Team report attribution
- First-author attribution "Yang et al." is technically correct but unusual for large team reports. Some prefer "Qwen Team, 2025".
- **Status**: CITED

### P2-4. `jin2020textfooler` — Missing AAAI issue number
- Volume 34 correct; full citation should include No. 05 for precision.
- **Status**: CITED

---

## Uncited Entries (18 total)

The following .bib entries are not referenced by any `\cite`, `\citep`, or `\citet` in the .tex files:

| # | Key | Has Issues? | Notes |
|---|-----|-------------|-------|
| 1 | `he2021deberta` | ✓ Clean | DeBERTa v1; v3 (`he2023debertav3`) is cited |
| 2 | `devlin2019bert` | ✓ Clean | BERT base paper |
| 3 | `zou2023gcg` | ✓ Clean | GCG attack |
| 4 | `chen2020simclr` | ✓ Clean | SimCLR |
| 5 | `grill2020byol` | ✓ Clean | BYOL |
| 6 | `marchiori2025jdapt` | ✗ P0-9 | Wrong title |
| 7 | `wang2026trajguard` | ✗ P0-8 | Wrong title + wrong author |
| 8 | `templeton2024saemitigators` | ✗ P2-2 | Misleading key |
| 9 | `alon2023perplexity` | ✓ Clean | Perplexity-based detection |
| 10 | `phute2023selfdefense` | ✓ Clean | LLM self defense |
| 11 | `nian2025jaildam` | ✓ Clean | JailDAM (VLM) |
| 12 | `anil2024manyshot` | ✓ Clean | Many-shot jailbreaking |
| 13 | `jain2023baseline` | ✓ Clean | Baseline defenses |
| 14 | `shen2025antidote` | ✗ P0-7 | Duplicate of cited `shen2024jailbreakantidote` |
| 15 | `hsu2024improved` | ✗ P0-1 | Fabricated — delete |
| 16 | `li2025m2s` | ✗ P0-2 | Wrong authors + title — delete |
| 17 | `li2025repejailbreak` | ✓ Clean | RepE jailbreak (COLING 2025) |
| 18 | `galinkin2024improved` | ✓ Clean | Correct version of arXiv 2412.01547 |

**Recommendation**: Remove all 18 uncited entries to avoid reviewer complaints about dangling references. If any are needed for future text additions, re-add with verified metadata.

---

## Verified Entries (68 ✓)

All remaining 68 entries passed verification — paper exists, title matches, authors correct, venue correct, arXiv ID correct (where applicable):

`inan2023llamaguard`, `zeng2024shieldgemma`, `anthropic2025constitutional`, `deepcontext2026`, `tong2025biid`, `safedream2026`, `bullwinkel2025repeng`, `prasad2008pdtb`, `stolcke2000dialogueact`, `austin1962speechacts`, `searle1969speechacts`, `cialdini2001influence`, `zeng2024pap`, `russinovich2024crescendo`, `chao2023pair`, `wei2023jailbroken`, `hagendorff2026reasoning`, `fitd2024`, `zou2023gcg`, `lin2023toxicchat`, `li2024mhj`, `gururangan2018artifacts`, `niven2019probing`, `nasr2025attackermovessecond`, `andriushchenko2024adaptive`, `he2021deberta`, `he2023debertav3`, `kopf2023openassistant`, `kornblith2019cka`, `gururangan2020dontstop`, `caruana1997multitask`, `phang2018stilts`, `liu2019mtdnn`, `howard2018ulmfit`, `dasanmartino2020semeval`, `dasanmartino2019fine`, `li2020bertattack`, `devlin2019bert`, `conneau2018probing`, `hewitt2019structural`, `liu2019roberta`, `wang2019persuasion`, `mazeika2024harmbench`, `kadali2026trace`, `hua2026rcs`, `xie2024gradsafe`, `xu2024safedecoding`, `zou2024circuitbreakers`, `zhang2025jbshield`, `perez2022redteaming`, `kulkarni2026latentadversarial`, `derya2026revisitingjbshield`, `lee2020biobert`, `beltagy2019scibert`, `chen2020simclr`, `grill2020byol`, `zhang2021understanding`, `maennel2020random`, `alon2023perplexity`, `phute2023selfdefense`, `nian2025jaildam`, `anil2024manyshot`, `jain2023baseline`, `li2025repejailbreak`, `kadali2025internallayers`, `markov2023holistic`, `alobaid2026echochamber`, `galinkin2024improved`

---

## Flagged Entries — Detailed Verification Notes

### Specifically requested entries:

1. **`shen2025antidote` vs `shen2024jailbreakantidote`**: Confirmed duplicate (same arXiv 2410.02298). Keep `shen2025antidote` (ICLR 2025 `@inproceedings`), delete `shen2024jailbreakantidote`, update citation keys in .tex. → **P0-7**

2. **`hsu2024improved` vs `galinkin2024improved`**: Same arXiv ID 2412.01547. `galinkin2024improved` has correct authors (Galinkin & Sablotny). `hsu2024improved` has fabricated authors — delete it. → **P0-1**

3. **`ren2024actorattack`**: Venue is ACL 2025, not ICLR 2025. → **P0-3**

4. **`robey2024smoothllm`**: Published in TMLR, not ICML 2024. → **P0-6**

5. **`mehrotra2024tap`**: Title subtitle wrong ("with the Pruning of Candidate Outputs" → "Automatically"). → **P0-5**

6. **`jiang2024redqueen`**: Published title, venue, and year all differ from bib. → **P0-4**
