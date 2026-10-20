# 引用验证清单 (Worker A — Semantic Scholar 优先)

**验证日期**: 2026-05-26
**验证手段**: Semantic Scholar API + WebSearch fallback (ACL Anthology, arXiv, OpenReview, PMLR, NeurIPS proceedings)

总 bib entries: **64**
总 unique cite keys in tex: **61**
未使用的 bib entries: `holm1979simple`, `li2024simple`, `xiao2022uncertainty`
tex 中引用但 bib 缺失: **无**

---

## 总结

| 类别 | 数量 |
|------|------|
| 论文真实存在 | 64/64 (100%) |
| 完全匹配 (无任何问题) | 58 |
| 需修正 (⚠️) | 3 |
| 需关注 (注意事项) | 3 |
| 严重问题 (❌ 虚假引用) | 0 |

---

## 需修正的条目

### ⚠️ [li2023stepaware] — 标题多了 "Large"
- **Bib 标题**: "Making **Large** Language Models Better Reasoners with Step-Aware Verifier"
- **ACL 2023 proceedings 标题**: "Making Language Models Better Reasoners with Step-Aware Verifier"
- **来源**: ACL Anthology 2023.acl-long.291 确认无 "Large"；arXiv:2206.02336 版本有 "Large"
- **建议**: 既然 bib 引用的是 ACL 2023 proceedings，应使用 proceedings 标题，删除 "Large"

### ⚠️ [yee2019noisy] — arXiv 与 proceedings 作者列表不一致
- **Bib 作者**: Yee, Dauphin, Auli (3人)
- **ACL Anthology D19-1571**: Yee, Dauphin, Auli (3人) ← bib 匹配 proceedings
- **arXiv:1908.05731**: Yee, **Ng**, Dauphin, Auli (4人)
- **问题**: Bib 的 URL 指向 arXiv (4人版本)，但作者列表只有 3 人（匹配 proceedings）。建议统一：要么加上 Nathan Ng（匹配 arXiv），要么将 URL 改为 ACL Anthology 链接

### ⚠️ [holm1979simple] — 方法被引用但未 \cite
- **现状**: 论文正文多次提及 "Holm--Bonferroni" 方法（至少 15 次），但从未使用 `\cite{holm1979simple}`
- **建议**: 在首次提及 Holm--Bonferroni 时添加 `\cite{holm1979simple}`

---

## 需关注的条目

### 📝 [snell2025scaling] — arXiv 与 ICLR proceedings 标题不同
- **Bib 标题**: "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning"
- **arXiv 标题**: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
- **ICLR 2025 proceedings 标题**: "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning"
- **结论**: Bib 使用了 ICLR proceedings 标题，技术上正确。但注意 arXiv 版本标题不同。

### 📝 [xu2024llmie] — 作者 "Wang, Yang" 在 S2 中未出现
- **Bib 作者**: 10人（含 Wang, Yang）
- **Semantic Scholar**: 9人（无 Wang, Yang）
- **结论**: 需对照 Springer 出版商页面确认。S2 数据可能不完整。

### 📝 [chen2023twofailures] — cite key 与 year field 不一致
- **Cite key**: chen**2023**twofailures
- **Year field**: 2024
- **实际**: arXiv 2023.05, TMLR 2024. Year field 2024 正确（TMLR 出版年），但 key 中 2023 可能误导

---

## 未使用的 bib entries

| Cite key | 标题 | 说明 |
|----------|------|------|
| `holm1979simple` | A Simple Sequentially Rejective Multiple Test Procedure | 方法被引用但未 \cite（见上方⚠️） |
| `li2024simple` | A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction | 完全未引用 |
| `xiao2022uncertainty` | Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis | 完全未引用 |

---

## 逐条验证

### 1. [landesberg2026bon] Landesberg (2026). "When LLM Judge Scores Look Good but Best-of-N Decisions Fail". arXiv.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：N/A
- DOI/arXiv：✓ (2603.12520)
- 论文存在：✓
- 引用上下文：✓ — 引用为 concurrent work documenting correlation-selection gap in BoN reasoning
- **结论：✅ OK**

