# exp_deberta_c4_1b5 诊断报告

## 结论：训练正常完成，应将状态从 "failed" 改为 "success"

## 日志尾部关键信息

日志路径：`/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4_1b5/qwen_rw.log`

- 3 个 epoch 全部完成，loss 持续下降（1.43 → 1.24 → 1.14）
- 最终输出 pairwise AUC 结果和 K* 值
- 最后一行：`06:57:36 [INFO] Done.`
- **无任何错误、OOM、CUDA error 或 traceback**

## 核心指标

| Pair | DeBERTa AUC | 95% CI | OBD Baseline | Delta |
|------|-------------|--------|-------------|-------|
| 0v1 | 0.9923 | [0.9907, 0.9937] | 0.987 | +0.0053 |
| 1v2 | 0.7052 | [0.6977, 0.7129] | 0.6262 | +0.0790 |
| 2v3 | 0.5988 | [0.5905, 0.6063] | 0.5496 | +0.0492 |
| 3v4 | 0.5698 | [0.5626, 0.5774] | 0.5294 | +0.0404 |
| 4v5 | 0.5475 | [0.5404, 0.5542] | 0.5182 | +0.0293 |

K*(theta=0.6) = 2，耗时 3441 秒（约 57 分钟）

## 结果文件

```
/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4_1b5/
├── qwen_rw.json      (1.3KB, 2026-05-20 06:57)  # 完整 metrics
├── qwen_rw.log       (15KB,  2026-05-20 06:57)   # 训练日志
└── qwen_rw_oof.npz   (812KB, 2026-05-20 06:57)   # OOF predictions
```

## 误判原因

Cron 监控检测进程死亡且无 W&B sentinel，自动判定为 failed。但该实验不使用 W&B，训练实际已正常完成并输出全部结果文件。属于 false positive。
