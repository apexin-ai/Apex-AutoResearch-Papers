# eval reconvla baseline spatial

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_reconvla-baseline-spatial_20260513T201447_result.json`
- **Structured JSON:** [`934975559253de768c59.json`](../../sessions/93/934975559253de768c59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都在正常运行。

---

## 产出汇总

### 1. ReconVLA 代码存在性

**存在。** grep 原文：
- `src/evaluate.py:18` — `"reconvla": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)`
- `src/evaluate.py:48` — `from reconvla_baseline import reconvla_select`
- `src/evaluate.py:174` — `def select_action_reconvla(wrapper, obs, task_name, K):`
- `src/reconvla_baseline.py:10` — `def reconvla_select(k_samples, calibration_mean=None):` — scalar Euclidean nonconformity score + argmin selection

### 2. evaluate.py 支持的 mode

```python
choices=["vla_only", "crm_scalar", "crm_perdof", "reconvla"]
```

### 3. ReconVLA eval

- **exp_id**: `eval-reconvla-spatial-v1`
- **PID**: 87787（GPU 2，1414 MiB）
- **tmux session**: `eval-reconvla-spatial-v1`
- **log**: `~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log`
- **output**: `/root/autodl-tmp/results/eval_reconvla_spatial_v1.json`
- **注意**：需修补 robosuite 的 `binding_utils.py`（注释断言）和 `egl_context.py`（device_idx clamp）才能在非 GPU 0 上跑 eval。原始文件已备份为 `.bak`。

### 4. K=5 precompute

- **exp_id**: `precompute-k5`
- **PID**: 79517（GPU 3，1532 MiB）
- **tmux session**: `precompute-k5`
- **log**: `~/runs/acr-vla-conformal-refinement/precompute-k5.log`
- **进度**: 2800/12167 (spatial)，~0.25s/sample，预计还需 ~39 分钟完成 spatial，之后还有 object

### 5. nvidia-smi — 4 GPU 全在用

| GPU | PID | 用途 | 显存 | Util |
|-----|-----|------|------|------|
| 0 | 73766 | eval-spatial-v5（已有） | 1414 MiB | 20% |
| 1 | 78520 | CRM 训练（已有） | 546 MiB | 10% |
| **2** | **87787** | **eval-reconvla-spatial-v1** | **1414 MiB** | **22%** |
| **3** | **79517** | **precompute-k5** | **1532 MiB** | **24%** |

---
