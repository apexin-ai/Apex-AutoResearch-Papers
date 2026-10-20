# research reference verify r5

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference-verify-r5_20260516T052707_result.json`
- **Structured JSON:** [`8ea17fbe4b41bd839c99.json`](../../sessions/8e/8ea17fbe4b41bd839c99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Reference Verification Report
==============================

(a) Dawid & Skene 1979: ✅ VERIFIED
    Full citation: A. P. Dawid and A. M. Skene. "Maximum Likelihood Estimation of
    Observer Error-Rates Using the EM Algorithm." Journal of the Royal Statistical
    Society, Series C (Applied Statistics), 28(1):20–28, 1979.

    BibTeX:
    @article{dawid1979maximum,
      author    = {Dawid, A. P. and Skene, A. M.},
      title     = {Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},
      journal   = {Journal of the Royal Statistical Society. Series C (Applied Statistics)},
      volume    = {28},
      number    = {1},
      pages     = {20--28},
      year      = {1979},
      publisher = {Wiley},
      doi       = {10.2307/2346806}
    }

(b) ProbGuard: ✅ EXISTS
    Full citation: Haoyu Wang, Christopher M. Poskitt, Jiali Wei, and Jun Sun.
    "ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety."
    arXiv preprint arXiv:2508.00500, 2025.
    Note: v1 submitted Aug 2025, v3 updated Mar 2026.

(c) Quantifying Behavioral Degradation: ✅ EXISTS
    注意：论文完整标题是 "Agent Drift: Quantifying Behavioral Degradation in
    Multi-Agent LLM Systems Over Extended Interactions"（带前缀 "Agent Drift:"）。
    如果 bib 中只写了副标题部分，需要补全。
    Full citation: Abhishek Rath. "Agent Drift: Quantifying Behavioral Degradation
    in Multi-Agent LLM Systems Over Extended Interactions."
    arXiv preprint arXiv:2601.04170, 2026.

(d) Zhan et al. 2019: ✅ VERIFIED
    Full citation: Eric Zhan, Stephan Zheng, Yisong Yue, Long Sha, and Patrick Lucey.
    "Generating Multi-Agent Trajectories using Programmatic Weak Supervision."
    In International Conference on Learning Representations (ICLR), 2019.
    arXiv:1803.07612. OpenReview: https://openreview.net/forum?id=rkxw-hAcFQ
```

**总结**：4 篇全部真实存在，无 hallucination。需注意：
- **(a)** 需补入 bib（上面已提供 BibTeX）
- **(c)** 标题可能不完整——完整标题带 "Agent Drift:" 前缀，检查 bib 中是否一致

Sources:
- [Dawid & Skene 1979 - Wiley](https://rss.onlinelibrary.wiley.com/doi/abs/10.2307/2346806)
- [Dawid & Skene 1979 - JSTOR](https://www.jstor.org/stable/2346806?seq=1)
- [ProbGuard - arXiv](https://arxiv.org/abs/2508.00500)
- [Agent Drift - arXiv](https://arxiv.org/abs/2601.04170)
- [Zhan et al. 2019 - arXiv](https://arxiv.org/abs/1803.07612)
- [Zhan et al. 2019 - OpenReview](https://openreview.net/forum?id=rkxw-hAcFQ)

---