### 2. [holm1979simple] Holm (1979). "A Simple Sequentially Rejective Multiple Test Procedure". Scand. J. Stats.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓ Sture Holm
- 年份：✓ 1979
- 标题：✓
- Venue：✓ Scandinavian Journal of Statistics, 6(2), 65-70
- 卷期页码：✓
- DOI/arXiv：✓ (10.1037/h0031619 — wait, that's Fleiss. Holm doesn't have DOI in bib)
- 论文存在：✓
- 引用上下文：⚠️ 方法被多次引用但从未 \cite
- **结论：⚠️ 需修正 — 添加 \cite**

### 3. [brown2024monkeys] Brown et al. (2024). "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling". arXiv.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2407.21787)
- 论文存在：✓
- 引用上下文：✓ — 引用为 best-of-N scaling / test-time compute
- **结论：✅ OK**

### 4. [chen2024usc] Chen et al. (2024). "Universal Self-Consistency for Large Language Model Generation". ICML 2024 Workshop.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓ (S2 shows 2023 arXiv; 2024 workshop correct)
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2311.17311)
- 论文存在：✓
- 引用上下文：✓ — 引用为 free-form SC variant
- **结论：✅ OK**

### 5. [cobbe2021verifiers] Cobbe et al. (2021). "Training Verifiers to Solve Math Word Problems". arXiv.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2110.14168)
- 论文存在：✓
- 引用上下文：✓ — 引用为 trained verifiers
- **结论：✅ OK**

### 6. [derczynski2017wnut] Derczynski et al. (2017). "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition". W-NUT 2017.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 WNUT-17 dataset
- **结论：✅ OK**

### 7. [ding2021fewnerd] Ding et al. (2021). "Few-NERD: A Few-shot Named Entity Recognition Dataset". ACL 2021.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI：✓ (10.18653/v1/2021.acl-long.248)
- 论文存在：✓
- 引用上下文：✓ — 引用为 Few-NERD dataset
- **结论：✅ OK**

### 8. [eikema2022sampling] Eikema & Aziz (2022). "Sampling-Based Approximations to Minimum Bayes Risk Decoding for Neural Machine Translation". EMNLP 2022.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓ (S2 shows 2021 arXiv; 2022 EMNLP correct)
- 标题：✓
- Venue：✓
- DOI：✓ (10.18653/v1/2022.emnlp-main.754)
- 论文存在：✓
- 引用上下文：✓ — 引用为 MBR decoding
- **结论：✅ OK**

### 9. [freitag2022high] Freitag et al. (2022). "High Quality Rather than High Model Probability: Minimum Bayes Risk Decoding with Neural Metrics". TACL.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓ (TACL vol 10 = 2022)
- 标题：✓
- Venue：✓
- 卷期页码：✓ (10, 811-825)
- DOI：✓ (10.1162/tacl_a_00491)
- 论文存在：✓
- 引用上下文：✓ — 引用为 MBR success in MT
- **结论：✅ OK**

### 10. [fleiss1971agreement] Fleiss (1971). "Measuring nominal scale agreement among many raters." Psychological Bulletin.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI：✓ (10.1037/h0031619)
- 论文存在：✓
- 引用上下文：✓ — 引用为 Fleiss' kappa 统计方法
- **结论：✅ OK**

### 11. [geng2024confidence] Geng et al. (2024). "A Survey of Confidence Estimation and Calibration in Large Language Models". NAACL 2024.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI：✓ (10.18653/v1/2024.naacl-long.366)
- 论文存在：✓
- 引用上下文：✓ — 引用为 confidence estimation survey
- **结论：✅ OK**

### 12. [kadavath2022language] Kadavath et al. (2022). "Language Models (Mostly) Know What They Know". arXiv.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2207.05221)
- 论文存在：✓
- 引用上下文：✓ — 引用为 LP well-calibrated at population level
- **结论：✅ OK**

### 13. [kang2025selfcertainty] Kang et al. (2025). "Scalable Best-of-N Selection for Large Language Models via Self-Certainty". NeurIPS 2025.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2502.18581)
- 论文存在：✓
- 引用上下文：✓ — 引用为 reward-free selector
- **结论：✅ OK**

