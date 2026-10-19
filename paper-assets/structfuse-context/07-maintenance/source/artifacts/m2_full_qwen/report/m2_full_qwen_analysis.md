# m2_full_qwen 实验分析

> 分析时间: 2026-05-14
> 服务器: bjb1-42106
> 模型: Qwen2.5-Coder-3B + LoRA (r=16)

## 实验完成状态

**严重问题：9 个 runs 中只有 1 个完成。**

| Run | 状态 | 说明 |
|-----|------|------|
| random_s42 | ✅ 完成 | 3 epochs, 4242 steps, 所有 checkpoint 已保存 |
| random_s43 | ❌ 未完成 | 加载模型后停止，无训练步骤输出 |
| random_s44 | ❌ 未开始 | - |
| embedding_distance_s42 | ❌ 未开始 | - |
| embedding_distance_s43 | ❌ 未开始 | - |
| embedding_distance_s44 | ❌ 未开始 | - |
| dataflow_aware_s42 | ❌ 未开始 | - |
| dataflow_aware_s43 | ❌ 未开始 | - |
| dataflow_aware_s44 | ❌ 未开始 | - |

**原因分析**：wrapper script (`run_m2_full_qwen.sh`) 的 SEEDS 被改为 `(43 44)`（不含 42），s42 是更早独立跑的。s43+ wrapper 在 19:24:14 启动 random_s43，模型加载完成后无后续输出（可能 OOM / 进程被 kill / 磁盘满）。wrapper log (`m2_full_qwen.log`) 只有 4 行。

---

## random_s42 完整 Metrics

### 训练配置
- batch_size: 8, lr: 2e-5, warmup: 0.1, temperature: 0.07
- num_negatives: 7, hard_negative_ratio: 0.5
- max_seq_length: 2048, gradient_checkpointing: True
- LoRA r=16, proj_dim=256
- early_stopping_patience: 0 (disabled)
- 1414 batches/epoch × 3 epochs = 4242 total steps

### Eval Metrics (每 500 步)

| Step | Epoch | val_loss | R@1 | R@5 | R@10 |
|------|-------|----------|------|------|------|
| 500 | ~0.35 | 0.4869 | 0.5332 | 0.9540 | 1.0 |
| 1000 | ~0.71 | **0.4651** | **0.5527** | **0.9594** | 1.0 |
| 1500 | ~1.06 | 0.5365 | 0.5228 | 0.9550 | 1.0 |
| 2000 | ~1.41 | 0.5162 | 0.5228 | 0.9544 | 1.0 |
| 2500 | ~1.77 | 0.5264 | 0.5268 | 0.9564 | 1.0 |
| 3000 | ~2.12 | 0.5406 | 0.5356 | 0.9493 | 1.0 |
| 3500 | ~2.47 | 0.5601 | 0.5336 | 0.9493 | 1.0 |
| 4000 | ~2.83 | 0.5510 | 0.5346 | 0.9440 | 1.0 |
| Final | 3.0 | 0.5456 | 0.5503 | 0.9463 | 1.0 |

### Best Checkpoints

| Criterion | Step | val_loss | R@1 |
|-----------|------|----------|------|
| Best val_loss | 1000 | 0.4651 | 0.5527 |
| Best R@1 | 1000 | 0.4651 | 0.5527 |

两个 best 指标在同一步取得（step 1000）。

### 训练动态
- **峰值在 epoch 1 中期** (step 1000)，之后 val_loss 持续上升（overfitting）
- R@1 在 epoch 2-3 下降到 0.522-0.535 范围，最终 eval 有所回升到 0.5503
- R@5 从 0.959 逐步下降到 0.946
- R@10 始终为 1.0（天花板效应）
- **3 epochs 过多**：最佳点在 epoch 1 就达到，后续只是 overfit。D026 决策（s43/s44 跑 2 epochs）方向正确，但即使 2 epochs 也偏多

---

## Checkpoint 路径

```
/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/
├── best_by_val_loss/     # step 1000, val_loss=0.4651, R@1=0.5527
│   ├── model.pt
│   └── training_config.json
├── best_by_recall_at_1/  # step 1000, R@1=0.5527
│   ├── model.pt
│   └── training_config.json
└── final/                # step 4242, R@1=0.5503
    ├── model.pt
    └── training_config.json
```

其他 8 个 run 无有效 checkpoint。

---

## vs Pilot (m2_embed_verify) 对比

| Strategy | Pilot R@1 | Full R@1 (s42 best) | Delta |
|----------|-----------|---------------------|-------|
| random | 0.5357 | 0.5527 | +0.0170 |
| embedding_distance | 0.5557 | N/A | - |
| dataflow_aware | 0.5436 | N/A | - |

Full data random_s42 比 pilot random 高 +1.7pp，说明更多训练数据有帮助。但由于 embedding/dataflow runs 未完成，**无法验证核心假设**（embedding > random 在 full data 上是否成立）。

---

## 统计分析

**无法进行。** 只有 random strategy 的 1 个 seed 完成。需要至少：
- random: 3 seeds → 计算 mean ± std
- embedding_distance: 3 seeds → 计算 mean ± std
- dataflow_aware: 3 seeds → 计算 mean ± std

才能做 strategy 间的统计比较。

---

## 结论

1. **实验未完成**：9 runs 中只有 random_s42 完成训练。random_s43 启动后停止（疑似 OOM/crash），其余 7 个 run 未启动。
2. **random_s42 结果**：best R@1=0.5527 (step 1000)，比 pilot random (+1.7pp) 有改善，确认 full data 有帮助。
3. **过拟合严重**：最佳点在 epoch 1 中期，3 epochs 明显过多。建议后续 runs 用 1-2 epochs + early stopping (patience=2)。
4. **核心假设未验证**：embedding > random 在 full data 上是否成立？无法回答，需要重跑 embedding 和 dataflow runs。

## 行动建议

1. **诊断 random_s43 失败原因**：查看 GPU 内存状态、dmesg、是否有 OOM kill 记录
2. **重启剩余 8 runs**：修复问题后重跑 s43/s44 和所有 embedding/dataflow runs
3. **调整训练参数**：考虑 num_epochs=2, early_stopping_patience=2（s43+ 脚本已设置）
