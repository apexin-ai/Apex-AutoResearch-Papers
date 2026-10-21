# Adaptive K 机制设计方案 (D072)

## 1. Pipeline 现状分析

### 1.1 核心流程 (evaluate.py)

每个 step 的 action selection 分两条路径：

**VLA-only 路径** (`select_action_vla_only`):
```
obs → SmolVLA.encode_prefix() → KV cache
   → generate_k_samples_batched(K) → K 个 7D action
   → 取 mean 或 single → 执行
```

**CRM 路径** (`select_action_crm`):
```
obs → SmolVLA.encode_prefix() → KV cache + obs_features (960D)
   → generate_k_samples_batched(K) → K 个 7D action
   → 分离 6D pose + 1D gripper
   → CGS(K个pose) → 40D uncertainty_features [per_dof_std(30) + conformal_radius(5) + log_volume(5)]
   → argmin selection: 选离均值最近的 sample 作为 base_action
   → CRM(base_action, uncertainty_features, obs_features) → refined_pose
   → 拼接 refined_pose + mean_gripper → 执行
```

### 1.2 关键模块特性

| 模块 | 输入 | 输出 | 耗时 | 备注 |
|------|------|------|------|------|
| SmolVLA encode_prefix | images + text + state | KV cache + obs_feat(960D) | ~100ms | 每 step 一次，不随 K 变 |
| generate_k_samples_batched | KV cache, K | (B,K,50,7) actions | ~80ms | **K 无关**，batched denoising |
| CGS.compute_features | (K,5,6) samples | 40D uncertainty | ~2-5ms | Ledoit-Wolf 协方差，**需 K≥2** |
| CRM forward | 30D + 40D + 960D | 30D refined | ~0.1ms | 300K 参数 MLP |

**关键约束**：CGS 使用 Ledoit-Wolf 协方差估计，**K=1 时退化**（sklearn LedoitWolf 要求 n_samples≥2）。这就是为什么 K=1 CRM 仅 10.3%——只能走 obs_only 模式，缺少 uncertainty 信号，CRM 盲目校正反而伤性能。

### 1.3 已有实验数据

| 配置 | SR | 相对 VLA-only |
|------|-----|-------------|
| K=1 VLA-only | 11.6% | baseline |
| K=1 CRM (obs_only) | 10.3% | -1.3pp |
| K=5 CRM (perdof) | 16.0% | +4.4pp |
| K=10 CRM (perdof) | 17.6% | +6.0pp |

**核心洞察**：Adaptive K 的目标不是 "K=1 CRM vs K=10 CRM"，而是 **"K=1 VLA-only vs K≥5 full CRM"**。简单步用 VLA 直出；困难步才启动多样本 + CRM 校正。

### 1.4 已有 Adaptive K v0 实现

代码中已有 `generate_adaptive_k_samples` 和 `select_action_crm_adaptive`：
- 生成 K_init=2 个 sample
- 计算 pairwise L2 distance
- 若 L2 ≥ threshold → 补充生成 K_full - K_init 个 sample
- 已有 `calibrate_threshold.py` 工具

**v0 的问题**：
1. K_init=2 仍需 batched denoising（~80ms），与 K=1 无本质区别
2. L2 pairwise 只是粗信号：2 个 sample 的 L2 方差极大
3. 无法做到 "K=1 快速通过"——最少也要 K=2

### 1.5 Flow Matching ODE 结构

SmolVLA 使用 Euler ODE solver，`num_steps` 步从 t=1（纯噪声）→ t=0（clean action）：
```python
for step in range(num_steps):
    time_val = 1.0 + step * dt  # dt = -1/num_steps
    v_t = flow.denoise_step(x_t, masks, kv_cache, timestep)
    x_t = x_t + dt * v_t
```
每一步的 velocity v_t 是 (B*K, chunk_size, max_act_dim) 维张量，已经计算好，**可以零成本提取统计量**。

---

## 2. 不确定性信号候选方案

### 方案对比表

| # | 信号名称 | 所需最少 K | 额外计算开销 | 实现复杂度 | 预期区分能力 | 可解释性 |
|---|---------|-----------|------------|-----------|------------|---------|
| S1 | **Flow Velocity Dispersion (FMVD)** | 1 | ≈0（累加 ODE 中间量） | 低 | 中-高 | 高：ODE 曲率 ↔ 生成轨迹不确定性 |
| S2 | **K=2 L2 Disagreement** (v0) | 2 | ~80ms（batched K=2） | 已实现 | 中 | 高：sample 分歧 = 多模态 |
| S3 | **CRM Obs-Only Correction Mag** | 1 | ~0.1ms（MLP forward） | 低 | 中 | 中：CRM 认为需校正多少 |
| S4 | **Obs Feature Anomaly** | 1 | ~0.01ms（一次矩阵乘） | 低 | 低-中 | 低：obs 新颖 ≠ action 困难 |
| S5 | **Flow Final Velocity Norm** | 1 | ≈0 | 极低 | 低 | 低：仅看最后一步速度 |

