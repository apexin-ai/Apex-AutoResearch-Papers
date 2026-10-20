# analysis n1a answer region ii

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n1a_answer_region_ii_20260515T125432_result.json`
- **Structured JSON:** [`e5c169a13bed37480fc6.json`](../../sessions/e5/e5c169a13bed37480fc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**16/16 条件下，answer-region 的 compound degradation 均显著低于 reasoning-region**（所有 p < 1e-60，Cohen's d = −1.2 到 −20.7）。

机制：
- Answer tokens（`\boxed{...}` 区域）的 attention sparsity 显著高于 reasoning tokens（DeepSeek: 0.856 vs 0.711; Qwen: 0.940 vs 0.884）
- 87-98% 的 answer tokens 落在 **high_sparsity phase**，该 phase 的 compound PPL 放大仅 1.2-3.0x
- 而 low_sparsity phase（高 II 区）的 PPL 放大高达 8-83x，但 answer tokens 几乎不在此 phase（<2%）

**对审稿人的回应**：高 II 值集中在中间推理阶段的 low-sparsity tokens，而最终答案计算区域因 attention 天然聚焦（高 sparsity），compound interaction 影响极小。PPL-based II 不直接转化为 accuracy loss——answer tokens 被其注意力模式"自然屏蔽"。

交付物：
- 报告：`artifacts/n1a_answer_region/report.md`
- JSON 数据：服务器 `analysis_output/n1a_answer_region_analysis.json`
- 分析脚本：服务器 `n1a_answer_region_analysis.py`

---
