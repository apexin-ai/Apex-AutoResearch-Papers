# run gate1b vip mlp

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_gate1b-vip-mlp_20260515T061045_result.json`
- **Structured JSON:** [`f4927678afa7c89edcf4.json`](../../sessions/f4/f4927678afa7c89edcf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Base64 输出被截断，无法直接传输。服务器上的 artifacts/ 已有所有产出文件，本地也已注册 JSON。可以报告结果了。

## Gate 1(b) MLP on VIP Features 结果

### 训练配置
- 特征: VIP embeddings (1024-dim, ResNet50-based)
- 数据: 50 条 LIBERO-Object 轨迹 (40 train / 10 test)
- 训练样本: 6296 train, 1512 test
- MLP 架构: Linear(1024→512) → ReLU → Linear(512→128) → ReLU → Linear(128→1) → Sigmoid
- 超参: lr=1e-3, batch_size=256, patience=10, seed=42

### MLP 训练结果

| Feature | Test R² | Test MAE | Best Epoch | Early Stop |
|---------|---------|----------|------------|------------|
| VIP (1024-dim) | **0.9847** | **0.0280** | 18 | epoch 28 |

### Gate 1(b) 判定: **PASSED** (R² = 0.9847 > 0.8 阈值)

### 产出文件 (westd-34887:/root/temp-adv-distill-vla/artifacts/)
| 文件 | 大小 | 说明 |
|------|------|------|
| gate1b_results.json | 261B | 结果 JSON |
| gate1b_mlp_layer_0.png | 115K | predicted vs actual t/T 散点图 |
| gate1b_training_curves.png | 42K | 训练/验证 loss 曲线 |
| gate1b_mlp_layer_0.pt | 2.3M | MLP checkpoint |

### 关键观察
- VIP 1024 维特征经 MLP 非线性变换后 R²=0.9847，远超 0.8 阈值
- MAE 仅 0.028，即平均预测误差不到 3% 的轨迹进度
- 训练仅需 18 个 epoch 即收敛（28 epoch 触发 early stop）
- 虽然 raw cos_sim Spearman ρ=0.727（Gate 1(c) 未严格通过），但 MLP 能有效学习非线性映射将 progress structure 放大到 R²≈0.98

---
