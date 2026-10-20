# paper research bib sync

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_paper_research_bib_sync_20260520T215727.jsonl`
- **Structured JSON:** [`84ffdbfab3218fe6c116.json`](../../sessions/84/84ffdbfab3218fe6c116.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-20T21:59:17.894909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260520T215727",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T21:59:17.895432+00:00_

1	meta:
2	  last_updated: '2026-05-20T22:30:00Z'
3	  total_papers: 33
4	categories:
5	  - key: irt-llm
6	    label: IRT for LLM Evaluation
7	  - key: contamination-detection
8	    label: Benchmark Contamination Detection
9	  - key: person-fit
10	    label: Person-Fit Statistics (Psychometrics)
11	  - key: post-rl-contamination
12	    label: Post-RL Contamination
13	  - key: irt-foundations
14	    label: IRT Foundations
15	  - key: llm-evaluation-infrastructure
16	    label: LLM Evaluation Infrastructure
17	papers:
18	  psnirt2026:
19	    title: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"
20	    authors: ["Zhou, H.", "Huang, H.", "Zhao, Z.", "Han, L.", "Wang, H.", "Chen, K.", "Yang, M.", "Bao, W.", "Dong, J.", "Xu, B.", "Zhu, C.", "Cao, H.", "Zhao, T."]
21	    year: 2026
22	    venue: "AAAI 2026 Oral"
23	    url: "https://arxiv.org/abs/2505.15055"
24	    doi: ""
25	    bibtex_key: psnirt2026
26	    category: irt-llm
27	    role: foundation
28	    relevance: "Provides calibrated 4PL item parameters (a,b,c,d) for 41,871 items across 11 benchmarks — the item bank our method builds on"
29	    abstract: ""
30	    semantic_scholar_id: ""
31	    verified: true
32	    added_by: director
33	    added_at: '2026-05-20T08:00:00Z'
34	
35	  atlas2025:
36	    title: "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"
37	    authors: ["Li, P.", "Tang, X.", "Chen, S.", "Cheng, Y.", "Metoyer, R.", "Hua, T.", "Chawla, N. V."]
38	    year: 2025
39	    venue: "arXiv preprint"
40	    url: "https://arxiv.org/abs/2511.04689"
41	    doi: ""
42	    bibtex_key: atlas2025
43	    category: irt-llm
44	    role: background
45	    relevance: "ATLAS uses IRT for adaptive testing efficiency; related IRT-for-LLM work but not person-fit"
46	    abstract: ""
47	    semantic_scholar_id: ""
48	    verified: true
49	    added_by: director
50	    added_at: '2026-05-20T08:00:00Z'
51	
52	  constat2024:
53	    title: "ConStat: 
…[truncated 23457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260520T215727",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T21:59:17.895721+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
  "content": "% =============================================================================\n% IRT for LLM Evaluation\n% =============================================================================\n\n@article{martinezplumed2019,\n  title = {Item Response Theory in {AI}: Analysing Machine Learning Classifiers at the Instance Level},\n  author = {Mart{\\'\\i}nez-Plumed, F. and Prud{\\^e}ncio, R. B. C. and Mart{\\'\\i}nez-Us{\\'o}, A. and Hern{\\'a}ndez-Orallo, J.},\n  journal = {Artificial Intelligence},\n  year = {2019},\n  doi = {10.1016/j.artint.2018.09.004},\n  url = {https://www.sciencedirect.com/science/article/pii/S0004370219300220},\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  title = {tinyBenchmarks: Evaluating {LLMs} with Fewer Examples},\n  author = {Polo, F. M. and Weber, L. and Choshen, L. and Sun, Y. and Xu, G. and Yurochkin, M.},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.14992},\n}\n\n@article{atlas2025,\n  title = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  author = {Li, P. and Tang, X. and Chen, S. and Cheng, Y. and Metoyer, R. and Hua, T. and Chawla, N. V.},\n  journal = {arXiv preprint arXiv:2511.04689},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.04689},\n}\n\n@inproceedings{psnirt2026,\n  title = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  author = {Zhou, H. and Huang, H. and Zhao, Z. and Han, L. and Wang, H. and Chen, K. and Yang, M. and Bao, W. and Dong, J. and Xu, B. and Zhu, C. and Cao, H. and Zhao, T.},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2505.15055},\n}\n\n% =============================================================================\n% Benchmark Contamination Detection\n% =============================================================================\n\n@inproceedings{dodge2021,\n  title = {Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus},\n  author = {Dodge, J. and Sap, M. and Marasovi{\\'c}, A. and Agnew, W. and Ilharco, G. and Groeneveld, D. and Mitchell, M. and Gardner, M.},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2021},\n  doi = {10.18653/v1/2021.emnlp-main.98},\n  url = {https://aclanthology.org/2021.emnlp-main.98/},\n}\n\n@inproceedings{magar2022,\n  title = {Data Contamination: From Memorization to Exploitation},\n  author = {Magar, I. and Schwartz, R.},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.acl-short.18},\n  url = {https://aclanthology.org/2022.acl-short.18/},\n}\n\n@inproceedings{sainz2023,\n  title = {{NLP} Evaluation in Trouble: On the Need to Measure {LLM} Data Contamination for each Benchmark},\n  author = {Sainz, O. and Campos, J. and Garc{\\'\\i}a-Ferrero, I. and Etxaniz, J. and Lopez de Lacalle, O. and Agirre, E.},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-emnlp.722},\n  url = {https://aclanthology.org/2023.findings-emnlp.722/},\n}\n\n@inproceedings{jacovi2023,\n  title = {Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks},\n  author = {Jacovi, A. and Caciularu, A. and Goldman, O. and Goldberg, Y.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.308},\n  url = {https://aclanthology.org/2023.emnlp-main.308/},\n}\n\n@inproceedings{constat2024,\n  title = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  author = {Dekoninck, J. and M{\\\"u}ller, M. and Vechev, M.},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.16281},\n}\n\n@inproceedings{minkprob2024,\n  title = {Detecting Pretraining Data from Large Language Models},\n  author = {Shi, W. and Ajith, A. and Xia, M. and Huang, Y. and Liu, D. and Blevins, T. and Chen, D. and Zettlemoyer, L.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.16789},\n}\n\n@inproceedings{oren2024,\n  title = {Proving Test Set Contamination in Black-Box Language Models},\n  author = {Oren, Y. and Meister, N. and Chatterji, N. S. and Ladhak, F. and Hashimoto, T.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.17623},\n}\n\n@inproceedings{golchin2024,\n  title = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  author = {Golchin, S. and Surdeanu, M.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.08493},\n}\n\n@inproceedings{deng2024,\n  title = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  author = {Deng, C. and Zhao, Y. and Tang, X. and Gerstein, M. and Cohan, A.},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.482},\n  url = {https://aclanthology.org/2024.naacl-long.482/},\n}\n\n@inproceedings{codec2026,\n  title = {Detecting Data Contamination in {LLMs} via In-Context Learning},\n  author = {Zawalski, M. and Boubdir, M. and Ba{\\l}azy, K. and Nushi, B. and Ribalta, P.},\n  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2510.27055},\n}\n\n% =============================================================================\n% Person-Fit Statistics (Psychometrics)\n% =============================================================================\n\n@article{drasgow1985,\n  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},\n  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  year = {1985},\n  doi = {10.1111/j.2044-8317.1985.tb00817.x},\n}\n\n@article{meijer2001,\n  title = {Methodology Review: Evaluating Person Fit},\n  author = {Meijer, R. R. and Sijtsma, K.},\n  journal = {Applied Psychological Measurement},\n  year = {2001},\n  doi = {10.1177/01466210122031957},\n  url = {https://journals.sagepub.com/doi/abs/10.1177/01466210122031957},\n}\n\n@article{snijders2001,\n  title = {Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Parameter},\n  author = {Snijders, T. A. B.},\n  journal = {Psychometrika},\n  year = {2001},\n  doi = {10.1007/BF02294437},\n  url = {https://link.springer.com/article/10.1007/BF02294437},\n}\n\n@article{karabatsos2003,\n  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},\n  author = {Karabatsos, G.},\n  journal = {Applied Measurement in Education},\n  year = {2003},\n  doi = {10.1207/S15324818AME1604_2},\n  url = {https://www.tandfonline.com/doi/abs/10.1207/S15324818AME1604_2},\n}\n\n@article{sinharay2017,\n  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?},\n  author = {Sinharay, S.},\n  journal = {Applied Psychological Measurement},\n  year = {2017},\n  doi = {10.1177/0146621617698453},\n  url = {https://pmc.ncbi.nlm.nih.gov/articles/PMC5978524/},\n}\n\n@article{hong2021lzm,\n  title = {Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types},\n  author = {Hong, M. and Lin, L. and Cheng, Y.},\n  journal = {Psychometrika},\n  year = {2021},\n  doi = {10.1007/s11336-021-09756-3},\n  url = {https://link.springer.com/article/10.1007/s11336-021-09756-3},\n}\n\n% =============================================================================\n% Post-RL Contamination\n% =============================================================================\n\n@article{wang2025fragility,\n  title = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},\n  author = {Wang, H. and Li, H. and Ko, B. and Zhang, H.},\n  journal = {arXiv preprint arXiv:2510.02386},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.02386},\n}\n\n@inproceedings{selfcritique2026,\n  title = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  author = {Tao, Y. and Wang, T. and Dong, Y. and Liu, H. and Zhang, K. and Hu, X. and Li, G.},\n  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2510.09259},\n}\n\n@article{zhang2026rlvr,\n  title = {Detecting {RLVR} Training Data via Structural Convergence of Reasoning},\n  author = {Zhang, H. and Yang, Y. and Yan, J. and Bao, G. and Zhang, Y. and Zhang, Y.},\n  journal = {arXiv preprint arXiv:2602.11792},\n  year = {2026},\n  url = {https://arxiv.org/abs/2602.11792},\n}\n\n% =============================================================================\n% IRT Foundations\n% =============================================================================\n\n@incollection{birnbaum1968,\n  title = {Some Latent Trait Models and Their Use in Inferring an Examinee's Ability},\n  author = {Birnbaum, A.},\n  booktitle = {Statistical Theories of Mental Test Scores},\n  publisher = {Addison-Wesley},\n  year = {1968},\n  editor = {Lord, F. M. and Novick, M. R.},\n  pages = {397--479},\n}\n\n@book{lord1980,\n  title = {Applications of Item Response Theory to Practical Testing Problems},\n  author = {Lord, F. M.},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {1980},\n  doi = {10.4324/9780203056615},\n}\n\n@techreport{barton1981,\n  title = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  author = {Barton, M. A. and Lord, F. M.},\n  institution = {Educational Testing Service},\n  year = {1981},\n  number = {RR-81-20},\n  doi = {10.1002/j.2333-8504.1981.tb01255.x},\n  url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2333-8504.1981.tb01255.x},\n}\n\n@book{embretson2000,\n  title = {Item Response Theory for Psychologists},\n  author = {Embretson, S. E. and Reise, S. P.},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {2000},\n  doi = {10.4324/9781410605269},\n}\n\n@book{deayala2009,\n  title = {The Theory and Practice of Item Response Theory},\n  author = {de Ayala, R. J.},\n  publisher = {Guilford Press},\n  year = {2009},\n}\n\n% =============================================================================\n% LLM Evaluation Infrastructure\n% =============================================================================\n\n@inproceedings{hendrycks2021mmlu,\n  title = {Measuring Massive Multitask Language Understanding},\n  author = {Hendrycks, D. and Burns, C. and Basart, S. and Zou, A. and Mazeika, M. and Song, D. and Steinhardt, J.},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.03300},\n}\n\n@misc{beeching2023openllm,\n  title = {Open {LLM} Leaderboard},\n  author = {Beeching, E. and Fourrier, C. and Habib, N. and Han, S. and Lambert, N. and Rajani, N. and Sanseviero, O. and Tunstall, L. and Wolf, T.},\n  year = {2023},\n  howpublished = {HuggingFace},\n  url = {https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard},\n}\n\n@misc{gao2023evalharness,\n  title = {A Framework for Few-Shot Language Model Evaluation},\n  author = {Gao, L. and Tow, J. and Abbasi, B. and Biderman, S. and Black, S. and DiPofi, A. and Foster, C. and Golding, L. and Hsu, J. and Le Noac'h, A. and Li, H. and McDonell, K. and Muennighoff, N. and Ociepa, C. and Phang, J. and Reynolds, L. and Schoelkopf, H. and Skowron, A. and Sutawika, L. and Tang, E. and Thite, A. and Wang, B. and Wang, K. and Zou, A.},\n  year = {2023},\n  howpublished = {Zenodo},\n  doi = {10.5281/zenodo.10256836},\n  url = {https://zenodo.org/records/10256836},\n}\n\n@article{chang2024survey,\n  title = {A Survey on Evaluation of Large Language Models},\n  author = {Chang, Y. and Wang, X. and Wang, J. and Wu, Y. and Yang, L. and Zhu, K. and Chen, H. and Yi, X. and Wang, C. and Wang, Y. and Ye, W. and Zhang, Y. and Chang, Y. and Yu, P. S. and Yang, Q. and Xie, X.},\n  journal = {ACM Transactions on Intelligent Systems and Technology},\n  year = {2024},\n  doi = {10.1145/3641289},\n  url = {https://arxiv.org/abs/2307.03109},\n}\n\n@article{biderman2024lessons,\n  title = {Lessons from the Trenches on Reproducible Evaluation of Language Models},\n  author = {Biderman, S. and Schoelkopf, H. and Sutawika, L. and Gao, L. and Tow, J. and Abbasi, B. and Aji, A. F. and Ammanamanchi, P. S. and Black, S. and Clive, J. and DiPofi, A. and Etxaniz, J. and Fattori, B. and Forde, J. Z. and Foster, C. and Hsu, J. and Jaiswal, M. and Lee, W. Y. and Li, H. and Lovering, C. and Muennighoff, N. and Pavlick, E. and Phang, J. and Skowron, A. and Tan, S. and Tang, X. and Wang, K. A. and Winata, G. I. and Yvon, F. and Zou, A.},\n  journal = {arXiv preprint arXiv:2405.14782},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.14782},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260520T215727",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
    "content": "% =============================================================================\n% IRT for LLM Evaluation\n% =============================================================================\n\n@article{martinezplumed2019,\n  title = {Item Response Theory in {AI}: Analysing Machine Learning Classifiers at the Instance Level},\n  author = {Mart{\\'\\i}nez-Plumed, F. and Prud{\\^e}ncio, R. B. C. and Mart{\\'\\i}nez-Us{\\'o}, A. and Hern{\\'a}ndez-Orallo, J.},\n  journal = {Artificial Intelligence},\n  year = {2019},\n  doi = {10.1016/j.artint.2018.09.004},\n  url = {https://www.sciencedirect.com/science/article/pii/S0004370219300220},\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  title = {tinyBenchmarks: Evaluating {LLMs} with Fewer Examples},\n  author = {Polo, F. M. and Weber, L. and Choshen, L. and Sun, Y. and Xu, G. and Yurochkin, M.},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.14992},\n}\n\n@article{atlas2025,\n  title = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  author = {Li, P. and Tang, X. and Chen, S. and Cheng, Y. and Metoyer, R. and Hua, T. and Chawla, N. V.},\n  journal = {arXiv preprint arXiv:2511.04689},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.04689},\n}\n\n@inproceedings{psnirt2026,\n  title = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  author = {Zhou, H. and Huang, H. and Zhao, Z. and Han, L. and Wang, H. and Chen, K. and Yang, M. and Bao, W. and Dong, J. and Xu, B. and Zhu, C. and Cao, H. and Zhao, T.},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2505.15055},\n}\n\n% =============================================================================\n% Benchmark Contamination Detection\n% =============================================================================\n\n@inproceedings{dodge2021,\n  title = {Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus},\n  author = {Dodge, J. and Sap, M. and Marasovi{\\'c}, A. and Agnew, W. and Ilharco, G. and Groeneveld, D. and Mitchell, M. and Gardner, M.},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2021},\n  doi = {10.18653/v1/2021.emnlp-main.98},\n  url = {https://aclanthology.org/2021.emnlp-main.98/},\n}\n\n@inproceedings{magar2022,\n  title = {Data Contamination: From Memorization to Exploitation},\n  author = {Magar, I. and Schwartz, R.},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.acl-short.18},\n  url = {https://aclanthology.org/2022.acl-short.18/},\n}\n\n@inproceedings{sainz2023,\n  title = {{NLP} Evaluation in Trouble: On the Need to Measure {LLM} Data Contamination for each Benchmark},\n  author = {Sainz, O. and Campos, J. and Garc{\\'\\i}a-Ferrero, I. and Etxaniz, J. and Lopez de Lacalle, O. and Agirre, E.},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-emnlp.722},\n  url = {https://aclanthology.org/2023.findings-emnlp.722/},\n}\n\n@inproceedings{jacovi2023,\n  title = {Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks},\n  author = {Jacovi, A. and Caciularu, A. and Goldman, O. and Goldberg, Y.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.308},\n  url = {https://aclanthology.org/2023.emnlp-main.308/},\n}\n\n@inproceedings{constat2024,\n  title = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  author = {Dekoninck, J. and M{\\\"u}ller, M. and Vechev, M.},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.16281},\n}\n\n@inproceedings{minkprob2024,\n  title = {Detecting Pretraining Data from Large Language Models},\n  author = {Shi, W. and Ajith, A. and Xia, M. and Huang, Y. and Liu, D. and Blevins, T. and Chen, D. and Zettlemoyer, L.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.16789},\n}\n\n@inproceedings{oren2024,\n  title = {Proving Test Set Contamination in Black-Box Language Models},\n  author = {Oren, Y. and Meister, N. and Chatterji, N. S. and Ladhak, F. and Hashimoto, T.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.17623},\n}\n\n@inproceedings{golchin2024,\n  title = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  author = {Golchin, S. and Surdeanu, M.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.08493},\n}\n\n@inproceedings{deng2024,\n  title = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  author = {Deng, C. and Zhao, Y. and Tang, X. and Gerstein, M. and Cohan, A.},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.482},\n  url = {https://aclanthology.org/2024.naacl-long.482/},\n}\n\n@inproceedings{codec2026,\n  title = {Detecting Data Contamination in {LLMs} via In-Context Learning},\n  author = {Zawalski, M. and Boubdir, M. and Ba{\\l}azy, K. and Nushi, B. and Ribalta, P.},\n  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2510.27055},\n}\n\n% =============================================================================\n% Person-Fit Statistics (Psychometrics)\n% =============================================================================\n\n@article{drasgow1985,\n  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},\n  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  year = {1985},\n  doi = {10.1111/j.2044-8317.1985.tb00817.x},\n}\n\n@article{meijer2001,\n  title = {Methodology Review: Evaluating Person Fit},\n  author = {Meijer, R. R. and Sijtsma, K.},\n  journal = {Applied Psychological Measurement},\n  year = {2001},\n  doi = {10.1177/01466210122031957},\n  url = {https://journals.sagepub.com/doi/abs/10.1177/01466210122031957},\n}\n\n@article{snijders2001,\n  title = {Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Parameter},\n  author = {Snijders, T. A. B.},\n  journal = {Psychometrika},\n  year = {2001},\n  doi = {10.1007/BF02294437},\n  url = {https://link.springer.com/article/10.1007/BF02294437},\n}\n\n@article{karabatsos2003,\n  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},\n  author = {Karabatsos, G.},\n  journal = {Applied Measurement in Education},\n  year = {2003},\n  doi = {10.1207/S15324818AME1604_2},\n  url = {https://www.tandfonline.com/doi/abs/10.1207/S15324818AME1604_2},\n}\n\n@article{sinharay2017,\n  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?},\n  author = {Sinharay, S.},\n  journal = {Applied Psychological Measurement},\n  year = {2017},\n  doi = {10.1177/0146621617698453},\n  url = {https://pmc.ncbi.nlm.nih.gov/articles/PMC5978524/},\n}\n\n@article{hong2021lzm,\n  title = {Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types},\n  author = {Hong, M. and Lin, L. and Cheng, Y.},\n  journal = {Psychometrika},\n  year = {2021},\n  doi = {10.1007/s11336-021-09756-3},\n  url = {https://link.springer.com/article/10.1007/s11336-021-09756-3},\n}\n\n% =============================================================================\n% Post-RL Contamination\n% =============================================================================\n\n@article{wang2025fragility,\n  title = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},\n  author = {Wang, H. and Li, H. and Ko, B. and Zhang, H.},\n  journal = {arXiv preprint arXiv:2510.02386},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.02386},\n}\n\n@inproceedings{selfcritique2026,\n  title = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  author = {Tao, Y. and Wang, T. and Dong, Y. and Liu, H. and Zhang, K. and Hu, X. and Li, G.},\n  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2510.09259},\n}\n\n@article{zhang2026rlvr,\n  title = {Detecting {RLVR} Training Data via Structural Convergence of Reasoning},\n  author = {Zhang, H. and Yang, Y. and Yan, J. and Bao, G. and Zhang, Y. and Zhang, Y.},\n  journal = {arXiv preprint arXiv:2602.11792},\n  year = {2026},\n  url = {https://arxiv.org/abs/2602.11792},\n}\n\n% =============================================================================\n% IRT Foundations\n% =============================================================================\n\n@incollection{birnbaum1968,\n  title = {Some Latent Trait Models and Their Use in Inferring an Examinee's Ability},\n  author = {Birnbaum, A.},\n  booktitle = {Statistical Theories of Mental Test Scores},\n  publisher = {Addison-Wesley},\n  year = {1968},\n  editor = {Lord, F. M. and Novick, M. R.},\n  pages = {397--479},\n}\n\n@book{lord1980,\n  title = {Applications of Item Response Theory to Practical Testing Problems},\n  author = {Lord, F. M.},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {1980},\n  doi = {10.4324/9780203056615},\n}\n\n@techreport{barton1981,\n  title = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  author = {Barton, M. A. and Lord, F. M.},\n  institution = {Educational Testing Service},\n  year = {1981},\n  number = {RR-81-20},\n  doi = {10.1002/j.2333-8504.1981.tb01255.x},\n  url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2333-8504.1981.tb01255.x},\n}\n\n@book{embretson2000,\n  title = {Item Response Theory for Psychologists},\n  author = {Embretson, S. E. and Reise, S. P.},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {2000},\n  doi = {10.4324/9781410605269},\n}\n\n@book{deayala2009,\n  title = {The Theory and Practice of Item Response Theory},\n  author = {de Ayala, R. J.},\n  publisher = {Guilford Press},\n  year = {2009},\n}\n\n% =============================================================================\n% LLM Evaluation Infrastructure\n% =============================================================================\n\n@inproceedings{hendrycks2021mmlu,\n  title = {Measuring Massive Multitask Language Understanding},\n  author = {Hendrycks, D. and Burns, C. and Basart, S. and Zou, A. and Mazeika, M. and Song, D. and Steinhardt, J.},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.03300},\n}\n\n@misc{beeching2023openllm,\n  title = {Open {LLM} Leaderboard},\n  author = {Beeching, E. and Fourrier, C. and Habib, N. and Han, S. and Lambert, N. and Rajani, N. and Sanseviero, O. and Tunstall, L. and Wolf, T.},\n  year = {2023},\n  howpublished = {HuggingFace},\n  url = {https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard},\n}\n\n@misc{gao2023evalharness,\n  title = {A Framework for Few-Shot Language Model Evaluation},\n  author = {Gao, L. and Tow, J. and Abbasi, B. and Biderman, S. and Black, S. and DiPofi, A. and Foster, C. and Golding, L. and Hsu, J. and Le Noac'h, A. and Li, H. and McDonell, K. and Muennighoff, N. and Ociepa, C. and Phang, J. and Reynolds, L. and Schoelkopf, H. and Skowron, A. and Sutawika, L. and Tang, E. and Thite, A. and Wang, B. and Wang, K. and Zou, A.},\n  year = {2023},\n  howpublished = {Zenodo},\n  doi = {10.5281/zenodo.10256836},\n  url = {https://zenodo.org/records/10256836},\n}\n\n@article{chang2024survey,\n  title = {A Survey on Evaluation of Large Language Models},\n  author = {Chang, Y. and Wang, X. and Wang, J. and Wu, Y. and Yang, L. and Zhu, K. and Chen, H. and Yi, X. and Wang, C. and Wang, Y. and Ye, W. and Zhang, Y. and Chang, Y. and Yu, P. S. and Yang, Q. and Xie, X.},\n  journal = {ACM Transactions on Intelligent Systems and Technology},\n  year = {2024},\n  doi = {10.1145/3641289},\n  url = {https://arxiv.org/abs/2307.03109},\n}\n\n@article{biderman2024lessons,\n  title = {Lessons from the Trenches on Reproducible Evaluation of Language Models},\n  author = {Biderman, S. and Schoelkopf, H. and Sutawika, L. and Gao, L. and Tow, J. and Abbasi, B. and Aji, A. F. and Ammanamanchi, P. S. and Black, S. and Clive, J. and DiPofi, A. and Etxaniz, J. and Fattori, B. and Forde, J. Z. and Foster, C. and Hsu, J. and Jaiswal, M. and Lee, W. Y. and Li, H. and Lovering, C. and Muennighoff, N. and Pavlick, E. and Phang, J. and Skowron, A. and Tan, S. and Tang, X. and Wang, K. A. and Winata, G. I. and Yvon, F. and Zou, A.},\n  journal = {arXiv preprint arXiv:2405.14782},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.14782},\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T21:59:17.896035+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260520T215727",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T21:59:17.896204+00:00_

33 篇 BibTeX 条目已生成，按 6 个 category 分组，组内按 year 升序排列。entry type 映射：会议 → `@inproceedings`，期刊 → `@article`，arXiv → `@article`，书籍 → `@book`，书章节 → `@incollection`，技术报告 → `@techreport`，HuggingFace/Zenodo → `@misc`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_bib_sync_20260520T215727"
}
```

</details>

---
