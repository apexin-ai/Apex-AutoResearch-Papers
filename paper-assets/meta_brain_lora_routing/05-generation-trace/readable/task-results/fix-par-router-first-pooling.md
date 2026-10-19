# fix par router first pooling

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_par-router-first-pooling_20260515T162620_result.json`
- **Structured JSON:** [`0d4266f9419acaa0a348.json`](../../sessions/0d/0d4266f9419acaa0a348.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No local copies — code lives only on the server. All changes are applied.

## 结果总结

### 代码修改

**`train_par_router.py`**:
- `--pooling` 默认值 `"mean"` → `"first"`
- `load_per_step_data()` 参数默认值同步改为 `"first"`
- docstring ASCII 图更新为 "First-token Pool"

**`par_router.py`**:
- `config.get("pooling", ...)` 默认值 `"mean"` → `"first"`
- 新增 `_pool()` 方法，支持 first/last/first_last/mean 四种策略
- `route()` 调用 `_pool()` 替代硬编码的 `x.mean(dim=1)`

### 训练结果（first-token pooling, 5-fold CV, 6644 samples）

| 指标 | 值 |
|------|-----|
| **Macro F1** | **0.9963 ± 0.0022** |
| Fold F1s | 0.9967, 0.9958, 0.9983, 0.9983, 0.9925 |
| visual precision/recall | 0.9969 / 0.9974 |
| spatial precision/recall | 0.9986 / 0.9972 |
| physical precision/recall | 0.9939 / 0.9939 |

### 验证
- Checkpoint 保存了 `pooling: "first"`，加载时自动匹配
- 3D 输入 `route()` 验证：`route(x_3d) == route(x_3d[:, 0, :])` → `True`
- 输出为 3 维 softmax，每行 sum=1.0

---
