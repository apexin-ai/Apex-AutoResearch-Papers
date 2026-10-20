# analysis eval 3B d100 s123 a32

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_3B_d100_s123_a32_20260516T033005_result.json`
- **Structured JSON:** [`98df8201027dfd272f94.json`](../../sessions/98/98df8201027dfd272f94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成（status=DONE, conclusion=success）。以下是结果汇总：

## exp_001_eval_3B_d100_s123_a32_batch 结果

| Benchmark | Aligned | Para-aligned | Δ (aligned−para) |
|-----------|---------|-------------|-------------------|
| **MMLU** | 0.6330 (8889/14042) | 0.6598 (4352/6596) | −0.027 |
| **GSM8K** | 0.7074 (933/1319) | 0.5746 (131/228) | **+0.133** |
| **ARC** | 0.8251 (967/1172) | 0.8049 (561/697) | +0.020 |
| HumanEval | 0.1159 (19/164) | 0.0000 (0/26) | +0.116 |

### 与已有 3B d100 数据对比

| | s42 α16 aligned | s123 α16 aligned | **s123 α32 aligned** | s42 α16 para | s123 α16 para | **s123 α32 para** |
|---|---|---|---|---|---|---|
| MMLU | 0.642 | 0.632 | **0.633** | 0.659 | 0.657 | **0.660** |
| GSM8K | 0.697 | 0.732 | **0.707** | 0.583 | 0.588 | **0.575** |
| ARC | 0.840 | 0.831 | **0.825** | 0.809 | 0.816 | **0.805** |
| HumanEval | 0.122 | 0.183 | **0.116** | 0.115 | 0.077 | **0.000** |

### 关键发现

1. **GSM8K 污染信号明确**：aligned (0.707) 远高于 d000 baseline (~0.18)，且 aligned−para Δ=+0.133 是最大的 benchmark gap
2. **α32 vs α16 差异不大**：核心 benchmark (MMLU/GSM8K/ARC) 差距均 <3pp，α32 略低但在 seed 方差范围内
3. **HumanEval para=0/26**：n 太小（仅 26 题），高方差，不影响整体结论
4. **无 OOM/crash**，eval 正常完成

---
