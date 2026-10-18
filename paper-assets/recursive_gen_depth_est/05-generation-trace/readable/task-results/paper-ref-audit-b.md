# paper ref audit B

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_ref-audit-B_20260526T104639_result.json`
- **Structured JSON:** [`d6b5712df261c29c5a46.json`](../../sessions/d6/d6b5712df261c29c5a46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have enough verification data now. Let me produce the final report.

---

# 引用核查报告（Worker B：从正文 cite 出发）

## 1. 全部正文引用逐条核查

格式：`[状态] cite_key | authors | year | title_first_5_words | venue | 问题描述`

```
[✓] shumailov2024_nature | Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal | 2024 | AI models collapse when trained | Nature 631:755-759 | —
[✓] dohmatob2024_tale_of_tails | Dohmatob, Feng, Yang, Charton, Kempe | 2024 | A Tale of Tails: Model | ICML 2024 / arXiv:2402.07043 | —
[✓] seddik2024synthetic | Seddik, Chen, Hayou, Youssef, Debbah | 2024 | How Bad is Training on | arXiv:2404.05090 | —
[✓] alemohammad2024_mad | Alemohammad, Casco-Rodriguez, Luzi, ... | 2024 | Self-Consuming Generative Models Go MAD | ICLR 2024 / arXiv:2307.01850 | —
[✓] geng2026_markovian | Geng, Mohamed, Shang, Vazirgiannis, Poibeau | 2026 | Markovian Generation Chains in Large | arXiv:2603.11228 | —
[✓] bertrand2024_stability | Bertrand, Bose, Duplessis, Jiralerspong, Gidel | 2024 | On the Stability of Iterative | ICLR 2024 Spotlight / arXiv:2310.00429 | —
[✗] shi2025_closer_look | Shi, Wu, Zhang, Zhang, Tao, Qu | 2025 | A Closer Look at Model | NeurIPS 2025 Spotlight | Bib 缺 arXiv 编号 (2509.16499)；且该论文主要研究 diffusion models，论文 §related_work 描述"refinements address generalization-to-memorization transitions"对 LLM 语境而言略 stretch（但 cite key OK）
[✓] dohmatob2025_strong_collapse | Dohmatob, Feng, Subramonian, Kempe | 2025 | Strong Model Collapse | ICLR 2025 Spotlight / arXiv:2410.04840 | —
[✓] schaeffer2025 | Schaeffer, Kazdan, Arulandu, Koyejo | 2025 | Position: Model Collapse Does Not | arXiv:2503.03150 | —
[✗] wu2025_detection_survey | Wu, Yang, Zhan, Yuan, Chao, Wong | 2025 | A Survey on LLM-Generated | Computational Linguistics 51(1):275-338 | Bib 写 pages={275--354}，实际为 275-338（页码错误）
[✓] mitchell2023_detectgpt | Mitchell, Lee, Khazatsky, Manning, Finn | 2023 | DetectGPT: Zero-Shot Machine-Generated Text | ICML 2023 (Oral) / arXiv:2301.11305 | —
[✓] fast_detectgpt2024 | Bao, Zhao, Teng, Yang, Zhang | 2024 | Fast-DetectGPT: Efficient Zero-Shot Detection | ICLR 2024 / arXiv:2310.05130 | —
[✓] binoculars2024 | Hans, Schwarzschild, Cherepanova, Kazemi, ... | 2024 | Spotting LLMs With Binoculars: | ICML 2024 / arXiv:2401.12070 | —
[✓] gehrmann2019_gltr | Gehrmann, Strobelt, Rush | 2019 | GLTR: Statistical Detection and | ACL 2019 System Demo / arXiv:1906.04043 | —
[✓] verma2024_ghostbuster | Verma, Fleisig, Tomlin, Klein | 2024 | Ghostbuster: Detecting Text Ghostwritten | NAACL 2024 / arXiv:2305.15047 | —
[✓] tulchinskii2023_intrinsic_dim | Tulchinskii, Kuznetsov, Kushnareva, ... | 2023 | Intrinsic Dimension Estimation for Robust | NeurIPS 2023 / arXiv:2306.04723 | —
[✓] kirchenbauer2023_watermark | Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein | 2023 | A Watermark for Large | ICML 2023 / arXiv:2301.10226 | —
[✓] sadasivan2023_paraphrase | Sadasivan, Kumar, Balasubramanian, Wang, Feizi | 2023 | Can AI-Generated Text be | arXiv:2303.11156 | —
[✓] pudasaini2026_detection_fails | Pudasaini, Miralles-Pechuán, Lillis, Salvador | 2026 | Why AI-Generated Text Detection | arXiv:2603.23146 | —
[✓] bevendorff2025_two_paradigms | Bevendorff, Wiegmann, Richter, Potthast, Stein | 2025 | The Two Paradigms of LLM | Findings of ACL 2025 (pp. 3762-3787) | —
[✓] carlini2021_extracting | Carlini, Tramer, Wallace, Jagielski, ... | 2021 | Extracting Training Data from | USENIX Security 2021 / arXiv:2012.07805 | —
[✓] shi2024_minkprob | Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, Zettlemoyer | 2024 | Detecting Pretraining Data from | ICLR 2024 / arXiv:2310.16789 | —
[✓] ilyas2022datamodels | Ilyas, Park, Engstrom, Leclerc, Madry | 2022 | Datamodels: Understanding Predictions with | ICML 2022 (arXiv:2202.00622) | Bib 标题用 proceedings 版（"Understanding..."），arXiv 题为 "Predicting Predictions from Training Data"——两者皆为同一篇论文官方版本，OK
[✓] christ2024_undetectable | Christ, Gunn, Zamir | 2024 | Undetectable Watermarks for Language | COLT 2024 PMLR 247:1125-1139 / arXiv:2306.09194 | —
[✓] zhu2025_trove | Zhu, Xiao, Wang, Zhai, Zhou, Zong | 2025 | TROVE: A Challenge for | ACL 2025 / arXiv:2503.15289 | —
[✓] editlens2026 | Thai, Emi, Masrour, Iyyer | 2026 | EditLens: Quantifying the Extent | ICLR 2026 / arXiv:2510.03154 | —
[✓] uchendu2020_attribution | Uchendu, Le, Shu, Lee | 2020 | Authorship Attribution for Neural | EMNLP 2020 (pp. 8384-8395) | —
[✓] mohamed2025_broken_telephone | Mohamed, Geng, Vazirgiannis, Shang | 2025 | LLM as a Broken Telephone: | ACL 2025 Long / arXiv:2502.20258 | —
[✓] coral2020 | Cao, Mirjalili, Raschka | 2020 | Rank Consistent Ordinal Regression | Pattern Recognition Letters 140:325-331 / arXiv:1901.07884 | —
[✓] cloc2025 | Pitawela, Carneiro, Chen | 2025 | CLOC: Contrastive Learning for | CVPR 2025 / arXiv:2504.17813 | —
[✓] holtzman2020_nucleus | Holtzman, Buys, Du, Forbes, Choi | 2020 | The Curious Case of | ICLR 2020 / arXiv:1904.09751 | —
[✓] finlayson2024_closing | Finlayson, Hewitt, Koller, Swayamdipta, Sabharwal | 2024 | Closing the Curious Case | ICLR 2024 / arXiv:2310.01693 | —
[✓] garces_arias2025_decoding_decoded | Garcés Arias, Li, Heumann, Assenmacher | 2025 | Decoding Decoded: Understanding Hyperparameter | COLING 2025 / arXiv:2410.06097 | —
[✓] wiher2022_decoding | Wiher, Meister, Cotterell | 2022 | On Decoding Strategies for | TACL 2022 vol.10 pp.997-1012 | —
[✓] basu2021_mirostat | Basu, Ramachandran, Keskar, Varshney | 2021 | Mirostat: A Neural Text | ICLR 2021 / arXiv:2007.14966 | —
[✓] strobl2008_conditional | Strobl, Boulesteix, Kneib, Augustin, Zeileis | 2008 | Conditional variable importance for | BMC Bioinformatics 9:307 | —
[✓] hooker2021_permutation | Hooker, Mentch, Zhou | 2021 | Unrestricted Permutation forces Extrapolation: | Statistics and Computing 31:82 | —
[✓] hosmer2000 | Hosmer, Lemeshow | 2000 | Applied Logistic Regression | Wiley 2nd Edition | —
[✗] he2021_deberta_v3 | He, Gao, Chen | 2021 | DeBERTaV3: Improving DeBERTa using | ICLR 2023 / arXiv:2111.09543 | Bib year 写 2021 且 booktitle=ICLR，实际 ICLR 2023 接收（2021 是 arXiv 上线时间）。应改为 year={2023}
[✓] liu2019_roberta | Liu, Ott, Goyal, Du, Joshi, Chen, Levy, Lewis, Zettlemoyer, Stoyanov | 2019 | RoBERTa: A Robustly Optimized | arXiv:1907.11692 | —
[✓] qwen2.5 | Qwen Team | 2024 | Qwen2.5 Technical Report | arXiv:2412.15115 | —
[✓] llama3 | Grattafiori et al. | 2024 | The Llama 3 Herd | arXiv:2407.21783 | —
[✓] mccullagh1980_ordinal | McCullagh | 1980 | Regression Models for Ordinal | JRSS Series B 42(2):109-142 (with discussion) | —
[✓] frank2001 | Frank, Hall | 2001 | A Simple Approach to | ECML 2001 LNCS 2167 pp.145-156 | —
[✓] rennie2005 | Rennie, Srebro | 2005 | Loss Functions for Preference | IJCAI 2005 Workshop on Advances in Preference Handling | —
[✓] hu2022lora | Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang, Chen | 2022 | LoRA: Low-Rank Adaptation of | ICLR 2022 / arXiv:2106.09685 | —
[✓] diveye2026 | Basani, Chen | 2026 | Diversity Boosts AI-Generated Text | TMLR 2026 / arXiv:2509.18880 | —
[✓] drayson2025_detection_prevents_collapse | Drayson, Yilmaz, Lampos | 2025 | Machine-generated text detection prevents | EMNLP 2025 (pp. 29657-29673) | —
```

## 2. 引用上下文匹配问题

| cite_key | 上下文 | 匹配评估 |
|---|---|---|
| `shi2025_closer_look` | "refinements address generalization-to-memorization transitions" | 该论文主要研究 diffusion models 的 generalization→memorization，并非 LLM 模型崩塌。论文 related work 上下文在讨论 LLM/text 的 model collapse；cite 在 NeurIPS 2025 主题上是 valid，但读者可能误以为该论文研究 LLM。建议在句中显式标注"diffusion models" 或换 cite 为更直接相关的 LLM 工作。 |
| `ilyas2022datamodels` | "Datamodels \cite{ilyas2022datamodels}, watermarks ..., TROVE ... address membership inference or source attribution but remain binary or cooperation-dependent." | Datamodels 严格说是预测训练样本对模型行为的影响（influence/attribution-of-training-points），不是传统意义的 membership inference。语义略有 stretch，但 attribution 类比可接受。 |
| `cloc2025` | section_appendix.tex 中 "DCOL \cite{cloc2025}" | 文中"DCOL"是作者自定义的命名（基于 CLOC 方法的变体），cite 指向 CLOC 原论文是合理的（说明方法来源）。 |

未发现 cite A 描述了 B 的明确错误，但 `shi2025_closer_look` 在域上是 diffusion → LLM 的跨域引用，建议复核。

## 3. Orphan References（bib 中未被正文引用的条目）

共 **29 条** orphan：

```
dohmatob2024_demystified
gerstgrasser2024_accumulate
marchi2024_heat_death
knowledge_collapse2025
sigma2026_spectral
synthetic_eggs2026
yi2026_escaping_collapse
muennighoff2023scaling
bakshi2026_collapse_improvement
wang2026_contamination
falahati2026_curated
pu2026_generator_barrier
wang2023_seqxgpt
bevendorff2026_pan
wang2024_m4_semeval
li2024_mage
yang2024_dnagpt
kazdan2025_collapse_or_thrive
suresh2025_rate_collapse
wenzek2020_ccnet
dugan2024_raid
guo2024curious
padmakumar2024diversity
briesch2024selfconsuming
janitza2016_ordinal_rf
guo2024_biscope
kasa2024_ordinality
zhang2024_minkpp
lakens2017
```

由于 ACL/EMNLP 模板下 `\bibliography` 只输出实际被引用的 entry，这些条目不会出现在最终 PDF 中——不算硬错误，但 bib 文件冗余较多，建议清理或在草稿阶段标注。

注：`drafts/14b_scenarios.tex` 不在 `main.tex` 的 `\input` 链中，其中的 `\cite{llama3}` / `\cite{qwen2.5}` 不进入编译。

## 4. 统计汇总

- 总计正文实际使用 cite keys：**48** 个 unique 条目
- ✓ 通过：**46**
- ✗ 有问题：**2**
- Orphan references in .bib (未被正文引用)：**29** 个

## 5. 具体错误及建议修复

### ✗ 错误 1：`wu2025_detection_survey` 页码错误
- **文件**：`references.bib:171`
- **当前**：`pages = {275--354}`
- **实际**：`pages = {275--338}`（来源：MIT Press / ACL Anthology 官方页面，DOI 10.1162/coli_a_00549）
- **修复**：将 `pages = {275--354}` 改为 `pages = {275--338}`

### ✗ 错误 2：`he2021_deberta_v3` 年份错误
- **文件**：`references.bib:437-444`
- **当前**：`year = {2021}`, `booktitle = {Proceedings of ICLR}`
- **实际**：ICLR 2023 接收（arXiv 上线时间 2021-11，但会议接收在 2023）
- **修复**：将 `year = {2021}` 改为 `year = {2023}`（cite key 名称为 `he2021_*` 保留即可，但 entry 内 year 字段应反映会议年份；或将 cite key 重命名为 `he2023_deberta_v3`，但会需要在所有 .tex 中替换调用）

## 6. 次要建议

- `shi2025_closer_look` 域差异（diffusion vs LLM）：若审稿人挑刺，可在 `related_work.tex:6` 引文处补一句限定语，或换为更直接的 LLM model-collapse refinement 工作。
- `ilyas2022datamodels` 在 "membership inference or source attribution" 描述下略 stretch；可考虑改写为 "training-data influence attribution"。
- Bib 中 29 个 orphan entries 建议在投稿前清理（虽不影响最终 PDF，但暴露给共作者/reviewer 时显得草率）。

Sources:
- [Wu et al. survey - ACL Anthology](https://aclanthology.org/2025.cl-1.8/)
- [DeBERTaV3 - arXiv 2111.09543](https://arxiv.org/abs/2111.09543)
- [Shi et al. A Closer Look - NeurIPS 2025](https://neurips.cc/virtual/2025/poster/119754)
- [Bertrand et al. ICLR 2024 Spotlight](https://github.com/qb3/gen_models_dont_go_mad)
- [Shumailov et al. Nature 2024](https://www.nature.com/articles/s41586-024-07566-y)

---
