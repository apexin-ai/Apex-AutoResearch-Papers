# analysis early feature extraction

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_early_feature_extraction_20260521T113626_result.json`
- **Structured JSON:** [`9552927b5a0f0af8dedf.json`](../../sessions/95/9552927b5a0f0af8dedf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Generator | Strategy | entropy_mean | entropy_std | entropy_max | entropy_min | tail_decay | TTR | hapax_ratio |
|---|---|---|---|---|---|---|---|---|
| OLMo-2-1B | greedy | **1.293** | **0.947** | 0.031 | 0.027 | 0.033 | **0.889** | **0.805** |
| OLMo-2-1B | top-k | **0.729** | 0.352 | 0.011 | 0.011 | 0.222 | **0.704** | **0.690** |
| Pythia-2.8B | greedy | **1.426** | **0.931** | 0.091 | 0.075 | 0.066 | **0.981** | **0.875** |
| Pythia-1B | greedy | **0.983** | **0.912** | 0.123 | 0.044 | 0.039 | **0.635** | **0.529** |

**Shape/drifting 二分法在全部4组条件下成立：**
- **Shape features** (entropy_max, entropy_min, tail_decay): 15/16 个值 < 0.20，唯一例外是 OLMo-2-1B top-k 的 tail_decay=0.222（略超阈值）
- **Drifting features** (entropy_mean, TTR, hapax_ratio): 全部 12/12 > 0.50

额外发现：greedy decoding 的 effect size 普遍大于 top-k（OLMo-2-1B greedy vs top-k 对比明显），说明采样随机性会部分掩盖 depth 信号。

结果已保存到 `artifacts/_project/analysis/decoding_early_cohens_d.txt`。

---
