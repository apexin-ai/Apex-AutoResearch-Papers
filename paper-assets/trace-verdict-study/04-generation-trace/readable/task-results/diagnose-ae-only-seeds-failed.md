# diagnose ae only seeds failed

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ae_only_seeds_failed_20260516T062804_result.json`
- **Structured JSON:** [`ff425969d9d032335f1f.json`](../../sessions/ff/ff425969d9d032335f1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个实验都成功完成了，不是失败。** Cron 误判。

## 日志结果

### ae_only_seed456
- 训练完成：444/444 steps, 3 epochs, train_loss=0.0574, runtime=2h34m
- 评估完成：**Accuracy 99.9%** (95% CI: 99.7%–100.0%), pass F1=1.00, fail F1=1.00
- 结果已保存到 `eval_results.json` 和 `predictions.jsonl`

### ae_only_seed123
- 训练完成：444/444 steps, 3 epochs, train_loss=0.0583, runtime=2h25m
- 评估完成：**Accuracy 99.1%** (95% CI: 98.5%–99.6%), pass F1=0.99, fail F1=0.98
- 结果已保存到 `eval_results.json` 和 `predictions.jsonl`

## 误判原因

两个进程正常退出（return_code=0），训练+评估全部跑完。Cron 检测到"进程不存在"时判定为 dead，但实际是进程已完成退出。可能是 sentinel 文件写入时机或 W&B 上报延迟导致 cron 在进程结束后未识别到成功标记。

## 当前服务器状态
- **GPU 0**: 正在跑 `label_only_seed123`（41GB VRAM, 100% util）
- **GPU 1**: 空闲
- 磁盘：数据盘 47%，根分区 80%（剩 6.2GB）
- 无 ae_only 残留进程

**结论：无需重试，两个实验已成功产出结果。需要修复 cron 监控的完成检测逻辑。**

---
