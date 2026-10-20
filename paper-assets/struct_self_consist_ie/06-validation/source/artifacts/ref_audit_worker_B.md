# 引用验证清单 (Worker B — Google Scholar / DBLP 优先)

**验证日期**: 2026-05-26
**验证方式**: WebSearch (Google Scholar, DBLP, ACL Anthology, arXiv, NeurIPS/ICML proceedings)

总 bib entries: **64**
总 cite keys in tex: **61**
未使用的 bib entries: `holm1979simple`, `li2024simple`, `xiao2022uncertainty`
tex 中引用但 bib 缺失: **无**

---

## 问题汇总

| 严重性 | 条目 | 问题 |
|--------|------|------|
| ⚠️ 需修正 | `kang2025selfcertainty` | NeurIPS volume 号错：写了 38，应为 39（NeurIPS 2025 = 第 39 届） |
| ⚠️ 需修正 | `yee2019noisy` | 缺少作者 Nathan Ng（应为 4 人，非 3 人） |
| ⚠️ 需修正 | `shinn2023reflexion` | 缺少作者 Edward Berman（应为 6 人，非 5 人） |
| ⚠️ 需修正 | `li2023stepaware` | 标题不一致：bib 写 "Making **Large** Language Models..."，ACL 2023 正式版为 "Making Language Models..."（无 "Large"） |
| ⚠️ 建议修正 | `dong2024xgrammar` | 已在 MLSys 2025 正式发表，bib 仅列 arXiv preprint，建议更新 venue |
| ⚠️ 建议修正 | `fleiss1971agreement` | 缺少 volume (76) 和 pages (378–382) |
| ⚠️ 建议修正 | `geifman2017selective` | "NeurIPS 30" 时间上不准确，2017 年会议名称仍为 NIPS（2018 年才改名 NeurIPS） |
| 🧹 清理 | `holm1979simple` | 未被引用，可移除 |
| 🧹 清理 | `li2024simple` | 未被引用，可移除 |
| 🧹 清理 | `xiao2022uncertainty` | 未被引用，可移除 |

---

## 逐条验证

### 1. [landesberg2026bon] Landesberg (2026). "When LLM Judge Scores Look Good but Best-of-N Decisions Fail". arXiv:2603.12520.
- 在线验证：arXiv ✓ 找到
- 作者：✓
- 年份：✓ 2026
- 标题：✓
- Venue：✓ arXiv preprint
- DOI/arXiv：✓ 2603.12520
- 论文存在：✓
- 引用上下文：✓ — "\citet{landesberg2026bon} independently document a correlation-selection gap in best-of-N reasoning: global judge r=0.47 masks within-prompt r=0.27" 准确描述了论文内容
- **结论：✅ OK**

### 2. [holm1979simple] Holm (1979). "A Simple Sequentially Rejective Multiple Test Procedure". Scandinavian J. Statistics 6(2), 65–70.
- 在线验证：Google Scholar ✓ 找到（经典论文，5万+引用）
- 作者：✓ Sture Holm
- 年份：✓ 1979
- 标题：✓
- Venue：✓ Scandinavian Journal of Statistics, Vol 6, No 2, pp 65–70
- DOI/arXiv：N/A（1979年无DOI）
- 论文存在：✓
- 引用上下文：N/A — **未在任何 tex 文件中被引用**
- **结论：⚠️ 未使用，建议移除或确认是否需要**

### 3. [brown2024monkeys] Brown et al. (2024). "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling". arXiv:2407.21787.
- 在线验证：arXiv ✓ | Google Scholar ✓
- 作者：✓ Brown, Juravsky, Ehrlich, Clark, Le, Ré, Mirhoseini
- 年份：✓ 2024
- 标题：✓
- Venue：✓ arXiv preprint（确认仍为 preprint，未正式发表于会议）
- DOI/arXiv：✓ 2407.21787
- 论文存在：✓
- 引用上下文：✓ — 用于引用推理任务中 inference compute scaling、oracle F1 scaling 对比
- **结论：✅ OK**

### 4. [chen2024usc] Chen et al. (2024). "Universal Self-Consistency for Large Language Model Generation". ICML 2024 Workshop on In-Context Learning. arXiv:2311.17311.
- 在线验证：arXiv ✓ | ICML 2024 workshop ✓
- 作者：✓ 全部 10 位作者正确
- 年份：✓ 2024
- 标题：✓
- Venue：✓ ICML 2024 Workshop on In-Context Learning
- DOI/arXiv：✓ 2311.17311
- 论文存在：✓
- 引用上下文：✓ — "free-form variants face limits where sub-output agreement does not yield selection gain"
- **结论：✅ OK**

### 5. [cobbe2021verifiers] Cobbe et al. (2021). "Training Verifiers to Solve Math Word Problems". arXiv:2110.14168.
- 在线验证：arXiv ✓ | Google Scholar ✓
- 作者：✓ 全部 12 位作者正确
- 年份：✓ 2021
- 标题：✓
- Venue：✓ arXiv preprint（确认仍为 preprint）
- DOI/arXiv：✓ 2110.14168
- 论文存在：✓
- 引用上下文：✓ — 作为 "trained verifiers" 引用，准确
- **结论：✅ OK**

