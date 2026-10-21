# code llama rp10 filter and extract

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-rp10-filter-and-extract_20260516T113203_result.json`
- **Structured JSON:** [`314e6f08510a5bb1f158.json`](../../sessions/31/314e6f08510a5bb1f158.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

## Phase 1: Soft Filter 结果

| Depth | 原始 | 过滤后 | 移除数 | 比例 |
|-------|------|--------|--------|------|
| 0 | 995 | 995 | 0 | 0.0% |
| 1 | 984 | 872 | 112 | 11.4% |
| 2 | 943 | 533 | 410 | 43.5% |
| 3 | 899 | 315 | 584 | 65.0% |
| 4 | 859 | 222 | 637 | 74.2% |
| **Total** | **4680** | **2937** | **1743** | **37.2%** |

退化比例随 depth 单调递增，符合预期。

## Phase 2: 3-ref 特征提取

全部完成，每个文件 2937 条记录：
- `features_pythia410m.jsonl` (90th NLL threshold: 6.17)
- `features_olmo2-1b.jsonl` (90th NLL threshold: 5.33)
- `features_qwen3-06b.jsonl` (90th NLL threshold: 6.02)

字段：seed_id, depth, entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio

## 使用脚本

- **新建**：`llama_filter_and_extract.py`（基于已有 `extract_features.py` 的特征计算逻辑，新增 soft filter + 多 ref model 支持 + task 指定的 tail_decay 定义）
- 总耗时约 60s（5090 GPU 上 Pythia 18s + OLMo ~20s + Qwen ~20s）

---
