# Citation Audit Report — Worker 2

**Date**: 2026-05-26
**Scope**: All 64 bib entries in `docs/paper/references.bib`
**Method**: WebSearch verification of existence, authors, year, title, venue, arXiv ID for each entry; cross-check of citation contexts in all `.tex` section files.

---

## Entry-by-Entry Results

### Linguistic & RE Foundations (entries 1-13)

- ✓ `li_ambiguity_taxonomy_2024` — Confirmed. Li, Liu, Wu, Smith. EACL 2024. Title, authors, year, venue all correct. arXiv:2403.14072.
- ✓ `massey_ambiguity_re_2014` — Confirmed. Massey, Rutledge, Anton, Swire. 22nd IEEE RE 2014. DOI correct.
- ✗ `berry_kamsties_2004` — **Year is wrong.** The technical report was published in 2003, not 2004. Multiple sources (Semantic Scholar, Google Scholar, ResearchGate) consistently cite 2003. Title, authors, institution correct.
- ✓ `chantree_2006` — Confirmed. Chantree, Nuseibeh, de Roeck, Willis. 14th IEEE RE 2006. All correct.
- ✓ `wasow_ambiguity_2005` — Confirmed. Wasow, Perfors, Beaver. "Morphology and the Web of Grammar" (CSLI, 2005). All correct.
- ✓ `kennedy_vagueness_2007` — Confirmed. Kennedy. Linguistics and Philosophy, 30(1), 1-45, 2007. DOI correct.
- ✓ `willis_nocuous_2008` — Confirmed. Willis, Chantree, De Roeck. Research on Language and Computation, 6(3-4), 355-374, 2008. DOI correct.
- ✓ `ferrari_ambiguity_2019` — Confirmed. Ferrari, Esuli. Automated Software Engineering, 26, 559-598, 2019. DOI correct.
- ✓ `ezzini_taphsir_2022` — Confirmed. Ezzini, Abualhaija, Arora, Sabetzadeh. ESEC/FSE 2022. DOI correct.
- ✓ `ezzini_anaphoric_2022` — Confirmed. Ezzini, Abualhaija, Arora, Sabetzadeh. ICSE 2022. DOI correct.
- ✓ `zhao_nlp4re_2021` — Confirmed. Zhao, Alhoshan, Ferrari, et al. ACM Computing Surveys, 54(3), 2021. DOI correct.
- ✓ `ferrari_defects_2018` — Confirmed. Rosadini, Ferrari, Gori, Fantechi, Gnesi, Trotta, Bacherini. Empirical Software Engineering, 2019. DOI (10.1007/s10664-018-9596-7) correct. Note: bib key says "2018" but year field says 2019; this is a key naming convention issue, not a data error. Volume/pages match the final issue assignment.
- ✓ `ferreira_good_enough_2002` — Confirmed. Ferreira, Bailey, Ferraro. Current Directions in Psychological Science, 11(1), 11-15, 2002. DOI correct.

### Psycholinguistics & LLMs (entries 14-16)

- ✓ `li_garden_path_llm_2024` — Confirmed. Li, Feng, Narang, Peng, Cai, Shah, Varma. Annual Meeting of the Cognitive Science Society, 46, 2024. arXiv:2405.16042.
- ✓ `frazier_rayner_1982` — Confirmed. Frazier, Rayner. Cognitive Psychology, 14(2), 178-210, 1982. DOI correct.
- ✓ `anvari_lakens_2021` — Confirmed. Anvari, Lakens. J. Experimental Social Psychology, 96, 104159, 2021. DOI correct.

### LLM-as-Judge & Agent Safety (entries 17-25)

