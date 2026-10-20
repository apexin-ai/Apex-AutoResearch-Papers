# analysis cegis full results and phase2 check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cegis-full-results-and-phase2-check_20260520T085652_result.json`
- **Structured JSON:** [`d8f30ae83b78e4d28419.json`](../../sessions/d8/d8f30ae83b78e4d28419.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. CEGIS 完整结果 (204/204) — westd-16639 ✅

`results.json` 包含全部 204 题，实验已完成（无 CEGIS 进程运行）。

| | Accuracy | Correct | Delta vs SC |
|---|---|---|---|
| **SC baseline** | 54.41% | 111/204 | — |
| **R1 (CEGIS)** | 57.84% | 118/204 | **+3.43pp** |
| **R2** | 57.35% | 117/204 | +2.94pp |
| **R3** | 57.84% | 118/204 | +3.43pp |

UNSAT 衰减：R1 127 traces (5.19%) → R2 48 (1.96%) → R3 25 (1.02%)
Wall time: ~51 min, Extraction calls: 2448, Refinement calls: 175

**与部分结果 (90题) 的对比：**
- 90题时：R1 +2.4pp，R2/R3 无改善
- 204题时：R1 +3.43pp，R2 +2.94pp，R3 +3.43pp
- **饱和模式改变**：R2/R3 从零增益恢复到 +2.94/+3.43pp，R1 增益也从 +2.4pp 提升到 +3.43pp。更多数据点让 CEGIS refinement 的效果更稳定了。

⚠️ `aggregated_results.json` 是中间产物（仅 125 题），以 `results.json` 为准。

---

### 2. Cross-model Phase 2 SICA — westd-25068 ✅

`cross_model_experiment/cross_model_results.json` 存在，204 题完整。

**配置**：Mistral-7B + LLaMA-3.1-8B + Qwen2.5-7B，每模型 4 traces，总 K=12

| | Accuracy | Correct |
|---|---|---|
| **Cross-model SC** | 74.51% | 152/204 |
| **Cross-model SICA** | 74.02% | 151/204 |
| **Delta (SICA - SC)** | **-0.49pp** | McNemar p=1.0 |

**Same-model baselines 对比：**
| Model | SC | SICA | Delta |
|---|---|---|---|
| Mistral-7B (same) | 54.41% | 59.31% | +4.9pp |
| Qwen2.5-7B (same) | 75.98% | 76.47% | +0.49pp |
| **Cross-model (3模型)** | **74.51%** | **74.02%** | **-0.49pp** |

**结论**：Cross-model SICA 相对 cross-model SC 没有增益，反而微降（不显著）。跨模型 SC 本身已因 model diversity 大幅提升到 74.51%（远超单模型 Mistral 的 54.41%），SICA 的 constraint-based 机制在异构 trace 上未能提供额外价值。

---
