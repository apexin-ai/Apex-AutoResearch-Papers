# code wiki domain mistral

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wiki_domain_mistral_20260524T094357_result.json`
- **Structured JSON:** [`53f54f7159bf0b96cc44.json`](../../sessions/53/53f54f7159bf0b96cc44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这个实验已经全部完成了。总结：

**Mistral-7B Wikipedia depth chain — 已有完整结果**

### 单模型结果 (`results/exp_wiki_mistral7b/`)
| Pair | AUC |
|------|-----|
| 0v1 | 0.9607 |
| 1v2 | 0.5552 |
| 2v3 | 0.5236 |
| 3v4 | 0.5181 |
| 4v5 | 0.5012 |
| **K\*** | **1** |

### Multi-source 结果 (`results/exp_wiki_multi_source/`)
- Generators: qwen1b5 + llama8b + mistral7b，Scorer: Qwen2.5-1.5B
- Unified scorer (no label): 0v1 AUC=0.9603, 1v2=0.5685 → **K\*=1**
- Unified scorer (with label): 0v1 AUC=0.9685, 1v2=0.5790 → **K\*=1**
- Vocab-only: K\*=1

Wiki K\*=1 已确认（scorer-controlled），与预期一致。Mistral domain profile 完整：**Wiki=1, C4=1, Code=2, arXiv=3**。

数据（5K docs × 6 depths）、features.csv、cross-scoring、bootstrap CI 全部齐全，无需重跑。

---
