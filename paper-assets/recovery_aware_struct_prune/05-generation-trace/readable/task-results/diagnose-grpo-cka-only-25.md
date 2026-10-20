# diagnose grpo cka only 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_cka_only_25_20260521T032152_result.json`
- **Structured JSON:** [`25678a9b6984a9829ab7.json`](../../sessions/25/25678a9b6984a9829ab7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论明确了。

## 结果

**训练已成功完成，没有失败。**

关键证据：
- `trainer_state.json`: `global_step=100`, `should_training_stop=true`, 10 个 logging entries 全部存在
- `completions/`: 10 个 parquet 文件（step 10-100），完整
- `output.log` 最后一行：`2026-05-21 11:09:22,161 [INFO] GRPO v4 recovery training complete.`
- `wandb-summary.json`: 包含 step 100 的完整 metrics（reward=0.288, loss=0.112, kl=0.0018）
- W&B run `mirgxi5b` 本地数据 2.4MB，已记录到 step 2821

**"进程反复死亡 5 次" 的真相**：PID 310542 不是"死亡"——它正常退出了。训练从 10:48 开始，11:09 完成（约 21 分钟，100 步 × ~12s/步 = ~1200s 合理）。

**"无日志文件" 原因**：启动命令没有 `> ~/runs/.../grpo_cka_only_25.log 2>&1` 重定向，stdout 只进了 W&B 的 `output.log`。

**"无 W&B 数据" 需要核实**：本地 W&B 数据完整。可能是 `project` 配置错误 — training_args 中 `project=huggingface`（而非 `recovery_aware_struct_prune`），导致数据上传到了错误的 W&B project。同时 `run_name=grpo_sft_cka_only_25`（多了 `sft_` 前缀），可能造成在目标 project 里搜不到。

**磁盘警告**：grpo_cka_only_25 占 36GB（含 15GB optimizer.pt），磁盘仅剩 19GB (98%)。

```json
{"root_cause":"W&B project 配置为 'huggingface' 而非 'recovery_aware_struct_prune'，run_name 为 'grpo_sft_cka_only_25'（多了sft_前缀）。训练本身已成功完成 100 步。日志未重定向到文件。","error_type":"infrastructure","fix_steps":["1. 确认训练已完成，无需重跑","2. 用 wandb sync 将本地数据同步到正确 project: wandb sync /root/recovery_aware_struct_prune/wandb/run-20260521_104813-mirgxi5b --project recovery_aware_struct_prune","3. 删除 checkpoint-100/optimizer.pt (15GB) 释放磁盘: rm /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25/checkpoint-100/optimizer.pt","4. 修复 train_grpo_v5.py 中的 project 和 run_name 参数，防止后续实验再次写错 project"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "W&B project 配置为 'huggingface' 而非 'recovery_aware_struct_prune'，run_name 为 'grpo_sft_cka_only_25'（多了sft_前缀）。训练本身已成功完成 100 步。日志未重定向到文件。",
    "error_type": "infrastructure",
    "fix_steps": [
      "1. 确认训练已完成，无需重跑",
      "2. 用 wandb sync 将本地数据同步到正确 project: wandb sync /root/recovery_aware_struct_prune/wandb/run-20260521_104813-mirgxi5b --project recovery_aware_struct_prune",
      "3. 删除 checkpoint-100/optimizer.pt (15GB) 释放磁盘: rm /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25/checkpoint-100/optimizer.pt",
      "4. 修复 train_grpo_v5.py 中的 project 和 run_name 参数，防止后续实验再次写错 project"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
