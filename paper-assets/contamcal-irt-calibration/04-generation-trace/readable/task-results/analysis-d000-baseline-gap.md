# analysis d000 baseline gap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d000_baseline_gap_20260514T205159_result.json`
- **Structured JSON:** [`bd9cb066d40ff2a959e0.json`](../../sessions/bd/bd9cb066d40ff2a959e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### MMLU item-aligned d000 baseline gap

| 模型 | d000 orig (aligned) | d000 para | d000 gap | d100 gap (已知) | delta-of-deltas |
|------|---------------------|-----------|----------|-----------------|-----------------|
| 1.5B | 58.78% | 60.96% | **-2.18pp** | -2.90pp | **-0.72pp** |
| 3B   | N/A | N/A | N/A | -3.50pp | pending |

**关键发现**：
- d000（无 contamination）已经有 -2.18pp 的 gap，即 paraphrase 本身就比 original 更容易
- d100 的 gap 是 -2.90pp，delta-of-deltas 仅 -0.72pp（< 1pp）
- **结论**：negative gap 主要是 paraphrase 本身的常数偏移（paraphrase 更容易），contamination 仅额外贡献约 0.72pp，效应很小

3B d000 的 para_aligned eval 结果不存在（`Qwen2.5-3B_d000_s42_para_aligned` 目录缺失），需要先跑 3B d000 的 paraphrase eval 才能计算。

---