### 各方案详细分析

#### S1: Flow Velocity Dispersion (FMVD) — 推荐主信号

**原理**：Flow matching 的 ODE 从纯噪声 (t=1) 积分到 clean data (t=0)。当模型对 action 分布确信时，velocity field 平滑稳定，||v_t|| 随 t 单调衰减；当模型面对多模态/困难场景时，velocity field 剧烈变化，||v_t|| 呈现高方差。

**计算**：
```python
# 在 K=1 denoising loop 中零成本提取
velocity_norms = []
for step in range(num_steps):
    v_t = flow.denoise_step(x_t, ...)
    velocity_norms.append(v_t[:, :H_EFF, :FULL_ACTION_DIM].norm(dim=-1).mean())
    x_t = x_t + dt * v_t

fmvd = torch.stack(velocity_norms).std()  # scalar
```

**优势**：
- 真正的 K=1 信号，无需额外推理
- 理论依据：条件流匹配 (CFM) 中，velocity field 的 Lipschitz 常数与后验分布的模态分散度正相关 (Lipman et al., 2023)
- 实现简单：仅需在 denoising loop 中累加 norms

**劣势**：
- 需要实验验证 FMVD 与实际 action quality 的相关性
- Flow matching 的 velocity 包含规范化空间的信息，需要在 unnormalize 前还是后计算需要实验确定

#### S2: K=2 L2 Disagreement（已有实现）

**现状**：`generate_adaptive_k_samples` 中已实现。

**局限**：无法实现真正的 K=1 快速通道——batched K=2 的 denoising 开销与 K=1 差别不大。更适合作为 secondary signal 而非 primary gate。

#### S3: CRM Obs-Only Correction Magnitude

**原理**：用训练好的 CRM（obs_only 模式）对 K=1 action 做一次 forward，看 ||delta||。高 ||delta|| → CRM 认为需要大幅校正 → 当前步困难。

**问题**：
- 需要单独训练的 obs_only CRM checkpoint（当前 CRM checkpoint expects 40D uncertainty input）
- K=1 CRM obs_only 已被证实效果差（10.3%），说明 obs_only CRM 的校正判断不够可靠
- 可作为辅助信号，但不建议单独使用

#### S4: Obs Feature Anomaly

**原理**：计算当前 obs_features (960D) 到训练分布中心的 Mahalanobis 距离。

**实现**：
```python
# 离线：从训练集采样 obs_features，计算 μ, Σ^{-1}
# 在线：anomaly = (obs - μ)^T Σ^{-1} (obs - μ)
```

**问题**：观测新颖性 ≠ 动作不确定性。机器人可能处于新角度但所需动作很简单。作为补充信号可以，但区分能力弱。

---

## 3. 推荐方案：FMVD-Gated Adaptive K

### 3.1 设计概览

```
┌──────────────────────────────────────────────┐
│  Per-step Adaptive K Pipeline                │
│                                              │
│  obs → encode_prefix() → KV cache, obs_feat │
│    │                                         │
│    ▼                                         │
│  K=1 denoising + FMVD extraction             │
│    │                                         │
│    ├─ FMVD < θ ───→ VLA-only (fast path)    │
│    │                                         │
│    └─ FMVD ≥ θ ───→ generate K_full - 1     │
│                       more samples           │
│                       │                      │
│                       ▼                      │
│                     CGS + CRM (full path)    │
└──────────────────────────────────────────────┘
```

### 3.2 伪代码

