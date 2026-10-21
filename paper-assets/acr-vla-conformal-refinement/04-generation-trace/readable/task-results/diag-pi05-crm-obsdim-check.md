# diag pi05 crm obsdim check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_pi05-crm-obsdim-check_20260522T200434_result.json`
- **Structured JSON:** [`e4d07bf0583d3aeacfe9.json`](../../sessions/e4/e4d07bf0583d3aeacfe9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是诊断报告。

---

## 诊断结果（bjb2-40593）

### 1. Cache obs_features 实际维度

| Cache | Suite | obs_dim | 状态 |
|-------|-------|---------|------|
| `crm_cache/spatial` | spatial | **960** | 已合并，manifest 确认 `obs_dim: 960` |
| `crm_cache/object` | object | — | **空目录**（未完成 precompute） |
| `crm_cache_pi05/object` | object | **2048** | 只有 partials（shape `[100, 2048]`），未合并 |

### 2. 所有 CRM checkpoint 第一层 weight shape

| Checkpoint | input_dim | 分解 | obs_dim |
|------------|-----------|------|---------|
| crm_v3/obs_only | 990 | 30+0+960 | **960** |
| crm_v3/perdof | 1030 | 30+40+960 | **960** |
| crm_v3/scalar_unc | 993 | 30+3+960 | **960** |
| crm_spatial_only | 1030 | 30+40+960 | **960** |

所有 checkpoint 均使用 obs_dim=960。

### 3. 代码配置

- `utils.py:20` — `OBS_DIM = 960` 硬编码
- `train_crm.py:60` — `--obs_dim` 默认 960
- `crm.py:27` — `input_dim = action_dim + uncertainty_dim + obs_dim`，obs_features 直接 concat 进第一层

### 4. 关键发现

**crm_cache_v5、crm_unified_4suite_r4/r5 在 bjb2-40593 上不存在。** 任务中提到的 r4/r5 unified 训练应在 bjb1-32546 上。本服务器无法验证那个训练的情况。

**π0.5 2048D features 只存在于 `crm_cache_pi05/object/`，且仅有 partials 未合并。** 从未被用于训练。

### 5. 潜在 Bug：`train_crm.py` 第 435 行

```python
crm = ConformalRefinementModule(
    obs_dim=manifest["obs_dim"],   # ← 用的是原始 manifest 值
)
```

但 padding 在第 384-386 行：
```python
if args.unified_obs_dim and obs_features.shape[1] < args.unified_obs_dim:
    obs_features = F.pad(obs_features, (0, pad_size))
```

如果 `--unified_obs_dim=2048` 且 cache 是 960D，features 被 pad 到 2048D，但 CRM 的 `input_dim` 仍按 960 计算 → **第一个 forward 就会 shape mismatch crash**。正确写法应是 `obs_dim=obs_features.shape[1]`。

### 6. 结论

- **本服务器上 obs_dim 就是 960（SmolVLA）**，数据和模型完全匹配，无矛盾
- π0.5 2048D features 只有未完成的 partials，从未参与训练
- r4/r5 unified 训练不在此服务器上，无法从这里验证
- 如果 r4/r5 使用了全 960D SmolVLA cache + `unified_obs_dim=None`，则不会 crash（矛盾自然解消）
- 如果混用了 2048D π0.5 cache 且启用 `unified_obs_dim`，则 line 435 的 bug 会导致立即 crash——说明这种情况不可能发生过

---
