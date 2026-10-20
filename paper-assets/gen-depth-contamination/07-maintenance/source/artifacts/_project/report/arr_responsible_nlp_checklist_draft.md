# ARR Responsible NLP Research Checklist — Draft Answers
## Project: gen-depth-contamination (EMNLP 2026 via ARR May)

---

### A. Limitations

**A1: Did you discuss the limitations of your work?**
- **Yes** — Limitations section (unnumbered, after Section 7) covers three points: (1) scope limited to 1B–8B models, English only, prompt-chain generation; (2) 15 statistical features provide a lower bound; (3) threshold sensitivity of K* across θ ∈ [0.55, 0.70].

**A2: Did you discuss any potential risks of your work?**
- **Yes** — Ethics Statement discusses dual-use concern (depth estimation could inform adversarial evasion strategies), and notes this risk is shared by all detection research.

---

### B. Ethics / Broader Impact

**B1: Does your paper describe potential risks, harms, or misuses?**
- **Yes** — Ethics Statement (after Limitations) explicitly addresses adversarial dual-use: depth estimation techniques could help adversaries calibrate rewriting to evade detection. Notes binary detection remains robust (AUC ≥ 0.96 at 0v1).

**B2: Does the paper describe any measures taken to mitigate these risks?**
- **Partial** — The paper notes that binary detection robustness mitigates the dual-use concern, but does not describe specific access-control or responsible-release measures.
- ⚠️ **用户确认**: 是否需要补充具体的 mitigation 措施（如 staged release、responsible disclosure 等）？

**B3: Does your paper use any protected attributes (e.g., race, gender)?**
- **No** — Not applicable. The work operates on text corpora without demographic attributes.

**B4: Does your paper comply with the ACL Code of Ethics?**
- **Yes**

---

### C. Computational Experiments

**C1: Did you report the number of parameters in each model used?**
- **Yes** — All 10 model configurations report parameter counts (1B–8B): Qwen2.5-1.5B, Pythia-1.4B/6.9B, OLMo-1B, LLaMA-3.1-8B, Mistral-7B, Gemma-2-2B, Qwen2.5-7B.

**C2: Did you report information about computing infrastructure used?**
- **No** — ⚠️ **论文中未提及 GPU 类型、训练/推理时间、计算平台。** 需要补充。
- ⚠️ **用户确认**: 请提供使用的 GPU 型号、生成和训练的总计算时间（GPU hours），以及估算的碳排放（可选）。

**C3: Did you report the evaluation metrics, along with the measures of statistical significance?**
- **Yes** — 报告了 pairwise AUC、Bootstrap 95% CIs (1,000–10,000 resamples)、permutation tests (p < 0.001)、Bonferroni correction (α_corr = 0.005)、Spearman ρ、ANOVA (η²_p)、McNemar test。统计严谨度高。

**C4: Did you run your experiments with different random seeds?**
- **Yes** — Primary seed = 42; robustness replication with seed = 123 (Wikipedia, C4); filtering experiments use 5 seeds (51 total runs).

**C5: Did you report the hyperparameter search strategy (e.g., grid search, random search)?**
- **Partial** — 超参数值已完整报告（LightGBM: n_estimators=200, lr=0.05, max_depth=6; LoRA: rank=8, α=16; decoding: p=0.95, T=1.0 等），但未说明是否进行了超参数搜索，还是直接使用固定值。
- ⚠️ **用户确认**: 这些超参数是通过搜索确定的还是基于经验/先前工作直接设定的？如果有搜索，请提供搜索范围。

**C6: Did you report the number of training and evaluation examples?**
- **Yes** — 5,000 seed documents per configuration, 30,000 total (6 depth levels), 5-fold GroupKFold CV (n=500 per class in test split). Filtering: MMLU & HellaSwag with standard splits.

---

### D. Data

**D1: Did you state the names and versions of all datasets used?**
- **Yes** — C4 (English validation split), Wikipedia, arXiv abstracts. Downstream: MMLU, HellaSwag.
- ⚠️ **用户确认**: 是否需要补充具体的 dataset version/snapshot date（如 C4 的具体版本号）？

**D2: Did you discuss whether the data you are using/curating contains PII or offensive content?**
- **Partial** — Ethics Statement mentions "do not involve personally identifiable information." C4 is known to contain some PII in its raw form, but the paper uses it as-is without additional filtering.

**D3: Did you provide the license for each dataset?**
- **No** — ⚠️ **论文中未提及数据集的 license 信息。**
- C4: ODC-BY (Open Data Commons Attribution License)
- Wikipedia: CC BY-SA 3.0
- arXiv: arXiv license (varies by paper)
- MMLU / HellaSwag: MIT
- ⚠️ **用户确认**: 请确认上述 license 信息是否准确，是否需要在论文中添加。

