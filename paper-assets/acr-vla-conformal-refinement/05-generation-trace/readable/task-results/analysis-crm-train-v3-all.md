# analysis crm train v3 all

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crm-train-v3-all_20260514T182857_result.json`
- **Structured JSON:** [`0254053dc70e3adbd005.json`](../../sessions/02/0254053dc70e3adbd005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 查询失败（可能未配置或训练未接入 W&B），日志数据已足够。以下是完整分析。

---

## CRM v3 训练实验结果汇总

### 指标表

| 指标 | perdof (full) | scalar_unc | obs_only |
|------|:---:|:---:|:---:|
| **best_val_loss** | **1.191387** | 1.192936 | 1.193424 |
| **best_epoch** | 50 | 50 | 50 |
| **final_train_loss** | 1.874177 | 1.915589 | 1.885808 |
| **total_epochs** | 50/50 | 50/50 | 50/50 |
| **CRM params** | 337,438 | — | 327,198 |
| **checkpoint size** | 1.3M | 1.3M | 1.3M |
| **EXIT_CODE** | 0 | 0 | 0 |

训练数据：2402 samples, K=10, obs_dim=960, spatial benchmark, norm_stats 已加载。

---

### 三模型对比

**perdof vs scalar_unc**：perdof 略优，差异 0.001549（0.13%）。几乎可以忽略。

**perdof vs obs_only**：perdof 略优，差异 0.002037（0.17%）。同样微不足道。

**关键发现：三个 input_mode 的 val_loss 几乎完全相同（1.191–1.193 区间内）。** conformal features（per-DoF scores、scalar uncertainty）对 CRM 学习几乎没有贡献。obs_only 仅用观测特征就达到了同等水平。

所有三个实验的 val_loss 曲线都是单调递减、到 epoch 50 仍在缓慢下降（未完全收敛），但改善幅度已极小（epoch 45→50 改善 < 0.001）。

---

### 与 v2 对比

| 模型 | v2 val_loss | v3 val_loss | 变化 |
|------|:---:|:---:|:---:|
| perdof | 0.050501 | 1.191387 | +22.6x |
| scalar_unc | 0.047202 | 1.192936 | +24.3x |
| obs_only | 0.018 (旧版) | 1.193424 | +65.3x |

**v3 loss 比 v2 高约 24 倍。** 这不应理解为"退化"——v2 的低 loss 是在 buggy 6D state + 未归一化输入上计算的，loss scale 完全不同。D018 归一化修复后损失函数的输入分布根本性改变，两者不可直接比较。

v2 中 obs_only（0.018）远优于 perdof（0.050），暗示 v2 的 conformal features 因 1500x scale 差异实际是在注入噪声。v3 归一化后三者拉平，印证了 D018 诊断。

---

### 结论

**conclusion: negative**

训练本身成功完成（3/3 正常退出，checkpoint 已保存），但实验结果是 **negative result**：

1. 归一化修复消除了 scale 差异导致的伪影，训练过程稳定
2. 但修复后 conformal features 的边际增益仅 0.17%，统计上不显著
3. CRM 几乎完全依赖 observation features，conformal scores 未提供额外信息

这对 conformal refinement 假说是一个挑战——CRM 无法从 conformal scores 中学到有用的 correction signal。可能原因：
- conformal scores 与 observation 高度共线（信息冗余）
- 当前 CRM 架构（337K params, 256 hidden）容量不足以利用 conformal features
- K=10 的 conformal set 信息量不足

---

### 建议的 registry 字段值

```yaml
# perdof
conclusion: negative
metrics:
  best_val_loss: 1.191387
  best_epoch: 50
  final_train_loss: 1.874177

# scalar_unc
conclusion: negative
metrics:
  best_val_loss: 1.192936
  best_epoch: 50
  final_train_loss: 1.915589

# obs_only
conclusion: negative
metrics:
  best_val_loss: 1.193424
  best_epoch: 50
  final_train_loss: 1.885808
```

---
