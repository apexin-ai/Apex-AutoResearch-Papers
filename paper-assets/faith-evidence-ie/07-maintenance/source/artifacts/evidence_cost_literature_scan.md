# Evidence Cost Literature Scan
**Date**: 2026-05-16
**Objective**: 搜索 "evidence generation cost in information extraction" 相关文献，评估 FREIGE 发现的新颖性。

## FREIGE 的核心发现
- No-evidence SFT: rel_f1 = 0.4876
- Evidence SFT: rel_f1 = 0.4106
- **Evidence tax**: -7.7 F1 points (generative SFT, DocRE, LLM fine-tuning)

## 搜索结论

### 新颖性评估: **高度新颖**

**没有任何现有工作在以下组合条件下量化过 evidence 对主任务的性能代价：**
1. Generative (seq2seq) evidence 生成（非 extractive attention supervision）
2. Document-level relation extraction（非 sentence-level）
3. LLM SFT fine-tuning（非 prompting）
4. 明确量化 evidence 导致的 rel_f1 下降

### 与现有工作的关键区别

| 工作 | 设定 | Evidence 对 RE 的影响 | 与 FREIGE 的差异 |
|------|------|---------------------|-----------------|
| DREEAM (Ma+, EACL 2023) | Encoder-based, attention supervision | **帮助** RE (+2 F1) | 非生成式；evidence 是 attention 监督信号 |
| E2GRE (Huang+, 2021) | Encoder-based, joint prediction | **帮助** RE | 非生成式；evidence 是 auxiliary classification head |
| Two Flints (Tang & Surdeanu, CL 2023) | Extractive rationale + RE classification | **帮助** RE (+4% F1) | Sentence-level；extractive 非 generative |
| Resck+ (NAACL 2024 Findings) | Text classification + rationale plausibility | **微弱影响** (negligible) | Classification 非 extraction；非 seq2seq |
| Mind Your Step (Geng+, 2024/ICML 2025) | CoT prompting | **有害** (up to -36.3%) | Prompting 非 SFT；非 IE task |
| CoT-ER (EMNLP 2023 Findings) | Few-shot prompting with evidence for RE | **帮助** RE | Prompting 非 SFT；sentence-level |
| Rationalization Survey (Gurrapu+, 2023) | Survey | 列为 desiderata: "should not hurt" | 仅声明不应有害，未量化 |

### 核心洞察

**Encoder-based discriminative 模型**中，evidence 作为 attention supervision 或 auxiliary task 通常**帮助** RE（DREEAM、E2GRE、CDER、Two Flints）。这是因为 evidence 信号引导模型聚焦相关 context，属于 implicit knowledge injection。

**Generative LLM SFT** 中，要求模型同时生成 evidence 和 relation 是一个**更困难的任务**——模型必须在有限的 output capacity 中分配 token budget 给两个子任务。FREIGE 的 -7.7 F1 量化了这个 "faithfulness tax"，这在文献中是首次。

## 找到的新论文（需加入 literature_map.yaml）

### 1. It Takes Two Flints to Make a Fire (Direct Competitor)
- **Authors**: Zheng Tang, Mihai Surdeanu
- **Year**: 2023
- **Venue**: Computational Linguistics, Vol. 49, Issue 1
- **URL**: https://aclanthology.org/2023.cl-1.3/
- **Key Finding**: Joint training of RE classifier + explanation sequence labeler. Joint training HELPS RE (+~4% F1 on CoNLL04). Explanation classifier operates on extractive features.
- **Role**: direct_competitor
- **Critical Difference**: Sentence-level, extractive, discriminative model. 与 FREIGE 的 generative DocRE 设定相反——他们发现 joint 有益，我们发现 joint 有害。这个对比强化了我们的 contribution。