### 6. [derczynski2017wnut] Derczynski et al. (2017). "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition". W-NUT 2017.
- 在线验证：ACL Anthology ✓ (W17-4418)
- 作者：✓ Derczynski, Nichols, van Erp, Limsopatham
- 年份：✓ 2017
- 标题：✓
- Venue：✓ W-NUT 2017
- DOI/arXiv：N/A
- 论文存在：✓
- 引用上下文：✓ — WNUT-17 数据集来源引用
- **结论：✅ OK**

### 7. [ding2021fewnerd] Ding et al. (2021). "Few-NERD: A Few-shot Named Entity Recognition Dataset". ACL 2021, pp 3198–3213.
- 在线验证：ACL Anthology ✓ (2021.acl-long.248)
- 作者：✓ 全部 8 位作者正确
- 年份：✓ 2021
- 标题：✓
- Venue：✓ ACL 2021 Long Papers
- 卷期页码：✓ pp 3198–3213
- DOI：✓ 10.18653/v1/2021.acl-long.248
- 论文存在：✓
- 引用上下文：✓ — Few-NERD 数据集来源引用
- **结论：✅ OK**

### 8. [eikema2022sampling] Eikema, Aziz (2022). "Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation". EMNLP 2022, pp 10978–10993.
- 在线验证：ACL Anthology ✓ (2022.emnlp-main.754)
- 作者：✓
- 年份：✓ 2022
- 标题：✓
- Venue：✓ EMNLP 2022
- 卷期页码：✓ pp 10978–10993
- DOI：✓ 10.18653/v1/2022.emnlp-main.754
- 论文存在：✓
- 引用上下文：✓ — MBR decoding 标准引用
- **结论：✅ OK**

### 9. [freitag2022high] Freitag et al. (2022). "High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics". TACL 10, pp 811–825.
- 在线验证：ACL Anthology ✓ (2022.tacl-1.47)
- 作者：✓ Freitag, Grangier, Tan, Liang
- 年份：✓ 2022
- 标题：✓
- Venue：✓ TACL, volume 10
- 卷期页码：✓ pp 811–825
- DOI：✓ 10.1162/tacl_a_00491
- 论文存在：✓
- 引用上下文：✓ — "MBR's success in machine translation"
- **结论：✅ OK**

### 10. [fleiss1971agreement] Fleiss (1971). "Measuring nominal scale agreement among many raters." Psychological Bulletin.
- 在线验证：Google Scholar ✓（经典论文）
- 作者：✓ Joseph L. Fleiss
- 年份：✓ 1971
- 标题：✓
- Venue：✓ Psychological Bulletin
- DOI：✓ 10.1037/h0031619
- 论文存在：✓
- 引用上下文：✓ — "inter-rater agreement adapted to entity sets"
- **结论：⚠️ 需修正** — 缺少 `volume = {76}` 和 `pages = {378--382}`

### 11. [geng2024confidence] Geng et al. (2024). "A Survey of Confidence Estimation and Calibration in Large Language Models". NAACL 2024.
- 在线验证：ACL Anthology ✓ (2024.naacl-long.366)
- 作者：✓ 全部 6 位作者正确
- 年份：✓ 2024
- 标题：✓
- Venue：✓ NAACL 2024 Long Papers
- DOI：✓ 10.18653/v1/2024.naacl-long.366
- 论文存在：✓
- 引用上下文：✓ — confidence estimation 引用
- **结论：✅ OK**

### 12. [kadavath2022language] Kadavath et al. (2022). "Language Models (Mostly) Know What They Know". arXiv:2207.05221.
- 在线验证：arXiv ✓ | Google Scholar ✓
- 作者：✓ 全部 34 位作者正确
- 年份：✓ 2022
- 标题：✓
- Venue：✓ arXiv preprint
- DOI/arXiv：✓ 2207.05221
- 论文存在：✓
- 引用上下文：✓ — "LP is well-calibrated at population level"
- **结论：✅ OK**

### 13. [kang2025selfcertainty] Kang, Zhao, Song (2025). "Scalable Best-of-N Selection for Large Language Models via Self-Certainty". NeurIPS 2025.
- 在线验证：arXiv ✓ (2502.18581) | NeurIPS 2025 poster ✓
- 作者：✓ Kang, Zhao, Song
- 年份：✓ 2025
- 标题：✓
- Venue：✗ — bib 写 "Advances in Neural Information Processing Systems **38**"，但 NeurIPS 2025 是第 **39** 届（NeurIPS 2024 = 38th）
- DOI/arXiv：✓ 2502.18581
- 论文存在：✓
- 引用上下文：✓ — "Reward-free selectors"
- **结论：⚠️ 需修正** — volume 号 38 → 39

### 14. [kuhn2023semantic] Kuhn, Gal, Farquhar (2023). "Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation". ICLR 2023.
- 在线验证：arXiv ✓ (2302.09664) | OpenReview ✓
- 作者：✓
- 年份：✓ 2023
- 标题：✓
- Venue：✓ ICLR 2023
- DOI/arXiv：✓ 2302.09664
- 论文存在：✓
- 引用上下文：✓ — "Semantic uncertainty" 和 "model-internal alternatives"
- **结论：✅ OK**

