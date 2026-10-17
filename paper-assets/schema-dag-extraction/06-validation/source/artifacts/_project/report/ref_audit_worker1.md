# Reference Audit Report (Worker 1/3)

**Date**: 2026-05-26
**Bib file**: `docs/paper/references.bib`
**Total entries**: 63

---

## Per-Entry Verification

### General / Statistical / Methodology

```
✓ cohen-1988-statistical: 确认正确 — Jacob Cohen, 2nd ed, Lawrence Erlbaum Associates, 1988
✓ schuirmann-1987-tost: 确认正确 — J Pharmacokinetics Biopharmaceutics 15(6):657-680, 1987, DOI correct
✓ rothman-1990: 确认正确 — Epidemiology 1(1):43-46, 1990, DOI correct
✓ lakens-2017-equivalence: 确认正确 — SPPS 8(4):355-362, 2017, DOI correct
✓ robinson-1950-ecological: 确认正确 — Am Sociol Rev 15(3):351-357, 1950
✓ dror-2018-significance: 确认正确 — ACL 2018, pp.1383-1392, authors match
✓ card-2020-power: 确认正确 — EMNLP 2020, pp.9263-9274, authors match
```

### Label Noise / Confusion / Soft Labels

```
✓ muller2019when: 确认正确 — NeurIPS 2019, vol.32, authors match
✓ collier-2021-correlated-noise: 确认正确 — CVPR 2021, pp.1551-1560, authors match
✓ guo-2021-label-confusion: 确认正确 — AAAI 2021, vol.35, pp.12929-12936, DOI correct
✓ snell2017prototypical: 确认正确 — NeurIPS 2017, vol.30, authors match
✗ peterson2019human: [页码错误] bib 写 pages={9617--9626}，实际 ICCV 2019 论文页码为 9616--9625（差一页，DOI: 10.1109/ICCV.2019.00971）
✓ dubey-2018-pairwise-confusion: 确认正确 — ECCV 2018, pp.71-88, authors match
```

### Ecological Fallacy / Annotation

```
⚠ baan-2023-ecological: [bib key 误导] bib key 为 "baan-2023" 但第一作者为 Orlikowski，无 Baan。论文内容（title/authors/venue/pages）全部正确：ACL 2023 Short Papers, pp.1017-1029
```

### Zero-shot IE / Schema Methods

```
✓ llm-pee-2025: 确认正确 — EMNLP 2025, pp.34377-34399, authors match
✓ parse-2025: 确认正确 — EMNLP 2025 Industry Track, pp.2749-2763, authors match
✓ crossagentie-2025: 确认正确 — Findings of ACL 2025, pp.13953-13977, authors match
✓ cmas-ner-2025: 确认正确 — ACM Web Conference 2025, DOI correct（注：bib 缺 pages，实际为 4183-4195）
✓ uniner-2024: 确认正确 — ICLR 2024, arXiv 2308.03279
✓ gollie-2024: 确认正确 — ICLR 2024, arXiv 2310.03668
✓ gliner-2024: 确认正确 — NAACL 2024, pp.5364-5376, arXiv 2311.08526
✓ gliner2-2025: 确认正确 — EMNLP 2025 System Demos, pp.130-140
✓ iepile-2024: 确认正确 — ACL 2024 Short Papers, pp.127-146
✓ knowcoder-2024: 确认正确 — ACL 2024, pp.8758-8779, arXiv 2403.07969
✓ slot-2025: 确认正确 — EMNLP 2025 Industry Track, pp.472-491
✓ oneke-2025: 确认正确 — WWW 2025 Companion, DOI correct, arXiv 2412.20005
✓ xie-zeroshot-ner-2023: 确认正确 — EMNLP 2023, pp.7935-7956
✓ wadhwa-re-llm-2023: 确认正确 — ACL 2023, pp.15566-15589
✓ relationprompt-2022: 确认正确 — Findings of ACL 2022, pp.45-57
✓ josifoski-2022-genie: 确认正确 — NAACL 2022, pp.4626-4643
✓ codeie-2023: 确认正确 — ACL 2023, pp.15339-15353
✓ adelie-2024: 确认正确 — EMNLP 2024, pp.7371-7387
✓ reflect-learn-2026: 确认正确 — AAAI 2026, vol.40, pp.34923-34931, DOI correct
✓ shachar-2025-ner-retriever: 确认正确 — Findings of EMNLP 2025, pp.11175-11186
✓ boylan-2025-glirel: 确认正确 — NAACL 2025, pp.8230-8245
```

### Surveys / Background

