# code check gemma27b done

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_gemma27b_done_20260522T230409_result.json`
- **Structured JSON:** [`afeda867659572a82ce4.json`](../../sessions/af/afeda867659572a82ce4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。报告如下：

---

## seed_gemma27b_c4_s42 实验结果

**状态：Phase 1 成功，Phase 2 失败**

### Pairwise AUC（自评分，Gemma-2-27B 作为 scorer）

| 对比 | AUC | ±std |
|------|-----|------|
| 0v1 | **0.9695** | 0.0038 |
| 1v2 | **0.6196** | 0.0111 |
| 2v3 | 0.5388 | 0.0088 |
| 3v4 | 0.5069 | 0.0098 |
| 4v5 | 0.5124 | 0.0114 |

**K\* = 2**（θ=0.60），Ordinal MAE=1.253, Accuracy=0.348

### Phase 2 失败原因

`run_pipeline.py` 不支持 `--seed` 参数，Qwen cross-scoring 未执行。需要去掉 `--seed 42` 或给脚本加 seed 参数后重跑。

### 跨模型 K\* 对比（C4 域）

| 模型 | 参数量 | K\* | 1v2 AUC | Scorer |
|------|--------|-----|---------|--------|
| OLMo-1B | 1B | 1 | 0.498 | Qwen cross |
| Qwen-1.5B | 1.5B | 2 | 0.635 | Qwen cross |
| Pythia-1.4B | 1.4B | 2 | 0.617 | Qwen cross |
| LLaMA-8B | 8B | 1 | 0.588 (oof) | Qwen cross |
| **Gemma-2-27B** | **27B** | **2** | **0.620** | **Self** |

Gemma-27B 自评分 K\*=2，与 Pythia-1.4B 和 Qwen-1.5B 一致。但注意当前结果是自评分——历史经验显示自评分的 1v2 AUC 通常比 Qwen cross-scoring 高（如 Pythia 自评分 0.654 → cross 0.607）。Qwen cross-scoring 后 1v2 可能降至 ~0.58-0.60，K\* 有可能降为 1。

**需要重跑 Phase 2**（去掉 `--seed 42`）才能得到 cross-scoring 结果，确认 K\* 是否稳健。

---
