# m2_full_starcoder 训练状态检查

**检查时间**: 2026-05-14 ~23:00  
**服务器**: bjb1-42106, cuda:1  
**PID**: 74122 (alive, uptime 21h20m, 子进程 PID 76627 占用 GPU 55.4GB)

---

## 总体进度

| # | Run | Steps | 状态 |
|---|-----|-------|------|
| 1 | random_s42 (3ep) | 3700 / 4242 | **训练中 (87%)** |
| 2 | random_s43 (2ep) | 0 / 2828 | 待跑 |
| 3 | random_s44 (2ep) | 0 / 2828 | 待跑 |
| 4 | embedding_distance_s42 (3ep) | 0 / 4242 | 待跑 |
| 5 | embedding_distance_s43 (2ep) | 0 / 2828 | 待跑 |
| 6 | embedding_distance_s44 (2ep) | 0 / 2828 | 待跑 |
| 7 | dataflow_aware_s42 (3ep) | 0 / 4242 | 待跑 |
| 8 | dataflow_aware_s43 (2ep) | 0 / 2828 | 待跑 |
| 9 | dataflow_aware_s44 (2ep) | 0 / 2828 | 待跑 |

**全局进度**: 3700 / 26866 steps (**13.8%**)

---

## 当前 Run: random_s42

- Strategy: random, Seed: 42, Epochs: 3
- 1414 batches/epoch, total 4242 steps
- 当前: Epoch 3, step 3700
- 距离完成还差 542 steps

### Eval 历史

| Step | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| 500 | 0.6194 | 0.4352 | 0.9054 | 1.0 |
| 1000 | **0.6134** | 0.4537 | **0.9201** | 1.0 |
| 1500 | 0.6528 | 0.4490 | 0.9057 | 1.0 |
| 2000 | 0.6698 | 0.4456 | 0.9007 | 1.0 |
| 2500 | 0.6342 | **0.4604** | 0.9117 | 1.0 |
| 3000 | 0.6516 | 0.4544 | 0.9077 | 1.0 |
| 3500 | 0.6588 | 0.4534 | 0.9057 | 1.0 |

### Best Metrics

- **Best val_loss**: 0.6134 @step1000 (Epoch 1 末)
- **Best R@1**: 0.4604 @step2500 (Epoch 2 末)
- R@10 恒为 1.0

### 观察

- val_loss 在 step1000 后持续上升，过拟合趋势明显
- R@1 在 step2500 达到峰值 0.4604 后回落
- Epoch 3 (step 2800+) 未能进一步提升任何指标，loss 已过拟合
- 对 s43/s44 (2 epochs) 的设计是合理的——第 3 个 epoch 没有带来收益

---

## Checkpoints

仅 random_s42 有 checkpoint：
- `best_by_val_loss/model.pt` (step1000 snapshot)
- `best_by_recall_at_1/model.pt` (step2500 snapshot)

---

## 时间估算

- 训练开始: ~02:30, 已运行 ~20.5h 完成 3700 steps
- **每步耗时**: ~20s
- **random_s42 剩余**: 542 steps ≈ **3h**
- **剩余 8 runs**: 22624 steps ≈ **125h (5.2天)**
- **总剩余**: ~128h ≈ **5.3天** (预计完成: ~5月20日)

---

## 数据准备状态

Phase 1 (embedding negatives) 已全部完成，18 个训练/验证文件 + dataflow_graph.json 均已就绪（共 13GB），后续 runs 可直接开始训练无需等待数据准备。