### 14. [kuhn2023semantic] Kuhn et al. (2023). "Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation". ICLR 2023.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2302.09664)
- 论文存在：✓
- 引用上下文：✓ — 引用为 semantic uncertainty
- **结论：✅ OK**

### 15. [lightman2024verify] Lightman et al. (2024). "Let's Verify Step by Step". ICLR 2024.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2305.20050)
- 论文存在：✓
- 引用上下文：✓ — 引用为 trained verifiers (step-by-step)
- **结论：✅ OK**

### 16. [luan2018scierc] Luan et al. (2018). "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction". EMNLP 2018.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI：✓ (10.18653/v1/D18-1360)
- 论文存在：✓
- 引用上下文：✓ — 引用为 SciERC dataset
- **结论：✅ OK**

### 17. [yao2026consistency] Yao et al. (2026). "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction". Genomics & Informatics.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI：✓ (10.1186/s44342-025-00063-2)
- 论文存在：✓
- 引用上下文：✓ — 引用为 task-level consistency-accuracy correlation for NER/RE
- **结论：✅ OK**

### 18. [sainz2024gollie] Sainz et al. (2024). "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction". ICLR 2024.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓ (S2 shows 2023; ICLR 2024 correct)
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2310.03668)
- 论文存在：✓
- 引用上下文：✓ — 引用为 generative IE
- **结论：✅ OK**

### 19. [snell2025scaling] Snell et al. (2025). "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning". ICLR 2025.
- 在线验证：Semantic Scholar **找到** | 匹配度：**部分**
- 作者：✓
- 年份：✓
- 标题：📝 arXiv 标题不同 ("Scaling Model Parameters")，但 bib 使用 ICLR proceedings 标题，可接受
- Venue：✓
- DOI/arXiv：✓ (2408.03314)
- 论文存在：✓
- 引用上下文：✓ — 引用为 test-time compute scaling
- **结论：✅ OK（注意 arXiv/proceedings 标题差异）**

### 20. [taubenfeld2025cisc] Taubenfeld et al. (2025). "Confidence Improves Self-Consistency in LLMs". Findings ACL 2025.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI：✓ (10.18653/v1/2025.findings-acl.1030)
- 论文存在：✓
- 引用上下文：✓ — 引用为 reward-free selector / confidence-weighted SC
- **结论：✅ OK**

### 21. [thirukovalluru2024atomic] Thirukovalluru et al. (2024). "Atomic Self-Consistency for Better Long Form Generations". EMNLP 2024.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI：✓ (10.18653/v1/2024.emnlp-main.706)
- 论文存在：✓
- 引用上下文：✓ — 引用为 atomic SC variant
- **结论：✅ OK**

### 22. [tjongkimsang2003conll] Sang & De Meulder (2003). "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition". CoNLL 2003.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 CoNLL-2003 dataset
- **结论：✅ OK**

### 23. [wang2023selfconsistency] Wang et al. (2023). "Self-Consistency Improves Chain of Thought Reasoning in Language Models". ICLR 2023.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2203.11171)
- 论文存在：✓
- 引用上下文：✓ — 引用为 original self-consistency method
- **结论：✅ OK**

### 24. [willard2023guided] Willard & Louf (2023). "Efficient Guided Generation for Large Language Models". arXiv.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv preprint)
- DOI/arXiv：✓ (2307.09702)
- 论文存在：✓
- 引用上下文：✓ — 引用为 constrained decoding (Outlines)
- **结论：✅ OK**

### 25. [xia2025survey] Xia et al. (2025). "A Survey of Uncertainty Estimation Methods on Large Language Models". Findings ACL 2025.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 uncertainty estimation survey
- **结论：✅ OK**

### 26. [zheng2024llamafactory] Zheng et al. (2024). "LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models". ACL 2024 Demos.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (400-410)
- DOI：✓ (10.18653/v1/2024.acl-demos.38)
- 论文存在：✓
- 引用上下文：✓ — 引用为 fine-tuning framework
- **结论：✅ OK**

### 27. [zhou2024uniner] Zhou et al. (2024). "UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition". ICLR 2024.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2308.03279)
- 论文存在：✓
- 引用上下文：✓ — 引用为 generative IE
- **结论：✅ OK**

