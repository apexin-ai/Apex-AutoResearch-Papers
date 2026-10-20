# experiment dir i2 single model baselines

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-i2-single-model-baselines_20260520T172102_result.json`
- **Structured JSON:** [`22d7f04cc0b8d1f6e76d.json`](../../sessions/22/22d7f04cc0b8d1f6e76d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。关键发现：

| 模型 | SC@all | SC@5 (mean±std) |
|------|--------|-----------------|
| mistral-7b | 111/204 = **54.41%** | 56.03% ± 2.13% |
| qwen2.5-7b | 157/204 = **76.96%** | 74.41% ± 1.29% |
| qwen2.5-14b | 153/204 = **75.00%** | 75.64% ± 0.76% |
| qwen3-14b | 171/204 = **83.82%** | 82.64% ± 0.91% |

**结论：HGE-(b) 82.01% 存在 confound。**

Qwen3-14B 单模型 SC@all 已达 83.82%，**高于** HGE-(b) 的 82.01%（差值 -1.81 pp）。这意味着 HGE 的跨模型 ensemble 不仅没有带来增益，反而因为混入了较弱模型（Mistral 54%、Qwen2.5-7B 77%）而**拉低**了最强单模型的表现。HGE gain 并非来自 ensemble diversity，而是被最强模型 Qwen3-14B 所主导。

---
