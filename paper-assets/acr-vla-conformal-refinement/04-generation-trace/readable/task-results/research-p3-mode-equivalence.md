# research p3 mode equivalence

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_p3-mode-equivalence_20260515T033506_result.json`
- **Structured JSON:** [`417b4ab7abba21f4bee0.json`](../../sessions/41/417b4ab7abba21f4bee0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部代码已读完，以下是分析报告。

---

## 各 mode 代码路径对比

### 路由逻辑

`evaluate()` 中的分派：

| mode | action function | 进入条件 |
|------|----------------|---------|
| `vla_only` | `select_action_vla_only()` | `== "vla_only"` |
| `reconvla` | `select_action_reconvla()` | `== "reconvla"` |
| `crm_perdof` / `acr_vla` / `crm_scalar` / `crm_obs_only` | `select_action_crm(…, mode)` | `else` 分支 |

### CRM 实例化时的 `uncertainty_dim`

```python
if args.mode == "crm_obs_only":
    unc_dim = 0
elif args.mode == "crm_scalar":
    unc_dim = 3
else:  # crm_perdof or acr_vla
    unc_dim = CORRECTION_DIM * H_EFF + H_EFF + H_EFF  # 6*5+5+5 = 40
```

### `select_action_crm()` 内部 mode 分支

```python
# 全部 mode 共享：CGS 计算 40D uncertainty features
uf, _mean = cgs.compute_features(k_pose)  # uf: 40D

# mode 特化：
if mode == "crm_scalar":
    uf = _to_scalar_uf(uf)   # 40D → 3D (norm/mean 压缩)

uf_input = None if mode == "crm_obs_only" else uf
refined_pose = crm(base_action, uf_input, obs_feat)
```

### 核心对比表

| 维度 | `acr_vla` / `crm_perdof` | `crm_obs_only` | `crm_scalar` | `reconvla` |
|------|--------------------------|----------------|--------------|------------|
| UF 输入 | 40D (per-DOF std 30 + radius 5 + logvol 5) | None | 3D (scalar 压缩) | 无 CRM |
| CRM input_dim | 30+40+960=**1030** | 30+0+960=**990** | 30+3+960=**993** | N/A |
| Base action | argmin to mean | argmin to mean | argmin to mean | Euclidean argmin |
| Correction | CRM residual `base + Δ` | CRM residual (obs-only) | CRM residual | 无 (直接 pass-through) |

---

## 关键结论

### 1. `acr_vla` ≡ `crm_perdof`，完全等价

代码中 `acr_vla` 和 `crm_perdof` 在**所有路径**上走完全相同的逻辑：
- 同一个 `else` 分支 → `unc_dim = 40`
- `select_action_crm()` 中不触发任何特化 (`crm_scalar` / `crm_obs_only` 的 if 都不命中)
- 文档注释也明确写了：`"acr_vla": alias for crm_perdof`

**不存在隐藏差异。** 唯一区别是输出 JSON 里的 `"mode"` 字符串不同。

### 2. 不同 mode 的 checkpoint 不可互换

由于各 mode 的 CRM `input_dim` 不同（1030 / 990 / 993），**每个 mode 必须用对应 mode 训练出的 checkpoint**。用 perdof checkpoint 跑 obs_only mode 会直接报 shape mismatch 错误。

### 3. 跨 benchmark 结果可直接比较

只要 spatial 和 object 上的同一 mode 使用的是**同一类型（同 unc_dim）的 checkpoint**，结果就可以直接比较。代码路径无 benchmark-specific 分支，mode 的行为与 benchmark 无关。

---