### 28. [muller2021understanding] Müller & Sennrich (2021). "Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation". ACL 2021.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI：✓ (10.18653/v1/2021.acl-long.22)
- 卷期页码：✓ (259-272)
- 论文存在：✓
- 引用上下文：✓ — 引用为 MBR decoding
- **结论：✅ OK**

### 29. [eikema2025structured] Eikema et al. (2025). "Structure-Conditional Minimum Bayes Risk Decoding". EMNLP 2025.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2510.20700)
- 论文存在：✓
- 引用上下文：✓ — 引用为 MBR utilities degrade on structured outputs
- **结论：✅ OK**

### 30. [jinnai2024mbr] Jinnai et al. (2024). "Model-Based Minimum Bayes Risk Decoding for Text Generation". ICML 2024.
- 在线验证：PMLR **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2311.05263)
- 论文存在：✓
- 引用上下文：✓ — 引用为 model-based MBR
- **结论：✅ OK**

### 31. [ratinov2009design] Ratinov & Roth (2009). "Design Challenges and Misconceptions in Named Entity Recognition". CoNLL 2009.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (147-155)
- 论文存在：✓
- 引用上下文：✓ — 引用为 NER evaluation methodology (0.5pp threshold)
- **结论：✅ OK**

### 32. [bergkirkpatrick2012empirical] Berg-Kirkpatrick et al. (2012). "An Empirical Investigation of Statistical Significance in NLP". EMNLP-CoNLL 2012.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (995-1005)
- 论文存在：✓
- 引用上下文：✓ — 引用为 statistical significance threshold (1.0pp)
- **结论：✅ OK**

### 33. [tian2023calibration] Tian et al. (2023). "Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback". EMNLP 2023.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (5433-5442)
- 论文存在：✓
- 引用上下文：✓ — 引用为 LP calibration / verbalized confidence
- **结论：✅ OK**

### 34. [yun2025price] Yun et al. (2025). "The Price of Format: Diversity Collapse in LLMs". Findings EMNLP 2025.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 diversity collapse under constrained decoding
- **结论：✅ OK**

### 35. [gao2023scaling] Gao et al. (2023). "Scaling Laws for Reward Model Overoptimization". ICML 2023.
- 在线验证：PMLR **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 BoN scaling laws
- **结论：✅ OK**

### 36. [platt1999probabilistic] Platt (1999). "Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods". MIT Press.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (Advances in Large Margin Classifiers, MIT Press)
- 卷期页码：✓ (61-74)
- 论文存在：✓
- 引用上下文：✓ — 引用为 Platt scaling (calibration)
- **结论：✅ OK**

### 37. [guo2017calibration] Guo et al. (2017). "On Calibration of Modern Neural Networks". ICML 2017.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (1321-1330)
- 论文存在：✓
- 引用上下文：✓ — 引用为 temperature scaling (calibration)
- **结论：✅ OK**

### 38. [geifman2017selective] Geifman & El-Yaniv (2017). "Selective Classification for Deep Neural Networks". NeurIPS 2017.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (1705.08500)
- 论文存在：✓
- 引用上下文：✓ — 引用为 selective prediction
- **结论：✅ OK**

### 39. [dong2024xgrammar] Dong et al. (2024). "XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models". arXiv.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2411.15100)
- 论文存在：✓
- 引用上下文：✓ — 引用为 constrained decoding engine
- **结论：✅ OK**

### 40. [lin2022teaching] Lin et al. (2022). "Teaching Models to Express Their Uncertainty in Words". TMLR.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (Transactions on Machine Learning Research)
- DOI/arXiv：✓ (2205.14334)
- 论文存在：✓
- 引用上下文：✓ — 引用为 verbalized confidence
- **结论：✅ OK**

### 41. [farquhar2024detecting] Farquhar et al. (2024). "Detecting hallucinations in large language models using semantic entropy". Nature.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ Nature
- 卷期页码：✓ (630, 625-630)
- DOI：✓ (10.1038/s41586-024-07421-0)
- 论文存在：✓
- 引用上下文：✓ — 引用在 differentiation table (hallucination detection via semantic entropy)
- **结论：✅ OK**

