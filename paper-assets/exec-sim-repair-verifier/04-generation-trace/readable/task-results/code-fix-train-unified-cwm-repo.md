# code fix train unified cwm repo

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-train-unified-cwm-repo_20260516T065253_result.json`
- **Structured JSON:** [`7211ad2a818c565938b1.json`](../../sessions/72/7211ad2a818c565938b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据加载验证通过：
- swebench_full: 70748 条，全部有 `execution_output`，无 `target`，fallback 正常工作
- cwm_train: 15290 条，全部有 `target`，向后兼容

### 修改总结

**`get_target()` (L132-139)**：CWM 模式下优先读 `target`，fallback 到 `execution_output`，都没有返回 `None`

**`preprocess_split()` (L196-215)**：target 为 `None` 的样本被跳过，并打印 warning 日志

**兼容性**：
- cwm_train.jsonl（有 `target`）→ 走原有路径，无变化
- swebench_full（有 `execution_output`）→ fallback 到 `execution_output`，70748 条全部可用，0 条跳过

**远程同步**：已写入 `/home/sonny/exec-sim-repair-verifier/train_unified.py`

注意：任务描述中的 dry-run 命令用了 `--data_path`，但脚本实际的参数是 `--data_dir` + `--train_file`。正确的调用方式：
```bash
python train_unified.py --data_dir data/ --train_file swebench_full/swebench_train.jsonl --val_file swebench_full/swebench_val.jsonl --model_name_or_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct --task cwm --lora_rank 16 --max_steps 2 --batch_size 1 --no_wandb
```

---
