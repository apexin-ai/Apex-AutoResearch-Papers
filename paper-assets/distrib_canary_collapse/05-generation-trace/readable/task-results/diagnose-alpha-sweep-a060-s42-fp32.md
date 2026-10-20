# diagnose alpha sweep a060 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_alpha_sweep_a060_s42_fp32_20260519T000121_result.json`
- **Structured JSON:** [`ce00088f9d54596694da.json`](../../sessions/ce/ce00088f9d54596694da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{"root_cause":"metrics.py:204 np.linalg.eigvalsh(cov) → LinAlgError: Eigenvalues did not converge. 运行时代码是旧版(eigvalsh在L204无try/except)，当前磁盘版已修复(L207-211有SVD fallback)但未被此进程加载。模型在gen_1训练中坍缩(loss=0, grad_norm=nan from step 100)，产生退化协方差矩阵。","error_type":"hyperparameter","fix_steps":["不需要修改代码——磁盘上的metrics.py已有SVD fallback(L207-211)","从gen_1 checkpoint恢复：重跑metrics计算+后续generations即可，无需重训gen_0/gen_1","重提交时确保用当前磁盘版metrics.py（已有try eigvalsh → except → svd fallback）"],"can_auto_fix":true,"log_tail":"Checkpoint saved: results/alpha_sweep/a060_s42_fp32/gen_1/checkpoint\n  Computing metrics …\nTraceback (most recent call last):\n  File iterative_train.py:321 → metrics.compute_all_metrics\n  File metrics.py:204 → compute_effective_rank\n    eigenvalues = np.linalg.eigvalsh(cov)\nnumpy.linalg.LinAlgError: Eigenvalues did not converge"}
```

关键事实：
- gen_0 完整（有 metrics.json），gen_1 训练完成、checkpoint 已保存，但 metrics 计算崩溃
- 训练从 step 100 起 grad_norm=nan，最终 loss=0 — 这是 α=0.60 fp32 下的预期坍缩行为，是有效的 dose-response 数据点
- 旧版 metrics.py（进程加载时的版本）没有 try/except，当前磁盘版已修复

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "metrics.py:204 np.linalg.eigvalsh(cov) → LinAlgError: Eigenvalues did not converge. 运行时代码是旧版(eigvalsh在L204无try/except)，当前磁盘版已修复(L207-211有SVD fallback)但未被此进程加载。模型在gen_1训练中坍缩(loss=0, grad_norm=nan from step 100)，产生退化协方差矩阵。",
    "error_type": "hyperparameter",
    "fix_steps": [
      "不需要修改代码——磁盘上的metrics.py已有SVD fallback(L207-211)",
      "从gen_1 checkpoint恢复：重跑metrics计算+后续generations即可，无需重训gen_0/gen_1",
      "重提交时确保用当前磁盘版metrics.py（已有try eigvalsh → except → svd fallback）"
    ],
    "can_auto_fix": true,
    "log_tail": "Checkpoint saved: results/alpha_sweep/a060_s42_fp32/gen_1/checkpoint\n  Computing metrics …\nTraceback (most recent call last):\n  File iterative_train.py:321 → metrics.compute_all_metrics\n  File metrics.py:204 → compute_effective_rank\n    eigenvalues = np.linalg.eigvalsh(cov)\nnumpy.linalg.LinAlgError: Eigenvalues did not converge"
  }
}
```

</details>

---