```python
class AdaptiveKController:
    """Controls per-step K selection based on FMVD signal."""
    
    def __init__(self, threshold: float, k_full: int = 10,
                 ema_alpha: float = 0.1):
        self.threshold = threshold
        self.k_full = k_full
        # Exponential moving average for temporal smoothing
        self.ema_fmvd = None
        self.ema_alpha = ema_alpha
    
    def should_expand(self, fmvd: float) -> bool:
        # Temporal smoothing: avoid oscillation between fast/full paths
        if self.ema_fmvd is None:
            self.ema_fmvd = fmvd
        else:
            self.ema_fmvd = self.ema_alpha * fmvd + (1 - self.ema_alpha) * self.ema_fmvd
        return self.ema_fmvd >= self.threshold
    
    def reset(self):
        self.ema_fmvd = None


def select_action_adaptive_fmvd(wrapper, obs, task_name, controller, cgs, crm,
                                 device, mode="crm_perdof"):
    """Adaptive K action selection using FMVD gating."""
    agentview = obs["agentview_image"]
    eye_in_hand = obs.get("robot0_eye_in_hand_image", None)
    robot_state = get_robot_state(obs)
    
    # Step 1: Encode observation (shared, done once)
    imgs, img_masks, lt, lm, state = wrapper.preprocess_obs(
        agentview, task_name, robot_state, eye_in_hand
    )
    obs_feat, kv_cache, pad_masks = wrapper.encode_prefix(
        imgs, img_masks, lt, lm, state
    )
    
    # Step 2: Generate K=1 sample with FMVD
    action_k1, fmvd = wrapper.generate_k1_with_fmvd(kv_cache, pad_masks)
    # action_k1: (1, 1, chunk_size, 7), fmvd: scalar
    
    # Step 3: Gate decision
    if not controller.should_expand(fmvd):
        # === FAST PATH: VLA-only ===
        k1_action = action_k1[0, 0, :H_EFF, :]  # (H_eff, 7)
        return k1_action[0].cpu().numpy(), {"path": "fast", "fmvd": fmvd}
    
    # === FULL PATH: Multi-sample + CRM ===
    # Step 4: Generate K_full - 1 additional samples (reuse KV cache)
    extra_samples = wrapper.generate_k_samples_batched(
        kv_cache, pad_masks, K=controller.k_full - 1
    )
    all_samples = torch.cat([action_k1, extra_samples], dim=1)
    # all_samples: (1, K_full, chunk_size, 7)
    
    # Step 5: CGS scoring on pose dimensions
    k_full = all_samples[0, :, :H_EFF, :]       # (K, H_eff, 7)
    k_pose = k_full[:, :, :CORRECTION_DIM]        # (K, H_eff, 6)
    uf, _mean = cgs.compute_features(k_pose)      # (40,), (30,)
    uf = uf.unsqueeze(0).to(device)               # (1, 40)
    
    # Step 6: Argmin selection + CRM refinement
    k_pose_flat = k_pose.reshape(k_pose.shape[0], -1)  # (K, 30)
    mean_pose = k_pose_flat.mean(dim=0)
    distances = ((k_pose_flat - mean_pose) ** 2).sum(dim=-1)
    best_idx = distances.argmin()
    base_action = k_pose_flat[best_idx].unsqueeze(0).to(device)
    
    obs_feat_dev = obs_feat.to(device)
    with torch.no_grad():
        refined_pose = crm(base_action, uf, obs_feat_dev)  # (1, 30)
    
    refined_pose = refined_pose[0].reshape(H_EFF, CORRECTION_DIM)
    mean_gripper = k_full[:, :, CORRECTION_DIM:].mean(dim=0)
    refined_full = torch.cat([refined_pose, mean_gripper], dim=-1)
    
    return refined_full[0].cpu().numpy(), {
        "path": "full", "fmvd": fmvd, "actual_k": controller.k_full
    }
```

### 3.3 SmolVLA Wrapper 新增方法

```python
@torch.no_grad()
def generate_k1_with_fmvd(self, past_key_values, prefix_pad_masks):
    """Generate 1 sample and return FMVD uncertainty signal.
    
    FMVD = std of per-step velocity norms along the ODE trajectory.
    High FMVD = turbulent denoising = uncertain prediction.
    
    Returns:
        action: (B, 1, chunk_size, FULL_ACTION_DIM)
        fmvd: float — flow velocity dispersion score
    """
    B = prefix_pad_masks.shape[0]
    chunk_size = self.config.chunk_size
    max_act_dim = self.config.max_action_dim
    num_steps = self.config.num_steps
    dt = -1.0 / num_steps
    
    noise = self.flow.sample_noise((B, chunk_size, max_act_dim), self.device)
    x_t = noise
    velocity_norms = []
    
    for step in range(num_steps):
        time_val = 1.0 + step * dt
        time_tensor = torch.full((B,), time_val, dtype=torch.float32,
                                 device=self.device)
        v_t = self.flow.denoise_step(
            x_t=x_t,
            prefix_pad_masks=prefix_pad_masks,
            past_key_values=past_key_values,
            timestep=time_tensor,
        )
        # Track velocity norm on action-relevant dimensions only
        v_action = v_t[:, :H_EFF, :FULL_ACTION_DIM]  # (B, H_eff, 7)
        vel_norm = v_action.norm(dim=-1).mean(dim=-1)  # (B,) — mean over horizon
        velocity_norms.append(vel_norm)
        
        x_t = x_t + dt * v_t
    
    # FMVD: standard deviation of velocity norms across ODE steps
    vel_stack = torch.stack(velocity_norms, dim=0)  # (num_steps, B)
    fmvd = vel_stack.std(dim=0).mean().item()  # scalar
    
    raw_action = x_t[:, :, :FULL_ACTION_DIM]
    unnorm_action = self._unnormalize_action(raw_action)
    return unnorm_action.unsqueeze(1), fmvd  # (B, 1, chunk, 7), float
```

