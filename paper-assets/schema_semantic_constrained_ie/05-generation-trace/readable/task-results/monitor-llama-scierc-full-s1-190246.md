# monitor llama scierc full s1 190246

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_llama_scierc_full_s1_190246_20260514T143525_result.json`
- **Structured JSON:** [`9f8b7454edb5e9d01f14.json`](../../sessions/9f/9f8b7454edb5e9d01f14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## llama_scierc_full_s1 实验结果

| 指标 | Llama full_s1 | Llama unconstrained | Qwen3 full_s1 |
|------|:---:|:---:|:---:|
| **DR%** | **0.08%** | 13.3% | 0.93% |
| **RV%** | **0%** | 0.5% | 0% |
| **ET%** | **0%** | — | 0% |
| **CF%** | 6.56% | — | — |
| **E-F1** | 23.49% | 23.56% | **30.98%** |
| **R-F1** | 2.54% | 2.68% | **8.36%** |

**核心发现：**
- **约束合规性极好**：DR 从 unconstrained 的 13.3% 降到 0.08%，甚至优于 Qwen3 的 0.93%。仅 1 个 domain/range 违规（Compare 关系的 Task→Generic 对）。验证了 OntoCoDec 的 model-agnostic 特性。
- **抽取质量未受损也未提升**：E-F1 基本持平（23.49% vs 23.56%），R-F1 微降（2.54% vs 2.68%）。约束解决了合规性问题但没有改善 IE 能力。
- **Llama 显著弱于 Qwen**：E-F1 低 7.5pp，R-F1 低 5.8pp。Llama-3.1-8B 在 SciERC IE 任务上的基础能力明显不如 Qwen3-8B。
- **Cross-field consistency** 违规率 6.56%（162 例），主要是同一 mention 被标注为不同 entity type（如 Generic vs OtherScientificTerm）。

---
