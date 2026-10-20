# research missing references

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_missing-references_20260518T050823_result.json`
- **Structured JSON:** [`a8795b568259feb8207a.json`](../../sessions/a8/a8795b568259feb8207a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All searches complete. Here are the results:

---

## 1. Webb 2023 — Wild Cluster Bootstrap

```bibtex
@article{webb2023reworking,
  author    = {Matthew D. Webb},
  title     = {Reworking Wild Bootstrap-Based Inference for Clustered Errors},
  journal   = {Canadian Journal of Economics/Revue canadienne d'\'{e}conomique},
  year      = {2023},
  volume    = {56},
  number    = {3},
  pages     = {839--858},
  doi       = {10.1111/caje.12661},
  url       = {https://onlinelibrary.wiley.com/doi/10.1111/caje.12661}
}
```

---

## 2. Permadeath LLM Agent Literature

### BALROG (ICLR 2025)

```bibtex
@inproceedings{paglieri2025balrog,
  author    = {Davide Paglieri and Bart{\l}omiej Cupia{\l} and Samuel Coward and Ulyana Piterbarg and Maciej Wolczyk and Akbir Khan and Eduardo Pignatelli and {\L}ukasz Kuci\'{n}ski and Lerrel Pinto and Rob Fergus and Jakob Nicolaus Foerster and Jack Parker-Holder and Tim Rockt\"{a}schel},
  title     = {{BALROG}: Benchmarking Agentic {LLM} and {VLM} Reasoning On Games},
  booktitle = {The Thirteenth International Conference on Learning Representations (ICLR)},
  year      = {2025},
  url       = {https://arxiv.org/abs/2411.13543}
}
```

### NetPlay (IEEE CoG 2024)

```bibtex
@inproceedings{jeurissen2024netplay,
  author    = {Dominik Jeurissen and Diego Perez-Liebana and Jeremy Gow and Duygu Cakmak and James Kwan},
  title     = {Playing {NetHack} with {LLMs}: Potential \& Limitations as Zero-Shot Agents},
  booktitle = {2024 IEEE Conference on Games (CoG)},
  year      = {2024},
  url       = {https://arxiv.org/abs/2403.00690},
  doi       = {10.1109/CoG60054.2024.10645630}
}
```

### "Can LLMs Play NetHack Yet?" (2026)

**不是正式论文。** 这是一篇博客文章："It's 2026. Can LLMs Play Nethack Yet?" 发表在 "Vaguely Aligned" 博客上（作者 Ken），测试了新模型在 NetHack 上的表现（GPT-5.2 最高到 dungeon level 10，BALROG metric 12.56%）。不建议作为学术引用。如果需要 2026 的 NetHack agent 文献，目前没有找到正式发表的论文。

---

## 3. Safety-Aware Routing Literature

### SafeRoute (ACL Findings 2025) — 最直接匹配

```bibtex
@inproceedings{lee2025saferoute,
  author    = {Seanie Lee and Dong Bok Lee and Dominik Wagner and Minki Kang and Haebin Seong and Tobias Bocklet and Juho Lee and Sung Ju Hwang},
  title     = {{SafeRoute}: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
  year      = {2025},
  pages     = {2053--2069},
  address   = {Vienna, Austria},
  url       = {https://arxiv.org/abs/2502.12464}
}
```

这是最精确匹配 "safety-aware routing" 概念的论文：用二分类 router 区分 easy/hard 样本，将 hard 样本路由到更大的 safety guard 模型，实现效率与安全性的平衡。

### 备选：Sparse Models, Sparse Safety (arXiv 2025, ICLR 2026 投稿)

```bibtex
@article{jiang2025sparse,
  author    = {Yukun Jiang and Hai Huang and Mingjie Li and Yage Zhang and Michael Backes and Yang Zhang},
  title     = {Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts {LLMs}},
  journal   = {arXiv preprint arXiv:2602.08621},
  year      = {2025},
  url       = {https://arxiv.org/abs/2602.08621}
}
```

这篇从 MoE routing 角度研究 safety：发现特定 routing 配置会导致模型产出有害内容。角度不同但相关——如果论文需要的是 "在 model routing 决策中显式考虑 safety 因素"，SafeRoute 更合适；如果需要的是 "routing 机制本身的 safety 风险"，这篇更合适。

---

**不确定之处：**
- "Can LLMs Play NetHack Yet?" 没有找到 2025/2026 的正式论文，只有博客
- Safety-aware routing 是相对新的交叉方向，SafeRoute 是目前找到的最直接匹配，但它偏 guardrail model selection 而非 general LLM routing with safety constraints。如果 Paper Agent 需要的是另一种 framing，请补充上下文

---