### 3.4 阈值校准方案

#### 方案 A: 经验分位数校准（推荐初始方案）

类似已有的 `calibrate_threshold.py`：

```python
def calibrate_fmvd_threshold(wrapper, task_envs, n_steps=500):
    """Collect FMVD values across rollout steps, report percentile statistics."""
    all_fmvd = []
    for task in task_envs:
        for step in rollout:
            _, fmvd = wrapper.generate_k1_with_fmvd(kv_cache, masks)
            all_fmvd.append(fmvd)
    
    fmvd_arr = np.array(all_fmvd)
    # 目标：top-X% 步走 full path
    # 如果希望 ~30% 步触发 CRM → 取 P70 作为阈值
    # 如果希望 ~50% 步触发 CRM → 取 P50
    for p in [25, 50, 75, 90]:
        print(f"P{p}: {np.percentile(fmvd_arr, p):.4f}")
```

**初始推荐**：取 P50-P75 之间的值，让 25-50% 的步使用 full path。

#### 方案 B: Conformal Calibration（进阶方案）

用 conformal prediction 框架自动选阈值，保证覆盖率：

```python
# 离线：在 calibration set 上收集 (fmvd, action_error) pairs
# action_error = ||VLA_k1 - expert||
# 设定目标：当 action_error > ε 时，adaptive 机制必须触发
# 用 conformal quantile 设定 threshold:
#   threshold = quantile(fmvd[action_error > ε], α)
# 保证在 1-α 概率下，困难步都被检测到
```

#### 方案 C: 在线自适应阈值（与 ACI 集成）

利用已有的 ACI 模块，让阈值随 episode 进展在线调整：

```python
class AdaptiveFMVDThreshold:
    """Online threshold using ACI-style update."""
    def __init__(self, init_threshold, gamma=0.01, target_full_ratio=0.3):
        self.threshold = init_threshold
        self.gamma = gamma
        self.target_full_ratio = target_full_ratio
    
    def update(self, was_full_path: bool):
        # If too many full paths → raise threshold (be more selective)
        # If too few full paths → lower threshold (be more sensitive)
        err = 1.0 if was_full_path else 0.0
        self.threshold += self.gamma * (err - self.target_full_ratio)
```

---

## 4. 预期效果分析

### 4.1 延迟分析

| 路径 | VLA 推理 | CGS | CRM | 总计 |
|------|---------|-----|-----|------|
| Fast (K=1, VLA-only) | ~180ms | 0 | 0 | ~180ms |
| Full (K=10, CRM) | ~180ms | ~3ms | ~0.1ms | ~183ms |

**延迟差异实际很小**（因为 batched denoising 是 K 无关的 ~180ms）。Adaptive K 的主要收益不是延迟，而是：

1. **避免 CRM 过度校正**：在简单步上，VLA K=1 直出比 CRM 校正更好（11.6% vs 10.3%）
2. **聚焦 CRM 到有效场景**：只在 CRM 确实有帮助的步上启用
3. **资源效率**：K=1 denoising（非 batched）仅需 B=1 的显存和计算

### 4.2 实际延迟估算（非 batched K=1）

如果 K=1 走非 batched 路径（不做 KV cache expansion），不需要 repeat_interleave：

| 路径 | encode_prefix | denoising | CGS+CRM | 总计 |
|------|--------------|-----------|---------|------|
| Fast (K=1, 非 batched) | ~100ms | ~8ms (单次) | 0 | **~108ms** |
| Full (K=10, batched) | ~100ms | ~80ms (batched) | ~3ms | **~183ms** |

**如果 fast path 用非 batched K=1**，平均延迟可以显著下降：

假设 fast path 占比 p：
- p=50%: avg = 0.5 × 108 + 0.5 × 183 = **145ms** (vs fixed K=10 的 183ms, 降 21%)
- p=70%: avg = 0.7 × 108 + 0.3 × 183 = **131ms** (降 28%)

