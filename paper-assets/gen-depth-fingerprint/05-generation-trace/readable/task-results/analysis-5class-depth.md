# analysis 5class depth

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_5class-depth_20260515T073414_result.json`
- **Structured JSON:** [`cf06d1bbe88448e2285a.json`](../../sessions/cf/cf06d1bbe88448e2285a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**5-class LOGO 结果（已从服务器现有 `multi_classify_results.json` 提取）：**

| Held-out Generator | Macro F1 |
|---|---|
| OLMo-2-1B | 0.498 |
| Pythia-1B | 0.552 |
| Pythia-2.8B | 0.527 |
| Qwen3-0.6B | 0.506 |
| Qwen3-1.7B | 0.519 |
| Qwen3-8B | 0.437 |
| **Average** | **0.507 +/- 0.036** |

**Per-class F1：** gen-0=0.936, gen-1=0.635, gen-2=0.276, gen-3=0.261, gen-4=0.425

**vs 3-class：** F1 从 0.789 降到 0.507（-0.282），主要因为 gen-2/gen-3 几乎不可分（相邻深度混淆率 >35%）。

已写入：
- `appendix_finer_depth.tex` — 含两张表格 + 分析段落
- `main.tex` — 在 `appendix_prompt_type` 之后添加了 `\section{Finer-Grained Depth Classification}`

---
