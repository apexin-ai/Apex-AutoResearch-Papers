# research bib verify shi2024

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bib-verify-shi2024_20260523T123030_result.json`
- **Structured JSON:** [`d9fc01aef076b0cac065.json`](../../sessions/d9/d9fc01aef076b0cac065.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核实完成。以下是对比结果：

### arXiv:2402.14016 真实信息

- **标题**: Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment
- **作者**: Vyas Raina, Adian Liusie, Mark Gales
- **年份**: 2024

### 当前 bib 条目问题

`shi2024judgerobust` 条目存在 **严重错误**：

| 字段 | 当前 bib 值 | 正确值 |
|------|-----------|--------|
| author | Kaijie Shi, Fuwen Luo, Yew Ken Chia, Lidong Bing | **Vyas Raina, Adian Liusie, Mark Gales** |
| title | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | **Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment** |

作者和标题完全错误，是另一篇论文的信息被错误关联到了这个 arXiv ID。

### 修正后的完整 bib 条目

```bibtex
@article{raina2024judgerobust,
  author    = {Vyas Raina and Adian Liusie and Mark Gales},
  title     = {Is {LLM}-as-a-Judge Robust? {Investigating} Universal Adversarial Attacks on Zero-shot {LLM} Assessment},
  journal   = {arXiv preprint arXiv:2402.14016},
  year      = {2024},
  url       = {https://arxiv.org/abs/2402.14016},
  note      = {arXiv:2402.14016}
}
```

注意 cite key 也应从 `shi2024judgerobust` 改为 `raina2024judgerobust`，需同步更新所有 `.tex` 文件中的 `\cite{shi2024judgerobust}` 引用。是否需要我直接修改？

Sources:
- [arXiv:2402.14016](https://arxiv.org/abs/2402.14016)

---
