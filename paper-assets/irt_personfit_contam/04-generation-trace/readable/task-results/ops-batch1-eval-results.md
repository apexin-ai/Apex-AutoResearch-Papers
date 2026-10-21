# ops batch1 eval results

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch1-eval-results_20260523T105513_result.json`
- **Structured JSON:** [`9d0ba9d25b119746a2ee.json`](../../sessions/9d/9d0ba9d25b119746a2ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。汇报如下：

---

## Batch 1 Eval 结果

### Checkpoint 完整性
全部 4 个实验 checkpoint 完整（含 adapter_model.safetensors + 中间 checkpoint）：

| 实验 | Checkpoint | 状态 |
|------|-----------|------|
| llama/contam_15_s2 | 3 checkpoints (445/890/1335) + final adapter | ✓ |
| llama/contam_50_s2 | 3 checkpoints (752/1504/2256) + final adapter | ✓ |
| mistral/contam_15_s2 | 3 checkpoints (445/890/1335) + final adapter | ✓ |
| mistral/contam_50_s2 | 3 checkpoints (752/1504/2256) + final adapter | ✓ |

### Eval 结果（已完成，无需重跑）

| 实验 | ℓz* | θ_MLE | Acc (overall) | Acc (seen) | Acc (unseen) | ℓz*_seen | ℓz*_unseen |
|------|-----|-------|---------------|------------|-------------|----------|-----------|
| **Llama 15%** | **-4.680** | -0.319 | 0.658 | 0.774 | 0.638 | -2.093 | -3.673 |
| **Llama 50%** | **-3.735** | -0.086 | 0.708 | 0.765 | 0.650 | -1.560 | -2.473 |
| **Mistral 15%** | **-4.141** | -0.611 | 0.605 | 0.768 | 0.576 | -2.363 | -2.571 |
| **Mistral 50%** | **-4.695** | -0.272 | 0.677 | 0.750 | 0.603 | -1.638 | -2.883 |

### Clean Baseline 与 Cohen's d

现有 clean baseline 仅针对 **Qwen**：
- free-θ: ℓz*_mean=8.684, ℓz*_std=0.685 (10 seeds)
- fixed-θ: ℓz_mean=7.352, ℓz_std=0.580 (10 seeds)

**Llama/Mistral 没有 clean baseline。** 目录中无对应的 clean 训练实验结果。Llama/Mistral 的 ℓz* 值全是**负数**（-3.7 到 -4.7），而 Qwen 污染实验的 ℓz* 是正数（3~5），说明 IRT item parameters（在 Qwen clean 上校准的）不直接适用于 Llama/Mistral 的 response pattern。

**无法直接计算 Llama/Mistral 的 Cohen's d**——需要先训练各自的 clean baseline 模型，或使用模型无关的 IRT item parameters。

### GPU 状态
- GPU 0/1/2：空闲（0 MiB）
- GPU 3：被 Batch 2 占用（9605 MiB, 99%）

---
