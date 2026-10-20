# ssh launch seed123 v2 grpo westd1 v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch_seed123_v2_grpo_westd1_v3_20260522T143003_result.json`
- **Structured JSON:** [`172ecc365358a91d3881.json`](../../sessions/17/172ecc365358a91d3881.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正式启动。

## 汇报

1. **GPU:1 清理**：kill 了 PID 52151（`eval_gsm8k.py --model_path sft_depth_first_20`，depth-first SFT eval）
2. **旧 checkpoint**：`grpo_random_20_seed123/` 已删除
3. **新训练**：
   - PID: 53822（python 子进程），bash wrapper PID 53815
   - 输出目录: `grpo_random_20_seed123_v2`
   - wandb run: `j1ut733l` (`grpo_sft_random_20`)
   - 进度: 0/100 steps，训练 loop 已启动
4. **GPU:1 显存**: 25251 MiB，91% utilization
5. **日志**: `/tmp/grpo_random_seed123_v2.log`，启动正常

**附注**: 首次启动因 wandb 目录缺失失败（`/root/autodl-tmp/recovery_aware_struct_prune/wandb/` 不存在，`/root/recovery_aware_struct_prune/wandb` 是指向它的 symlink）。已创建目标目录后重启成功。

---
