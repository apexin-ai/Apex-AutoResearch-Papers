# R27 Reference Verification

## 1. DeNero et al. 2009
- **Status**: ✅ Found
- **Title**: Fast Consensus Decoding over Translation Forests
- **Authors**: John DeNero, David Chiang, Kevin Knight
- **Venue**: ACL-IJCNLP 2009 (Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP), pages 567–575, Suntec, Singapore
- **Year**: 2009
- **ID**: ACL Anthology: P09-1064 — https://aclanthology.org/P09-1064/
- **Relevance**: Proposes hypergraph-based consensus (MBR) decoding for MT using BLEU as similarity metric. Directly relevant to the paper's MBR equivalence proof for entity construction — establishes the foundational connection between consensus decoding and minimum Bayes risk in structured output spaces.

> **Note**: There is also a related 2009 paper by Pauls, DeNero & Klein: "Consensus Training for Consensus Decoding in Machine Translation" (EMNLP 2009, D09-1147). The DeNero-first-author paper above is the more likely intended reference given "consensus decoding for MT".

## 2. Desai & Durrett 2020
- **Status**: ✅ Found
- **Title**: Calibration of Pre-trained Transformers
- **Authors**: Shrey Desai, Greg Durrett
- **Venue**: EMNLP 2020 (Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing)
- **Year**: 2020
- **ID**: arXiv: 2003.07892 — https://arxiv.org/abs/2003.07892 | ACL Anthology: 2020.emnlp-main.21 — https://aclanthology.org/2020.emnlp-main.21/
- **Relevance**: Analyzes calibration of BERT/RoBERTa on NLI, paraphrase detection, commonsense reasoning. Finds pre-trained models are well-calibrated in-domain but degrade out-of-domain. Relevant to the paper's discussion of log-probability reliability as a selection signal and the correlation-selection gap diagnostic.

> **Note**: The reviewer described this as "calibration for sequence labeling", but the paper covers NLI/paraphrase/commonsense — not sequence labeling per se. The calibration methodology and findings are still relevant. Cite accurately in the paper.

## 3. Huang et al. 2024
- **Status**: ✅ Found
- **Title**: Large Language Models Cannot Self-Correct Reasoning Yet
- **Authors**: Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou
- **Venue**: ICLR 2024 (The Twelfth International Conference on Learning Representations)
- **Year**: 2024 (arXiv: October 2023)
- **ID**: arXiv: 2310.01798 — https://arxiv.org/abs/2310.01798 | OpenReview: https://openreview.net/forum?id=IkmD3fKBPQ
- **Relevance**: Demonstrates that LLMs struggle with intrinsic self-correction (without external feedback), and performance can degrade after self-correction attempts. Directly relevant to the paper's finding that self-consistency fails in structured generation — provides the reasoning-domain parallel showing SC/self-verification limitations are not unique to IE.

## 4. "Aronica et al. 2024"
- **Status**: ⚠️ Paper found, but author attribution is INCORRECT
- **Title**: A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction
- **Actual Authors**: Yinghao Li, Rampi Ramprasad, Chao Zhang (**NO author named "Aronica"**)
- **Venue**: Findings of EMNLP 2024, pages 5133–5148, Miami, Florida
- **Year**: 2024
- **ID**: arXiv: 2402.13364 — https://arxiv.org/abs/2402.13364 | ACL Anthology: 2024.findings-emnlp.295 — https://aclanthology.org/2024.findings-emnlp.295/
- **Code**: https://github.com/Yinghao-Li/GnO-IE
- **Relevance**: Proposes the G&O (Generate & Organize) method that separates content generation from output structuring in a two-step pipeline, reducing errors when LLMs produce structured IE output (NER, RE). Directly relevant as a complementary approach to improving structured generation quality.

> **⚠️ IMPORTANT**: Reviewer 2 cited this as "Aronica et al., 2024" but no author named Aronica exists on this paper. This is likely an AI reviewer hallucination of the author name. The correct citation is **Li et al. (2024)**. When adding to the paper, use the correct authors: Yinghao Li, Rampi Ramprasad, and Chao Zhang.

---

## Summary

| # | Cited As | Status | Correct Citation | Venue |
|---|----------|--------|-----------------|-------|
| 1 | DeNero et al. 2009 | ✅ Found | DeNero, Chiang & Knight 2009 | ACL-IJCNLP 2009 |
| 2 | Desai & Durrett 2020 | ✅ Found | Desai & Durrett 2020 | EMNLP 2020 |
| 3 | Huang et al. 2024 | ✅ Found | Huang et al. 2024 | ICLR 2024 |
| 4 | Aronica et al. 2024 | ⚠️ Author wrong | **Li, Ramprasad & Zhang 2024** | Findings of EMNLP 2024 |

### Recommended BibTeX keys
- `denero2009fast`
- `desai2020calibration`
- `huang2024large`
- `li2024simple`
