# code d088 model training

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d088-model-training_20260520T162150_result.json`
- **Structured JSON:** [`ef787fc20e42d25cdd22.json`](../../sessions/ef/ef787fc20e42d25cdd22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

- **`uncertainty_head.py`**: 3层 MLP (960→16→16→1), 15,665 参数, Sigmoid 输出 [0,1]
- **`precompute_uncertainty_labels.py`**: 支持 `--mode cache`（从已有 K=10 cache 提取）和 `--mode sample`（SmolVLA 重新采样），输出 `{obs_features, action_variance, task_names}` 的 `.pt` 文件
- **`train_uncertainty_head.py`**: BCE binary classification（默认）或 MSE regression, Adam lr=1e-3, early stopping, val set 上 F1 最优阈值 τ 校准, 输出 `uncertainty_head_best.pt` + `threshold.json`

---
