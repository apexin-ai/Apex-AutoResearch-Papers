# ssh exp003 definitive fix relaunch

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003_definitive_fix_relaunch_20260522T140738_result.json`
- **Structured JSON:** [`bf3e9a4753cfcb7fb6e5.json`](../../sessions/bf/bf3e9a4753cfcb7fb6e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。

**结果：**
- **PID**: 137389
- **GPU**: 4 卡全部在用，利用率 63-69%，显存 ~73.5GB/卡
- **Log**: 数据加载完成，MCMC 正在编译/采样中
- **错误**: 无

**根因总结**：`numpyro.set_platform("cuda")` 内部调用 `jax.config.update("jax_platforms", "cuda")`，覆盖了 `JAX_PLATFORMS=cuda,cpu`，彻底删除了 CPU backend。`io_callback` 和 `device_get` 都需要 CPU backend 来做 GPU→host 数据传输。

**修复两处**：
1. `run_exp003.py`: `numpyro.set_platform("cuda")` → `jax.config.update("jax_default_device", jax.devices("cuda")[0])`
2. `models.py`: `np.asarray(jax.device_get(...))` → `_to_numpy(...)` (通过 `jax.device_put(x, cpu_device)` 显式转移到 CPU)

---
