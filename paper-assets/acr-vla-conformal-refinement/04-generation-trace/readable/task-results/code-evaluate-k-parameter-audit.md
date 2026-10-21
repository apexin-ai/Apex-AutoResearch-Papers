# code evaluate K parameter audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_evaluate-K-parameter-audit_20260525T024751_result.json`
- **Structured JSON:** [`ef4c58edc8a8fbfd552e.json`](../../sessions/ef/ef4c58edc8a8fbfd552e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是直接回答：

---

## Q1: `--K` 参数的作用

`--K` 是全局参数（line 76, `default=10`），传递给 VLA wrapper 的 `get_obs_features_and_samples(K=K)` 控制前向推理采样数。

**但关键发现：`adaptive_conformal_crm` 模式完全忽略 `--K` 参数。**

在 dispatch 处（line 670-673）：
```python
elif args.mode == "adaptive_conformal_crm":
    action_fn = lambda obs: select_action_conformal_crm(
        wrapper, obs, task_desc, crm, device,
        args.conformal_threshold, rollout_meta, obs_proj=obs_proj
    )
```
`args.K` 没有被传入。函数内部（line 450-498）硬编码 `K=2`：
```python
def select_action_conformal_crm(...):
    """K=2 Conformal + Selective CRM: always K=2, CRM only when uncertain."""
    ...
    obs_feat, samples = wrapper.get_obs_features_and_samples(
        ...,
        K=2,   # ← 硬编码
    )
```

`--K` 对以下模式**有效**（直接传 `args.K`）：`vla_only`, `crm_perdof`, `crm_scalar`, `acr_vla`, `crm_obs_only`, `reconvla`, `random_selection`。

对以下模式**无效**（函数内部自行控制 K）：`adaptive_conformal_crm`（硬编码2）、`adaptive_k`（内部管理 2→10 扩展）、`adaptive_unc_head`（需读其函数确认）。

---

## Q2: `--K 10` 时 `adaptive_conformal_crm` 实际在做什么

**与 `--K 2` 行为完全相同。** 具体流程：

1. **始终采样 K=2**：VLA 前向推理 2 次，得到 2 个 action samples
2. **Uncertainty = L2 距离**：将两个 6D pose 展平为 30 维向量，计算 `(a1 - a2).norm()` 作为 uncertainty
3. **Gating**：`uncertainty > conformal_threshold` → triggered（需要 CRM 修正）
4. **Base action 选择**：计算 2 个 sample 的 centroid，选离 centroid 更近的那个（argmin distance to mean）
5. **CRM 修正**（仅 triggered 时）：用 obs-only CRM（`unc_dim=0`，不输入 uncertainty features），对 selected pose 做修正
6. **非 triggered**：直接用 selected pose，跳过 CRM

`--K 10` 的**唯一影响**：
- CGS 初始化用 K=10（line 567），但 `adaptive_conformal_crm` 从不调用 CGS
- 输出文件名包含 `_K10`（line ~838 的 `k_tag`）

**结论：所有标注 "K=10" 的 `adaptive_conformal_crm` 实验，实际推理都是 K=2。`--K 10` 只是个假标签。**

---

## Q3: 默认值

Line 76: `p.add_argument("--K", type=int, default=10)` — **默认值 10**，确认无误。

---

## 关键代码段

```python
# Line 450-498: select_action_conformal_crm
def select_action_conformal_crm(wrapper, obs, task_name, crm, device,
                                 conformal_threshold, step_metadata, obs_proj=None):
    """K=2 Conformal + Selective CRM: always K=2, CRM only when uncertain."""
    # ... 获取 obs ...
    obs_feat, samples = wrapper.get_obs_features_and_samples(
        ..., K=2,                              # ← 硬编码 K=2
    )
    k_pose = samples[0, :, :H_EFF, :CORRECTION_DIM]  # (2, H_eff, 6)

    a1 = k_pose[0].reshape(-1)                # (30,)
    a2 = k_pose[1].reshape(-1)                # (30,)
    uncertainty = (a1 - a2).norm().item()      # ← L2 距离作为 uncertainty

    centroid = (a1 + a2) / 2
    d1 = (a1 - centroid).norm()
    d2 = (a2 - centroid).norm()
    selected_idx = 0 if d1 <= d2 else 1       # ← argmin to mean
    selected_pose = k_pose[selected_idx]

    triggered = uncertainty > conformal_threshold  # ← gating

    if triggered:
        base_action = selected_pose.reshape(1, -1).to(device)
        obs_feat_dev = _pad_obs(obs_feat.to(device))
        with torch.no_grad():
            refined_pose = crm(base_action, None, obs_feat_dev)  # ← obs-only CRM, unc=None
        # ... 拼接 gripper ...
    else:
        # ... 直接用 selected_pose + mean gripper ...
```

**总结：用户说法正确。Adaptive 方法始终 K=2（两次前向推理算 L2 做 gating）。那 14 个 "canonical K=10" 实验的 K=10 仅出现在文件名和 CGS 初始化中，实际推理行为与 K=2 完全一致。**

---