### 15. [lightman2024verify] Lightman et al. (2024). "Let's Verify Step by Step". ICLR 2024.
- 在线验证：arXiv ✓ (2305.20050) | OpenReview ✓
- 作者：✓ 全部 10 位作者正确（注：arXiv 用 "Yura Burda"/"Harri Edwards"，DBLP 用 "Yuri Burda"/"Harrison Edwards"，两种形式均可接受）
- 年份：✓ 2024
- 标题：✓
- Venue：✓ ICLR 2024
- DOI/arXiv：✓ 2305.20050
- 论文存在：✓
- 引用上下文：✓ — "trained verifiers"
- **结论：✅ OK**

### 16. [luan2018scierc] Luan et al. (2018). "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction". EMNLP 2018.
- 在线验证：ACL Anthology ✓ (D18-1360)
- 作者：✓ Luan, He, Ostendorf, Hajishirzi
- 年份：✓ 2018
- 标题：✓
- Venue：✓ EMNLP 2018
- DOI：✓ 10.18653/v1/D18-1360
- 论文存在：✓
- 引用上下文：✓ — SciERC 数据集来源引用
- **结论：✅ OK**

### 17. [yao2026consistency] Yao et al. (2026). "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction". Genomics & Informatics.
- 在线验证：Google Scholar ✓ | DOI ✓
- 作者：✓ Yao, Nédellec, Xia, Bossy
- 年份：✓ 2026
- 标题：✓
- Venue：✓ Genomics & Informatics
- DOI：✓ 10.1186/s44342-025-00063-2
- 论文存在：✓
- 引用上下文：✓ — "Prior work reports task-level correlations between consistency and accuracy"
- **结论：✅ OK**

### 18. [sainz2024gollie] Sainz et al. (2024). "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction". ICLR 2024.
- 在线验证：arXiv ✓ (2310.03668) | OpenReview ✓
- 作者：✓ Sainz, García-Ferrero, Agerri, Lopez de Lacalle, Rigau, Agirre
- 年份：✓ 2024
- 标题：✓
- Venue：✓ ICLR 2024
- DOI/arXiv：✓ 2310.03668
- 论文存在：✓
- 引用上下文：✓ — "generative IE"
- **结论：✅ OK**

### 19. [snell2025scaling] Snell et al. (2025). "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning". ICLR 2025.
- 在线验证：arXiv ✓ (2408.03314) | OpenReview ✓
- 作者：✓ Snell, Lee, Xu, Kumar
- 年份：✓ 2025
- 标题：✓（bib 标题与 ICLR proceedings 版一致；arXiv 版标题略有不同——"Scaling Model Parameters" vs "Scaling Parameters for Reasoning"）
- Venue：✓ ICLR 2025 (Oral)
- DOI/arXiv：✓ 2408.03314
- 论文存在：✓
- 引用上下文：✓ — "best-of-N with compute-optimal allocation"
- **结论：✅ OK**

### 20. [taubenfeld2025cisc] Taubenfeld et al. (2025). "Confidence Improves Self-Consistency in LLMs". Findings of ACL 2025.
- 在线验证：ACL Anthology ✓ | DOI ✓
- 作者：✓ Taubenfeld, Sheffer, Ofek, Feder, Goldstein, Gekhman, Yona
- 年份：✓ 2025
- 标题：✓
- Venue：✓ Findings of ACL 2025
- DOI：✓ 10.18653/v1/2025.findings-acl.1030
- 论文存在：✓
- 引用上下文：✓ — "Reward-free selectors"
- **结论：✅ OK**

### 21. [thirukovalluru2024atomic] Thirukovalluru, Huang, Dhingra (2024). "Atomic Self-Consistency for Better Long Form Generations". EMNLP 2024.
- 在线验证：ACL Anthology ✓ (2024.emnlp-main.706)
- 作者：✓
- 年份：✓ 2024
- 标题：✓
- Venue：✓ EMNLP 2024 main
- DOI：✓ 10.18653/v1/2024.emnlp-main.706
- 论文存在：✓
- 引用上下文：✓ — "atomic variants face limits where sub-output agreement does not yield selection gain"
- **结论：✅ OK**

### 22. [tjongkimsang2003conll] Tjong Kim Sang, De Meulder (2003). "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition". CoNLL 2003.
- 在线验证：ACL Anthology ✓ (W03-0419)
- 作者：✓
- 年份：✓ 2003
- 标题：✓
- Venue：✓ CoNLL 2003
- DOI/arXiv：N/A
- 论文存在：✓
- 引用上下文：✓ — CoNLL-2003 数据集来源引用
- **结论：✅ OK**

### 23. [wang2023selfconsistency] Wang et al. (2023). "Self-Consistency Improves Chain of Thought Reasoning in Language Models". ICLR 2023.
- 在线验证：arXiv ✓ (2203.11171) | OpenReview ✓
- 作者：✓ 全部 8 位作者正确
- 年份：✓ 2023
- 标题：✓
- Venue：✓ ICLR 2023
- DOI/arXiv：✓ 2203.11171
- 论文存在：✓
- 引用上下文：✓ — 核心 self-consistency 引用
- **结论：✅ OK**

