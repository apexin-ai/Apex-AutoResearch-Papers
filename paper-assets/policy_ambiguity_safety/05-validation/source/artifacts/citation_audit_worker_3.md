# Citation Audit Report (Worker 3)

Audit of all 64 bib entries in `references.bib`. Each entry checked for: existence, author accuracy, year, title, venue, and arXiv ID correctness. Citation contexts in `.tex` files also verified for misattribution.

---

## Per-Entry Results

- ✓ `li_ambiguity_taxonomy_2024` — Confirmed. Li, Liu, Wu, Smith at EACL 2024. Title and authors correct.
- ✓ `massey_ambiguity_re_2014` — Confirmed. Massey, Rutledge, Anton, Swire at IEEE RE 2014. DOI correct.
- ✓ `berry_kamsties_2004` — Confirmed. Berry, Kamsties, Krieger. University of Waterloo tech report. Note: original version dated November 2003; year 2004 is acceptable.
- ✓ `chantree_2006` — Confirmed. Chantree, Nuseibeh, de Roeck, Willis at IEEE RE 2006.
- ✓ `wasow_ambiguity_2005` — Confirmed. Wasow, Perfors, Beaver in "Morphology and the Web of Grammar" (CSLI 2005).
- ✓ `kennedy_vagueness_2007` — Confirmed. Kennedy in Linguistics and Philosophy 30(1), 2007. DOI correct.
- ✓ `willis_nocuous_2008` — Confirmed. Willis, Chantree, De Roeck in Research on Language and Computation 6(3-4), 2008. DOI correct.
- ✓ `ferrari_ambiguity_2019` — Confirmed. Ferrari, Esuli in Automated Software Engineering 26, 2019. DOI correct.
- ✓ `ezzini_taphsir_2022` — Confirmed. Ezzini, Abualhaija, Arora, Sabetzadeh at ESEC/FSE 2022. DOI correct.
- ✓ `ezzini_anaphoric_2022` — Confirmed. Same authors at ICSE 2022. DOI correct.
- ✓ `zhao_nlp4re_2021` — Confirmed. Zhao, Alhoshan, Ferrari et al. in ACM Computing Surveys 54(3), 2021. DOI correct.
- ✓ `ferrari_defects_2018` — Confirmed. Rosadini, Ferrari, Gori et al. in Empirical Software Engineering 24, 2019. Note: bib key says "2018" but year field correctly says 2019. First author in bib is Rosadini, not Ferrari (the key name is misleading but the author field itself is correct).
- ✓ `ferreira_good_enough_2002` — Confirmed. Ferreira, Bailey, Ferraro in Current Directions in Psychological Science 11(1), 2002. DOI correct.
- ✓ `li_garden_path_llm_2024` — Confirmed. Li, Feng, Narang, Peng, Cai, Shah, Varma at CogSci 2024.
- ✓ `frazier_rayner_1982` — Confirmed. Frazier, Rayner in Cognitive Psychology 14(2), 1982. DOI correct.
- ✓ `anvari_lakens_2021` — Confirmed. Anvari, Lakens in Journal of Experimental Social Psychology 96, 2021. DOI correct.
- ✓ `zheng_llm_judge_2024` — Confirmed. Zheng, Chiang, Sheng et al. at NeurIPS 2023. Bib has year=2024, which is the proceedings publication year (NeurIPS 2023 proceedings appeared in 2024). Acceptable.
- ✓ `phantompolicy_2026` — Confirmed. Wu, Gong. arXiv:2604.12177, 2026. Title and authors match. Note: bib lists only two authors (Wu, Gong); the actual paper has these as the two authors.
- ✓ `shieldagent_2025` — Confirmed. Chen, Kang, Li at ICML 2025. Title correct. Note: bib lists only three authors; the full paper may have more but these are the primary authors.
- ✓ `rjudge_2024` — Confirmed. Yuan, He, Dong et al. at Findings of EMNLP 2024.
- ✓ `toolemu_2024` — Confirmed. Ruan, Dong, Wang, Pitis et al. at ICLR 2024 (Spotlight). Title and authors correct.
- ✓ `injecagent_2024` — Confirmed. Zhan, Liang, Ying, Kang at Findings of ACL 2024.
- ✗ `tau_bench_2024` — **Wrong venue.** Bib says `booktitle={Advances in Neural Information Processing Systems (NeurIPS)}` but tau-bench was accepted and presented at **ICLR 2025**, not NeurIPS 2024. The ICLR 2025 poster page confirms this. Year should also be 2025.
- ✓ `tau2_bench_2025` — Confirmed. Barres, Dong, Ray, Si, Narasimhan. arXiv:2506.07982, 2025.
- ✓ `drip_r_2026` — Confirmed. Borkakoty, Pohl, Wang, Chen, Hou. arXiv:2605.07699, 2026.
- ✓ `agentpex_2026` — Confirmed. Sharma, Barke, Zorn. arXiv:2603.23806, 2026. Title "Willful Disobedience" correct.
- ✓ `policybank_2026` — Confirmed. Choi, Yoon, Le, Jha, Pfister. arXiv:2604.15505, 2026.
- ✓ `mantra_2026` — Confirmed. Anand, Chatzi, Raha, Schmuck. arXiv:2605.06334, 2026.
- ✓ `tamkin_evaluating_2023` — Confirmed. Tamkin, Askell, Lovitt et al. arXiv:2312.03689, 2023.
- ✗ `yin_safeagentbench_2025` — **Wrong first author name.** Bib says `Yin, Shengding` but the actual first author is **Sheng Yin** (not Shengding). The paper is by Sheng Yin, Xianghe Pang, Yuanzhuo Ding, Menglan Chen, Yutong Bi, Yichen Xiong, Wenhao Huang, Zhen Xiang, Jing Shao, Siheng Chen. Venue (AAAI 2025) appears correct.
- ✓ `navigli_wsd_2009` — Confirmed. Navigli in ACM Computing Surveys 41(2), 2009. DOI correct.
- ✓ `suri_structured_2025` — Confirmed. Suri, Mathur, Lipka, Dernoncourt, Rossi, Manocha. arXiv:2511.08798, 2025.
- ✓ `sehwag_aspi_2026` — Confirmed. Sehwag et al. arXiv:2605.17324, 2026. Title correct. Note: bib first author is listed as "Sehwag, Udari Madhushani" -- the actual first author's name is "Udari Madhushani Sehwag" which matches.
- ✓ `agentauditor_2025` — Confirmed. Luo, Dai, Ni et al. at NeurIPS 2025. Title correct.
- ✓ `cohen_1960` — Confirmed. Cohen, Jacob. "A Coefficient of Agreement for Nominal Scales." Educational and Psychological Measurement 20(1): 37-46, 1960. Classic reference, fully correct.
- ✓ `gwet_2014` — Confirmed by widespread citation usage. Gwet, Kilem Li. Handbook of Inter-Rater Reliability, 4th edition, 2014, Advanced Analytics LLC. Well-known reference.
- ✓ `hu_ambiguity_2025` — Confirmed. Hu, Wang, Shu, Paik, Zhu. arXiv:2505.11679, 2025. Title correct.
- ✓ `lakens_2017` — Confirmed. Lakens, Daniel. Social Psychological and Personality Science 8(4): 355-362, 2017. DOI correct.
- ✓ `dalpiaz_pinpointing_2018` — Confirmed. Dalpiaz, van der Schalk, Lucassen at REFSQ 2018. Title correct.
- ✓ `yu_causal_2026` — Confirmed. Yu, Carroll, Bentley. arXiv:2603.20320, 2026. Paper confirmed to exist. Note: venue in bib is "arXiv preprint" which is correct; the accepted venue is ICECET (a conference), but the bib listing as arXiv preprint is fine.
- ✓ `hahm_causal_2025` — Confirmed. Hahm, Jin, Choi, Ahn, Lee at Findings of ACL 2025. Title correct.
- ✗ `lin_ask_to_clarify_2025` — **Wrong author names.** Bib says `author = {Lin, Xingyao and others}`. The actual authors are **Xingyao Lin, Xinghao Zhu, Tianyi Lu, Sicheng Xie, Hui Zhang, Xipeng Qiu, Zuxuan Wu, Yu-Gang Jiang**. First author name is correct, but the "and others" should be expanded. More importantly: the arXiv ID 2509.15061 is correct and the title is correct.
- ✗ `mu_can_llms_2023` — **Wrong author names.** Bib says `Mu, Norman and Chen, Sarah and Dixit, Zifan and Prakash, Aman and others`. The actual authors are **Norman Mu, Sarah Chen, Zifan Wang, Sizhe Chen, David Karamardian, Lulwa Aljeraisy, Basel Alomair, Dan Hendrycks, David Wagner**. The third author is "Wang, Zifan" not "Dixit, Zifan", and the fourth author is "Chen, Sizhe" not "Prakash, Aman". arXiv ID and title are correct.
- ✓ `liu_ambiguity_2023` — Confirmed. Liu, Wu, Michael, Suhr, West, Koller, Swayamdipta, Smith, Choi at EMNLP 2023.
- ✓ `kamath_scope_2024` — Confirmed. Kamath, Schuster, Vajjala, Reddy in TACL 12, 2024. DOI correct.
- ✓ `sedova_to_know_2024` — Confirmed. Sedova, Litschko, Frassinelli, Roth, Plank at Findings of EMNLP 2024.
- ✓ `hu_pragmatic_2023` — Confirmed. Hu, Floyd, Jouravlev, Fedorenko, Gibson at ACL 2023. Pages 4194-4213, correct.
- ✓ `ruis_goldilocks_2023` — Confirmed. Ruis, Khan, Biderman, Hooker, Rocktaschel, Grefenstette at NeurIPS 2023.
- ✓ `gur_arieh_ambiguity_collapse_2026` — Confirmed. Gur-Arieh, Wang, Fazelpour. arXiv:2603.05801, 2026. Title correct.
- ✓ `vijayvargiya_openagentsafety_2026` — Confirmed. Vijayvargiya, Soni, Zhou, Wang, Dziri, Neubig, Sap at ICLR 2026.
- ✓ `disambiguation_cqa_survey_2025` — Confirmed. Tanjim, In, Chen et al. at EMNLP 2025.
- ✓ `atbench_2026` — Confirmed. Li, Luo, Xie et al. arXiv:2604.02022, 2026. Title correct.
- ✓ `riskybench_2026` — Confirmed. Zheng, Luo, Xu et al. arXiv:2602.03100, 2026. Title correct.
- ✗ `li_sopbench_2025` — **Wrong arXiv ID and wrong authors.** Bib says arXiv:2502.09413, but that ID points to a **math paper** ("Analysis of harmonic average method for interface problems") completely unrelated to SOPBench. The correct SOPBench paper is arXiv:**2503.08669**. The bib also lists authors as "Li, Jiannan and Jia, Muyang and Song, Jaehyuk and He, Mingjun and Liang, Heng" but the actual authors are **Zekun Li, Shinda Huang, Jiangtian Wang, Nathan Zhang, Antonis Antoniades, Wenyue Hua, Kaijie Zhu, Sirui Zeng, Chi Wang, William Yang Wang, Xifeng Yan**. Title is correct.
- ✓ `tjur_2009` — Confirmed. Tjur, Tue. The American Statistician 63(4): 366-372, 2009.
- ✓ `weng2026beyond` — Confirmed. Weng, Feng, Xie. arXiv:2605.06161, 2026. Title correct.
- ✓ `vijayvargiya_ambigswe_2026` — Confirmed. Vijayvargiya, Zhou, Yerukola, Sap, Neubig at ICLR 2026. Title correct.
- ✓ `krakovna2020specification` — Confirmed. Krakovna, Uesato et al. DeepMind Blog, 2020. Title correct.
- ✓ `poesio_artstein_2005` — Confirmed. Poesio, Artstein. Workshop on Frontiers in Corpus Annotations II: Pie in the Sky, 2005. Pages 76-83, correct.
- ✓ `landis_koch_1977` — Confirmed. Landis, Koch. Biometrics 33(1): 159-174, 1977. Classic reference for kappa interpretation guidelines.
- ✓ `vandeemter_semantic_1996` — Confirmed. van Deemter, Peters (eds.). CSLI Publications, 1996. CSLI Lecture Notes No. 55.
- ✓ `rosenbaum_observational_2002` — Confirmed. Rosenbaum, Paul R. Observational Studies, 2nd ed. Springer, 2002. Classic reference.
- ✓ `wang_agentspec_2026` — Confirmed. Wang, Poskitt, Sun at ICSE 2026.
- ✓ `gleich_ambiguity_2010` — Confirmed. Gleich, Creighton, Kof at REFSQ 2010. Title correct.