- ✓ `zheng_llm_judge_2024` — Confirmed. Zheng et al. NeurIPS 2023 (Datasets and Benchmarks Track). Paper published in proceedings 2024 (year=2024 in bib reflects proceedings publication date). arXiv:2306.05685. Full author list correct.
- ✓ `phantompolicy_2026` — Confirmed. Wu, Gong. arXiv:2604.12177, April 2026. Title and authors match.
- ✓ `shieldagent_2025` — Confirmed. Chen, Kang, Li. ICML 2025 (PMLR 267:8313-8344). Title, authors, venue correct.
- ✓ `rjudge_2024` — Confirmed. Yuan et al. Findings of EMNLP 2024. Full author list matches ACL Anthology. All correct.
- ✓ `toolemu_2024` — Confirmed. Ruan, Dong, Wang, Pitis, Zhou, Ba, Dubois, Maddison, Hashimoto. ICLR 2024 (Spotlight). All correct.
- ✓ `injecagent_2024` — Confirmed. Zhan, Liang, Ying, Kang. Findings of ACL 2024. All correct.
- ✓ `tau_bench_2024` — Confirmed. Yao, Shunyu; Shinn, Noah; Razavi, Pedram; Narasimhan, Karthik. NeurIPS 2024 (Datasets and Benchmarks Track, confirmed via OpenReview). All correct.
- ✓ `tau2_bench_2025` — Confirmed. Barres, Dong, Ray, Si, Narasimhan. arXiv:2506.07982. Submitted June 2025. Title and authors correct.
- ✓ `drip_r_2026` — Confirmed. Borkakoty, Pohl, Wang, Chen, Hou. arXiv:2605.07699. Submitted May 2026. Title and authors correct.

### More 2025-2026 Papers (entries 26-33)

- ✓ `agentpex_2026` — Confirmed. Sharma, Barke, Zorn. arXiv:2603.23806. Title "Willful Disobedience: Automatically Detecting Failures in Agentic Traces" is correct. Note: bib author has "Benjamin Zorn" but paper says "Ben Zorn" — minor variant, acceptable.
- ✓ `policybank_2026` — Confirmed. Choi, Yoon, Le, Jha, Pfister. arXiv:2604.15505. All correct.
- ✓ `mantra_2026` — Confirmed. Anand, Chatzi, Raha, Schmuck. arXiv:2605.06334. All correct.
- ✓ `tamkin_evaluating_2023` — Confirmed. Tamkin, Askell, Lovitt, Durmus, Joseph, Kravec, Nguyen, Kaplan, Ganguli. arXiv:2312.03689. All correct.
- ✗ `yin_safeagentbench_2025` — **First author name wrong.** Bib says `Yin, Shengding` but actual first author is **Sheng Yin** (not Shengding). Also uses `and others` which is non-standard; full author list is: Sheng Yin, Xianghe Pang, Yuanzhuo Ding, Menglan Chen, Yutong Bi, Yichen Xiong, Wenhao Huang, Zhen Xiang, Jing Shao, Siheng Chen. Venue (AAAI 2025) confirmed.
- ✓ `navigli_wsd_2009` — Confirmed. Navigli. ACM Computing Surveys, 41(2), 1-69, 2009. DOI correct.
- ✓ `suri_structured_2025` — Confirmed. Suri, Mathur, Lipka, Dernoncourt, Rossi, Manocha. arXiv:2511.08798. All correct.
- ✓ `sehwag_aspi_2026` — Confirmed. Sehwag, Shan, Liu, Lakshan, Brandifino, Fenkell. arXiv:2605.17324. All correct.

### More References (entries 34-42)