### 24. [willard2023guided] Willard, Louf (2023). "Efficient Guided Generation for Large Language Models". arXiv:2307.09702.
- 在线验证：arXiv ✓ | DBLP ✓
- 作者：✓ Brandon T. Willard, Rémi Louf
- 年份：✓ 2023
- 标题：✓
- Venue：✓ arXiv preprint（确认仍为 preprint，无正式 venue）
- DOI/arXiv：✓ 2307.09702
- 论文存在：✓
- 引用上下文：✓ — "constrained decoding"
- **结论：✅ OK**

### 25. [xia2025survey] Xia et al. (2025). "A Survey of Uncertainty Estimation Methods on Large Language Models". Findings of ACL 2025.
- 在线验证：ACL Anthology ✓ (2025.findings-acl.1101)
- 作者：✓ Xia, Xu, Zhang, Liu
- 年份：✓ 2025
- 标题：✓
- Venue：✓ Findings of ACL 2025
- DOI/arXiv：N/A
- 论文存在：✓
- 引用上下文：✓ — confidence estimation 引用
- **结论：✅ OK**

### 26. [zheng2024llamafactory] Zheng et al. (2024). "LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models". ACL 2024 System Demos, pp 400–410.
- 在线验证：ACL Anthology ✓ (2024.acl-demos.38)
- 作者：✓ Zheng, Zhang, Zhang, Ye, Luo
- 年份：✓ 2024
- 标题：✓
- Venue：✓ ACL 2024 System Demonstrations
- 卷期页码：✓ pp 400–410
- DOI：✓ 10.18653/v1/2024.acl-demos.38
- 论文存在：✓
- 引用上下文：✓ — 训练框架引用
- **结论：✅ OK**

### 27. [zhou2024uniner] Zhou et al. (2024). "UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition". ICLR 2024.
- 在线验证：OpenReview ✓ | arXiv ✓ (2308.03279)
- 作者：✓ Zhou, Zhang, Gu, Chen, Poon
- 年份：✓ 2024
- 标题：✓
- Venue：✓ ICLR 2024
- DOI/arXiv：✓ 2308.03279
- 论文存在：✓
- 引用上下文：✓ — "generative IE"
- **结论：✅ OK**

### 28. [muller2021understanding] Müller, Sennrich (2021). "Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation". ACL 2021, pp 259–272.
- 在线验证：ACL Anthology ✓ (2021.acl-long.22)
- 作者：✓
- 年份：✓ 2021
- 标题：✓
- Venue：✓ ACL 2021 Long Papers
- 卷期页码：✓ pp 259–272
- DOI：✓ 10.18653/v1/2021.acl-long.22
- 论文存在：✓
- 引用上下文：✓ — MBR decoding
- **结论：✅ OK**

### 29. [eikema2025structured] Eikema, Rutkiewicz, Giulianelli (2025). "Structure-Conditional Minimum Bayes Risk Decoding". EMNLP 2025.
- 在线验证：ACL Anthology ✓ (2025.emnlp-main.1616) | arXiv ✓ (2510.20700)
- 作者：✓
- 年份：✓ 2025
- 标题：✓
- Venue：✓ EMNLP 2025
- DOI/arXiv：✓ 2510.20700
- 论文存在：✓
- 引用上下文：✓ — "MBR utilities degrade on structured outputs"
- **结论：✅ OK**

### 30. [jinnai2024mbr] Jinnai et al. (2024). "Model-Based Minimum Bayes Risk Decoding for Text Generation". ICML 2024.
- 在线验证：PMLR ✓ (v235, pp 22326–22347) | arXiv ✓ (2311.05263)
- 作者：✓ Jinnai, Morimura, Honda, Ariu, Abe
- 年份：✓ 2024
- 标题：✓
- Venue：✓ ICML 2024
- DOI/arXiv：✓ 2311.05263
- 论文存在：✓
- 引用上下文：✓ — "extension to summarization, code generation, and captioning"
- **结论：✅ OK**

### 31. [ratinov2009design] Ratinov, Roth (2009). "Design Challenges and Misconceptions in Named Entity Recognition". CoNLL 2009, pp 147–155.
- 在线验证：ACL Anthology ✓ (W09-1119)
- 作者：✓
- 年份：✓ 2009
- 标题：✓
- Venue：✓ CoNLL 2009
- 卷期页码：✓ pp 147–155
- 论文存在：✓
- 引用上下文：✓ — "threshold below which NER differences are considered negligible"
- **结论：✅ OK**

### 32. [bergkirkpatrick2012empirical] Berg-Kirkpatrick, Burkett, Klein (2012). "An Empirical Investigation of Statistical Significance in NLP". EMNLP-CoNLL 2012, pp 995–1005.
- 在线验证：ACL Anthology ✓ (D12-1091)
- 作者：✓
- 年份：✓ 2012
- 标题：✓
- Venue：✓ EMNLP-CoNLL 2012
- 卷期页码：✓ pp 995–1005
- 论文存在：✓
- 引用上下文：✓ — "significant-difference threshold established in NER evaluation methodology"（论文研究 NLP 整体的统计显著性，含 NER，引用可接受）
- **结论：✅ OK**

