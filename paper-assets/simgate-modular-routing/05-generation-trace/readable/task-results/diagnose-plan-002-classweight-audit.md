# diagnose plan 002 classweight audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-002-classweight-audit_20260514T051944_result.json`
- **Structured JSON:** [`ebb2f463ef99c775fc71.json`](../../sessions/eb/ebb2f463ef99c775fc71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集到所有关键证据。以下是审计结论。

## 审计结论

### Q1: class_weights 是否生效？
**YES** — 真正生效了。

代码证据：
- `WeightedCETrainer.compute_loss()`（`router_sft_train.py:264-270`）正确覆盖了 HF Trainer 的 `compute_loss`，使用 `CrossEntropyLoss(weight=self._class_weights.to(logits.device))`
- class_weights tensor 被显式 `.to(logits.device)` 搬到正确设备
- `main()` 中通过 `compute_class_weights("auto", train_samples)` 计算后传入 `WeightedCETrainer(class_weights=class_weights, ...)`

运行时证据：
- 日志确认 `Class weights: [11.07, 0.52]`
- **关键铁证**：trainer_state 的 grad_norm 呈双峰分布——大部分 step 为 0.3~0.8，但间歇性飙升至 42~44。这种 ~80× 的梯度差异**只有在 loss 中使用了 11.07× 权重时才会出现**，普通 CE loss 不会产生这种模式

### Q2: WeightedRandomSampler 是否生效？
**YES** — 真正生效了。

代码证据：
- `WeightedCETrainer.get_train_dataloader()`（`router_sft_train.py:275-282`）正确覆盖了 Trainer 的 dataloader 创建方法
- 当 `self._weighted_sampler is not None` 时，返回自定义 `DataLoader(sampler=self._weighted_sampler)`，完全绕过了 Trainer 默认的 sampler 逻辑
- sampler 权重计算正确：`1.0 / train_label_counts[label]`，确保 minority 样本被高概率抽到

运行时证据：
- 日志确认 `Upsampling enabled: WeightedRandomSampler with N draws/epoch`

### Q3: 退化根因

**class_weights 和 oversampling 都生效了，但无法在 1 epoch + batch_size 4 的条件下克服 95.4%/4.6% 的极端不平衡。**

具体原因：

1. **只跑了 1 epoch**：trainer_state 显示 `num_train_epochs: 1, max_steps: 383`。而 `launch_plan002.sh` 配置的是 3 epoch——dryrun 用了不同的参数
2. **batch_size=4 导致梯度极不稳定**：trainer_state 显示 `train_batch_size: 4`（launch script 配的是 32）。权重比 11.07:0.52 ≈ 21:1，在 batch=4 下产生双峰梯度（0.5 vs 42），优化器在两种极端之间震荡
3. **Loss 未收敛**：loss 在 0.17~1.03 之间震荡，最后一步仍为 0.42，eval_loss=0.48。模型没学到有效决策边界
4. **"全预测 deterministic"是 1 epoch 下的最优捷径**：即使有 11× 权重，训练集仅 ~72 个 internal 样本（被重复采样），1 epoch 不足以学出泛化特征。模型走了最省力路径——全部预测 majority 类

### 补充发现

**dryrun 的实际运行参数与 `launch_plan002.sh` 不一致：**

| 参数 | launch_plan002.sh | 实际 dryrun |
|------|------------------|-------------|
| epochs | 3 | 1 |
| batch_size | 32 | 4 |
| output_dir | results/plan_002_router/ | checkpoints/plan-002-dryrun/ |

**Registry notes 说"未启用 class_weights/oversampling"是错误的。** 日志和梯度模式都证明两者均已启用。

### 建议

正式训练需要修改：
1. **epochs ≥ 3**（让模型充分见过 minority 样本）
2. **batch_size ≥ 16**（减少梯度方差，让每个 batch 的 loss 信号更稳定）
3. **降低 class_weight 比例**：11:0.5 太激进，建议 `sqrt` 缩放（如 3.3:0.72）或使用 focal loss
4. **监控 per-class loss**：在 eval 时分别输出 internal/deterministic 的 loss 和 recall，及早发现退化

---
