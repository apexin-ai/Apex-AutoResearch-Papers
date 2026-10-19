# ops watcher mechanism and sc eval

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_watcher_mechanism_and_sc_eval_20260516T032321_result.json`
- **Structured JSON:** [`1d64db5cb1b64ef19e93.json`](../../sessions/1d/1d64db5cb1b64ef19e93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Watcher 机制

- **触发方式**: `kill -0 $PID` 检查目标进程存活。Qwen watcher (PID 966920) 监视 PID 337267；StarCoder watcher (PID 20226) 监视 PID 519791
- **检查间隔**: 300 秒（5 分钟）
- **Pause 方法**: `kill -STOP 966920`（Qwen watcher）/ `kill -STOP 20226`（StarCoder watcher），恢复用 `kill -CONT`。也可直接 kill 后手动启动 supplement
- **时间窗口**: 主链结束后，watcher 最多 300 秒内检测到，检测到后 **立即** 启动 supplement，无额外等待。实际可操作窗口 = 0~300 秒（取决于 sleep 周期位置）。要插入操作需先 pause watcher

## Pool=50 Eval 进度

- **PID 138134**: alive，已运行 ~3 分 39 秒
- **当前 checkpoint**: `dataflow_aware_s43/best_by_recall_at_1`（第 1 个）
- **Encoding 进度**: 71/94 batches (76%)
- **已完成**: **0/12**（仍在第一个 checkpoint 的 query encoding 阶段）
- **结果文件**: 尚未生成
- **GPU VRAM**:
  - cuda:0: 70,702 / 97,887 MiB（72%），与 Qwen dataflow_aware_s44 训练共存
  - cuda:1: 53,467 / 97,887 MiB（55%），StarCoder embedding_distance_s43 训练中

## StarCoder Eval

- **可用 checkpoints**（best_by_recall_at_1）:
  1. `random_s42`
  2. `random_s43`
  3. `random_s44`
  4. `embedding_distance_s42`
  
  共 **4 个**。当前正在训练 `embedding_distance_s43`（已跑 1h17m），后续还有更多

- **能否在 cuda:1 并行**: **可以但有风险**。cuda:1 剩余 43.8 GB，StarCoder2-3B eval 推理约需 6-8 GB，VRAM 够用。但与训练共享 GPU 会竞争计算资源，可能拖慢训练速度。参考 cuda:0 的情况（eval + 训练共存在 72% VRAM），应该可行

- **启动命令**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
mkdir -p /root/autodl-tmp/structfuse/results && \
nohup bash -c 'cd /root/structfuse/evaluation && CUDA_VISIBLE_DEVICES=1 python evaluate_pool50.py \
  --checkpoint-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder \
  --data-path /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \
  --base-model /root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b \
  --pool-size 50 \
  --num-samples 5 \
  --batch-size 32 \
  --gpu 0 \
  --batch-mode \
  --output /root/autodl-tmp/structfuse/results/pool50_eval_starcoder_all.json' > /tmp/pool50_eval_starcoder.log 2>&1 & echo "PID=$!"
```

注意：`--gpu 0` 因为 `CUDA_VISIBLE_DEVICES=1` 使物理 GPU 1 映射为逻辑 GPU 0。`--base-model` 路径需确认——当前用的是 `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`，从训练命令中提取。如果只想评估已完成的 4 个 checkpoint，可能需要确认 evaluate_pool50.py 是否会跳过正在训练中的 checkpoint（没有 `best_by_recall_at_1` 的会自动跳过）。

---