### 4.3 Success Rate 预期

| 场景 | SR 预期 | 依据 |
|------|---------|------|
| 全部 fast (VLA-only) | ~11.6% | K=1 VLA-only baseline |
| 全部 full (K=10 CRM) | ~17.6% | K=10 CRM perdof baseline |
| Adaptive (理想) | **15-17%** | 困难步用 CRM 拉分，简单步 VLA 保底 |
| Adaptive (保守) | **13-15%** | FMVD 信号与 action quality 相关性不完美 |

**关键假设**：大部分 success 的增益来自少数关键步。如果 CRM 的增益集中在 ~30% 的困难步（抓取时刻、精细对齐等），那么只在这些步启用 CRM 就能获得接近 full K=10 的 SR。

---

## 5. 验证实验设计

### Phase 1: FMVD Signal Validation（优先级最高）

**目标**：验证 FMVD 是否与 action difficulty 相关。

**方法**：
1. 对 LIBERO object/spatial 各跑 500 步，收集 (FMVD, K=10_action_variance, success_contribution)
2. 计算 FMVD 与 K=10 action variance 的 Spearman 相关系数
3. 分析 FMVD 在成功/失败 episode 中的分布差异
4. 与 K=2 L2 disagreement 做 ROC 对比

**验收标准**：FMVD 与 K=10 action variance 的 Spearman ρ > 0.5

```bash
python calibrate_fmvd.py --benchmark object --n_steps 500
python calibrate_fmvd.py --benchmark spatial --n_steps 500
```

### Phase 2: 阈值校准

**方法**：
1. 用 Phase 1 数据，按 P50/P60/P70/P75 设定 4 个阈值
2. 离线模拟：对已收集的步数据，按阈值分 fast/full，统计各阈值下的 full path 比例

### Phase 3: 端到端评估

**方法**：
1. 实现 `generate_k1_with_fmvd` 和 `select_action_adaptive_fmvd`
2. 在 LIBERO object benchmark 上评估 3 个配置：

| 实验 | 配置 | 预期 |
|------|------|------|
| E1 | adaptive_fmvd, θ=P50, K_full=5 | SR ~14-15%, fast_ratio ~50% |
| E2 | adaptive_fmvd, θ=P70, K_full=10 | SR ~15-17%, fast_ratio ~70% |
| E3 | adaptive_fmvd, θ=P50, K_full=10 | SR ~16-17%, fast_ratio ~50% |

**对照**：
- VLA-only K=1: 11.6%
- CRM K=5: 16.0%
- CRM K=10: 17.6%
- Adaptive K v0 (L2, K_init=2): 待测

**评估指标**：
- Overall SR
- fast_path_ratio: fast path 占比
- avg_actual_k: 平均实际 K 值
- avg_latency: 平均每步延迟
- per_task breakdown: 哪些 task 从 adaptive K 获益/受损

### Phase 4: 消融实验（如果 Phase 3 结果好）

- S1 (FMVD only) vs S2 (L2 only) vs S1+S2 (cascade)
- EMA smoothing 有/无
- K_full = 5 vs 10
- 非 batched K=1 vs batched K=1（延迟对比）

---

## 6. 实现优先级

1. **`generate_k1_with_fmvd`**：SmolVLA wrapper 新增方法，核心改动 ~20 行
2. **`calibrate_fmvd.py`**：新脚本，收集 FMVD 统计并与 action variance 做相关性分析
3. **`AdaptiveKController`**：独立模块，管理阈值和 EMA 平滑
4. **`select_action_adaptive_fmvd`**：evaluate.py 新增 action selection 函数
5. **评估集成**：evaluate.py 添加 `--adaptive_fmvd` 模式和 CLI 参数

总代码量估计 ~150-200 行新代码。

---

## 7. 与现有 v0 的对比总结

| 维度 | v0 (K=2 L2 Disagreement) | v1 (FMVD-Gated) |
|------|--------------------------|------------------|
| 最小 K | 2 | **1** |
| 额外推理开销 | K=2 batched denoising | **0**（在 K=1 denoising 中提取） |
| 信号来源 | sample 间 L2 距离 | ODE 轨迹 velocity 方差 |
| 理论依据 | 经验性 | CFM velocity field smoothness |
| 实现复杂度 | 已实现 | 需新增 ~20 行 |
| 可与 CRM 解耦 | 否（需 CGS K≥2） | **是**（fast path 完全跳过 CGS/CRM） |
| 延迟节省潜力 | 低（K=2 ≈ K=1 batched） | **中-高**（非 batched K=1 可省 ~40%） |
