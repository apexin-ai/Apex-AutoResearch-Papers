# paper fix rlsf bib

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-rlsf-bib_20260521T065002_result.json`
- **Structured JSON:** [`a78f9f6364a6e27f5d4e.json`](../../sessions/a7/a78f9f6364a6e27f5d4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。Diff 如下：

**`docs/paper/references.bib`**（标题修正，作者原本已正确）：
```diff
-  title        = {{RLSF: Reinforcement Learning via Symbolic Feedback}},
+  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},
```

**`paper/references.bib`**（同步后，作者和标题均已修正）：
```diff
-  author       = {Abhinav Jha and Shikhar Murty and J. Zico Kolter and others},
-  title        = {{Reinforcement Learning via Symbolic Feedback}},
+  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},
+  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},
```

编译通过，无新 warning（仅有既存的 hyperref Unicode token 警告）。

Sources:
- [arXiv:2405.16661 - RLSF: Fine-tuning LLMs via Symbolic Feedback](https://arxiv.org/abs/2405.16661)
- [Semantic Scholar - RLSF](https://www.semanticscholar.org/paper/RLSF:-Fine-tuning-LLMs-via-Symbolic-Feedback-Jha-Jana/be992d914389d9e4462df1911e6ede7645b66f86)

---
