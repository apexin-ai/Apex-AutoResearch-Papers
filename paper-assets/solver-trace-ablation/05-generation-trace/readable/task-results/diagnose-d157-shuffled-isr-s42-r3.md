# diagnose d157 shuffled isr s42 r3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d157-shuffled-isr-s42-r3_20260520T162218_result.json`
- **Structured JSON:** [`787ca18fb5d4364e073b.json`](../../sessions/78/787ca18fb5d4364e073b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 训练已成功完成

日志确认 500/500 步全部跑完：

```
2026-05-21 00:18:12,732 INFO Saving final model
2026-05-21 00:18:24,903 INFO Final reward stats: {'parse_rate': 1.0, 'prove_rate': 0.117, 'mean_isr': 0.05850817099567102}
2026-05-21 00:18:24,903 INFO Done.
train_runtime: 4239.3s, train_loss: 0.0118, epoch: 2.0
```

### EXIT_CODE=129 原因

Cron 监控在训练完成后发送了 SIGHUP（因为找不到 W&B metrics 而判定失败）。但训练进程在收到信号前已经打印了 "Done." 并保存了模型。这是 **误判**——`--no_wandb` 下无 W&B 指标是预期行为。

### Output 目录完整

```
/root/autodl-tmp/outputs/d157_shuffled_isr_s42_r3/
├── model-00001-of-00002.safetensors  (4.6GB)
├── model-00002-of-00002.safetensors  (2.9GB)
├── checkpoint-500/
├── reward_log.jsonl
├── config.json, tokenizer files, etc.
```

### 最终指标

| 指标 | 值 |
|------|-----|
| prove_rate | 0.117 |
| mean_isr | 0.0585 |
| parse_rate | 1.0 |
| train_loss | 0.0118 |

### d157-shuffled-isr-s43 状态

正在运行（PID 800347，00:20 启动，GPU 0）。eval_sta.py 也已在对 s42_r3 模型做评估（PID 801090）。

---
