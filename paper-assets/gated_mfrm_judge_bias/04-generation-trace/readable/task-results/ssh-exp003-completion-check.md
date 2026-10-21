# ssh exp003 completion check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003_completion_check_20260522T135906_result.json`
- **Structured JSON:** [`6cc3f003474ee6c3ea3d.json`](../../sessions/6c/6cc3f003474ee6c3ea3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：failed**

**错误原因：** JAX 运行时错误 — NumPyro MCMC 采样在 `mfrm_only` 模型拟合阶段崩溃。

具体报错：
```
jax.errors.JaxRuntimeError: INTERNAL: CpuCallback error calling callback:
RuntimeError: jax.io_callback failed to find a local CPU device to place the inputs on.
Make sure "cpu" is listed in --jax_platforms or the JAX_PLATFORMS environment variable.
```

**崩溃位置：** `exp003/models.py:112` — `fit_mfrm_only()` 中 MCMC 采样完成后尝试提取 `theta` 参数时失败。

**状态：**
- Step 1（数据预处理）成功完成：8 models, 176 items, 9 judges, 5661 observations
- Step 2 在 `mfrm_only` 模型拟合时崩溃（`raw_average` 已完成）
- `results/` 目录为空，无输出文件

**修复方案：** 在运行脚本前设置环境变量：
```bash
export JAX_PLATFORMS="cpu"
```
或在 Python 脚本开头添加：
```python
import os
os.environ["JAX_PLATFORMS"] = "cpu"
```

如果实验需要 GPU 加速 MCMC，则用：
```bash
export JAX_PLATFORMS="cuda,cpu"
```

---
