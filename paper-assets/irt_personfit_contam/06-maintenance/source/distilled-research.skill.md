# IRT × Person-Fit × Contamination Detection — Research Patterns

Distilled from 10 papers (8 deep, 2 abstract). Domain: LLM contamination detection + psychometric person-fit + IRT evaluation.

## Evaluation Consensus

- **Primary metric**: AUC/AUROC (6/10). Psychometrics uses Type I error + power (3/10). IRT-eval uses Kendall tau (2/10). **来源**: Min-K%, CoDeC, ConStat | **置信度**: 高
- **Benchmark set**: GSM8K (4/10), ARC (4/10), MMLU (3/10), HellaSwag (3/10), AIME (3/10), GPQA (3/10). 4-6 benchmarks across domains is standard. **置信度**: 高
- **No variance reported**: 6/8 papers use single-run AUC. Only ATLAS (MAE±SE) and Sinharay (10 replications) report uncertainty. Reviewer vulnerability. **置信度**: 高

## Method Landscape

- **Log-prob methods dominate but proven fragile**: Min-K%/PPL/Zlib appear in 4+ papers as baselines. Wang et al. (ICLR 2026) proves all 10 fail (~50% AUROC) on RL-trained reasoning models. **置信度**: 高
- **Two contamination definitions**: (1) data-overlap/membership inference (Min-K%, CoDeC), (2) performance-based/inflated scores (ConStat). Performance-based gaining traction. **置信度**: 中
- **IRT rising for LLM eval**: PSN-IRT (AAAI 2026 Oral) + ATLAS both use IRT to replace accuracy. Fisher-information item selection improves ranking. Neither addresses contamination via person-fit. **置信度**: 中

## Research Gaps (Our Niche)

- **No person-fit × LLM contamination bridge**: Person-fit (lz, lz*, Ht, Ls) is established for human test fraud (karabatsos2003, sinharay2017, hong2021lzm). IRT applied to LLMs (psnirt2026, atlas2025). Nobody combines them. 0/10 papers. **置信度**: 高
- **RL-robustness unsolved**: Log-prob methods fail for reasoning models. Person-fit operates on response patterns, not log-probs — potentially RL-robust. **来源**: Wang et al., Self-Critique | **置信度**: 中
- **Sample-level detection with guarantees missing**: CoDeC = dataset-level only. ConStat = model×benchmark p-values. Person-fit provides per-examinee z-scores with known null (Ls ~ N(0,1)). **来源**: CoDeC, ConStat, Sinharay | **置信度**: 高

## Experimental Design Patterns

- **Controlled contamination required**: ConStat fine-tunes 18 models; Self-Critique injects into RL data; Wang uses 2×2 factorial. Ground-truth essential for credibility. 4/10. **置信度**: 高
- **Multi-family model coverage**: 3-5 families across scales. IRT needs large calibration pools (3000+ in ATLAS). 6/10. **置信度**: 高
- **Simulation + real data**: Psychometric standard (sinharay2017). NLP uses controlled fine-tuning + wild evaluation. Our paper should do both. 3/10. **置信度**: 高
