# prepare post recovery eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_post_recovery_eval_20260514T183617_result.json`
- **Structured JSON:** [`eb6a24c3fb849d625bb7.json`](../../sessions/eb/eb6a24c3fb849d625bb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出总结

**脚本已创建并验证**：`/root/recovery_aware_struct_prune/src/run_post_recovery_eval.sh`

**eval_gsm8k.py 参数确认**：
- `--model_path`：必需，接受目录路径，通过 `load_pruned_model` 加载（支持剪枝后的非均匀结构）
- `--output_path`：输出 JSON 路径（注意是 `--output_path` 不是 `--output_file`）
- `--max_samples`、`--max_new_tokens`、`--dtype`（默认 bfloat16）、`--seed`（默认 42）

**Checkpoint 格式**：`train_grpo.py` 训练结束后调 `trainer.save_model(output_dir)` 直接保存到 output_dir 根目录，不是 checkpoint 子目录。脚本已处理两种情况。

**当前状态**：两个目录目前只有 `completions/` 子目录（步骤 10-80 的 parquet），模型文件尚未写入（训练未完成）。

### GRPO 完成后执行命令

```bash
# RASP recovery eval on cuda:0
bash src/run_post_recovery_eval.sh rasp 20 0

# Standard recovery eval on cuda:1 (if checkpoint exists)
bash src/run_post_recovery_eval.sh standard 20 1
```

两个 eval 可并行跑（各用一张 GPU），互不干扰。

---