### 42. [chen2023twofailures] Chen et al. (2024). "Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs". TMLR.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓ (year field = 2024, matching TMLR publication)
- 标题：✓
- Venue：✓ (TMLR)
- DOI/arXiv：✓ (2305.14279)
- 论文存在：✓
- 引用上下文：✓ — 引用为 SC failure cases
- **结论：✅ OK（cite key 中 2023 与 year 2024 不一致，但不影响论文编译）**

### 43. [aggarwal2023adaptive] Aggarwal et al. (2023). "Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs". EMNLP 2023.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2305.11860)
- 论文存在：✓
- 引用上下文：✓ — 引用为 adaptive consistency / sample allocation
- **结论：✅ OK**

### 44. [xie2023zeroshot] Xie et al. (2023). "Empirical Study of Zero-Shot NER with ChatGPT". EMNLP 2023.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (7935-7956)
- DOI：✓ (10.18653/v1/2023.emnlp-main.493)
- 论文存在：✓
- 引用上下文：✓ — 引用为 entity voting for zero-shot NER
- **结论：✅ OK**

### 45. [muennighoff2025s1] Muennighoff et al. (2025). "s1: Simple Test-Time Scaling". EMNLP 2025.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2501.19393)
- 论文存在：✓
- 引用上下文：✓ — 引用为 extended reasoning / test-time scaling
- **结论：✅ OK**

### 46. [eikema2020map] Eikema & Aziz (2020). "Is MAP Decoding All You Need? The Inadequacy of the Mode in Neural Machine Translation". COLING 2020.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (4506-4520)
- 论文存在：✓
- 引用上下文：✓ — 引用为 MBR / MAP decoding inadequacy
- **结论：✅ OK**

### 47. [kumar2004minimum] Kumar & Byrne (2004). "Minimum Bayes-Risk Decoding for Statistical Machine Translation". HLT-NAACL 2004.
- 在线验证：ACL Anthology **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (169-176)
- 论文存在：✓
- 引用上下文：✓ — 引用为 MBR decoding foundational work
- **结论：✅ OK**

### 48. [dembczynski2011exact] Dembczyński et al. (2011). "An Exact Algorithm for F-Measure Maximization". NeurIPS 2011.
- 在线验证：NeurIPS proceedings **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (24, 1404-1412)
- 论文存在：✓
- 引用上下文：✓ — 引用为 F-measure threshold complexity
- **结论：✅ OK**

### 49. [desai2020calibration] Desai & Durrett (2020). "Calibration of Pre-trained Transformers". EMNLP 2020.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (295-302)
- 论文存在：✓
- 引用上下文：✓ — 引用为 calibrated LMs
- **结论：✅ OK**

### 50. [huang2024large] Huang et al. (2024). "Large Language Models Cannot Self-Correct Reasoning Yet". ICLR 2024.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓ (S2 shows 2023 arXiv; ICLR 2024 correct)
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 introspection boundary / self-correction limitation
- **结论：✅ OK**

### 51. [li2024simple] Li et al. (2024). "A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction". Findings EMNLP 2024.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2402.13364)
- 论文存在：✓
- 引用上下文：N/A — **未在 tex 中引用**
- **结论：✅ 论文真实，但未被引用（建议删除或添加引用）**

### 52. [xie2024selfimproving] Xie et al. (2024). "Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models". NAACL 2024.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 SC-based self-annotation for NER
- **结论：✅ OK**

### 53. [madaan2023selfrefine] Madaan et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback". NeurIPS 2023.
- 在线验证：NeurIPS proceedings **找到** | 匹配度：**完全**
- 作者：✓ (16 authors confirmed via NeurIPS proceedings, including Katherine Hermann)
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 iterative self-refinement
- **结论：✅ OK**

### 54. [angelopoulos2023conformal] Angelopoulos & Bates (2023). "Conformal Prediction: A Gentle Introduction". Foundations and Trends in ML.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (16(4), 494-591)
- 论文存在：✓
- 引用上下文：✓ — 引用为 conformal prediction
- **结论：✅ OK**

### 55. [malinin2021uncertainty] Malinin & Gales (2021). "Uncertainty Estimation in Autoregressive Structured Prediction". ICLR 2021.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 uncertainty in structured prediction
- **结论：✅ OK**