### 33. [tian2023calibration] Tian et al. (2023). "Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback". EMNLP 2023, pp 5433–5442.
- 在线验证：ACL Anthology ✓ (2023.emnlp-main.330)
- 作者：✓ 全部 8 位作者正确
- 年份：✓ 2023
- 标题：✓
- Venue：✓ EMNLP 2023
- 卷期页码：✓ pp 5433–5442
- 论文存在：✓
- 引用上下文：✓ — "LP is well-calibrated at population level" 和 verbalized confidence
- **结论：✅ OK**

### 34. [yun2025price] Yun et al. (2025). "The Price of Format: Diversity Collapse in LLMs". Findings of EMNLP 2025.
- 在线验证：ACL Anthology ✓ (2025.findings-emnlp.836)
- 作者：✓ Yun, An, Wang, Peng, Shang
- 年份：✓ 2025
- 标题：✓
- Venue：✓ Findings of EMNLP 2025
- 论文存在：✓
- 引用上下文：✓ — "diversity collapse under constrained decoding"
- **结论：✅ OK**

### 35. [gao2023scaling] Gao, Schulman, Hilton (2023). "Scaling Laws for Reward Model Overoptimization". ICML 2023.
- 在线验证：PMLR ✓ (v202, pp 10835–10866)
- 作者：✓
- 年份：✓ 2023
- 标题：✓
- Venue：✓ ICML 2023
- 论文存在：✓
- 引用上下文：✓ — "BoN scaling laws"
- **结论：✅ OK**

### 36. [platt1999probabilistic] Platt (1999). "Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods". Advances in Large Margin Classifiers, pp 61–74. MIT Press.
- 在线验证：Google Scholar ✓（经典论文）
- 作者：✓ John C. Platt
- 年份：✓ 1999
- 标题：✓
- Venue：✓ Advances in Large Margin Classifiers, MIT Press
- 卷期页码：✓ pp 61–74
- 论文存在：✓
- 引用上下文：✓ — "Platt scaling fits a logistic regression"
- **结论：✅ OK**

### 37. [guo2017calibration] Guo et al. (2017). "On Calibration of Modern Neural Networks". ICML 2017, pp 1321–1330.
- 在线验证：PMLR ✓ (v70)
- 作者：✓ Guo, Pleiss, Sun, Weinberger
- 年份：✓ 2017
- 标题：✓
- Venue：✓ ICML 2017
- 卷期页码：✓ pp 1321–1330
- 论文存在：✓
- 引用上下文：✓ — "temperature scaling divides logits by a scalar"
- **结论：✅ OK**

### 38. [geifman2017selective] Geifman, El-Yaniv (2017). "Selective Classification for Deep Neural Networks". NeurIPS 30.
- 在线验证：NeurIPS proceedings ✓ | arXiv ✓ (1705.08500)
- 作者：✓
- 年份：✓ 2017
- 标题：✓
- Venue：⚠️ — bib 写 "Advances in Neural Information Processing Systems" volume 30，但 2017 年会议名称仍为 **NIPS**（2018 年才改名 NeurIPS）。"NeurIPS 30" 不准确，应为 "NIPS 2017" 或 "Advances in Neural Information Processing Systems 30"
- DOI/arXiv：✓ 1705.08500
- 论文存在：✓
- 引用上下文：✓ — "selective prediction" 和 "support abstention"
- **结论：⚠️ 建议修正** — venue 名称时间错误（NIPS vs NeurIPS）。实际影响较小，因 booktitle 用的是通用的 "Advances in Neural Information Processing Systems"。

### 39. [dong2024xgrammar] Dong et al. (2024). "XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models". arXiv:2411.15100.
- 在线验证：arXiv ✓ | MLSys 2025 ✓
- 作者：✓ Dong, Ruan, Cai, Lai, Xu, Zhao, Chen
- 年份：✓/⚠️ — arXiv preprint 2024，但已在 **MLSys 2025** 正式发表
- 标题：✓
- Venue：⚠️ — bib 仅列 arXiv preprint，但论文已被 MLSys 2025 接收并发表
- DOI/arXiv：✓ 2411.15100
- 论文存在：✓
- 引用上下文：✓ — constrained decoding engine
- **结论：⚠️ 建议修正** — 应更新为 MLSys 2025 venue

### 40. [lin2022teaching] Lin, Hilton, Evans (2022). "Teaching Models to Express Their Uncertainty in Words". TMLR.
- 在线验证：arXiv ✓ (2205.14334) | TMLR ✓
- 作者：✓
- 年份：✓ 2022
- 标题：✓
- Venue：✓ Transactions on Machine Learning Research (TMLR)
- DOI/arXiv：✓ 2205.14334
- 论文存在：✓
- 引用上下文：✓ — verbalized confidence baseline
- **结论：✅ OK**

### 41. [farquhar2024detecting] Farquhar et al. (2024). "Detecting hallucinations in large language models using semantic entropy". Nature 630, pp 625–630.
- 在线验证：Nature ✓ | Google Scholar ✓
- 作者：✓ Farquhar, Kossen, Kuhn, Gal
- 年份：✓ 2024
- 标题：✓
- Venue：✓ Nature, volume 630
- 卷期页码：✓ pp 625–630
- DOI：✓ 10.1038/s41586-024-07421-0
- 论文存在：✓
- 引用上下文：✓ — novelty comparison table
- **结论：✅ OK**

