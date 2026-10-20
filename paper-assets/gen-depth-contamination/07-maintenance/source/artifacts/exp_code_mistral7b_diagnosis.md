# exp_code_mistral7b 诊断报告

**日期**: 2026-05-19  
**结论**: 实验已成功完成，cron 监控系统误判为 failed

## 根本原因：监控误报（非实验失败）

实验于 07:50 启动，18:54 正常完成（耗时约 11 小时），进程以 exit code 0 退出。cron 系统误判原因：

1. **日志路径不匹配**: 监控期望的日志在 `~/runs/gen-depth-contamination/exp_code_mistral7b.log`（不存在）。实际日志写入 `results/exp_code_mistral7b.log`，且早期输出还写到了 `/dev/pts/3`（终端 session）
2. **无 W&B metrics**: pipeline 未配置 W&B 上报
3. **无 sentinel 文件**: pipeline 正常退出但未写 sentinel，监控检测到进程死亡即判定失败

## 数据完成情况

| Depth | 文件 | 行数 | 大小 | 时间 |
|-------|------|------|------|------|
| 0 | depth_0.jsonl | 5,500 | 4.1M | 07:06 |
| 1 | depth_1.jsonl | 5,500 | 4.1M | 09:59 |
| 2 | depth_2.jsonl | 5,500 | 4.3M | 12:09 |
| 3 | depth_3.jsonl | 5,500 | 4.3M | 14:19 |
| 4 | depth_4.jsonl | 5,500 | 4.2M | 16:30 |
| 5 | depth_5.jsonl | 5,500 | 4.2M | 18:40 |

features.csv (8.7M) 已生成。**全部 6 个 depth 完整生成，共 33,000 行。**

## 分析结果

所有分析阶段均已完成，结果文件：
- `summary.txt` / `jsd.json` / `pairwise_auc.json` / `ordinal_results.json` / `feature_importance.json`

关键指标：
- **K\* = 2**（AUC > 0.60 的最大 depth）
- Pairwise AUC: 0→1 = 0.919, 1→2 = 0.615, 2→3 = 0.529, 3→4 = 0.529, 4→5 = 0.510
- Pairwise JSD: 0→1 = 0.047, 1→2 = 0.012, 之后趋近 0.003
- Ordinal MAE = 1.32, Accuracy = 0.32

## 是否需要重跑

**不需要。** 实验已完整完成，所有产出文件存在且内容正确。

## 建议修复（针对监控系统）

1. 将该实验在 cron 系统中标记为 completed
2. 后续实验启动时确保日志路径与监控期望路径一致（`~/runs/gen-depth-contamination/` 下）
3. 考虑在 pipeline 正常退出时写入 sentinel 文件，避免监控误判
