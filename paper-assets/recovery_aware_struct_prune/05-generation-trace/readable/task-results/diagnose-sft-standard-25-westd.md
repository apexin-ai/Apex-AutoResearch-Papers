# diagnose sft standard 25 westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_standard_25_westd_20260516T164827_result.json`
- **Structured JSON:** [`8141112d501bc74ac585.json`](../../sessions/81/8141112d501bc74ac585.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练实际上成功完成了，不是真正的失败。**

## 诊断结果

**根因**：训练正常完成后进程退出，cron 监控将正常退出误判为进程崩溃（process dead），反复尝试重启并最终标记为 failed。

**关键日志行**：
```
{'train_runtime': '2492', 'train_samples_per_second': '5.998', 'train_steps_per_second': '0.751', 'train_loss': '0.8381', 'epoch': '2'}
Writing model shards: 100%|██████████| 1/1 [00:14<00:00, 14.13s/it]
2026-05-17 00:37:23,150 [INFO] SFT recovery complete.
```

训练跑完了 1870 steps / 2 epochs，最终 train_loss=0.8381，mean_token_accuracy≈0.81，模型已保存。无 OOM、无 CUDA 错误、无磁盘错误。

**修复建议**：
- 训练本身无需重跑，模型已保存到 `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25`
- cron 监控逻辑需要区分正常退出（exit code 0 + 日志含 "SFT recovery complete"）和异常崩溃
- 如果 cron 重启导致了额外的训练运行，检查输出目录是否被覆盖

**磁盘/GPU 当前状态**：
| 资源 | 状态 |
|------|------|
| 根分区 `/` | 5.1G/30G (17%) ✓ |
| 数据盘 `/root/autodl-tmp/` | 425G/750G (57%) ✓ |
| GPU 0 | 54740MiB 占用, 89% util (其他实验) |
| GPU 1 | 17652MiB 占用, 90% util (当前有进程 PID 25341) |
| GPU 2 | 12994MiB 占用, 94% util |
| GPU 3 | 12896MiB 占用, 89% util |

GPU 1 上当前有 python 进程（PID 25341），可能是 cron 重启的实例——建议确认该进程是什么，避免重复训练浪费资源。

---
