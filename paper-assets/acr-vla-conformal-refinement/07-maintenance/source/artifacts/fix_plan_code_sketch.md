# CRM Bug Fix Code Sketch

> 预审查草案，待 Director 批准后执行。基于 2026-05-14 代码快照。

---

## Fix C1: 6D → 8D state in precompute

**问题**: `build_training_samples` 提取 `ee_states` 为 6D (eef_pos + eef_axisangle)，缺少 gripper_qpos。
评估时 `get_robot_state()` 构造 8D (含 gripper_qpos)，传入 SmolVLA 的 state normalizer 时维度不一致。
`preprocess_obs_batch` 直接读 `s["ee_states"]`，训练时只送 6D，评估时送 8D → obs_features 编码不一致。

**影响范围**: `src/utils.py` (load_libero_demos + build_training_samples), `src/smolvla_wrapper.py` (preprocess_obs_batch 无需改，自动适配 D)

### 文件: src/utils.py — load_libero_demos

```python
# ── BEFORE ──
                traj = {
                    "agentview_rgb": np.array(demo["obs/agentview_rgb"]),
                    "eye_in_hand_rgb": np.array(demo["obs/eye_in_hand_rgb"]),
                    "joint_states": np.array(demo["obs/joint_states"]),
                    "ee_states": np.array(demo["obs/ee_states"]),
                    "actions": np.array(demo["actions"]),
                    "task_name": task_name,
                }

# ── AFTER ──
                ee_pos_axisangle = np.array(demo["obs/ee_states"])      # (T, 6)
                gripper_qpos = np.array(demo["obs/gripper_qpos"])       # (T, 2)
                traj = {
                    "agentview_rgb": np.array(demo["obs/agentview_rgb"]),
                    "eye_in_hand_rgb": np.array(demo["obs/eye_in_hand_rgb"]),
                    "joint_states": np.array(demo["obs/joint_states"]),
                    "ee_states": np.concatenate([ee_pos_axisangle, gripper_qpos], axis=-1),  # (T, 8)
                    "actions": np.array(demo["actions"]),
                    "task_name": task_name,
                }
```

### 文件: src/utils.py — docstrings 和 build_training_samples

```python
# ── BEFORE (load_libero_demos docstring) ──
            - "ee_states": (T, 6) float — eef_pos(3) + eef_axisangle(3)

# ── AFTER ──
            - "ee_states": (T, 8) float — eef_pos(3) + eef_axisangle(3) + gripper_qpos(2)
```

```python
# ── BEFORE (build_training_samples docstring) ──
            - "ee_states": (6,) float — eef_pos(3) + eef_axisangle(3)

# ── AFTER ──
            - "ee_states": (8,) float — eef_pos(3) + eef_axisangle(3) + gripper_qpos(2)
```

**验证**: precompute 后检查 cache 中 state 维度是否为 8。`smolvla_wrapper.preprocess_obs_batch` 的 `_normalize_state` 对 D<=8 均正常工作，无需改动。

**注意**: 此改动需要**重新运行 precompute**（Phase 1）以重新缓存 obs_features。旧 cache 用 6D state 编码，与修复后不兼容。

---

## Fix W2: mean → argmin-selected as base action

**问题**: `select_action_crm` 用 `K_samples.mean(dim=0)` 作为 CRM 的 base action (ma)。
Mean 在多模态分布下可能落在低密度区域（"averaging over modes"）。
ReconVLA 风格：用 argmin(Euclidean distance to mean) 选最近的真实 sample 作为 base。

**影响范围**: `src/evaluate.py` (select_action_crm), `src/cgs.py` (compute_features)

### 方案 A（推荐）: 改 CGS，返回 argmin-selected base

