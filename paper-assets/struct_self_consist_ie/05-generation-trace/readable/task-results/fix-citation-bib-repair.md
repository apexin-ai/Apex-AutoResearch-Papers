# fix citation bib repair

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_citation_bib_repair_20260517T091424_result.json`
- **Structured JSON:** [`2d8ed9adad3852c898ac.json`](../../sessions/2d/2d8ed9adad3852c898ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 fixes applied and synced. Summary:

```
=== Fix 1: xie2024selfevaluation (CRITICAL) ===
BEFORE: author = {Xie, Jie and Lu, Kai and Dong, Rui and Pan, Liangming and Han, Qi and Wang, Shasha and Huang, Deyu and Zhang, Junlan}
        booktitle = {Advances in Neural Information Processing Systems (NeurIPS)}, year = {2024}
AFTER:  author = {Ren, Jie and Zhao, Yao and Vu, Tu and Liu, Peter J. and Lakshminarayanan, Balaji}
        booktitle = {NeurIPS 2023 Workshop on ``I Can't Believe It's Not Better''}, year = {2023}

=== Fix 2: deguchi2024centroid (CRITICAL) ===
BEFORE: author = {Deguchi, Hiroyuki and Kamigaito, Hidetaka and Watanabe, Taro}
        booktitle = {EMNLP}, pages = missing
AFTER:  author = {Deguchi, Hiroyuki and Sakai, Yusuke and Kamigaito, Hidetaka and Watanabe, Taro and Tanaka, Hideki and Utiyama, Masao}
        booktitle = {Findings of the Association for Computational Linguistics: ACL 2024}, pages = {11009--11018}

=== Fix 3: tian2023calibration (MINOR) ===
BEFORE: title truncated (missing "Fine-Tuned with Human Feedback")
        author = {Tian, Katherine and Mitchell, Eric and Yao, Huaxiu and Manning, Christopher D. and Finn, Chelsea}
        pages = {1278--1294}
AFTER:  title = {Just Ask for Calibration: ... Fine-Tuned with Human Feedback}
        author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.}
        pages = {5433--5442}

=== Fix 4: oh2026latentsc (MINOR) ===
BEFORE: @article, journal = {arXiv preprint arXiv:2508.18395}
AFTER:  @inproceedings, booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)}

=== Fix 5: chen2024usc (MINOR) ===
BEFORE: booktitle = {arXiv preprint (ICML 2024 Workshop ICL)}
AFTER:  booktitle = {ICML 2024 Workshop on In-Context Learning}
```

---
