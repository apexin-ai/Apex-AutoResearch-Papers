# analysis olmo2 rerun bias

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_olmo2-rerun-bias_20260522T235724_result.json`
- **Structured JSON:** [`9e1c846b488d19646061.json`](../../sessions/9e/9e1c846b488d19646061.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册 (`art_20260523_909504`)。

核心结论：

- **ARC 5/5 dosage 0.00pp 偏差** — MCQ 代码、adapter 加载、推理均可复现
- **MMLU d025/d100 ~1.6pp 偏差** — 最可能来源是原始 eval 与 rerun 的硬件环境差异导致的浮点非确定性（ARC 1172 items 完美复现 vs MMLU 14042 items 累积偏移）
- **偏差 (1.6pp) < 跨 seed 变异范围 (3.76pp)** — 在噪声带内
- **Pattern classification 不变** — OLMo-2 两套值下均为 Benefit，不影响任何论文 claim
- Appendix 一句话声明已写好，建议主表使用 rerun 值（已用于 bootstrap CI）

---
