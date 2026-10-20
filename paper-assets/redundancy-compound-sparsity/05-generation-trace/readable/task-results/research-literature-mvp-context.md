# research literature mvp context

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-mvp-context_20260511T224539_result.json`
- **Structured JSON:** [`1dd1385a0358a5019f16.json`](../../sessions/1d/1dd1385a0358a5019f16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已创建：

**`literature_map.yaml`** — 6 个类别，共 24 篇论文：
- **direct-competitor** (4): DejaVu, PowerInfer, TurboSparse, MInference
- **kv-eviction** (5): H2O, SnapKV, PyramidKV, StreamingLLM, KIVI
- **activation-sparsity** (4): ReLUfication, CATS, ProSparse, TEAL
- **cross-axis** (4): Mixture-of-Depths, LayerSkip, ShortGPT, Not All Tokens Are What You Need
- **redundancy-signal** (4): Token Merging, FastV, Pause Tokens, Scissorhands
- **evaluation** (4): MATH, GSM8K, MMLU, LongBench

所有论文标注 `verified: false`，每篇包含 `relation_to_carc` 说明与本项目的定位关系。

**`experiment_plan.yaml`** — 14 个实验，分三级优先级：
- **P0** (1): mvp-001（已在 registry，PREPARING）
- **P1** (8): scale-14b, cross-arch-llama, composability-matrix, conditioned-r2, reasoning-phase-profile, downstream-accuracy, kv-eviction-standalone, wallclock-speedup
- **P2** (5): ablation-ema, ablation-similarity-metric, scale-32b, long-context-eval

覆盖 Strong 路径（跨轴 narrative 全链条）和 Suggestive 路径（downstream utility + KV eviction 为主证据）。包含依赖 DAG 和 14 天 timeline mapping。

---
