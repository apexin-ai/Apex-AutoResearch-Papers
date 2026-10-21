# check llama3b adaptive completion

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama3b_adaptive_completion_20260517T135031_result.json`
- **Structured JSON:** [`da9e0c6e0709e4636a8d.json`](../../sessions/da/da9e0c6e0709e4636a8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

**llama3b_adaptive_seed42 训练正常完成。**

| 项目 | 结果 |
|---|---|
| 完成步数 | 6103/6103 (100%) |
| Final model | `/root/autodl-tmp/provenance_weight_training/output/models/llama3b_adaptive_seed42/final` |
| **Adaptive PPL** | **10.58** |
| Uniform baseline PPL | 10.38 |
| **差异** | **+0.20（adaptive 更差）** |
| cuda:1 | 空闲（eval 进程已退出） |

**关键发现：Adaptive weighting 在 Llama-3.2-3B 上 PPL 比 uniform 高 0.20，未能复现在 GPT-2 上的优势。** 跨模型泛化假设被否定——adaptive 方法的收益可能依赖于模型架构或规模。

Registry 已更新为 DONE (conclusion=success，指训练成功完成，但 PPL 结果表明假设被否定)。

---
