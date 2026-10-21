# Reference Audit Report — Worker C

Audit date: 2026-05-26

Each entry verified via WebSearch for: existence, authors, title, year, venue, and cite-context correctness.

---

## Per-Entry Results

```
[kirchenbauer2023watermark] ✓ | ICML 2023, pp. 17061–17084. Authors, title, venue all confirmed.
[drayson2025] ✓ | EMNLP 2025. Authors, title correct. arXiv 2502.15654 confirmed.
[schaeffer2025position] ✓ | arXiv preprint arXiv:2503.03150. Authors, title correct. Not yet formally published at a conference (invited talk at ICLR 2025; under review elsewhere). Listing as arXiv is appropriate.
[kazdan2025collapse] ✓ | ICML 2025 poster confirmed (icml.cc/virtual/2025/poster/44713). Authors, title correct.
[mitchell2023detectgpt] ✓ | ICML 2023. Authors, title correct. arXiv 2301.11305 confirmed.
[basani2026diveye] ✓ | TMLR 2026 confirmed (DBLP, GitHub "[TMLR '26]"). Authors (Basani, Chen), title, ISSN correct.
[zawalski2026codec] ✓ | ICLR 2026 confirmed (OpenReview YlpaaYxx4t). Authors, title correct. arXiv 2510.27055 confirmed.
[zhang2024minkpp] ✓ | ICLR 2025 Spotlight. Bib year=2025 correct (cite key says 2024, irrelevant). Authors, title correct.
[shumailov2024collapse] ✓ | Nature 2024, vol. 631, pp. 755–759. Authors (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal), title, DOI all correct.
[alemohammad2024selfconsuming] ✓ | ICLR 2024. Authors, title correct. arXiv 2307.01850 confirmed.
[dohmatob2024model] ✓ | ICML 2024, pp. 11165–11197. Authors (Dohmatob, Feng, Yang, Charton, Kempe), title correct.
[xie2023dsir] ✓ | NeurIPS 2023. Authors (Xie, Santurkar, Ma, Liang), title correct.
[tirumala2023d4] ✓ | NeurIPS 2023 Datasets & Benchmarks. Authors (Tirumala, Simig, Aghajanyan, Morcos), title correct.
[xie2023doremi] ✓ | NeurIPS 2023. Authors, title correct.
[hans2024binoculars] ✓ | ICML 2024. Authors, title correct. arXiv 2401.12070 confirmed.
[alain2017understanding] ✓ | ICLR 2017 Workshop. Authors (Alain, Bengio), title correct.
[belinkov2022probing] ✓ | Computational Linguistics 48(1):207–219, 2022. Author, title, volume, pages, DOI all correct.
[bao2024fast] ✓ | ICLR 2024. Authors (Bao, Zhao, Teng, Yang, Zhang), title correct.
[frank2001ordinal] ✓ | ECML 2001, pp. 145–156. Authors (Frank, Hall), title, DOI correct.
[cheng2025beyond] ✓ | WWW 2025 (ACM Web Conference). Authors, title correct. arXiv 2410.14259 confirmed.
[mehta2025beyond] ✓ | arXiv preprint arXiv:2511.17602. Author (Sushant Mehta), title, year correct.
[sun2025aigt] ✓ | ACL 2025. Authors, title correct. arXiv 2412.18148 confirmed.
[spennemann2025quantifying] ✓ | arXiv preprint arXiv:2504.08755. Author (Dirk H. R. Spennemann), title, year correct.
[dohmatob2025strong] ✓ | ICLR 2025. Authors (Dohmatob, Feng, Subramonian, Kempe), title correct.
[wang2024semeval] ✓ | SemEval 2024 (co-located with NAACL). Authors, title correct.
[gerstgrasser2024model] ✓ | COLM 2024. Authors, title correct. arXiv 2404.01413 confirmed.
[guo2024curious] ✓ | Findings of NAACL 2024. Authors, title correct. Minor: "Clavel, Chloe" could use diacritics (Chloé), but functionally acceptable in BibTeX.
[briesch2023selfconsuming] ✓ | arXiv preprint arXiv:2311.16822, year 2023. Authors, title correct. Remains unpublished at a venue.
[padmakumar2024writing] ✓ | ICLR 2024. Authors (Padmakumar, He), title correct. Confirmed via ICLR 2024 slides and NSF record.
[krishna2023paraphrasing] ✓ | NeurIPS 2023. Authors, title correct. arXiv 2303.13408 confirmed.
[sadasivan2023detect] ✓ | arXiv preprint arXiv:2303.11156. Authors, title correct. Submitted to ICLR 2024 but acceptance status unclear from public sources; listing as arXiv preprint is safe.
[hao2025rewrite] ✓ | ACL 2025, pp. 6421–6434. Authors, title correct.
[wang2025unveiling] ✓ | ACL 2025, pp. 12740–12755. Authors (Wang, Li, Yan, Cheng, Zhang), title, venue, pages all correct.
[fu2025theoretical] ✓ | ICLR 2025 (OpenReview WttfQGwpES). Authors, title correct. arXiv 2502.18865 confirmed.
[verma2024ghostbuster] ✓ | NAACL 2024, pp. 1702–1717. Authors, title, pages correct.
[dugan2024raid] ✓ | ACL 2024, pp. 12463–12492. Authors, title, pages correct.
[liang2023gpt] ✓ | Patterns 4(7):100779, 2023. Authors, title, volume, pages correct.
```

## Cite-Context Issues

One contextual concern (bibliographic entry itself is correct):

- **related_work.tex:11** — `liang2023gpt` is cited as "GPTZero~\cite{liang2023gpt}" in the phrase "benchmarks such as RAID and GPTZero evaluate robustness at scale." The Liang et al. paper is about **detector bias against non-native English writers**, not about GPTZero as a benchmark. GPTZero is a commercial detection tool (Tian et al.) without a standalone academic paper; Liang et al. merely evaluate it as one of several biased detectors. The cite is tangentially related but the sentence implies liang2023gpt *is* the GPTZero benchmark paper, which it is not.

## Summary

| Metric | Count |
|--------|-------|
| Total entries | 37 |
| ✓ Correct | 37 |
| ✗ Bibliographic errors | 0 |
| Cite-context flags | 1 (liang2023gpt used as "GPTZero" benchmark reference) |

All 37 bib entries are real papers with correct authors, titles, years, and venues. No hallucinated references found. One minor cite-context misattribution flagged above.
