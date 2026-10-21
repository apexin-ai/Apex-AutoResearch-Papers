# diag exp014 probe r1 constant

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp014-probe-r1-constant_20260518T174334_result.json`
- **Structured JSON:** [`abb0f8e270b0a06fef5f.json`](../../sessions/ab/abb0f8e270b0a06fef5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因确认

**Probe 训练完全失败**，原因是 feature 未归一化导致梯度爆炸→sigmoid 饱和→梯度死亡。

复现数据：
```
Epoch 1: loss=1.4623  grad_norm=154.22  (梯度爆炸)
Epoch 2: loss=49.9229 grad_norm=0.0000  (sigmoid 饱和，梯度归零)
Epoch 3+: loss=50.0000 grad_norm=0.0000  (永久卡死)
```

### 机制

1. exp-001 activations 的 per-sample norm 平均 **372**（layer 32/33 的 norm 高达 840-978）
2. `nn.Linear(4096,1)` 随机初始化权重 ∈ [-0.016, 0.016]，但 x 的大 norm 使得初始 logits 已偏移（mean=-2.35）
3. Adam 第一步更新（grad_norm=154）直接将权重推到极端 → sigmoid 输出对所有样本 = 0.0（float32 精度下）
4. `BCELoss(-log(0))` 对 50% positive 样本 → loss ≈ 50。sigmoid 导数为 0 → 梯度永久为零

### Probe 权重统计（当前保存的 probe.pt）
- Weight shape: [1, 4096]，norm=3.85
- 对 **全部 362 个** exp-001 样本: P(syc) = 0.0000, R1 = 1.0000

### 修复验证

标准化 features + BCEWithLogitsLoss 后：
```
acc=0.9945, AUROC=0.9999
P(syc)|invalid_pressure: mean=0.9671
P(syc)|valid_correction: mean=0.0331
```

### 需要修复的文件

1. **`probe_module.py`**:
   - `train_probe()`: 对特征做 standardization (zero-mean, unit-var)，用 `BCEWithLogitsLoss` 替换 `sigmoid + BCELoss`
   - `LinearProbe`: 将归一化参数 (mean, std) 存为 `register_buffer`，在 `forward()` 中自动归一化
   - `save_probe()` / `load_probe()`: 保存/加载归一化统计量

2. **`run_exp014_dryrun.py`** 和 **`run_exp014_continuous_probe.py`** 中的 `ProbeTrainer.compute_r1()`: 如果归一化已 bake 进 `LinearProbe.forward()`，则 **无需改动**。

### 修复建议

需要我直接修改 `probe_module.py` 实现上述修复吗？

---
