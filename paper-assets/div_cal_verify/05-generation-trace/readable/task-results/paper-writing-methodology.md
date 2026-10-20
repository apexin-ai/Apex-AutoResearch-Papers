# paper writing methodology

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_methodology_20260513T185410_result.json`
- **Structured JSON:** [`aafd45988539d7689af6.json`](../../sessions/aa/aafd45988539d7689af6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Methodology section 写入 `docs/paper/methodology.tex`，已注册为 artifact。

内容概要：
- **3.1 Base Model and Dataset**: GPT2-125M + WikiText-103，说明选择理由
- **3.2 Self-Training Protocol**: 8 代迭代，500K tokens/代，累积微调，完整超参数
- **3.3 Data Selection Methods**: 4 种方法（Uncurated/RGDS/External-only/Random 50%）+ 对照逻辑的 factorial ablation 结构
- **3.4 Selection Ratio**: SR 公式定义、三种解释（>1, <1, ≈1）、rare trigram 定义
- **3.5 Evaluation Metrics**: PPL, rare n-gram ratio, Distinct-n, Self-BLEU, RankMe, k-NN probe
- **3.6 Reproducibility**: 3 seeds，共享 checkpoint 和数据池

待处理：Contriever 引用标记为 `[CITATION NEEDED: Izacard et al. 2022 Contriever]`，需补充 bib 条目。

---