### 42. [chen2023twofailures] Chen et al. (2024). "Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs". TMLR.
- 在线验证：arXiv ✓ (2305.14279) | TMLR ✓
- 作者：✓ Chen, Phang, Parrish, Padmakumar, Zhao, Bowman, Cho
- 年份：✓ year=2024 正确（TMLR 发表年）；cite key 用 2023 反映 preprint 年，可接受
- 标题：✓
- Venue：✓ TMLR
- DOI/arXiv：✓ 2305.14279
- 论文存在：✓
- 引用上下文：✓ — "SC can fail when consistent outputs are wrong"
- **结论：✅ OK**（key-year 轻微不一致但可接受）

### 43. [aggarwal2023adaptive] Aggarwal et al. (2023). "Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs". EMNLP 2023.
- 在线验证：arXiv ✓ (2305.11860) | EMNLP 2023 ✓
- 作者：✓ Aggarwal, Madaan, Yang, Mausam
- 年份：✓ 2023
- 标题：✓
- Venue：✓ EMNLP 2023
- DOI/arXiv：✓ 2305.11860
- 论文存在：✓
- 引用上下文：✓ — novelty comparison table
- **结论：✅ OK**

### 44. [xie2023zeroshot] Xie et al. (2023). "Empirical Study of Zero-Shot NER with ChatGPT". EMNLP 2023, pp 7935–7956.
- 在线验证：ACL Anthology ✓ (2023.emnlp-main.493)
- 作者：✓ Xie, Li, Zhang, Zhang, Liu, Wang
- 年份：✓ 2023
- 标题：✓
- Venue：✓ EMNLP 2023
- 卷期页码：✓ pp 7935–7956
- DOI：✓ 10.18653/v1/2023.emnlp-main.493
- 论文存在：✓
- 引用上下文：✓ — "propose entity voting for zero-shot NER"
- **结论：✅ OK**

### 45. [muennighoff2025s1] Muennighoff et al. (2025). "s1: Simple Test-Time Scaling". EMNLP 2025.
- 在线验证：arXiv ✓ (2501.19393) | ACL Anthology ✓ (2025.emnlp-main.1025)
- 作者：✓ 全部 10 位作者正确
- 年份：✓ 2025
- 标题：✓（注：原作者用全小写 "s1: Simple test-time scaling"，bib 用 title case，BibTeX style 会自动处理）
- Venue：✓ EMNLP 2025
- DOI/arXiv：✓ 2501.19393
- 论文存在：✓
- 引用上下文：✓ — "extended reasoning"
- **结论：✅ OK**

### 46. [eikema2020map] Eikema, Aziz (2020). "Is MAP Decoding All You Need? The Inadequacy of the Mode in Neural Machine Translation". COLING 2020, pp 4506–4520.
- 在线验证：ACL Anthology ✓ (2020.coling-main.398)
- 作者：✓
- 年份：✓ 2020
- 标题：✓
- Venue：✓ COLING 2020
- 卷期页码：✓ pp 4506–4520
- 论文存在：✓
- 引用上下文：✓ — MBR decoding foundational reference
- **结论：✅ OK**

### 47. [kumar2004minimum] Kumar, Byrne (2004). "Minimum Bayes-Risk Decoding for Statistical Machine Translation". HLT-NAACL 2004, pp 169–176.
- 在线验证：ACL Anthology ✓ (N04-1022)
- 作者：✓
- 年份：✓ 2004
- 标题：✓
- Venue：✓ HLT-NAACL 2004
- 卷期页码：✓ pp 169–176
- 论文存在：✓
- 引用上下文：✓ — MBR decoding foundational reference
- **结论：✅ OK**

### 48. [dembczynski2011exact] Dembczyński et al. (2011). "An Exact Algorithm for F-Measure Maximization". NeurIPS 24, pp 1404–1412.
- 在线验证：NeurIPS proceedings ✓
- 作者：✓ Dembczyński, Waegeman, Cheng, Hüllermeier
- 年份：✓ 2011
- 标题：✓
- Venue：✓ NeurIPS (NIPS) 2011, vol 24
- 卷期页码：✓ pp 1404–1412
- 论文存在：✓
- 引用上下文：✓ — "Set-level F1 admits no closed-form threshold"
- **结论：✅ OK**

### 49. [desai2020calibration] Desai, Durrett (2020). "Calibration of Pre-trained Transformers". EMNLP 2020, pp 295–302.
- 在线验证：ACL Anthology ✓ (2020.emnlp-main.21)
- 作者：✓
- 年份：✓ 2020
- 标题：✓
- Venue：✓ EMNLP 2020
- 卷期页码：✓ pp 295–302
- 论文存在：✓
- 引用上下文：✓ — "calibrated LMs"
- **结论：✅ OK**

### 50. [huang2024large] Huang et al. (2024). "Large Language Models Cannot Self-Correct Reasoning Yet". ICLR 2024.
- 在线验证：OpenReview ✓ (IkmD3fKBPQ)
- 作者：✓ Huang, Chen, Mishra, Zheng, Yu, Song, Zhou
- 年份：✓ 2024
- 标题：✓
- Venue：✓ ICLR 2024
- 论文存在：✓
- 引用上下文：✓ — "introspection boundary"（论文论证 LLM 无法 self-correct reasoning，用于支持 models encode quality internally but can't self-judge 的论点）
- **结论：✅ OK**

