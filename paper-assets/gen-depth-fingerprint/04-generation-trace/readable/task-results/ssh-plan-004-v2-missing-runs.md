# ssh plan 004 v2 missing runs

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan-004-v2-missing-runs_20260515T024227_result.json`
- **Structured JSON:** [`77b54947dc3e134fd793.json`](../../sessions/77/77b54947dc3e134fd793.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 5 个补跑完成！all_seed456 也完成了！**

## Plan-004-v2 补跑结果汇总

| Variant | Seed | eval_loss | perplexity |
|---------|------|-----------|------------|
| depth0_only | 42 | 0.9865 | 2.6818 |
| depth0_only | 123 | 0.9863 | 2.6800 |
| depth0_only | 456 | 0.9865 | 2.6817 |
| depth01 | 42 | 0.8703 | 2.3877 |
| depth01 | 123 | 0.8700 | 2.3869 |

## 额外完成

**all_seed456**: eval_loss=0.8482, perplexity=2.3354

## 观察

- **depth0_only** 三个种子结果非常一致（perplexity ~2.68），方差极小
- **depth01** 两个种子也很一致（perplexity ~2.387），与之前已有的 seed=456 (perplexity=2.387) 完全吻合
- **all_seed456** (perplexity=2.335) 与前两个 all seeds（如果有的话）可做对比
- depth0_only 的 perplexity 明显高于 depth01 和 all，说明仅用 depth=0 数据训练效果确实较差

plan-014 (Qwen3-8B 生成) 进度 635/996 (~64%)，仍在 GPU 0 上运行。

---