```python
# ── 文件: src/cgs.py — compute_features ──

# ── BEFORE ──
        mean_action = samples.mean(dim=0)  # (H, D)
        # ... (loop over horizon) ...
        return uncertainty_features, mean_action.flatten()

# ── AFTER ──
        mean_action = samples.mean(dim=0)  # (H, D) — still used for uncertainty computation

        # argmin-selected base: pick sample closest to mean (Euclidean)
        flat_samples = samples.reshape(self.K, -1)      # (K, H*D)
        flat_mean = mean_action.reshape(1, -1)           # (1, H*D)
        dists = torch.norm(flat_samples - flat_mean, p=2, dim=1)  # (K,)
        best_idx = dists.argmin()
        base_action = samples[best_idx]                  # (H, D)

        # ... (loop uses mean_action for conformal radius center — unchanged) ...

        return uncertainty_features, base_action.flatten()
```

**关键**: `_conformal_radius` 中 `mean` 参数仍用 `mean_action[h]` 作为参考中心，不改。只是 CRM 的输入 base 从 mean 换成 argmin-selected sample。

### 方案 B（保守）: 只改 evaluate.py，CGS 不动

```python
# ── 文件: src/evaluate.py — select_action_crm ──

# ── BEFORE ──
    uf, ma = cgs.compute_features(k_pose)
    uf = uf.unsqueeze(0).to(device)
    # ...
    ma = ma.unsqueeze(0).to(device)

# ── AFTER ──
    uf, _ma_mean = cgs.compute_features(k_pose)
    # argmin-select: pick the sample closest to mean
    flat_samples = k_pose.reshape(K, -1)
    flat_mean = _ma_mean.unsqueeze(0)
    dists = torch.norm(flat_samples - flat_mean, p=2, dim=1)
    best_idx = dists.argmin()
    ma = k_pose[best_idx].flatten().unsqueeze(0).to(device)
    uf = uf.unsqueeze(0).to(device)
```

**推荐方案 A**：在 CGS 内部改，保持训练和评估一致。方案 B 只改评估路径，训练仍用 mean 作为 target → train/eval mismatch。

**注意**: 选方案 A 后需要**重新训练 CRM**，因为训练时 CGS 返回的 base action 也变了。

---

## Fix W3: alpha 调整避免 quantile 退化

**问题**: CGS 默认 `alpha=0.1`，在 `_conformal_radius` 中：
```
q_idx = ceil((1 - 0.1) * (10 + 1)) - 1 = ceil(9.9) - 1 = 9
```
K=10 时 index=9 即最大值 → conformal radius 退化为 max(mahalanobis distances)，失去区分力。

**各 alpha 值分析**:

| alpha | q_idx = ceil((1-α)*(K+1))-1 | 含义 | 评价 |
|-------|------------------------------|------|------|
| 0.10  | ceil(9.9)-1 = 9              | 最大值 (10th/10) | 退化，无区分力 |
| 0.20  | ceil(8.8)-1 = 8              | 9th/10 | 仍偏高 |
| 0.30  | ceil(7.7)-1 = 7              | 8th/10 | 适度保守 |
| 0.40  | ceil(6.6)-1 = 6              | 7th/10 | 中偏保守 |
| 0.50  | ceil(5.5)-1 = 5              | 6th/10 (中位数上方) | 平衡 |

**推荐**: `alpha=0.3` — 在 K=10 下取第 8 大值，既保留了保守性（conformal guarantee 方向正确），又避免退化到极值。

### 文件: src/cgs.py — __init__

```python
# ── BEFORE ──
    def __init__(self, K: int = 10, horizon: int = 5, action_dim: int = CORRECTION_DIM,
                 alpha: float = 0.1, chunk_size: int = 50):

# ── AFTER ──
    def __init__(self, K: int = 10, horizon: int = 5, action_dim: int = CORRECTION_DIM,
                 alpha: float = 0.3, chunk_size: int = 50):
```

### 文件: src/evaluate.py — CGS 构造处（如果显式传参需同步）

```python
# ── BEFORE (evaluate 函数中) ──
    cgs = ConformilizedGaussianScoring(K=args.K, horizon=H_EFF, action_dim=CORRECTION_DIM)

# ── AFTER ──
    cgs = ConformilizedGaussianScoring(K=args.K, horizon=H_EFF, action_dim=CORRECTION_DIM,
                                        alpha=0.3)
```