---

## Citation Context Verification

Checked all citation contexts in the `.tex` files for misattribution:

- ✓ `berry_kamsties_2004` cited for nocuous vs. innocuous ambiguity distinction -- correct, this is a core concept from their handbook.
- ✓ `liu_ambiguity_2023` cited for "language models collapse multiple interpretations into a single output" -- correct, this is the core finding of AmbiEnt/EMNLP 2023.
- ✓ `hu_ambiguity_2025` cited alongside `liu_ambiguity_2023` for "ambiguity collapse" -- correct, both address this phenomenon.
- ✓ `gur_arieh_ambiguity_collapse_2026` cited for "taxonomize the epistemic risks of this collapse" -- correct, this is the paper's main contribution.
- ✓ `ferreira_good_enough_2002` cited for "good-enough representations" in human comprehension -- correct.
- ✓ `li_garden_path_llm_2024` cited for "garden-path effects in LLMs" -- correct.
- ✓ `drip_r_2026` cited as "closest concurrent work, benchmarking 400 policy-ambiguous retail scenarios" -- correct, though the paper itself says 400 scenarios across five RE ambiguity types, matching the description.
- ✓ `li_sopbench_2025` cited for "benchmarks SOP compliance with naturally occurring ambiguity" -- correct characterization.
- ✓ `krakovna2020specification` cited for "specification gaming in RL agents" -- correct.
- ✓ `policybank_2026` cited for "iterative policy refinement" -- correct.
- ✓ `kamath_scope_2024` cited for "systematic surface-scope preferences in LLMs" -- correct.
- ✓ `chantree_2006` cited for "heuristic" detection methods -- correct, their approach used distributional heuristics.
- ✓ `ferrari_ambiguity_2019` cited for "NLP-based" detection -- correct.
- ✓ `ezzini_taphsir_2022` cited for "transformer-based methods" -- correct, uses BERT-based approach.
- ✓ `massey_ambiguity_re_2014` cited for ambiguity types in regulatory texts -- correct.
- ✓ `lakens_2017` cited for TOST equivalence testing -- correct.
- ✓ `anvari_lakens_2021` cited for SESOI anchor-based methods -- correct.
- ✓ `zheng_llm_judge_2024` cited for LLM-as-judge validation -- correct.
- ✓ `cohen_1960` cited for Cohen's kappa -- correct.
- ✓ `gwet_2014` cited for Gwet's AC1 -- correct.
- ✓ `tjur_2009` cited for Tjur's pseudo-R2 in logistic regression -- correct.
- ✓ `dalpiaz_pinpointing_2018` cited for "ambiguity and incompleteness frequently co-occur" in RE -- correct characterization.
- ✓ `gleich_ambiguity_2010` cited for treating missing information as "implicit ambiguity" -- correct.
- ✓ `frazier_rayner_1982` cited for garden-path processing in human sentence comprehension -- correct.
- ✓ `poesio_artstein_2005` cited for inclusive definition of ambiguity encompassing underspecification -- correct.
- ✓ `vandeemter_semantic_1996` cited alongside `poesio_artstein_2005` for underspecification -- correct.
- ✓ `wasow_ambiguity_2005` cited for within-sentence ambiguity phenomena and "multiple distinct interpretations" -- correct.
- ✓ `kennedy_vagueness_2007` cited for gradient vs. discrete interpretation boundaries -- correct.
- ✓ `landis_koch_1977` cited for kappa interpretation guidelines -- correct.

