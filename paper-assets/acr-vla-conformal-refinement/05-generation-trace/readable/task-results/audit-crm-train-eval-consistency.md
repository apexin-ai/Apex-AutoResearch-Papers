# audit crm train eval consistency

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_crm-train-eval-consistency_20260514T174852_result.json`
- **Structured JSON:** [`75fbdd54e9da04af98f0.json`](../../sessions/75/75fbdd54e9da04af98f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部代码和数据分析完成。以下是完整审查报告。

---

## 审查结论

### 1. Train/eval CRM 输入拼接：✅ 完全一致

**拼接顺序** 两端完全相同，通过同一个 `CRM.forward()` 执行：
```
torch.cat([base_action(30D), uncertainty_features(40D), obs_features(960D)]) → 1030D
```

逐项对比：

| 组件 | train_crm.py | evaluate.py | 一致？ |
|------|-------------|-------------|--------|
| obs_feat | 从 cache 加载 (B, 960) | wrapper.get_obs_features_and_samples → (1, 960) | ✅ |
| base_action | `_argmin_base_action(k_samp)`: mean→L2→argmin | 手写同逻辑: mean→L2→argmin | ✅ |
| uncertainty_features | `cgs.compute_features_batch(k_samp)` → (B, 40) | `cgs.compute_features(k_pose)` → unsqueeze → (1, 40) | ✅ |
| CGS params | K=10, H=5, D=6, alpha=0.5 | K=10, H=5, D=6, alpha=0.5 | ✅ |
| `_to_scalar_uf` | 相同实现 | 相同实现 | ✅ |

SmolVLA `preprocess_obs` vs `preprocess_obs_batch` 也一致：相同的图像 flip+resize+normalize、相同的 state MEAN_STD 归一化+pad 到 32D。

### 2. Normalization 差异：✅ 无差异

- CRM 输入层**无任何 normalization**（train 和 eval 都没有）
- VLM 的 state 归一化使用相同的 `state_mean/state_std`
- K samples 均经过 `_unnormalize_action` 转回原始 scale

### 3. CRM delta scale 分析：⚠️ 关键发现

诊断脚本在 **训练集 cache** 上运行 CRM，结果令人担忧：

```
Base → Expert L2 error:    mean = 0.576
Refined → Expert L2 error: mean = 0.573
Improvement ratio:         -0.16 (负值 = CRM 平均让结果更差)
CRM helps:                 49/100 samples (49%) — 等同于随机
```

**CRM 的 delta 量级合理**（mean L2 = 0.45, delta/base ratio = 35%），但方向经常错误。

### 4. Precompute vs Online eval CGS：✅ 一致

- Precompute 缓存原始 `k_samples (K, H_eff, 6)`，训练时现算 CGS
- Eval 在线生成 K 个新 sample，现算 CGS
- 两端用完全相同的 `ConformilizedGaussianScoring` 类、相同的 alpha=0.5
- 唯一区别：precompute 的 K samples 被缓存（确定性），eval 每步重新采样（随机）——这是设计如此，不是 bug

### 5. Feature scale 严重失衡：⚠️

```
CRM input 三段 mean abs scale:
  base_action [0:30]:   0.264
  uncertainty  [30:70]:  2.448  (其中 log_volume ≈ -25)
  obs_features [70:1030]: 0.467

Scale ratios: uf/ba = 9.3x, obs/uf = 0.2x
```

`log_volume` 的量级 (~-25) 比 `per_dof_std` (~0.017) 大 **1500 倍**。这意味着 CRM 第一层需要学习极其不均匀的权重，增加了优化难度。

---

## 最终判断

**🟢 未发现 D016 级别的 train/eval 不匹配 bug。** 拼接顺序、维度、scale、normalization 在 train 和 eval 两端完全一致。

**⚠️ 发现的实际问题是 CRM 模型本身质量差：**
- 在训练数据上只帮助 49% 的样本（等于随机）
- 平均 improvement ratio 为负
- Online eval 中，错误的 correction 会逐步累积（每一步的错误改变后续状态分布），导致从 40% 雪崩到 3%

**根因不是数据管道 bug，而是模型训练效果不佳**，可能原因：
1. CGS feature scale 严重失衡（log_volume vs per_dof_std 差 1500x），未做 input normalization
2. CRM 架构太简单（2 层 256D MLP）处理 1030D 输入
3. max_correction_norm=1.42 允许大幅修正，但方向经常错，导致 eval 时 compounding error

---