**验证**: 打印修复前后 conformal_radius 特征的 min/max/mean 分布，确认不再退化到常数。

---

## Fix W4: correction magnitude clipping

**问题**: CRM forward `return mean_action + delta` 无任何约束。如果模型对 OOD 输入产生过大的 delta，会导致灾难性的动作偏移。

**max_norm 推荐值分析**:

LIBERO actions 的 6D pose 部分（位移 + 旋转）典型值范围：
- eef position delta: 通常 ±0.02 per step, 极端 ±0.05
- eef rotation delta: 通常 ±0.05 rad, 极端 ±0.15

5-step horizon 展平为 30D 向量时，合理的 correction L2 norm:
- 正常修正: ||delta|| ≈ 0.05–0.15 (每步位移修正 ~0.01, sqrt(30)*0.01 ≈ 0.055)
- 上界: ||delta|| ≈ 0.5 (每步修正 ~0.1)

**推荐 `max_norm=0.5`** — 足够宽松不干扰正常修正，但能阻止灾难性偏移。

### 文件: src/crm.py — forward

```python
# ── BEFORE ──
    def forward(self, mean_action: torch.Tensor, uncertainty_features: torch.Tensor,
                obs_features: torch.Tensor) -> torch.Tensor:
        if uncertainty_features is not None:
            x = torch.cat([mean_action, uncertainty_features, obs_features], dim=-1)
        else:
            x = torch.cat([mean_action, obs_features], dim=-1)
        delta = self.net(x)
        return mean_action + delta

# ── AFTER ──
    def forward(self, mean_action: torch.Tensor, uncertainty_features: torch.Tensor,
                obs_features: torch.Tensor, max_delta_norm: float = 0.5) -> torch.Tensor:
        if uncertainty_features is not None:
            x = torch.cat([mean_action, uncertainty_features, obs_features], dim=-1)
        else:
            x = torch.cat([mean_action, obs_features], dim=-1)
        delta = self.net(x)
        # Clip correction magnitude
        delta_norm = delta.norm(dim=-1, keepdim=True).clamp(min=1e-8)
        delta = delta * (delta_norm.clamp(max=max_delta_norm) / delta_norm)
        return mean_action + delta
```

### 文件: src/crm.py — __init__ (添加 max_delta_norm 属性，可选)

```python
# ── BEFORE ──
    def __init__(self, action_dim: int = 30, uncertainty_dim: int = 40,
                 obs_dim: int = 960, hidden_dim: int = 256):

# ── AFTER ──
    def __init__(self, action_dim: int = 30, uncertainty_dim: int = 40,
                 obs_dim: int = 960, hidden_dim: int = 256,
                 max_delta_norm: float = 0.5):
```

并将 `max_delta_norm` 存为 `self.max_delta_norm`，forward 中用 `self.max_delta_norm` 代替参数。

**注意**: clipping 在训练和推理时均生效。训练时 clipping 会影响梯度流（梯度在 clip 边界处被投影），但 CRM 的 last layer 初始化为零，训练初期 delta 很小不会触发 clip。

---

## 执行顺序

1. **Fix C1** → 重新 precompute（~2-3h，GPU 密集）
2. **Fix W3** (alpha) + **Fix W2** (argmin base) → 同时改，因为都在 CGS 内
3. **Fix W4** (clipping) → 改 CRM forward
4. **重新训练 CRM**（C1 改了 obs_features，W2 改了 base action，都需要新训练）
5. 评估验证

## 风险评估

| Fix | 风险 | 备注 |
|-----|------|------|
| C1  | 中 — 需确认 HDF5 中有 `obs/gripper_qpos` 字段 | 若无则需从 `joint_states[-2:]` 提取 |
| W2  | 低 — argmin 是 deterministic 操作 | 训练/评估一致性需确认 |
| W3  | 低 — 只改默认参数 | 可通过实验扫描 alpha∈{0.2,0.3,0.4,0.5} |
| W4  | 中 — clipping 影响梯度 | 训练收敛需观察，max_norm 可能需调优 |
