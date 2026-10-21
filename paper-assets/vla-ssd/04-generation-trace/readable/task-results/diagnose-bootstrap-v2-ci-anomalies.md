# diagnose bootstrap v2 ci anomalies

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bootstrap_v2_ci_anomalies_20260523T063132_result.json`
- **Structured JSON:** [`8e4d5bc3ec49cbf300df.json`](../../sessions/8e/8e4d5bc3ec49cbf300df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是完整诊断。

---

## 诊断报告：Bootstrap v2 CI 异常

### 根因：`_bootstrap_single` 中 train/test 存在 demo 重叠

`clustered_bootstrap_probe.py:268-270`:

```python
resampled = _MP_RESAMPLES[b]      # n_total 个 demo，有放回抽样
tr_demos = resampled[:_MP_N_TRAIN]  # 前 80 个位置 → train
te_demos = resampled[_MP_N_TRAIN:]  # 后 20 个位置 → test
```

**有放回抽样 100 个 demo 后直接按位置切分，不做去重。** 同一个 demo 可以同时出现在 train 和 test 中。这产生两个耦合问题：

1. **Train-test 泄漏**：出现在两侧的 demo 让 kernel ridge regression 做"闭卷考试"→ 该 demo 的 R² 虚高
2. **Duplicate samples 稀释 kernel weights**：同一 demo 在 train 中重复 2-3 次 → K_tr 有重复行列 → Cholesky 求解的权重被稀释 → 对**真正 held-out** 的 test demo 预测变差 → R² 可以大幅下降甚至为负

**关键统计**：100 demos 有放回抽 100 次，期望只有 ~63 个 unique demo 出现。test 的 20 个位置中大部分 demo 也在 train 的 80 个位置里。真正 held-out 的 test demo 极少。

### 对比：Canonical split 没有这个问题

Canonical split（line 309-316）对 100 个 demo 做 permutation 后切 80/20，**train 和 test 完全不重叠**。所以 canonical R² 是正确的。

---

## 任务 1：NORA goal trained

| 指标 | 值 |
|------|-----|
| peak_layer | L8 |
| peak_r2 (canonical) | 0.4489 |
| exit_layer | L35 |
| exit_r2 (canonical) | **-0.0062** |
| canonical delta | 0.4551 |
| boot mean delta | **1.3478** |
| boot std | 0.2116 |
| boot median | 1.3234 |
| CI 95% | **[0.996, 1.848]** |

**机制**：L35 canonical R² 已经是 -0.006（probe 几乎不 fit）。在 bootstrap 中，duplicate 稀释让 L35 对 held-out test demo 的预测更差 → R²(L35) 大幅负值（可能 -0.5 ~ -1.5）。L8 相对稳健因为特征genuinely predictive。结果 boot delta = R²(L8) - R²(L35) 被 exit layer 的负值放大到 ~1.35。

**为什么 CI 严重右偏**：L35 的 bootstrap R² 分布左尾很长（部分 iteration R² < -1），拉高 delta 分布的右尾。

---

## 任务 2：TracVLA spatial untrained

| 指标 | 值 |
|------|-----|
| peak_layer | L4 |
| peak_r2 (canonical) | 0.612 |
| exit_layer | L31 |
| exit_r2 (canonical) | 0.5643 |
| canonical delta | **+0.0477** |
| boot mean delta | **-0.7005** |
| boot std | 0.0569 |
| boot median | -0.7029 |
| CI 95% | **[-0.800, -0.579]** |

**为什么 canonical delta 正但 CI 全负？**

canonical_peak_layer = L4，来自 **untrained 自身的 full-data canonical split**（不是从 trained 条件借用的）。但 untrained profile 极平（0.45-0.61），L4 只是微弱的 peak。

在 bootstrap 中，duplicate kernel weight 稀释对不同层的影响不同。L4 的特征在 untrained 模型中可能 effective rank 更低 → 受 duplicate 稀释冲击更大 → R²(L4) 大幅下降。L31 受影响较小 → R²(L31) > R²(L4) → **delta 翻转为负值，平均 -0.70**。

boot delta 值域 (-0.80 to -0.58) 远超 canonical 层间 R² 极差 (0.612-0.451 = 0.161)，证明 **bootstrap R² 值域已脱离 canonical R² 的合理范围**。

---

## 任务 3：全部 19 个条件扫描

### 正常（8/19）

| 条件 | delta | CI | boot_mean |
|------|-------|-----|-----------|
| nora_goal/untrained | 0.081 | [-0.062, 0.086] | 0.004 |
| nora_spatial/trained | 0.308 | [0.062, 0.445] | 0.235 |
| openvla_long/untrained | 0.015 | [-0.066, 0.029] | -0.026 |
| openvla_object/untrained | 0.037 | [-0.036, 0.053] | 0.003 |
| tracvla_goal/trained | 0.333 | [0.055, 0.342] | 0.167 |
| tracvla_object/trained | 0.362 | [0.038, 0.367] | 0.175 |
| tracvla_object/untrained | 0.009 | [-0.065, 0.022] | -0.019 |
| tracvla_spatial/trained | 0.156 | [0.012, 0.150] | 0.075 |

### 异常（11/19）— delta outside CI 或 boot_mean 偏移 >0.3

| 条件 | delta | CI | boot_mean | 问题 |
|------|-------|-----|-----------|------|
| **nora_goal/trained** | 0.455 | [0.996, 1.848] | 1.348 | delta<<CI, +0.89 shift |
| **tracvla_spatial/untrained** | +0.048 | [-0.800, -0.579] | -0.701 | 方向翻转, -0.75 shift |
| nora_spatial/untrained | 0.089 | [-0.047, 0.061] | 0.003 | delta outside CI |
| openvla_goal/trained | 0.116 | [-0.253, -0.012] | -0.142 | 方向翻转 |
| openvla_goal/untrained | 0.148 | [-0.062, 0.075] | -0.003 | delta outside CI |
| openvla_long/trained | 0.076 | [-0.054, 0.060] | -0.005 | delta outside CI |
| openvla_object/trained | 0.055 | [-0.031, 0.052] | 0.006 | delta just outside CI |
| openvla_spatial/untrained | 0.073 | [-0.079, 0.060] | -0.016 | delta outside CI |
| tracvla_goal/untrained | 0.065 | [-0.187, -0.004] | -0.086 | 方向翻转 |
| tracvla_long/trained | 0.358 | [0.030, 0.336] | 0.156 | delta just outside CI |
| tracvla_spatial/trained | 0.156 | [0.012, 0.150] | 0.075 | delta marginally outside |

**共同特征**：boot_mean 系统性低于 canonical delta（除 nora_goal/trained 外）。这符合 duplicate 稀释导致的 R² 退化——但退化对 peak layer 和 exit layer 的影响不同，所以 delta 的偏移方向取决于哪一层更脆弱。

---

## 任务 4：tracvla_long/untrained 进度

**仍在跑**，当前处于特征提取阶段：
- PID 723018, 100% CPU
- 进度：2750/5000 samples, Task 5/10
- 速率 ~50 samples/17s → 剩余 ~2250 samples ≈ 13 min
- 提取完成后还需 bootstrap 1000 iterations

预计总完成时间：~25-30 分钟后。

---

## 建议修复

### 方案 A（推荐）：Monte Carlo Cross-Validation 替代有放回 bootstrap

每次 iteration 从 100 demos 中无放回随机抽 80 做 train、20 做 test，重复 1000 次。避免所有 duplicate/leakage 问题，CI 自然以 canonical delta 为中心。

```python
def _bootstrap_single(b):
    perm = _MP_RNGS[b].permutation(_MP_UNIQUE_DEMOS)
    tr_demos = perm[:_MP_N_TRAIN]
    te_demos = perm[_MP_N_TRAIN:]
    # ... 其余不变
```

### 方案 B（最小改动）：去重 test demos

```python
tr_set = set(resampled[:_MP_N_TRAIN].tolist())
te_demos = [d for d in resampled[_MP_N_TRAIN:] if d not in tr_set]
te_demos = list(set(te_demos))  # deduplicate test too
```

但这不解决 train 中的 duplicate 问题，boot R² 仍会偏离 canonical。

### 方案 C：Paired bootstrap

分别对 canonical train demos 和 canonical test demos 做有放回重采样，保持 train/test 不重叠。最保守但 variance 最小。

**我推荐方案 A**——实现简单、统计学上最干净、CI 解释最直接。

---
