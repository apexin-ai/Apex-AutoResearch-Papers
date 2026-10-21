# diagnose sft rasp rlvr 20 qwen math

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_rasp_rlvr_20_qwen_math_20260516T175240_result.json`
- **Structured JSON:** [`fa956c2b571685c93916.json`](../../sessions/fa/fa956c2b571685c93916.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验未失败，训练已正常完成。** Cron 监控误报。

日志最后几行：
```
{'train_runtime': '1729', 'train_loss': '0.4774', 'epoch': '2'}
Writing model shards: 100%|██████████| 1/1 [00:14<00:00, 14.42s/it]
2026-05-17 01:43:56,827 [INFO] SFT recovery complete.
```

- 训练跑满 2 个 epoch (1870/1870 steps)，runtime 1729 秒（~29 分钟），正常退出
- 模型已保存到 `/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20_qwen_math/`（model.safetensors 12.3GB 完整）
- 根分区 17%、数据盘 65%，磁盘正常
- 无 OOM、无错误

**根因**：进程正常结束退出后，Cron 监控探测到"进程不存在"且没有 sentinel 文件或 W&B run 来确认成功，将正常退出误判为异常死亡。

**修复建议**：在 `sft_recovery.py` 结束时写一个 sentinel 文件（如 `touch /root/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math.done`），让监控脚本能区分"训练完成退出"和"异常崩溃退出"。

---
