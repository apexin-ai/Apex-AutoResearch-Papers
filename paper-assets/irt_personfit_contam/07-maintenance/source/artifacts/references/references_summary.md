# References Summary

## 1. Test Security / Person-Fit Statistics

| Citation Key | Authors | Year | Venue | Contribution |
|---|---|---|---|---|
| `StOnge2011` | St-Onge, Valois, Abdous, Germain | 2011 | Applied Psychological Measurement | Monte Carlo study on how aberrance rates affect person-fit detection accuracy |
| `Tendeiro2014` | Tendeiro, Meijer | 2014 | Journal of Educational Measurement | Demonstrates usefulness of simple nonparametric statistics for detecting invalid test scores |
| `Reise1990` | Reise | 1990 | Applied Psychological Measurement | Compares item-fit and person-fit methods for assessing model-data fit in IRT |
| `Meijer2001` | Meijer, Sijtsma | 2001 | Applied Psychological Measurement | Comprehensive review of person-fit evaluation methods (classical + IRT-based) |
| `Drasgow1985` | Drasgow, Levine, Williams | 1985 | British J. Math. & Stat. Psych. | Introduces the $l_z$ statistic for appropriateness measurement |
| `Snijders2001` | Snijders | 2001 | Psychometrika | Derives $l_z^*$ — asymptotically correct standardization when ability is estimated |
| `Karabatsos2003` | Karabatsos | 2003 | Applied Measurement in Education | Systematic comparison of 36 person-fit statistics for aberrant response detection |
| `Levine1979` | Levine, Rubin | 1979 | Journal of Educational Statistics | Foundational work on measuring appropriateness of multiple-choice test scores |

## 2. IRT for LLMs / NLP

| Citation Key | Authors | Year | Venue | Contribution |
|---|---|---|---|---|
| `Lalor2019` | Lalor, Wu, Yu | 2019 | EMNLP | Learning IRT parameters using artificial crowds (DNN-generated responses) |
| `Rodriguez2021` | Rodriguez, Barrow, Hoyle, Lalor, Jia, Boyd-Graber | 2021 | ACL | Shows evaluation examples have different informativeness; proposes IRT-based leaderboards |
| `MaiaPolo2024` | Maia Polo, Weber, Choshen, Sun, Xu, Yurochkin | 2024 | ICML | tinyBenchmarks — IRT-based efficient LLM evaluation with fewer examples |
| `Zhuang2023` | Zhuang, Liu, Ning, et al. | 2023 | arXiv:2306.10512 | Adaptive testing perspective for efficiently measuring LLM cognitive ability |
| `Byrd2022` | Byrd, Srivastava | 2022 | ACL | Predicting difficulty and discrimination of natural language questions using IRT |

### UNVERIFIED
- **Yin, Shi, Wu, Chang (2024)** — IRT for LLM evaluation (NeurIPS). Searched: multiple combinations of author names + IRT + NeurIPS 2024. Could not locate a matching paper.

## 3. LLM Benchmark Contamination

| Citation Key | Authors | Year | Venue | Contribution |
|---|---|---|---|---|
| `Xu2024contamination` | Xu, Guan, Greene, Kechadi | 2024 | arXiv:2406.04244 | Survey on benchmark data contamination in LLMs |
| `Yang2023` | Yang, Chiang, Zheng, Gonzalez, Stoica | 2023 | arXiv:2311.04850 | Shows rephrased samples bypass string-matching decontamination |
| `Zhu2024` | Zhu, Chen, Wang, Gong, Yang, Xie | 2024 | ICLR | DyVal — graph-based dynamic evaluation to avoid contamination |
| `Oren2024` | Oren, Meister, Chatterji, Ladhak, Hashimoto | 2024 | ICLR | Statistical proof of test set contamination in black-box LLMs |
| `Golchin2024` | Golchin, Surdeanu | 2024 | ICLR | Time Travel — guided instruction method to trace contamination per instance |
| `Deng2024` | Deng, Zhao, Tang, Gerstein, Cohan | 2024 | NAACL | Empirical investigation of data contamination in modern benchmarks |
| `Wang2024selfevolving` | Wang, Long, Fan, Wei, Huang | 2024 | arXiv:2402.11443 | Multi-agent framework for dynamically evolving benchmarks |

### Notes
- User specified "Li, Zhang, et al. (2024)" for the contamination survey — closest match is `Xu2024contamination` (Xu, Guan, Greene, Kechadi).
- User specified "Xu, Jain, et al. (2024)" for benchmark self-evolving — closest match is `Wang2024selfevolving` (Wang, Long, Fan, Wei, Huang).

## 4. Memorization in Neural Networks

| Citation Key | Authors | Year | Venue | Contribution |
|---|---|---|---|---|
| `Carlini2023` | Carlini, Ippolito, Jagielski, Lee, Tramèr, Zhang | 2023 | ICLR | Three log-linear laws quantifying memorization across LLM scales |
| `Tirumala2022` | Tirumala, Markosyan, Zettlemoyer, Aghajanyan | 2022 | NeurIPS | Shows LLMs memorize training data without overfitting; analyzes training dynamics |
| `Feldman2020` | Feldman, Zhang | 2020 | NeurIPS | Long-tail memorization — influence estimation reveals why NNs memorize atypical examples |

## 5. LLM Evaluation / Benchmarks

| Citation Key | Authors | Year | Venue | Contribution |
|---|---|---|---|---|
| `Hendrycks2021` | Hendrycks, Burns, Basart, Zou, Mazeika, Song, Steinhardt | 2021 | ICLR | MMLU — 57-subject massive multitask benchmark for language understanding |
| `Cobbe2021` | Cobbe, Kosaraju, et al. | 2021 | arXiv:2110.14168 | GSM8K — 8.5K grade school math problems + verifier-based solving |
| `Chen2021` | Chen, Tworek, et al. | 2021 | arXiv:2107.03374 | HumanEval — 164 hand-crafted code generation problems (Codex paper) |
| `Clark2018` | Clark, Cowhey, et al. | 2018 | arXiv:1803.05457 | ARC — AI2 Reasoning Challenge for advanced question answering |
| `Zellers2019` | Zellers, Holtzman, Bisk, Farhadi, Choi | 2019 | ACL | HellaSwag — adversarially filtered commonsense inference benchmark |

## 6. RLHF / Post-training

| Citation Key | Authors | Year | Venue | Contribution |
|---|---|---|---|---|
| `Ouyang2022` | Ouyang, Wu, et al. | 2022 | NeurIPS | InstructGPT — RLHF pipeline for aligning LLMs with human instructions |
| `Shao2024` | Shao, Wang, Zhu, et al. | 2024 | arXiv:2402.03300 | DeepSeekMath — introduces GRPO (Group Relative Policy Optimization) |
| `Rafailov2023` | Rafailov, Sharma, Mitchell, Manning, Ermon, Finn | 2023 | NeurIPS | DPO — direct preference optimization without explicit reward model |

---

**Total: 30 verified entries + 1 unverified**