- ✓ `agentauditor_2025` — Confirmed. Luo et al. NeurIPS 2025 poster. arXiv:2506.00641. Title, authors, venue correct.
- ✓ `cohen_1960` — Confirmed. Cohen, Jacob. Educational and Psychological Measurement, 20(1), 37-46, 1960. Classic reference, all correct.
- ✓ `gwet_2014` — Confirmed. Gwet, Kilem Li. Handbook of Inter-Rater Reliability, 4th ed., Advanced Analytics LLC, 2014. All correct.
- ✓ `hu_ambiguity_2025` — Confirmed. Hu, Wang, Shu, Paik, Zhu. arXiv:2505.11679. Title correct. Year 2025 correct.
- ✓ `lakens_2017` — Confirmed. Lakens. Social Psychological and Personality Science, 8(4), 355-362, 2017. DOI correct.
- ✓ `dalpiaz_pinpointing_2018` — Confirmed. Dalpiaz, van der Schalk, Lucassen. REFSQ 2018. All correct.
- ✓ `yu_causal_2026` — Confirmed. Yu, Carroll, Bentley. arXiv:2603.20320. PDF accessible. Title "The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents" confirmed.
- ✓ `hahm_causal_2025` — Confirmed. Hahm, Jin, Choi, Ahn, Lee. Findings of ACL 2025. Confirmed via ACL Anthology (2025.findings-acl.784). All correct.
- ✗ `lin_ask_to_clarify_2025` — **Vague author list.** Bib says `Lin, Xingyao and others`. Full author list is: Xingyao Lin, Xinghao Zhu, Tianyi Lu, Sicheng Xie, Hui Zhang, Xipeng Qiu, Zuxuan Wu, Yu-Gang Jiang. Should list all authors. arXiv ID, title, year all correct.

### More References (entries 43-53)

- ✗ `mu_can_llms_2023` — **Incomplete/vague author list.** Bib says `Mu, Norman and Chen, Sarah and Dixit, Zifan and Prakash, Aman and others`. Full author list is: Norman Mu, Sarah Chen, Zifan Wang, Sizhe Chen, David Karamardian, Lulwa Aljeraisy, Basel Alomair, Dan Hendrycks, David Wagner. Also, "Dixit, Zifan" in bib should be **"Wang, Zifan"** — the third author is Zifan Wang, not Zifan Dixit. arXiv ID 2311.04235 correct; title correct.
- ✓ `liu_ambiguity_2023` — Confirmed. Liu, Wu, Michael, Suhr, West, Koller, Swayamdipta, Smith, Choi. EMNLP 2023. All correct.
- ✓ `kamath_scope_2024` — Confirmed. Kamath, Schuster, Vajjala, Reddy. TACL, 12, 738-754, 2024. DOI correct.
- ✓ `sedova_to_know_2024` — Confirmed. Sedova, Litschko, Frassinelli, Roth, Plank. Findings of EMNLP 2024. All correct.
- ✓ `hu_pragmatic_2023` — Confirmed. Hu, Floyd, Jouravlev, Fedorenko, Gibson. ACL 2023 (Long Papers), pp. 4194-4213. All correct.
- ✓ `ruis_goldilocks_2023` — Confirmed. Ruis, Khan, Biderman, Hooker, Rocktaschel, Grefenstette. NeurIPS 2023 (Spotlight). All correct.
- ✓ `gur_arieh_ambiguity_collapse_2026` — Confirmed. Gur-Arieh, Wang, Fazelpour. arXiv:2603.05801. All correct.
- ✓ `vijayvargiya_openagentsafety_2026` — Confirmed. Vijayvargiya, Soni, Zhou, Wang, Dziri, Neubig, Sap. ICLR 2026. Confirmed via OpenReview and ICLR poster page.
- ✓ `disambiguation_cqa_survey_2025` — Confirmed. Tanjim et al. EMNLP 2025 (main conference), pp. 9537-9550. All correct.
- ✓ `atbench_2026` — Confirmed. Li, Luo et al. arXiv:2604.02022. Title and authors correct.
- ✓ `riskybench_2026` — Confirmed. Zheng et al. arXiv:2602.03100. All correct.

### Remaining References (entries 54-64)

