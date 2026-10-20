# audit reference verification r5

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_reference-verification-r5_20260516T054837_result.json`
- **Structured JSON:** [`6944d760edf360e94b6b.json`](../../sessions/69/6944d760edf360e94b6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果如下：

---

**Paper (a): Dawid & Skene 1979**
```
Status: VERIFIED
Full citation: A. P. Dawid and A. M. Skene. "Maximum Likelihood Estimation of
  Observer Error-Rates Using the EM Algorithm." Journal of the Royal
  Statistical Society: Series C (Applied Statistics), 28(1):20–28, 1979.
Notes: 当前 bib 条目基本正确。journal 写 "Applied Statistics" 是可接受的简写。
  可补 DOI。
BibTeX 修正建议:
  @article{dawid1979em,
    title   = {Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},
    author  = {A. P. Dawid and A. M. Skene},
    journal = {Journal of the Royal Statistical Society: Series C (Applied Statistics)},
    volume  = {28},
    number  = {1},
    pages   = {20--28},
    year    = {1979},
    doi     = {10.2307/2346806},
  }
```

---

**Paper (b): ProbGuard**
```
Status: VERIFIED — 但 bib 条目作者名有误
Full citation: Haoyu Wang et al. "ProbGuard: Probabilistic Runtime Monitoring
  for LLM Agent Safety." arXiv preprint arXiv:2508.00500, 2025.
Notes: 论文真实存在。当前 bib 写 author = {Zijian Wang and others}，
  实际第一作者是 Haoyu Wang，需修正。
BibTeX 修正建议:
  @article{wang2025probguard,
    title   = {ProbGuard: Probabilistic Runtime Monitoring for {LLM} Agent Safety},
    author  = {Haoyu Wang and others},
    journal = {arXiv preprint arXiv:2508.00500},
    year    = {2025},
  }
```

---

**Paper (c): Agent Drift / Quantifying Behavioral Degradation**
```
Status: VERIFIED — bib 条目信息不完整
Full citation: Abhishek Rath. "Agent Drift: Quantifying Behavioral Degradation
  in Multi-Agent LLM Systems Over Extended Interactions."
  arXiv preprint arXiv:2601.04170, 2026.
Notes: 论文真实存在。当前 bib 缺 arXiv ID，author 只写了 "Rath and others"，
  标题也截断了（缺 "Over Extended Interactions"）。需补全。
BibTeX 修正建议:
  @article{rath2026agentdrift,
    title   = {Agent Drift: Quantifying Behavioral Degradation in Multi-Agent {LLM} Systems Over Extended Interactions},
    author  = {Abhishek Rath},
    journal = {arXiv preprint arXiv:2601.04170},
    year    = {2026},
  }
```

---

**Paper (d): Zhan et al. 2019**
```
Status: VERIFIED — ICLR 2019 确认
Full citation: Eric Zhan, Stephan Zheng, Yisong Yue, Long Sha, and Patrick Lucey.
  "Generating Multi-Agent Trajectories using Programmatic Weak Supervision."
  ICLR, 2019.
Notes: 当前 bib 条目完全正确，无需修改。OpenReview 确认为 ICLR 2019。
```

---

**总结**: 4 篇论文全部真实存在。Paper (a) 可补全期刊全称和 DOI；Paper (b) 需修正第一作者名；Paper (c) 需补全标题和 arXiv ID。Paper (d) 无误。

Sources:
- [Dawid & Skene 1979 – Wiley](https://rss.onlinelibrary.wiley.com/doi/abs/10.2307/2346806)
- [Dawid & Skene 1979 – JSTOR](https://www.jstor.org/stable/2346806?seq=1)
- [ProbGuard – arXiv](https://arxiv.org/abs/2508.00500)
- [Agent Drift – arXiv](https://arxiv.org/abs/2601.04170)
- [Zhan et al. 2019 – OpenReview (ICLR)](https://openreview.net/forum?id=rkxw-hAcFQ)
- [Zhan et al. 2019 – arXiv](https://arxiv.org/abs/1803.07612)

---
