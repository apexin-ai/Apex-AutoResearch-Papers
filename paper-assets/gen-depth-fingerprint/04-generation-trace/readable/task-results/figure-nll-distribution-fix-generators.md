# figure nll distribution fix generators

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_nll_distribution_fix_generators_20260520T185702_result.json`
- **Structured JSON:** [`a703db5ea65d68a81d6e.json`](../../sessions/a7/a703db5ea65d68a81d6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 修改内容
- `scripts/extract_token_nll.py` GENERATORS 字典：`"gemma-2-2b"` → `"qwen3-8b-base"`（路径 `data/qwen3-8b/generations_shard0.jsonl`）

### 新 median NLL（对比旧值）

| Depth | 旧 median | 新 median | 变化 |
|-------|-----------|-----------|------|
| 0 | 1.62 | **1.715** | +0.095 |
| 1 | 0.66 | **0.973** | +0.313 |
| 2 | 0.11 | **0.244** | +0.134 |
| 3 | 0.03 | **0.044** | +0.014 |
| 4 | 0.01 | **0.025** | +0.015 |

趋势不变（depth 越深 NLL 越低），但各 depth 的 median 均有所上升，qwen3-8b-base 比 gemma-2-2b 的 NLL 偏高。

### 输出文件
- `results/token_nll_by_depth.json` — 3.9MB
- `results/fig_appendix_nll_distribution.pdf` — 16KB
- `results/fig_appendix_nll_distribution.png` — 111KB

---
