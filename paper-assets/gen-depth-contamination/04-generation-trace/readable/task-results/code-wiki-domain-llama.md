# code wiki domain llama

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wiki_domain_llama_20260524T094623_result.json`
- **Structured JSON:** [`5e9226c85862d1c5c968.json`](../../sessions/5e/5e9226c85862d1c5c968.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已完整，无需重新运行实验。汇报结果：

## LLaMA-3.1-8B Wikipedia Depth Chain 结果

**K\* = 1**（AUC > 0.60 的最大深度），与其他模型在 Wiki domain 的结果一致。

### Pairwise AUC（相邻深度）

| 对比 | AUC | 判定 |
|------|-----|------|
| depth 0 vs 1 | **0.932** ± 0.006 | 可区分 |
| depth 1 vs 2 | 0.595 ± 0.008 | 不可区分 |
| depth 2 vs 3 | 0.539 ± 0.011 | 不可区分 |
| depth 3 vs 4 | 0.522 ± 0.012 | 不可区分 |
| depth 4 vs 5 | 0.521 ± 0.013 | 不可区分 |

### Pairwise JSD

| 对比 | JSD |
|------|-----|
| 0 vs 1 | 0.0617 |
| 1 vs 2 | 0.0093 |
| 2 vs 3 | 0.0054 |
| 3 vs 4 | 0.0039 |
| 4 vs 5 | 0.0038 |

### Ordinal Classification（6-class）
- MAE = 1.30, Accuracy = 33.1%

### Top-5 Feature Importance
1. freq_entropy (8784)
2. surp_d1_skew (8168)
3. surp_mean (8129)
4. surp_d2_mean (7833)
5. surp_d1_mean (7816)

**结论**: LLaMA-3.1-8B 在 Wikipedia domain 的 K\*=1，与之前其他模型（Mistral、OLMo、Qwen、Pythia）的 Wiki 结果完全一致。depth 0→1 有强信号（AUC 0.93），之后迅速饱和至随机水平。LLaMA 现在有 3-domain profile：C4 K\*=2, arXiv K\*=3, Wiki K\*=1。

---
