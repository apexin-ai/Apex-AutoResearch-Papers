# research citation verification w11

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_verification_w11_20260520T155942_result.json`
- **Structured JSON:** [`1a987c1e953dfffbef12.json`](../../sessions/1a/1a987c1e953dfffbef12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 1. Wang et al. (ACL 2025) — attractor cycles in recursive generation
**✅ 真实存在**

"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing"

```bibtex
@inproceedings{wang-etal-2025-unveiling,
  title     = {Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing},
  author    = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = jul,
  year      = {2025},
  address   = {Vienna, Austria},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2025.acl-long.624/},
  pages     = {12740--12755}
}
```

---

### 2. Sun et al. (2026) — late-stage stability in iterative text generation
**✅ 真实存在**

"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection"

```bibtex
@article{sun2026settles,
  title   = {When {AI} Settles Down: Late-Stage Stability as a Signature of {AI}-Generated Text Detection},
  author  = {Sun, Ke and Bao, Guangsheng and Cui, Han and Zhang, Yue},
  journal = {arXiv preprint arXiv:2601.04833},
  year    = {2026},
  url     = {https://arxiv.org/abs/2601.04833}
}
```

注意：该论文的焦点是用 late-stage volatility decay 做**检测**，而非研究 iterative generation 本身的 stability。审稿人描述的 framing 略有偏差但论文确实存在。

---

### 3. Guo et al. (ICLR 2024) — iterative retraining stability / model collapse
**⚠️ 近似匹配（作者+会议张冠李戴）**

ICLR 2024 上关于 iterative retraining stability 的论文是 **Bertrand et al.**，不是 Guo：

> Quentin Bertrand, Avishek Joey Bose, Alexandre Duplessis, Marco Jiralerspong, Gauthier Gidel. "On the Stability of Iterative Retraining of Generative Models on their Own Data." ICLR 2024 (Spotlight).

确实存在一篇 **Guo et al.** 关于 iterative training 导致 linguistic diversity 下降的论文，但发表在 **Findings of NAACL 2024**，不是 ICLR：

> Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, Chloé Clavel. "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text." Findings of NAACL 2024.

**结论：审稿人将两篇论文的作者和会议混在一起了。**

---

### 4. Li et al. (2024) — self-consuming generative models
**❌ 不存在（审稿人幻觉）**

2024 年 self-consuming generative models 方向的主要论文：
- Alemohammad et al. "Self-Consuming Generative Models Go MAD" (ICLR 2024)
- Bertrand et al. "Self-Consuming Generative Models with Curated Data..." (NeurIPS 2024)
- Gillman et al. "Self-Correcting Self-Consuming Loops" (ICML 2024)
- Fu et al. "Towards Theoretical Understandings of Self-Consuming Generative Models" (ICML 2024)

**没有任何一篇以 "Li" 为第一作者。** 搜索了 Google Scholar、Semantic Scholar、arXiv，包括不同关键词组合，均未找到匹配论文。

---

### 5. Zhang et al. (2024) — MMD-based AI text detection
**✅ 真实存在**

"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy"

```bibtex
@inproceedings{zhang2024detecting,
  title     = {Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy},
  author    = {Zhang, Shuhai and Song, Yiliao and Yang, Jiahao and Li, Yuanqing and Han, Bo and Tan, Mingkui},
  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},
  year      = {2024},
  url       = {https://openreview.net/forum?id=3fEKavFsnv}
}
```

---

### 6. Weng et al. (2025) — knowledge attribution in LLMs
**❌ 不存在（审稿人幻觉）**

搜索范围：Google Scholar、arXiv、ACL Anthology、NAACL/ACL/EMNLP/AAAI 2025 accepted papers。Yixuan Weng 在 CIKM 2024 有一篇 knowledge localization 相关论文（"Does Knowledge Localization Hold True?"），但主题是 entity vs relation knowledge，不是 knowledge attribution，且年份不符。2025 年 knowledge attribution 相关论文的第一作者均非 Weng。

---

### 汇总

| # | 引用 | 状态 | 说明 |
|---|------|------|------|
| 1 | Wang et al. (ACL 2025) | ✅ 真实 | attractor cycles，完全匹配 |
| 2 | Sun et al. (2026) | ✅ 真实 | late-stage stability，arXiv preprint |
| 3 | Guo et al. (ICLR 2024) | ⚠️ 张冠李戴 | ICLR 2024 是 Bertrand et al.；Guo et al. 在 NAACL 2024 |
| 4 | Li et al. (2024) | ❌ 幻觉 | 无此论文 |
| 5 | Zhang et al. (2024) | ✅ 真实 | MMD-MP，ICLR 2024 |
| 6 | Weng et al. (2025) | ❌ 幻觉 | 无此论文 |

Sources:
- [Wang et al. ACL 2025](https://aclanthology.org/2025.acl-long.624/)
- [Sun et al. 2026](https://arxiv.org/abs/2601.04833)
- [Bertrand et al. ICLR 2024](https://openreview.net/forum?id=JORAfH2xFd)
- [Guo et al. NAACL 2024](https://aclanthology.org/2024.findings-naacl.228/)
- [Zhang et al. ICLR 2024](https://openreview.net/forum?id=3fEKavFsnv)
- [Yixuan Weng ACL Anthology](https://aclanthology.org/people/yixuan-weng/)

---
