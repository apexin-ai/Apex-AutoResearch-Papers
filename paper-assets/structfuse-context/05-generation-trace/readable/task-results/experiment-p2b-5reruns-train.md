# experiment p2b 5reruns train

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_p2b_5reruns_train_20260512T172551_result.json`
- **Structured JSON:** [`aa4519a8016e1b1ab7df.json`](../../sessions/aa/aa4519a8016e1b1ab7df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。

**提交结果：**

1. **训练命令**：复用 `scripts/run_p2b_all.sh`，自动跳过 4 个已完成 run，串行执行 5 个剩余 run：
   - `embedding_distance` seed=123, 456
   - `dataflow_aware` seed=42, 123, 456
   - 参数：`--model-name models/Qwen/Qwen2.5-Coder-3B --batch-size 2 --lr 2e-5 --num-negatives 3 --max-seq-length 512 --use-lora --gradient-checkpointing --eval-steps 50 --save-steps 200 --num-epochs 3`

2. **磁盘**：`/root/autodl-tmp/` 有 76GB 可用，5 runs 足够

3. **tmux session**：`p2b_5reruns`，已跳过 4 个完成的 run，正在跑 `p2b_embedding_distance_s123`

4. **注意**：`WANDB_MODE=disabled`（原脚本设定），如果需要 wandb 记录需改脚本重跑。`CUDA_VISIBLE_DEVICES=4` 由 submit 框架注入，脚本内也设了 4，一致无冲突。

---
