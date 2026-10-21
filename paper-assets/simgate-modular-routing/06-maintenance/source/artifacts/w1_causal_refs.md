# Causal Inference References & Related Work Notes

## 1. Pearl (2009) — BibTeX

```bibtex
@book{pearl2009causality,
  title     = {Causality: Models, Reasoning, and Inference},
  author    = {Pearl, Judea},
  year      = {2009},
  edition   = {2nd},
  publisher = {Cambridge University Press},
  address   = {Cambridge, UK}
}
```

## 2. Rubin (1974) — BibTeX

```bibtex
@article{rubin1974estimating,
  title   = {Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies},
  author  = {Rubin, Donald B.},
  journal = {Journal of Educational Psychology},
  volume  = {66},
  number  = {5},
  pages   = {688--701},
  year    = {1974},
  publisher = {American Psychological Association}
}
```

## 3. "Check Yourself Before You Wreck Yourself" — 相关性判断

**论文信息**
- **标题**: Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety
- **作者**: Vamshi Krishna Bonagiri, Khanh Nguyen, Benjamin Plaut, Ponnurangam Kumaraguru
- **来源**: arXiv:2510.16492, NeurIPS 2025 Workshop (Reliable ML from Unreliable Data)

**判断: 高度相关。** 该论文提出 LLM agent 通过"主动退出"（quitting）机制避免灾难性失败，与 SimGate 的 modular routing（在高风险情形下将控制权路由到安全策略）在动机和机制上直接对应。SimGate 的 death-aware routing 本质上是一种结构化的 selective quitting — 当 router 检测到高死亡风险时，将 agent 路由到保守策略而非继续冒险。

**BibTeX**

```bibtex
@article{bonagiri2025check,
  title   = {Check Yourself Before You Wreck Yourself: Selectively Quitting Improves {LLM} Agent Safety},
  author  = {Bonagiri, Vamshi Krishna and Nguyen, Khanh and Plaut, Benjamin and Kumaraguru, Ponnurangam},
  journal = {arXiv preprint arXiv:2510.16492},
  year    = {2025}
}
```

**引用摘要**: Bonagiri et al. 证明 LLM agent 通过 prompted quitting 机制可在安全性上获得显著提升（+0.39/3.0），同时几乎不损失 helpfulness，表明 selective disengagement 是 agent 安全的高效策略。

## 4. Related Work 段落草稿（因果推断 + Agent Safety）

Our work draws on the causal inference framework to formalize the routing decision as an intervention problem. The potential outcomes framework \citep{rubin1974estimating} provides the theoretical basis for estimating counterfactual survival under alternative routing policies, while structural causal models \citep{pearl2009causality} enable us to reason about the causal mechanisms through which routing decisions affect episode outcomes. In the context of LLM agent safety, \citet{bonagiri2025check} recently demonstrated that prompting agents to selectively quit high-risk situations yields substantial safety improvements with negligible helpfulness loss; our modular routing approach extends this insight by replacing binary quit/continue decisions with a learned, fine-grained policy selector that routes agents to task-appropriate strategies based on predicted catastrophic failure risk.
