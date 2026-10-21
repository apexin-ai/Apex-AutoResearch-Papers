# read arxiv multi source results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_arxiv_multi_source_results_20260520T084450_result.json`
- **Structured JSON:** [`9fb50e55fd528a9b5e8a.json`](../../sessions/9f/9fb50e55fd528a9b5e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## arXiv Multi-Source 实验结果

**设置**: 域=arXiv, scorer=Qwen2.5-1.5B, generators=[qwen1b5, pythia1b4, llama8b], 1000 docs/generator, θ=0.6

### AUC 汇总

| Pair | Vocab-only (no label) | Vocab-only (with label) | Unified (no label) | Unified (with label) |
|------|----------------------|------------------------|--------------------|--------------------|
| 0v1 | 0.9431 | 0.9436 | 0.9899 | **0.9911** |
| 1v2 | 0.6922 | 0.7020 | 0.8117 | **0.8338** |
| 2v3 | 0.5890 | 0.5883 | 0.6247 | **0.6276** |
| 3v4 | 0.5082 | 0.5077 | 0.5269 | **0.5330** |
| 4v5 | 0.5176 | 0.5163 | 0.5321 | **0.5359** |

### K* 结果

| 方法 | K* |
|------|-----|
| Vocab-only (no label) | **2** |
| Vocab-only (with label) | **2** |
| Unified scorer (no label) | **3** |
| Unified scorer (with label) | **3** |

### C4 对比参考

C4 域下所有三种方法的 K* 均为 **2**。

**关键发现**: Unified scorer 在 arXiv 域上 K*=3，比 vocab-only 的 K*=2 多探测一代，且 AUC 全面高于 vocab-only（尤其 1v2: 0.83 vs 0.70）。with_label 变体带来微弱但一致的提升。

---