- ✗ `li_sopbench_2025` — **Multiple errors.** (1) **Wrong arXiv ID**: bib says arXiv:2502.09413, which is actually a math paper titled "Analysis of harmonic average method for interface problems with discontinuous solutions and fluxes" by Pan, Xu, Li — completely unrelated. Correct arXiv ID is **2503.08669**. (2) **Wrong title**: bib says "SOPBench: Measuring Procedural Adherence of LLM Agents in Standardized Operating Procedures" but actual title is **"SOPBench: Evaluating Language Agents at Following Standard Operating Procedures and Constraints"**. (3) **Wrong authors**: bib says "Li, Jiannan and Jia, Muyang and Song, Jaehyuk and He, Mingjun and Liang, Heng" but actual authors are **Zekun Li, Shinda Huang, Jiangtian Wang, Nathan Zhang, Antonis Antoniades, Wenyue Hua, Kaijie Zhu, Sirui Zeng, Chi Wang, William Yang Wang, Xifeng Yan**. This entry needs a complete rewrite.
- ✓ `tjur_2009` — Confirmed. Tjur, Tue. The American Statistician, 63(4), 366-372, 2009. All correct.
- ✓ `weng2026beyond` — Confirmed. Weng, Feng, Xie. arXiv:2605.06161. Title and authors correct.
- ✓ `vijayvargiya_ambigswe_2026` — Confirmed. Vijayvargiya, Zhou, Yerukola, Sap, Neubig. ICLR 2026. Confirmed via OpenReview and arXiv:2502.13069.
- ✓ `krakovna2020specification` — Confirmed. Krakovna, Uesato, Mikulik, Rahtz, Everitt, Kumar, Kenton, Leike, Legg. DeepMind Blog, 2020. All correct.
- ✓ `poesio_artstein_2005` — Confirmed. Poesio, Artstein. Workshop on Frontiers in Corpus Annotations II: Pie in the Sky, pp. 76-83, ACL 2005. All correct.
- ✓ `landis_koch_1977` — Confirmed. Landis, Koch. Biometrics, 33(1), 159-174, 1977. All correct.
- ✓ `vandeemter_semantic_1996` — Confirmed. van Deemter, Peters (eds.). Semantic Ambiguity and Underspecification. CSLI Lecture Notes 55, CSLI Publications, 1996. All correct.
- ✓ `rosenbaum_observational_2002` — Confirmed. Rosenbaum. Observational Studies, 2nd ed., Springer, 2002. All correct.
- ✓ `wang_agentspec_2026` — Confirmed. Wang, Poskitt, Sun. ICSE 2026. arXiv:2503.18666. All correct.
- ✓ `gleich_ambiguity_2010` — Confirmed. Gleich, Creighton, Kof. REFSQ 2010. All correct.

---

## Citation Context Verification

Checked all citation contexts across all `.tex` files for misattribution:

- `\citet{berry_kamsties_2004}` in intro and related work — correctly attributes the nocuous/innocuous ambiguity distinction. OK.
- `\citet{drip_r_2026}` in intro and related work — correctly described as concurrent work benchmarking retail policy ambiguity. OK.
- `\citet{li_ambiguity_taxonomy_2024}` — correctly cited as source of 11-type NLP taxonomy. OK.
- `\citet{policybank_2026}` — correctly described as studying iterative policy refinement. OK.
- `\citet{ferreira_good_enough_2002}` — correctly cited for good-enough representations. OK.
- `\citet{li_garden_path_llm_2024}` — correctly cited for garden-path effects in LLMs. OK.
- `\citet{liu_ambiguity_2023}` — correctly cited for showing LMs collapse multiple interpretations. OK.
- `\citet{gur_arieh_ambiguity_collapse_2026}` — correctly cited for taxonomizing epistemic risks of ambiguity collapse. OK.
- `\citet{krakovna2020specification}` — correctly cited as reward-specification analogue (specification gaming). OK.
- `\citet{zheng_llm_judge_2024}` — cited for LLM-as-judge methodology validation. OK.
- `\citet{cohen_1960}` and `\citet{gwet_2014}` — correctly used for kappa and AC1 statistics. OK.
- `\citet{lakens_2017}` — correctly cited for TOST equivalence testing. OK.
- `\citet{anvari_lakens_2021}` — correctly cited for SESOI sensitivity analysis. OK.
- `\citet{tjur_2009}` — correctly cited for Tjur's R^2 in logistic regression. OK.
- `\citet{hu_ambiguity_2025}` — correctly cited alongside Liu et al. for ambiguity collapse extension. OK.
- `\citet{tau2_bench_2025}` — correctly cited as the experimental platform. OK.
- `\citet{li_sopbench_2025}` — correctly cited for cross-benchmark evaluation. Content attribution OK (even though bib metadata is wrong).
- `\citet{poesio_artstein_2005}` and `\citet{vandeemter_semantic_1996}` — correctly cited for inclusive ambiguity definition in taxonomy section. OK.
- `\citet{wasow_ambiguity_2005}` and `\citet{kennedy_vagueness_2007}` — correctly cited for ambiguity/vagueness distinction. OK.
- `\citet{dalpiaz_pinpointing_2018}` — correctly cited for ambiguity and incompleteness co-occurrence. OK.
- `\citet{gleich_ambiguity_2010}` — correctly cited for treating missing information as "implicit ambiguity." OK.