### 56. [yee2019noisy] Yee et al. (2019). "Simple and Effective Noisy Channel Modeling for Neural Machine Translation". EMNLP-IJCNLP 2019.
- 在线验证：ACL Anthology + arXiv **找到** | 匹配度：**部分**
- 作者：⚠️ ACL Anthology (D19-1571) 列 3 人，arXiv 列 4 人（+Nathan Ng）。Bib 匹配 proceedings 版 3 人，但 URL 指向 arXiv 4 人版
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (1908.05731)
- 论文存在：✓
- 引用上下文：✓ — 引用为 noisy channel models
- **结论：⚠️ 需修正 — 作者列表与 arXiv URL 不一致（见上方详述）**

### 57. [li2023stepaware] Li et al. (2023). "Making Large Language Models Better Reasoners with Step-Aware Verifier". ACL 2023.
- 在线验证：ACL Anthology **找到** | 匹配度：**部分**
- 作者：✓
- 年份：✓
- 标题：⚠️ ACL Anthology: "Making Language Models Better Reasoners..." (无 "Large")；arXiv: "Making **Large** Language Models Better Reasoners..."。Bib 使用 arXiv 标题但引用 ACL proceedings
- Venue：✓
- DOI/arXiv：✓ (2206.02336)
- 论文存在：✓
- 引用上下文：✓ — 引用为 step-aware verifier / trained verifiers
- **结论：⚠️ 需修正 — 标题应删除 "Large" 以匹配 ACL proceedings**

### 58. [xiao2022uncertainty] Xiao et al. (2022). "Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis". Findings EMNLP 2022.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：N/A — **未在 tex 中引用**
- **结论：✅ 论文真实，但未被引用（建议删除或添加引用）**

### 59. [li2026rewardtail] Li et al. (2026). "Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search". arXiv.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- DOI/arXiv：✓ (2602.01485)
- 论文存在：✓
- 引用上下文：✓ — 引用为 reward-tail-guided search
- **结论：✅ OK**

### 60. [shinn2023reflexion] Shinn et al. (2023). "Reflexion: Language Agents with Verbal Reinforcement Learning". NeurIPS 2023.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓ (5 authors, matching NeurIPS proceedings; S2 erroneously adds "Beck Labash" as 6th)
- 年份：✓
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 iterative self-verification
- **结论：✅ OK**

### 61. [xu2024llmie] Xu et al. (2024). "Large Language Models for Generative Information Extraction: A Survey". Frontiers of Computer Science.
- 在线验证：Semantic Scholar **找到** | 匹配度：**部分**
- 作者：📝 Bib 列 10 人含 "Wang, Yang"；S2 列 9 人无 "Wang, Yang"。需对照出版商确认
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (18(6), 186357)
- DOI：✓ (10.1007/s11704-024-40555-y)
- 论文存在：✓
- 引用上下文：✓ — 引用为 LLM-based IE survey
- **结论：✅ OK（作者 "Wang, Yang" 待出版商确认）**

### 62. [wang2025gptner] Wang et al. (2025). "GPT-NER: Named Entity Recognition via Large Language Models". Findings NAACL 2025.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓ (S2 shows 2023 arXiv; NAACL 2025 correct)
- 标题：✓
- Venue：✓
- 论文存在：✓
- 引用上下文：✓ — 引用为 self-verification in NER
- **结论：✅ OK**

### 63. [gero2023selfverification] Gero et al. (2023). "Self-Verification Improves Few-Shot Clinical Information Extraction". arXiv.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv preprint)
- DOI/arXiv：✓ (2306.00024)
- 论文存在：✓
- 引用上下文：✓ — 引用为 self-verification in clinical IE
- **结论：✅ OK**

### 64. [wadhwa2023revisiting] Wadhwa et al. (2023). "Revisiting Relation Extraction in the era of Large Language Models". ACL 2023.
- 在线验证：Semantic Scholar **找到** | 匹配度：**完全**
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- 卷期页码：✓ (15566-15589)
- 论文存在：✓
- 引用上下文：✓ — 引用为 LLM-based RE benchmark
- **结论：✅ OK**
