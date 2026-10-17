# n2_deberta_finetune_001 训练状态检查

**检查时间**: 2026-05-15 20:48 UTC
**服务器**: gpu-6000pro-2

## 状态: 仍在运行

PID 231453, 启动于 20:12, 运行命令:
```
python src/n2_deberta_finetune.py --model_name /root/autodl-tmp/models/deberta-v3-base --output_dir results/n2_deberta_finetune --gpu 0
```

日志路径: `/root/runs/recursive_gen_depth_est/n2_deberta_finetune_001.log` (280 行)

## 进度

- **Fold 1/5 已完成** (3 epochs × 1000 steps)
- 当前正在进行 Fold 2+
- 预估总时间 ~3 小时 (5 folds × ~36 min/fold)，已跑 ~36 分钟

## Fold 1 训练日志

| Epoch | train_loss | val_acc |
|-------|-----------|---------|
| 1/3   | 0.7915    | 55.00%  |
| 2/3   | 0.4958    | 48.95%  |
| 3/3   | 0.3314    | 50.40%  |

**过拟合明显**: loss 从 0.79→0.33 持续下降，但 val_acc 在 epoch 1 达到峰值 55.0% 后反而下降。

## GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| GPU 0 | 21349MiB / 97887MiB | 100% | PID 231453 (python) |
| GPU 1 | 0MiB / 97887MiB | 0% | 无 |

## 旧 results.json (残留)

results 目录下 19:45 生成的 results.json 来自一次失败运行:
- n_folds=1, epochs=1, elapsed=3.5s
- 所有指标全为 0.0
- 不代表当前运行结果

## 与 RF Baseline 对比

| 方法 | Accuracy |
|------|----------|
| RF baseline | **78.2%** |
| DeBERTa Fold 1 (best val) | 55.0% |

DeBERTa Fold 1 val_acc 远低于 RF baseline 23.2 个百分点。

## 配置

```json
{
  "max_len": 512,
  "batch_size": 16,
  "lr": 2e-05,
  "epochs": 3,
  "warmup_ratio": 0.1,
  "seed": 42
}
```