### 2. Robust Explanation for Free or At the Cost of Faithfulness
- **Authors**: Zeren Tan, Yang Tian
- **Year**: 2023
- **Venue**: ICML 2023
- **URL**: https://proceedings.mlr.press/v202/tan23a.html
- **Key Finding**: 首次理论证明 robustness-faithfulness trade-off 存在。Robust model 可免费获得 robust explanation；non-robust model 提升 explanation robustness 需牺牲 faithfulness。
- **Role**: theoretical_foundation
- **Relevance**: 提供了 "faithfulness 有代价" 的理论框架，虽然研究对象是 post-hoc explanation 而非 generative evidence。

### 3. Rationalization for Explainable NLP: A Survey
- **Authors**: Sai Gurrapu et al.
- **Year**: 2023
- **Venue**: Frontiers in AI
- **URL**: https://www.frontiersin.org/articles/10.3389/frai.2023.1225093/full
- **Key Finding**: 首个 NLP rationalization 综述。列出 desiderata: "rationale extraction should not hurt task performance"。将 rationalization 分为 extractive 和 abstractive 两类。
- **Role**: background_survey
- **Relevance**: 明确了 "不应损害主任务" 是学界共识/期望，但没有论文系统量化违反这一 desiderata 的程度。FREIGE 的发现直接挑战了这一假设。

### 4. Chain of Thought with Explicit Evidence Reasoning for Few-shot RE (CoT-ER)
- **Authors**: Xilai Yin et al.
- **Year**: 2023
- **Venue**: EMNLP 2023 Findings
- **URL**: https://aclanthology.org/2023.findings-emnlp.153/
- **Key Finding**: 用 LLM 先生成 evidence，再 CoT 推理做 few-shot RE。与 fully-supervised SOTA 竞争力相当（FewRel 1.0/2.0）。
- **Role**: related_method
- **Relevance**: 在 prompting 设定下 evidence+CoT 有益。与 SFT 设定下 evidence 有害形成对比——说明 evidence cost 可能是 SFT 训练 specific 的问题。

### 5. Entity and Evidence Guided Relation Extraction for DocRED (E2GRE)
- **Authors**: Kevin Huang et al.
- **Year**: 2021
- **Venue**: RepL4NLP @ ACL 2021
- **URL**: https://aclanthology.org/2021.repl4nlp-1.30/
- **Key Finding**: Joint evidence prediction + relation extraction for DocRED。利用 pretrained LM attention 作为 evidence 特征，joint training 在 RE 和 evidence prediction 上均有增益。
- **Role**: direct_competitor
- **Relevance**: DocRE 上 joint evidence+RE 的先驱。但使用 encoder-based discriminative 模型，evidence 是 binary classification 而非 text generation。他们发现 joint 有益，与 FREIGE 相反。

### 6. Revisiting Relation Extraction in the era of Large Language Models
- **Authors**: Somin Wadhwa, Silvio Amir, Byron Wallace
- **Year**: 2023
- **Venue**: ACL 2023
- **URL**: https://aclanthology.org/2023.acl-long.868/
- **Key Finding**: GPT-3 few-shot 在 RE 上接近 SOTA。Seq2seq 大模型在 RE 上有竞争力但评估需要 human evaluation（exact match 低估性能）。
- **Role**: background
- **Relevance**: 建立了 LLM-based generative RE 的 baseline context。

## 总结

| 结论 | 详情 |
|------|------|
| 直接竞品 | **无**——没有论文在 generative SFT + DocRE 设定下量化 evidence cost |
| 间接对比 | Two Flints (sentence-level, extractive → 有益), E2GRE (encoder-based → 有益), CoT-ER (prompting → 有益) |
| 理论支撑 | Tan & Tian ICML 2023 (faithfulness 有理论代价), Rationalization Survey (desiderata: 不应有害) |
| 新颖性确认 | FREIGE 首次在 generative SFT DocRE 中量化 evidence tax (-7.7 F1) |
| Framing 建议 | "文献中 evidence 通常被认为有益（DREEAM, E2GRE, Two Flints）或至少无害（Rationalization Survey desiderata）。FREIGE 揭示了一个被忽视的现象：在 generative LLM SFT 中，faithfulness 有可量化的代价。" |
