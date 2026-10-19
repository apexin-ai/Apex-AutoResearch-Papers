# m2_full_qwen 训练状态检查

**时间**: 2026-05-14 ~23:00 CST (15:00 UTC)
**服务器**: bjb1-42106

## GPU 状态

| GPU | 型号 | VRAM 使用 | 利用率 | 用途 |
|-----|------|----------|--------|------|
| cuda:0 | RTX PRO 6000 Blackwell | 50.5 / 97.9 GB | 99% | m2_full_qwen random_s43 |
| cuda:1 | RTX PRO 6000 Blackwell | 55.4 / 97.9 GB | 100% | m2_full_starcoder random_s42 |

## 训练进度总览 (9 runs)

| # | Run | 状态 | 备注 |
|---|-----|------|------|
| 1 | random_s42 | ✅ 完成 | EXIT_CODE=0, 有 final + best checkpoints |
| 2 | **random_s43** | 🔄 **进行中** | epoch 1, step 900/1405 |
| 3 | random_s44 | ⏳ 排队 | |
| 4 | embedding_s42 | ⏳ 排队 | |
| 5 | embedding_s43 | ⏳ 排队 | |
| 6 | embedding_s44 | ⏳ 排队 | |
| 7 | dataflow_s42 | ⏳ 排队 | |
| 8 | dataflow_s43 | ⏳ 排队 | |
| 9 | dataflow_s44 | ⏳ 排队 | |

## random_s43 当前详情

- **开始时间**: 19:24 CST
- **已运行**: ~3.5 小时
- **进度**: epoch 1, step 900 / 2810 total (2 epochs x 1405 steps) ≈ 32%
- **训练速度**: ~4.2 steps/min

### Loss 趋势 (epoch 1)

| Step | Loss |
|------|------|
| 50 | 0.6791 |
| 100 | 0.7159 |
| 150 | 0.4708 |
| 200 | 0.4745 |
| 300 | 0.2247 |
| 500 | 0.3376 |
| 650 | 0.0693 |
| 850 | 0.0410 |
| 900 | 0.1186 |

Loss 整体下降良好，从 ~0.68 降至 ~0.04-0.12 区间。

### 最新 Eval Metrics (step 500)

| 指标 | 值 |
|------|-----|
| val_loss | 0.4476 |
| Recall@1 | 0.5357 |
| Recall@5 | 0.9699 |
| Recall@10 | 1.0000 |

下次 eval 在 step 1000。

### Checkpoints

- `best_by_val_loss` (保存于 21:29)
- `best_by_recall_at_1` (保存于 21:29)

## 时间估算

| 项目 | 估算 |
|------|------|
| random_s43 剩余 | ~7.6 小时 |
| 每个后续 run | ~11.2 小时 |
| 剩余 7 个 runs | ~78.4 小时 |
| **总剩余** | **~86 小时 (≈ 3.6 天)** |
| **预计全部完成** | **~5月18日 05:00 CST** |

## 磁盘

- `/root/autodl-tmp/`: 186G / 250G (75%), 剩余 65G
- 每个 run 的 checkpoint (LoRA) 约 200-500MB，9 runs 总计 ~2-5GB，空间充足

## 其他进程

- cuda:1 同时跑 m2_full_starcoder random_s42（PID 76627，已运行 ~20.5h）
- M1 数据提取 (batch_extract.py + codeql) 也在后台运行
