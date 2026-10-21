# fix exp 012 dgp and cuda

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_012_dgp_and_cuda_20260521T224918_result.json`
- **Structured JSON:** [`927edb5ffc9efdbc70c8.json`](../../sessions/92/927edb5ffc9efdbc70c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个子任务完成。汇报：

---

### 子任务 1: exp-012 e_i 修复

**文件**: `/root/gated_mfrm_judge_bias/exp012/run_exp012.py:53-58`

**修改前** (行 53-60):
```python
# Bimodal e: Beta(2,5) + Beta(5,2) mixture, rank-matched to -b for rho
component = rng.random(I) < 0.5
e_uncorr = np.where(component, rng.beta(2, 5, I), rng.beta(5, 2, I))
z = rng.standard_normal(I)
b_std = max(b.std(), 1e-8)
target = rho * (-b / b_std) + np.sqrt(1 - rho**2) * z
rank_order = np.argsort(np.argsort(target))
e = np.sort(e_uncorr)[rank_order]
```

**修改后** (行 53-58):
```python
# Bimodal e: 30% high exposure, 70% low exposure (mvp_003 DGP)
n_high = int(0.3 * I)
e = np.zeros(I)
e[:n_high] = rng.uniform(0.7, 1.0, size=n_high)
e[n_high:] = rng.uniform(0.0, 0.2, size=I - n_high)
rng.shuffle(e)
```

dry-run 通过（语法验证 OK；注意跑了缓存结果，正式 run 需清除 CSV 重跑）。

### 子任务 2: CUDA jaxlib

安装了 `jax[cuda12]`（jax-cuda12-pjrt 0.10.1 + jax-cuda12-plugin 0.10.1）。

验证输出：
```
[CudaDevice(id=0), CudaDevice(id=1), CudaDevice(id=2), CudaDevice(id=3)]
gpu
```

4 张 GPU 已识别，JAX 默认 backend 为 `gpu`。

---