**D4: Did you provide the URL or other access method for all datasets?**
- **Partial** — 数据集名称已提供，但未列出具体 URL 或 HuggingFace dataset ID。
- ⚠️ **用户确认**: Checklist 中可简要说明 "All datasets are publicly available via standard repositories (HuggingFace, etc.)"

**D5: Did you discuss whether and how consent was obtained from people whose data you used?**
- **N/A** — 使用的都是公开数据集（C4, Wikipedia, arXiv, MMLU, HellaSwag），无需单独获取同意。

**D6: Did you discuss whether the data you are using was collected in an ethical manner?**
- **N/A** — 使用已有公开数据集，数据收集伦理由原始数据集维护者负责。

---

### E. Code and Software

**E1: Did you include your code, data, and instructions for reproducing the main results?**
- **Partial** — Ethics Statement says "Code and data will be released upon acceptance." 论文中提供了完整的超参数和实验配置，但代码/数据尚未公开。
- Checklist 回答建议: "Yes, code and data will be released upon acceptance. Full hyperparameters and experimental configurations are provided in the paper and appendix."

**E2: Did you include the software and hardware requirements for running your code?**
- **No** — ⚠️ **未提及软件版本（PyTorch, transformers, LightGBM 版本）或硬件要求。**
- ⚠️ **用户确认**: 是否需要在 appendix 中补充 software/hardware requirements？

---

### F. Human Evaluation / Annotation

**F1: Did you report inter-annotator agreement?**
- **N/A** — 本研究不涉及人工评估或标注。

**F2: Did you provide details about the annotators?**
- **N/A**

**F3: Did you discuss whether and how consent was obtained from annotators?**
- **N/A**

**F4: Did you report information about compensation for annotators?**
- **N/A**

---

### G. Use of AI Assistants

**G1: Did you report the use of AI assistants in writing or conducting this research?**
- ⚠️ **用户确认**: 是否使用了 AI 辅助写作？如果是，需要在 Checklist 中声明（ARR 2025+ 要求）。

---

## 需要用户确认的项目

| # | 问题 | 类别 | 紧迫度 |
|---|------|------|--------|
| 1 | **计算资源**: GPU 型号、总 GPU hours、计算平台 | C2 | 🔴 必须补充 |
| 2 | **超参数搜索**: 是否进行了搜索？搜索范围？ | C5 | 🟡 建议补充 |
| 3 | **数据集 license**: 确认 C4/Wikipedia/arXiv/MMLU/HellaSwag 的 license | D3 | 🟡 建议确认 |
| 4 | **数据集版本**: C4 具体版本号/snapshot | D1 | 🟡 建议补充 |
| 5 | **软件版本**: PyTorch, transformers, LightGBM 等版本号 | E2 | 🟡 建议补充 |
| 6 | **AI 辅助写作声明** | G1 | 🟡 按 ARR 要求 |
| 7 | **Dual-use mitigation**: 是否需要补充具体措施 | B2 | 🟢 可选 |
| 8 | **数据集 URL**: 是否需要列出具体下载链接 | D4 | 🟢 可选 |

---

## 建议的 Checklist 简要回答模板

以下可直接用于 OpenReview submission form 填写（英文）：

> **A1 (Limitations):** Yes. Section "Limitations" discusses scope (model scale, English only, prompt-chain), feature set lower bound, and threshold sensitivity.
>
> **B (Risks):** Yes. Ethics Statement discusses dual-use risks of depth estimation for adversarial evasion and notes binary detection robustness as mitigation.
>
> **C1 (Parameters):** Yes. All 10 model configurations report parameter counts (1B–8B) in Section 3 and Table 1.
>
> **C2 (Compute):** [待补充 — 需要用户提供 GPU 型号和计算时间]
>
> **C3 (Significance):** Yes. Bootstrap CIs, permutation tests (p < 0.001), Bonferroni correction, ANOVA, McNemar tests reported throughout Sections 4–5 and Appendix.
>
> **C4 (Seeds):** Yes. Primary seed=42, robustness seed=123, 5 seeds for filtering experiments.
>
> **C5 (Hyperparameters):** All hyperparameters are reported. [待确认: 是否进行了搜索]
>
> **C6 (Data size):** Yes. 5,000 seeds × 6 depths × 10 configs; 5-fold GroupKFold; n=500/class test splits.
>
> **D1–D4 (Data):** All datasets are publicly available (C4, Wikipedia, arXiv, MMLU, HellaSwag). [待补充: license, version]
>
> **E1 (Code):** Code and data will be released upon acceptance.
>
> **F (Human eval):** N/A — no human evaluation conducted.
>
> **G (AI assistants):** [待用户确认]