### 51. [li2024simple] Li, Ramprasad, Zhang (2024). "A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction". Findings of EMNLP 2024.
- 在线验证：ACL Anthology ✓ | arXiv ✓ (2402.13364)
- 作者：✓
- 年份：✓ 2024
- 标题：✓
- Venue：✓ Findings of EMNLP 2024
- DOI/arXiv：✓ 2402.13364
- 论文存在：✓
- 引用上下文：N/A — **未在任何 tex 文件中被引用**
- **结论：⚠️ 未使用，建议移除或确认是否需要**

### 52. [xie2024selfimproving] Xie et al. (2024). "Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models". NAACL 2024.
- 在线验证：ACL Anthology ✓ (2024.naacl-short.49)
- 作者：✓ Xie, Li, Zhang, Liu, Wang
- 年份：✓ 2024
- 标题：✓
- Venue：✓ NAACL 2024 (Short Papers, pp 583–593)
- 论文存在：✓
- 引用上下文：✓ — "extend this with SC-based self-annotation"
- **结论：✅ OK**

### 53. [madaan2023selfrefine] Madaan et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback". NeurIPS 36.
- 在线验证：NeurIPS proceedings ✓
- 作者：✓ 全部 16 位作者正确
- 年份：✓ 2023
- 标题：✓
- Venue：✓ NeurIPS 2023 (volume 36)
- 论文存在：✓
- 引用上下文：✓ — "iterative self-refinement"
- **结论：✅ OK**

### 54. [angelopoulos2023conformal] Angelopoulos, Bates (2023). "Conformal Prediction: A Gentle Introduction". Foundations and Trends in ML, 16(4), pp 494–591.
- 在线验证：ACM DL ✓ | Google Scholar ✓
- 作者：✓
- 年份：✓ 2023
- 标题：✓
- Venue：✓ Foundations and Trends in Machine Learning
- 卷期页码：✓ Vol 16, No 4, pp 494–591
- 论文存在：✓
- 引用上下文：✓ — "conformal prediction"
- **结论：✅ OK**

### 55. [malinin2021uncertainty] Malinin, Gales (2021). "Uncertainty Estimation in Autoregressive Structured Prediction". ICLR 2021.
- 在线验证：OpenReview ✓
- 作者：✓ Andrey Malinin, Mark Gales
- 年份：✓ 2021
- 标题：✓
- Venue：✓ ICLR 2021
- 论文存在：✓
- 引用上下文：✓ — "uncertainty for structured prediction"
- **结论：✅ OK**

### 56. [yee2019noisy] Yee, Dauphin, Auli (2019). "Simple and Effective Noisy Channel Modeling for Neural Machine Translation". EMNLP-IJCNLP 2019.
- 在线验证：ACL Anthology ✓ (D19-1571) | arXiv ✓ (1908.05731)
- 作者：✗ — bib 列 3 位作者（Yee, Dauphin, Auli），但 ACL Anthology 和 arXiv 均列 **4 位作者**：Kyra Yee, **Nathan Ng**, Yann N. Dauphin, Michael Auli。**缺少 Nathan Ng**。
- 年份：✓ 2019
- 标题：✓
- Venue：✓ EMNLP-IJCNLP 2019
- DOI/arXiv：✓ 1908.05731
- 论文存在：✓
- 引用上下文：✓ — "noisy channel models"
- **结论：⚠️ 需修正** — 缺少作者 Nathan Ng

### 57. [li2023stepaware] Li et al. (2023). "Making Large Language Models Better Reasoners with Step-Aware Verifier". ACL 2023.
- 在线验证：ACL Anthology ✓ (2023.acl-long.291) | arXiv ✓ (2206.02336)
- 作者：✓ Li, Lin, Zhang, Fu, Chen, Lou, Chen
- 年份：✓ 2023
- 标题：✗ — bib 写 "Making **Large** Language Models Better Reasoners with Step-Aware Verifier"，但 ACL 2023 正式发表标题为 "Making Language Models Better Reasoners with Step-Aware Verifier"（**无 "Large"**）。arXiv 版本标题含 "Large"，但应以正式发表版为准。
- Venue：✓ ACL 2023
- DOI/arXiv：✓ 2206.02336
- 论文存在：✓
- 引用上下文：✓ — "trained verifiers"
- **结论：⚠️ 需修正** — 标题应删除 "Large"，与 ACL 2023 正式发表版一致

### 58. [xiao2022uncertainty] Xiao et al. (2022). "Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis". Findings of EMNLP 2022.
- 在线验证：ACL Anthology ✓ (2022.findings-emnlp.538)
- 作者：✓ Xiao, Liang, Bhatt, Neiswanger, Salakhutdinov, Morency
- 年份：✓ 2022
- 标题：✓
- Venue：✓ Findings of EMNLP 2022
- 论文存在：✓
- 引用上下文：N/A — **未在任何 tex 文件中被引用**
- **结论：⚠️ 未使用，建议移除或确认是否需要**