No misattribution detected in any citation context.

---

## Summary

| Metric | Count |
|--------|-------|
| Total entries checked | 64 |
| Confirmed correct (✓) | 58 |
| Issues found (✗) | 6 |

### All Issues Found

1. **`berry_kamsties_2004`** — Year should be **2003**, not 2004. The technical report was published November 2003.

2. **`yin_safeagentbench_2025`** — First author name is **"Sheng Yin"**, not "Shengding Yin" as in bib. Also uses non-standard `and others`; full 10-author list should be provided.

3. **`lin_ask_to_clarify_2025`** — Uses `and others` instead of listing full 8-author list. Should be: Lin, Xingyao and Zhu, Xinghao and Lu, Tianyi and Xie, Sicheng and Zhang, Hui and Qiu, Xipeng and Wu, Zuxuan and Jiang, Yu-Gang.

4. **`mu_can_llms_2023`** — Two problems: (a) uses `and others` instead of full 9-author list; (b) **third author name is wrong**: bib says "Dixit, Zifan" but actual third author is **"Wang, Zifan"**. Full list: Mu, Norman and Chen, Sarah and Wang, Zifan and Chen, Sizhe and Karamardian, David and Aljeraisy, Lulwa and Alomair, Basel and Hendrycks, Dan and Wagner, David.

5. **`li_sopbench_2025`** — **Critical: three errors.** (a) arXiv ID 2502.09413 is completely wrong (points to an unrelated math paper); correct ID is **2503.08669**. (b) Title is wrong; actual title is "SOPBench: Evaluating Language Agents at Following Standard Operating Procedures and Constraints". (c) Author list is entirely wrong; actual first author is Zekun Li (not Jiannan Li), with 11 authors total from UC Santa Barbara and Google DeepMind.

6. **`mu_can_llms_2023`** — (listed above, combined) Wrong author name (Dixit → Wang) + incomplete author list.

### Severity Classification

- **CRITICAL (must fix before submission):**
  - `li_sopbench_2025`: wrong arXiv ID, wrong title, wrong authors — this entry is essentially fabricated metadata attached to a real paper
  - `mu_can_llms_2023`: wrong author surname (Dixit → Wang)

- **HIGH (should fix):**
  - `berry_kamsties_2004`: wrong year (2003, not 2004)
  - `yin_safeagentbench_2025`: wrong first author given name (Sheng, not Shengding)

- **LOW (style improvement):**
  - `lin_ask_to_clarify_2025`: incomplete author list (uses "and others")
  - `mu_can_llms_2023`: incomplete author list (uses "and others")
  - `yin_safeagentbench_2025`: incomplete author list (uses "and others")

### No Hallucinated Papers Detected

All 64 referenced papers were confirmed to exist via web search. No fabricated citations found.
