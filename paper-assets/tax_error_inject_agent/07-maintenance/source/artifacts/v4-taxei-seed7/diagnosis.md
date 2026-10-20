# v4-taxei-seed7 诊断报告

## 结论：训练成功完成

Cron 采集 metrics 时训练刚启动（step 180/3387），误判为异常。实际训练正常跑完全部 3387 steps。

## 训练结果

| 指标 | 值 |
|------|-----|
| 总 steps | 3387/3387 |
| epochs | 3.0 |
| train_loss | 0.3568 |
| 最终 step loss | 0.1753 |
| token_acc (avg) | 0.9009 |
| 最终 step token_acc | 0.9328 |
| 训练时长 | 1h 49m 52s (6591.9s) |
| train_speed | 1.946 s/it |
| peak memory | 18.49 GiB |
| exit code | 0 |
| 结束时间 | 2026-05-15 23:30:47 |

## Checkpoint

- 路径: `/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387`
- adapter_model.safetensors: 174.7 MB
- optimizer.pt: 349.6 MB

## W&B

未使用 wandb，日志中无 wandb 相关记录。

## 与 v4-vanilla-seed7 对比

| 指标 | taxei-seed7 | vanilla-seed7 |
|------|-------------|---------------|
| 总 steps | 3387 | 1635 |
| train_loss | 0.3568 | 0.4153 |
| 训练时长 | 1h 49m | 59m |
| exit code | 0 | 0 |

taxei 数据集约为 vanilla 的 2 倍（steps 3387 vs 1635），loss 更低（0.357 vs 0.415）。

## GPU 状态

cuda:3 当前空闲（0 MiB, 0% util）。

## 建议

无需重跑。训练已成功完成。