### 59. [li2026rewardtail] Li, Qian, Mou (2026). "Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search". arXiv:2602.01485.
- 在线验证：arXiv ✓
- 作者：✓
- 年份：✓ 2026
- 标题：✓
- Venue：✓ arXiv preprint
- DOI/arXiv：✓ 2602.01485
- 论文存在：✓
- 引用上下文：✓ — "reward-tail-guided search"
- **结论：✅ OK**

### 60. [shinn2023reflexion] Shinn et al. (2023). "Reflexion: Language Agents with Verbal Reinforcement Learning". NeurIPS 36.
- 在线验证：NeurIPS proceedings ✓ | arXiv ✓ (2303.11366)
- 作者：✗ — bib 列 5 位作者（Shinn, Cassano, Gopinath, Narasimhan, Yao），但 NeurIPS 2023 正式 proceedings 列 **6 位作者**：Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao。**缺少 Edward Berman**。
- 年份：✓ 2023
- 标题：✓
- Venue：✓ NeurIPS 2023 (volume 36)
- 论文存在：✓
- 引用上下文：✓ — "Iterative self-verification"
- **结论：⚠️ 需修正** — 缺少作者 Edward Berman

### 61. [xu2024llmie] Xu et al. (2024). "Large Language Models for Generative Information Extraction: A Survey". Frontiers of Computer Science, 18(6):186357.
- 在线验证：Springer ✓ | Google Scholar ✓
- 作者：✓ 全部 10 位作者正确
- 年份：✓ 2024
- 标题：✓
- Venue：✓ Frontiers of Computer Science
- 卷期页码：✓ Vol 18, No 6, 186357
- DOI：✓ 10.1007/s11704-024-40555-y
- 论文存在：✓
- 引用上下文：✓ — "LLM-based IE has expanded rapidly"
- **结论：✅ OK**

### 62. [wang2025gptner] Wang et al. (2025). "GPT-NER: Named Entity Recognition via Large Language Models". Findings of NAACL 2025.
- 在线验证：ACL Anthology ✓ (2025.findings-naacl.239)
- 作者：✓ Wang, Sun, Li, Ouyang, Wu, Zhang, Li, Wang（8 位，与 ACL Anthology 一致）
- 年份：✓ 2025
- 标题：✓
- Venue：✓ Findings of NAACL 2025
- 论文存在：✓
- 引用上下文：✓ — "Self-verification approaches that prompt LLMs to validate their own extractions improve NER"
- **结论：✅ OK**

### 63. [gero2023selfverification] Gero et al. (2023). "Self-Verification Improves Few-Shot Clinical Information Extraction". arXiv:2306.00024.
- 在线验证：arXiv ✓
- 作者：✓ Gero, Singh, Cheng, Naumann, Galley, Gao, Poon
- 年份：✓ 2023
- 标题：✓
- Venue：✓ arXiv preprint（确认仍为 preprint，无正式 venue）
- DOI/arXiv：✓ 2306.00024
- 论文存在：✓
- 引用上下文：✓ — "clinical IE"
- **结论：✅ OK**

### 64. [wadhwa2023revisiting] Wadhwa, Amir, Wallace (2023). "Revisiting Relation Extraction in the era of Large Language Models". ACL 2023, pp 15566–15589.
- 在线验证：ACL Anthology ✓ (2023.acl-long.868)
- 作者：✓
- 年份：✓ 2023
- 标题：✓
- Venue：✓ ACL 2023 Long Papers
- 卷期页码：✓ pp 15566–15589
- 论文存在：✓
- 引用上下文：✓ — "benchmark LLM-based RE, confirming that structured outputs pose challenges distinct from free-form generation"
- **结论：✅ OK**

---

## 统计

| 类别 | 数量 |
|------|------|
| ✅ OK | 54 |
| ⚠️ 需修正 | 4 (kang2025selfcertainty, yee2019noisy, shinn2023reflexion, li2023stepaware) |
| ⚠️ 建议修正 | 3 (dong2024xgrammar, fleiss1971agreement, geifman2017selective) |
| 🧹 未使用 | 3 (holm1979simple, li2024simple, xiao2022uncertainty) |
| ❌ 论文不存在 / hallucinated | **0** |

**所有 64 篇论文均为真实存在的论文，无 hallucinated citations。**

---

## 建议修复清单（按优先级排序）

### 必须修复
1. **`kang2025selfcertainty`**: booktitle 中 "38" → "39"
2. **`yee2019noisy`**: 添加缺失作者 `Nathan Ng`（第二作者位置）
3. **`shinn2023reflexion`**: 添加缺失作者 `Edward Berman`（Cassano 和 Gopinath 之间）
4. **`li2023stepaware`**: title 中删除 "Large"（"Making Language Models Better Reasoners..."）

### 建议修复
5. **`dong2024xgrammar`**: 更新为 MLSys 2025 正式 venue
6. **`fleiss1971agreement`**: 添加 `volume = {76}`, `pages = {378--382}`
7. **`geifman2017selective`**: venue 无需改动（booktitle 已使用通用 "Advances in Neural Information Processing Systems"）

### 清理
8. 移除 3 个未引用 entry：`holm1979simple`, `li2024simple`, `xiao2022uncertainty`
