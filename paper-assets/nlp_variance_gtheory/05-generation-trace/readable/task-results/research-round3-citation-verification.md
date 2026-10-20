# research round3 citation verification

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_round3_citation_verification_20260522T090113_result.json`
- **Structured JSON:** [`b0a58692d2e000a66183.json`](../../sessions/b0/b0a58692d2e000a66183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verification complete. Here are the results:

---

### [1] MetaBench (Kipnis et al.)
- **状态**：存在
- **标题**：metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models
- **作者**：Alex Kipnis, Konstantinos Voudouris, Luca Schulze Buschoff, Eric Schulz
- **发表状态**：ICLR 2025 Conference（已确认）
- **BibTeX**：
```bibtex
@inproceedings{kipnis2025metabench,
    title={metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
    author={Kipnis, Alex and Voudouris, Konstantinos and Schulze Buschoff, Luca and Schulz, Eric},
    booktitle={Proceedings of the International Conference on Learning Representations},
    year={2025}
}
```
- **备注**：arXiv:2407.12844, 初投 2024-07-04, 修订 2025-02-20

---

### [2] ATLAS (Li et al.)
- **状态**：存在，已从 ICLR 2026 撤稿
- **标题**：Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks
- **作者**：Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla
- **发表状态**：ICLR 2026 Withdrawn Submission（OpenReview ID: iX39LhePyd, 提交 2025-09-19, 撤回 2026-01-02）。只能引为 arXiv preprint。
- **BibTeX**：
```bibtex
@article{li2025atlas,
    title={Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
    author={Li, Peiyu and Tang, Xiuxiu and Chen, Si and Cheng, Ying and Metoyer, Ronald and Hua, Ting and Chawla, Nitesh V.},
    journal={arXiv preprint arXiv:2511.04689},
    year={2025}
}
```
- **备注**：Reviewer 信息确认——已撤稿，不可标注 ICLR

---

### [3] Waldis et al. (2024)
- **状态**：需要 Director 确认具体引哪篇
- **最可能候选**：Holmes (TACL 2024)
- **标题**：Holmes: A Benchmark to Assess the Linguistic Competence of Language Models
- **作者**：Andreas Waldis, Yotam Perlitz, Leshem Choshen, Yufang Hou, Iryna Gurevych
- **发表状态**：Transactions of the Association for Computational Linguistics (TACL), Vol. 12, pp. 1616–1647, 2024
- **BibTeX**：
```bibtex
@article{waldis-etal-2024-holmes,
    title={Holmes: A Benchmark to Assess the Linguistic Competence of Language Models},
    author={Waldis, Andreas and Perlitz, Yotam and Choshen, Leshem and Hou, Yufang and Gurevych, Iryna},
    journal={Transactions of the Association for Computational Linguistics},
    volume={12},
    pages={1616--1647},
    year={2024},
    doi={10.1162/tacl_a_00718}
}
```
- **备注**：经过对 Waldis 的全部 2024 出版物排查（Google Scholar、DBLP、个人主页），**他没有直接关于 "evaluation robustness / benchmark variance" 的论文**。Holmes 是他最相关的 benchmark 论文，但主题是 linguistic competence probing，不是 evaluation reliability/variance。如果 Director 需要的是 evaluation robustness 方向的论文，可能混淆了以下论文之一：
  - Perlitz et al. "Do These LLM Benchmarks Agree? Fixing Benchmark Evaluation with BenchBench" (arXiv 2407.13696, NeurIPS 2025) — Waldis 不是作者
  - Madaan et al. "Quantifying Variance in Evaluation Benchmarks" (arXiv 2406.10229) — Waldis 不是作者
  - Siska et al. "Examining the Robustness of LLM Evaluation to the Distributional Assumptions of Benchmarks" (ACL 2024) — Waldis 不是作者

  **建议**：请 Director 确认是引 Holmes，还是实际需要 Perlitz 或其他人的 evaluation robustness 工作。

---

Sources:
- [MetaBench arXiv](https://arxiv.org/abs/2407.12844)
- [MetaBench ICLR 2025 Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4ebc26584810a189ef1e4f173aba4319-Abstract-Conference.html)
- [ATLAS arXiv](https://arxiv.org/abs/2511.04689)
- [ATLAS OpenReview (Withdrawn)](https://openreview.net/forum?id=iX39LhePyd)
- [Holmes ACL Anthology](https://aclanthology.org/2024.tacl-1.88/)
- [Andreas Waldis personal page](https://tresiwald.github.io/)

---
