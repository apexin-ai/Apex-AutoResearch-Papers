# analysis bootstrap ci v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci-v2_20260515T084115_result.json`
- **Structured JSON:** [`cf6fd8d3bdf6cff5cc23.json`](../../sessions/cf/cf6fd8d3bdf6cff5cc23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修正内容：**
- 原 `bootstrap_ci_6gen.py` 缺少训练集 downsample（类别平衡），导致 per-generator F1 偏差达 2.8pp
- 新脚本 `bootstrap_ci_v2.py` 加入 downsample，与 registry 评估流程一致，所有 per-generator 偏差 ≤ 0.32pp
- 结果已保存到服务器 `/root/gen-depth-fingerprint/results/bootstrap_ci_v2_results.json`
- 论文 Table 1 CI 列和正文 Qwen3-8B CI 引用已更新，point estimates 不变

---
