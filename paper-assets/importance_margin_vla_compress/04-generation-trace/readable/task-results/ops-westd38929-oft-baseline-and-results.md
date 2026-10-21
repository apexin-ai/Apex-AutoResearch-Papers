# ops westd38929 oft baseline and results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-oft-baseline-and-results_20260521T022253_result.json`
- **Structured JSON:** [`77904e465f09760ff2e5.json`](../../sessions/77/77904e465f09760ff2e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 循环正在运行，第一个 episode 完成（280 步，FAIL）。任务正常启动。

---

## 汇总结果

### 1. OFT Object baseline 提交
- **exp_id**: `eval_oft_baseline_object_seed42`
- **PID**: 370074
- **GPU**: cuda:2（因 GPU 0/1/3 被 v2 实验占用）
- **修复了 3 个 bug**:
  - `AutoModelForVision2Seq` → `AutoModelForImageTextToText`（transformers 4.57.6 兼容）
  - DDP state_dict `module.` 前缀 strip
  - LIBERO-plus 2518 tasks → 标准 LIBERO 10 tasks（绕过 benchmark，直接用 bddl/init 文件）
  - `torch.load` 加 `weights_only=False`（PyTorch 2.6+ 兼容）

### 2. Object v2 实验结果（仍在运行中）
3 个 v2 实验在 GPU 0/1/3 上，尚未完成：
- **eval_random_k095_seed42_v2** (GPU 0): 进行中，某 task 40/50 ep, task_sr=23/40
- **eval_random_k07_seed42_v2** (GPU 1): Task 7/10, Ep 10/50
- **eval_l2norm_k09_seed43_v2** (GPU 3): 某 task 30/50 ep, task_sr=20/30

**已完成的 v1 OFT l2norm 结果**（这些是 OpenVLA 原版 pruning，非 OFT）：

| 实验 | keep_ratio | SR |
|------|-----------|-----|
| l2norm_k0.95 | 0.95 | **70.6%** |
| l2norm_k0.9 | 0.90 | **70.6%** |
| l2norm_k0.5 | 0.50 | **39.2%** |
| l2norm_k0.3 | 0.30 | **25.0%** |

### 3. OFT Spatial/Goal checkpoint 下载状态
- **Spatial**: 5.8GB / ~23GB，下载中（`huggingface-cli download` 进程活跃），缺 model shards 1-3
- **Goal**: 6.2GB / ~23GB，下载中（同上），无 model shard 文件
- **Object**: 23GB，**已完成**
- 无 `.aria2` 文件，下载进程正常

### 4. SmolVLA Spatial 结果
**已完成**，overall SR = **8.0%** (40/500)，GPU 2 已释放

### 5. --help 完整输出
```
usage: eval_oft_libero.py [-h] --checkpoint CHECKPOINT
                          [--suite {libero_spatial,libero_object,libero_goal,libero_10,libero_90}]
                          [--prune_mode {none,l2norm,random}]
                          [--keep_ratio KEEP_RATIO]
                          [--num_episodes NUM_EPISODES] [--gpu GPU]
                          [--seed SEED] [--max_steps MAX_STEPS]
                          [--output OUTPUT] [--task_ids TASK_IDS]
                          [--load_in_8bit] [--load_in_4bit]
                          [--num_open_loop_steps NUM_OPEN_LOOP_STEPS]
                          [--no_proprio] [--no_wrist]
```

参数名：`--prune_mode`（非 --mode），`--keep_ratio`（非 --k_ratio），`--checkpoint`（必需）。

---