```
✓ llm4ie-survey-2024: 确认正确 — Frontiers of Computer Science 18(6), 2024, DOI correct
✓ instructuie-2023: 确认正确 — arXiv 2304.08085, still arXiv preprint
✓ promptner-2023: 确认正确 — arXiv 2305.15444, still arXiv preprint
✓ li2023evaluating: 确认正确 — arXiv 2304.11633, still arXiv preprint
```

### Embedding / Representation

```
✓ cai-isotropy-clusters-2021: 确认正确 — ICLR 2021, OpenReview URL correct
✓ lost-in-middle-2024: 确认正确 — TACL 2024, vol.12, pp.157-173, DOI correct
✓ chen-2026-multi-instance: 确认正确 — arXiv 2603.22608, year 2026 correct
```

### Zero-shot Classification / Label Space

```
✓ yin-2019-zero-shot-bench: 确认正确 — EMNLP 2019, pp.3914-3923, arXiv 1909.00161
✓ haystack-to-needle-2025: 确认正确 — arXiv 2502.08436, still arXiv preprint
✓ dlisc-2025: 确认正确 — arXiv 2505.14992, still arXiv preprint
✓ spt-2025: 确认正确 — arXiv 2506.01276, still arXiv preprint
✓ sclar-sensitivity-2024: 确认正确 — ICLR 2024, arXiv 2310.11324
```

### Schema-Guided Dialogue

```
✓ rastogi2020towards: 确认正确 — AAAI 2020, vol.34, pp.8689-8696, arXiv 1909.05855
✓ lee2022sgd: 确认正确 — AAAI 2022, vol.36, pp.10938-10946, arXiv 2110.06800
```

### Datasets

```
✓ fewnerd-2021: 确认正确 — ACL 2021, pp.3198-3213
✓ fewrel-2018: 确认正确 — EMNLP 2018, pp.4803-4809
✓ maven-2020: 确认正确 — EMNLP 2020, pp.1652-1671
✓ docred-2019: 确认正确 — ACL 2019, pp.764-777
```

### Models / Tools

```
✓ qwen3-2025: 确认正确 — arXiv 2505.09388, Qwen Team
✓ llama3-2024: 确认正确 — arXiv 2407.21783, Meta (bib lists first ~11 of ~560 authors, standard practice)
✓ sentence-bert-2019: 确认正确 — EMNLP 2019, pp.3982-3992
✓ minilm-2020: 确认正确 — NeurIPS 2020, vol.33, arXiv 2002.10957
✓ vllm-2023: 确认正确 — SOSP 2023 (29th Symposium on Operating Systems Principles)
✓ willard2023efficient: 确认正确 — arXiv 2307.09702, still arXiv preprint
✓ json-schema-bench-2025: 确认正确 — arXiv 2501.10868
✓ gemini-2025: 确认正确 — arXiv 2507.06261, Gemini Team, year 2025
```

### Vision / Large-scale Classification

```
✓ deng-2010-imagenet: 确认正确 — ECCV 2010, pp.71-84, DOI correct
```

### Familiarity / Zero-shot NER Evaluation

```
⚠ golde-2025-familiarity: [venue 名称过时] bib 写 "North American Chapter"，但 NAACL 2025 已正式更名为 "Nations of the Americas Chapter"。ACL Anthology 官方标题为 "Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics"。论文其他信息（authors/pages/arXiv ID）全部正确。注：同文件中 boylan-2025-glirel 已用正确新名，存在不一致。
```

---

## Summary

| Category | Count |
|----------|-------|
| Total entries | 63 |
| ✓ Confirmed correct | 60 |
| ✗ Error (must fix) | 1 |
| ⚠ Warning (should review) | 2 |

### Errors (must fix)

1. **peterson2019human** — 页码错误：`pages = {9617--9626}` → 应为 `{9616--9625}`。来源：ICCV 2019 OpenAccess CVF, Princeton University publication record, DOI 10.1109/ICCV.2019.00971。

### Warnings (should review)

1. **golde-2025-familiarity** — Venue 名称用了旧名 "North American Chapter"，NAACL 2025 官方已改名 "Nations of the Americas Chapter"。同文件中 `boylan-2025-glirel` 已用新名，不一致。建议统一为新名。

2. **baan-2023-ecological** — Bib key 名为 "baan-2023" 但论文第一作者为 Orlikowski（无任何作者叫 Baan）。Key 只是标签不影响引用正确性，但可能造成维护混乱。

### No hallucinated papers detected

所有 63 篇引用均经 WebSearch 验证存在，无虚构论文。

### Citation context check

基于 tex 文件中的引用上下文检查，所有 cite 均用于正确位置，未发现"引了 A 但说的是 B 的结论"的情况。