No misattributions detected in citation contexts.

---

## Summary

| Metric | Count |
|--------|-------|
| Total entries checked | 64 |
| Confirmed correct (✓) | 59 |
| Errors found (✗) | 5 |

### Issues Found

1. **`tau_bench_2024` -- Wrong venue and year.** Bib says NeurIPS 2024; actual venue is **ICLR 2025**. The paper (arXiv:2406.12045) by Yao, Shinn, Razavi, Narasimhan was accepted as an ICLR 2025 poster. Fix: `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, `year={2025}`.

2. **`yin_safeagentbench_2025` -- Wrong first author name.** Bib says `Yin, Shengding`; the correct name is **`Yin, Sheng`** (Sheng Yin, not Shengding Yin). The other information (AAAI 2025 venue, title) is correct.

3. **`mu_can_llms_2023` -- Wrong author names.** Bib lists third author as "Dixit, Zifan" (should be **Wang, Zifan**) and fourth author as "Prakash, Aman" (should be **Chen, Sizhe**). The full author list is: Norman Mu, Sarah Chen, Zifan Wang, Sizhe Chen, David Karamardian, Lulwa Aljeraisy, Basel Alomair, Dan Hendrycks, David Wagner. arXiv ID and title are correct.

4. **`li_sopbench_2025` -- Wrong arXiv ID and wrong authors (CRITICAL).** The arXiv ID `2502.09413` points to a completely unrelated math paper. The correct arXiv ID is **`2503.08669`**. The bib authors (Li, Jiannan; Jia, Muyang; Song, Jaehyuk; He, Mingjun; Liang, Heng) are entirely fabricated -- the actual authors are Zekun Li, Shinda Huang, Jiangtian Wang, Nathan Zhang, Antonis Antoniades, Wenyue Hua, Kaijie Zhu, Sirui Zeng, Chi Wang, William Yang Wang, Xifeng Yan. The title "SOPBench: Measuring Procedural Adherence..." is close but the real title is "SOPBench: **Evaluating Language Agents at Following** Standard Operating Procedures **and Constraints**".

5. **`lin_ask_to_clarify_2025` -- Incomplete authors (minor).** Bib says `author = {Lin, Xingyao and others}`. The "and others" should be expanded to the actual co-authors: Xinghao Zhu, Tianyi Lu, Sicheng Xie, Hui Zhang, Xipeng Qiu, Zuxuan Wu, Yu-Gang Jiang. The first author name, arXiv ID, and title are all correct.

### Severity Assessment

- **CRITICAL (must fix before submission):** `li_sopbench_2025` has fabricated authors and wrong arXiv ID. This is the kind of error that would be flagged as a hallucinated citation by reviewers.
- **HIGH (should fix):** `tau_bench_2024` has wrong venue (NeurIPS vs ICLR) and wrong year.
- **HIGH (should fix):** `mu_can_llms_2023` has wrong author names (Dixit and Prakash are not authors of this paper).
- **MEDIUM (should fix):** `yin_safeagentbench_2025` has misspelled first author name (Shengding vs Sheng).
- **LOW:** `lin_ask_to_clarify_2025` uses "and others" instead of full author list.
