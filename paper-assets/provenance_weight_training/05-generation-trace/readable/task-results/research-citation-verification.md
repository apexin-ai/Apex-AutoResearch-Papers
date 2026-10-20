# research citation verification

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_verification_20260519T061904_result.json`
- **Structured JSON:** [`55e18d2521d4ba3c7f66.json`](../../sessions/55/55e18d2521d4ba3c7f66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 论文 1: Kang et al. (EMNLP 2025) [验证结果: CONFIRMED]
- 标题: Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls
- 作者: Feiyang Kang, Newsha Ardalani, Michael Kuchnik, Youssef Emad, Mostafa Elhoushi, Shubhabrata Sengupta, Shang-Wen Li, Ramya Raghavendra, Ruoxi Jia, Carole-Jean Wu
- Venue/arXiv: EMNLP 2025 (Main), pages 10739–10758; arXiv 2510.01631
- 年份: 2025
- 可公开获取: Yes
- BibTeX:
```bibtex
@inproceedings{kang-etal-2025-demystifying,
    title     = "Demystifying Synthetic Data in {LLM} Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls",
    author    = "Kang, Feiyang and Ardalani, Newsha and Kuchnik, Michael and Emad, Youssef and Elhoushi, Mostafa and Sengupta, Shubhabrata and Li, Shang-Wen and Raghavendra, Ramya and Jia, Ruoxi and Wu, Carole-Jean",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    month     = nov,
    year      = "2025",
    address   = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url       = "https://aclanthology.org/2025.emnlp-main.544/",
    doi       = "10.18653/v1/2025.emnlp-main.544",
    pages     = "10739--10758",
}
```

---

### 论文 2: "ForTIFAI" (arXiv 2509.08972) [验证结果: PARTIAL MATCH — 作者不符]
- 标题: ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse
- 作者: **Soheil Zibakhsh Shabgahi, Pedram Aghazadeh, Azalia Mirhoseini, Farinaz Koushanfar** ⚠️ 没有 Zhang，引用声称 "Zhang et al." 是错误的
- Venue/arXiv: arXiv 2509.08972 (v4, 2025-11-05)
- 年份: 2025
- 可公开获取: Yes
- BibTeX:
```bibtex
@article{zibakhshshabgahi2025fortifai,
    title   = "{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse",
    author  = "Zibakhsh Shabgahi, Soheil and Aghazadeh, Pedram and Mirhoseini, Azalia and Koushanfar, Farinaz",
    journal = "arXiv preprint arXiv:2509.08972",
    year    = "2025",
}
```
⚠️ **问题**: 引用中写 "Zhang et al." 但实际第一作者是 Zibakhsh Shabgahi。bib key 和 author 字段需要修正。

---

### 论文 3: Yi et al. (arXiv 2510.16657) [验证结果: CONFIRMED]
- 标题: Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence
- 作者: Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu
- Venue/arXiv: arXiv 2510.16657 (v2, 2026-03-05)
- 年份: 2025
- 可公开获取: Yes
- BibTeX:
```bibtex
@article{yi2025escaping,
    title   = "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence",
    author  = "Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng",
    journal = "arXiv preprint arXiv:2510.16657",
    year    = "2025",
}
```

---

### 论文 4: wang2026survive (arXiv 2602.16065) [验证结果: CONFIRMED]
- 标题: Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training
- 作者: Kevin Wang, Hongqian Niu, Didong Li
- Venue/arXiv: arXiv 2602.16065
- 年份: 2026
- 可公开获取: Yes
- BibTeX:
```bibtex
@article{wang2026survive,
    title   = "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training",
    author  = "Wang, Kevin and Niu, Hongqian and Li, Didong",
    journal = "arXiv preprint arXiv:2602.16065",
    year    = "2026",
}
```

---

**汇总**: 4 篇中 3 篇完全确认，1 篇（ForTIFAI）arXiv ID 和标题正确但作者归属错误（非 Zhang et al.），需修正 bib key 和 author 字段。

Sources:
- [ACL Anthology — Kang et al. 2025](https://aclanthology.org/2025.emnlp-main.544/)
- [arXiv 2509.08972 — ForTIFAI](https://arxiv.org/abs/2509.08972)
- [arXiv 2510.16657 — Yi et al.](https://arxiv.org/abs/2510.16657)
- [arXiv 2602.16065 — Wang et al.](https://arxiv.org/abs/2602.16065)

---
