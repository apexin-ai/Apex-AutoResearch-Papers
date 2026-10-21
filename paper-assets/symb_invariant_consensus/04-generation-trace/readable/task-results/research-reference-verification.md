# research reference verification

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference-verification_20260520T152426_result.json`
- **Structured JSON:** [`9b544b421de1296857b3.json`](../../sessions/9b/9b544b421de1296857b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 references verified. Here are the results:

---

## 1. CLOVER (Ryu et al., ICLR 2025) — ✅ 确认

- **完整标题**: Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning
- **作者**: Hyun Ryu, Gyeongman Kim, Hyemin S. Lee, Eunho Yang
- **Venue**: ICLR 2025
- **arXiv**: 2410.08047

```bibtex
@inproceedings{ryu2025clover,
  title={Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning},
  author={Ryu, Hyun and Kim, Gyeongman and Lee, Hyemin S. and Yang, Eunho},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2025}
}
```

---

## 2. VERGE (arXiv 2601.20055) — ✅ 确认

- **完整标题**: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning
- **作者**: Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, Sam Bayless
- **arXiv**: 2601.20055 (January 2026)

```bibtex
@article{singh2026verge,
  title={{VERGE}: Formal Refinement and Guidance Engine for Verifiable {LLM} Reasoning},
  author={Singh, Vikash and Cassel, Darion and Weir, Nathaniel and Feng, Nick and Bayless, Sam},
  journal={arXiv preprint arXiv:2601.20055},
  year={2026}
}
```

---

## 3. "Not All Votes Count! Programs as Verifiers..." — ⚠️ 作者有误

- **完整标题**: Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning
- **实际作者**: Vernon Y.H. Toh, Deepanway Ghosal, Soujanya Poria（**不是 Xia et al.**）
- **arXiv**: 2410.12608 (October 2024)

```bibtex
@article{toh2024notallvotes,
  title={Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning},
  author={Toh, Vernon Y.H. and Ghosal, Deepanway and Poria, Soujanya},
  journal={arXiv preprint arXiv:2410.12608},
  year={2024}
}
```

> **修正**: 论文中引用需从 `(Xia et al., 2024)` 改为 `(Toh et al., 2024)`。

---

## 4. "Logical Soundness is not a Reliable Criterion..." (arXiv 2604.04177) — ✅ 确认

- **完整标题**: Position: Logical Soundness is not a Reliable Criterion for Neurosymbolic Fact-Checking with LLMs
- **作者**: Jason Chan, Robert Gaizauskas, Zhixue Zhao
- **arXiv**: 2604.04177 (April 2026)

```bibtex
@article{chan2026position,
  title={Position: Logical Soundness is not a Reliable Criterion for Neurosymbolic Fact-Checking with {LLMs}},
  author={Chan, Jason and Gaizauskas, Robert and Zhao, Zhixue},
  journal={arXiv preprint arXiv:2604.04177},
  year={2026}
}
```

---

## 5. Lakens (2017) — ✅ 确认

- **完整标题**: Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses
- **作者**: Daniël Lakens
- **Venue**: Social Psychological and Personality Science, 8(4), 355–362
- **DOI**: 10.1177/1948550617697177

```bibtex
@article{lakens2017equivalence,
  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},
  author={Lakens, Dani{\"e}l},
  journal={Social Psychological and Personality Science},
  volume={8},
  number={4},
  pages={355--362},
  year={2017},
  doi={10.1177/1948550617697177}
}
```

---

## 汇总

| # | 引用 | 状态 | 问题 |
|---|------|------|------|
| 1 | CLOVER (Ryu et al., ICLR 2025) | ✅ | — |
| 2 | VERGE (arXiv 2601.20055) | ✅ | — |
| 3 | Not All Votes Count (~~Xia~~ Toh et al., 2024) | ⚠️ | 作者错误：应为 Toh et al. |
| 4 | Logical Soundness (arXiv 2604.04177) | ✅ | — |
| 5 | Lakens (2017) | ✅ | — |

**唯一需要修正的是 #3**：作者从 "Xia et al." 改为 "Toh et al."，正文中所有 cite 处同步更新。

---
