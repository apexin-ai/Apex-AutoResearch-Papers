# D113 Table 2 + Narrative Fix Changelog

## Data Verification (Step 1)

Confirmed macro F1 from `selection_f1_table2.json` on autodl-5090:

| Method | F1 (2-seed mean +/- std) |
|--------|--------------------------|
| Oracle | 0.778 +/- 0.003 |
| Greedy | 0.645 +/- 0.001 |
| LP | 0.647 +/- 0.005 |
| SJ | 0.646 +/- 0.002 |
| FK | 0.646 +/- 0.001 |
| EM | 0.637 +/- 0.001 |
| VC | 0.623 +/- 0.004 |
| Random | 0.610 +/- 0.003 |

Table 2 in experiments.tex already had correct macro F1 values.

## Fixes Applied (Step 2)

| # | File | Change |
|---|------|--------|
| 1 | experiments.tex:92 | "Greedy achieves F1=0.663, surpassing all" -> "Selection approximately matches greedy (F1=0.645; +0.2pp, not significant)" |
| 2 | experiments.tex:77 | "Single" row already absent (previously removed) |
| 3 | experiments.tex:88 | LP delta already correct (+0.2pp, p=0.29) in current version |
| 4 | experiments.tex:92 | Same as #1 - narrative rewritten |
| 5 | discussion.tex:16 | "achieves F1=0.663, surpassing all" -> "LP selection approximately matches greedy (delta=+0.2pp, p=0.29)" |
| 6 | discussion.tex:43 | "+0.1pp" -> "+0.2pp"; "single-sample" -> "greedy" |
| 7 | abstract.tex:4 | "fails to outperform" -> "approximately matches...without significant improvement" |
| 8 | introduction.tex:11 | "fails to improve over greedy" -> "approximately matches greedy...without significant improvement" |
| 9 | introduction.tex:17 | "fail to outperform greedy" -> "approximately match greedy...without significant improvement" |
| 10 | introduction.tex:35 | C3: "Greedy (F1=0.663) surpasses all" -> "Selection recovers T=1.0 degradation (F1~0.645-0.647) but fails to close 13.3pp oracle gap" |
| 11 | limitations.tex:10 | "+0.4pp over greedy" -> "+0.2pp over greedy" (unified with discussion) |

## Verification (Step 3)

Post-edit grep confirms:
- `0.663`: 0 matches
- `surpass`: 0 matches
- `outperform` in main sections: only legitimate negated forms ("neither significantly outperforms", "without significantly outperforming")
- `Single` in main sections: only method.tex baseline definition (references appendix tables, out of scope)
