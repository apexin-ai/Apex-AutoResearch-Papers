# ssh merge strategy design

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_merge-strategy-design_20260515T120300_result.json`
- **Structured JSON:** [`d7850b7eba92b9c221b2.json`](../../sessions/d7/d7850b7eba92b9c221b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部语法通过。产出汇总：

### 已完成

| 产出 | 状态 | 文件 |
|------|------|------|
| **方案 C 实现** | ✅ 已完成+验证 | `src/sdgd/graph.py` (新增 `enforce_min_batch_size`) + `src/sdgd_decompose_cpu.py` (新增 `--min_batch_size` 参数) |
| **方案 A 骨架** | ✅ 函数可用 | `src/sdgd/merge.py` (新增 `merge_with_confidence`) |
| **方案 B+对比分析** | ✅ 文档 | `artifacts/exp008/merge_strategy_analysis.md` |
| **Dry-run 验证** | ✅ | `artifacts/exp008/decomposition_sdgd_zero_min8.json` |

### 方案 C Dry-run 关键数据

| | Before | After (min_batch_size=8) |
|---|--------|--------------------------|
| Batches | 8 | 4 |
| Sizes | [18,12,11,7,7,5,3,3] | [18,19,14,15] |
| Min batch | 3 | 14 |

灾难 batch 全部消除：旧 batch 6 (3 types, FP 86-90%) 和 batch 7 (3 types) 分别并入 14-type 和 15-type batch。Batch 数减半也意味着推理 cost 减半。

### 方案 A 使用方式
需要在 `sdgd_extract_gpu.py` 的 `SamplingParams` 中添加 `logprobs=1`，将 `output.outputs[0].cumulative_logprob / n_tokens` 作为 confidence 附加到每个 entity dict，然后 merge 阶段调用 `merge_with_confidence()` 替代 `merge_all_samples()`。

---
