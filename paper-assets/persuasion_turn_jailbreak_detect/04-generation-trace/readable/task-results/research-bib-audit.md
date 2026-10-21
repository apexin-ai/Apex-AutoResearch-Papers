# research bib audit

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bib-audit_20260521T214527_result.json`
- **Structured JSON:** [`908f9f7fe3e7d115eccf.json`](../../sessions/90/908f9f7fe3e7d115eccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All searches complete. Here's the compiled report.

## Part 1: 新增引用

### zhang2021understanding
```bibtex
@article{zhang2021understanding,
  title={Understanding Deep Learning (Still) Requires Rethinking Generalization},
  author={Zhang, Chiyuan and Bengio, Samy and Hardt, Moritz and Recht, Benjamin and Vinyals, Oriol},
  journal={Communications of the ACM},
  volume={64},
  number={3},
  pages={107--115},
  year={2021},
  doi={10.1145/3446776},
}
```

### maennel2020random
```bibtex
@inproceedings{maennel2020random,
  title={What Do Neural Networks Learn When Trained With Random Labels?},
  author={Maennel, Hartmut and Alabdulmohsin, Ibrahim M. and Tolstikhin, Ilya O. and Baldock, Robert J. N. and Bousquet, Olivier and Gelly, Sylvain and Keysers, Daniel},
  booktitle={Advances in Neural Information Processing Systems},
  year={2020},
}
```

### kang2018...
**未找到。** 多次搜索（关键词组合：Kang, Shin, 2018, random labels, memorization, neural networks）均无匹配结果。该领域 2018 年前后的相关论文主要是 Zhang et al. 2017 (ICLR) 和 Arpit et al. 2017 (ICML "A Closer Look at Memorization in Deep Networks")，均非 Kang & Shin 所著。建议确认论文标题或作者拼写。

## Part 2: 引用审计

**1. Austin 1962**: 正确，保留即可 — 1962 年初版（Harvard UP, posthumous, ed. by J.O. Urmson）是学术界最常引用的版本年份。1975 是 Urmson & Sbisà 编辑的第二版。绝大多数 NLP/语言学文献引用 1962。

**2. Cialdini 2001**: 正确 — 2001 4th edition (Allyn & Bacon) 是学术引用中最常见的版本之一。无需更换。如需引用最新研究可考虑 2021 新版，但 2001 4th ed 在现有文献中被广泛接受。

**3. Russinovich et al. (key=2024, year=2025)**: **正确** — 确认发表于 34th USENIX Security Symposium (USENIX Security '25), August 2025, Seattle, WA。key 保留 2024 的做法已有注释说明。

**4. Chao et al. PAIR (key=chao2023pair, year=2024)**: **需修改** — 多个来源（Semantic Scholar、ResearchGate、SaTML 2025 官方 Program 页面）确认该论文发表于 **SaTML 2025**（IEEE Conference on Secure and Trustworthy Machine Learning 2025），而非 2024。应将 `year={2024}` 改为 `year={2025}`。

**5. Hagendorff et al. 2026**: **正确但不完整** — 确认发表于 Nature Communications 17, 1435 (2026), DOI: 10.1038/s41467-026-69010-1。建议补充 volume/article number/DOI：
```
  volume={17},
  pages={1435},
  doi={10.1038/s41467-026-69010-1},
```

**6. Stolcke et al. 2000**: **正确** — Computational Linguistics 26(3):339–374, 2000。年份、期刊、卷号、页码全部匹配。

**7. Mann & Thompson 1988**: **正确** — Text & Talk (原名 Text) 8(3):243–281, 1988。DOI: 10.1515/text.1.1988.8.3.243。使用现代期刊名 "Text & Talk" 可接受。

**8. Prasad et al. 2008 PDTB**: **正确** — LREC 2008 (Marrakech, Morocco)。作者列表与官方记录一致。

**9. Howard & Ruder 2018 ULMFiT**: **正确** — ACL 2018, pages 328–339。DOI: 10.18653/v1/P18-1031。完全匹配。

**10. 其余条目汇总**: 逐一浏览了全部 31+ 个条目，未发现明显错误。注意事项：
- `andriushchenko2024adaptive`: key=2024 但 year=2025 (ICLR 2025)，与 Russinovich 同样模式，可接受。
- `ren2024actorattack`: 同上模式 (ICLR 2025)。
- 多个 arXiv preprint 条目无页码/卷号，这对 preprint 是正常的。
- `zou2023gcg`: 该论文后来被 ICML 2024 接收，当前标注为 arXiv 2023。如需更新可改为 ICML 2024 venue。

Sources:
- [Zhang et al. 2021 CACM](https://dl.acm.org/doi/10.1145/3446776)
- [Maennel et al. NeurIPS 2020](https://papers.nips.cc/paper/2020/hash/e4191d610537305de1d294adb121b513-Abstract.html)
- [Austin - How to Do Things with Words (Wikipedia)](https://en.wikipedia.org/wiki/How_to_Do_Things_with_Words)
- [Cialdini 2001 4th ed citation](https://www.scirp.org/reference/referencespapers?referenceid=539955)
- [Russinovich et al. USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/russinovich)
- [Chao et al. PAIR - Semantic Scholar](https://www.semanticscholar.org/paper/Jailbreaking-Black-Box-Large-Language-Models-in-Chao-Robey/4637f79ddfaf923ce569996ffa5b6cda1996faa1)
- [Hagendorff et al. Nature Communications 2026](https://www.nature.com/articles/s41467-026-69010-1)
- [Stolcke et al. 2000 - MIT Press](https://direct.mit.edu/coli/article/26/3/339/1648/Dialogue-Act-Modeling-for-Automatic-Tagging-and)
- [Mann & Thompson 1988 - De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/text.1.1988.8.3.243/html)
- [Prasad et al. 2008 - ACL Anthology](https://aclanthology.org/L08-1093/)
- [Howard & Ruder 2018 - ACL Anthology](https://aclanthology.org/P18-1031/)

---
