# code repobench eval check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repobench_eval_check_20260516T114440_result.json`
- **Structured JSON:** [`77cc931affd72e60c3c0.json`](../../sessions/77/77cc931affd72e60c3c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RepoBench-R Eval 就绪状态报告

### 1. eval_repobench.py 参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--checkpoint-path` | (required) | checkpoint 路径 |
| `--base-model` | None (自动从 config 检测) | 可选覆盖 |
| `--language` | both | python/java/both |
| `--split` | both | cff/cfr/both |
| `--difficulty` | both | easy/hard/both |
| `--batch-size` | 32 | |
| `--max-seq-length` | 2048 | |
| `--gpu` | 0 | GPU index |
| `--n-bootstrap` | 1000 | |
| `--output` | None | 输出 JSON 路径 |
| `--batch-mode` | flag | 批量模式 |

base_model 从 checkpoint config 的 `cfg["model_name"]` 自动读取，不需要手动指定。

### 2. run_repobench_all.sh 逻辑

- conda 激活 ✓ (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)
- `CUDA_VISIBLE_DEVICES=1` — 用 GPU 1
- 只评估 **Qwen** 的 7 个 checkpoint（best_by_val_loss）
- 跳过已有输出或不存在的 checkpoint
- PID 158952 等待循环 — 进程已死，`kill -0` 会立即失败，while 立即退出，**不阻塞**

### 3. RepoBench 数据 ✓

4 个文件全部就位：
- `python_cff.gz` (140MB), `python_cfr.gz` (97MB)
- `java_cff.gz` (271MB), `java_cfr.gz` (190MB)

### 4. 已有 RepoBench 结果

**零**。没有任何 repobench 相关 JSON 输出。之前的 PID 158952 被 kill 后没有产出。

### 5. 可用 Checkpoint 清单

**Qwen** (`m2_full_qwen/`, 7 个 config，每个有 best_by_val_loss + best_by_recall_at_1):

| Config | best_by_val_loss | best_by_recall_at_1 |
|--------|:---:|:---:|
| random_s42 | ✓ | ✓ |
| random_s43 | ✓ | ✓ |
| random_s44 | ✓ | ✓ |
| embedding_distance_s43 | ✓ | ✓ |
| embedding_distance_s44 | ✓ | ✓ |
| dataflow_aware_s43 | ✓ | ✓ |
| dataflow_aware_s44 | ✓ | ✓ |

**StarCoder** (`m2_full_starcoder/`, 5 个 config):

| Config | best_by_val_loss | best_by_recall_at_1 |
|--------|:---:|:---:|
| random_s42 | ✓ | ✓ |
| random_s43 | ✓ | ✓ |
| random_s44 | ✓ | ✓ |
| embedding_distance_s42 | ✓ | ✓ |
| embedding_distance_s43 | ✓ | ✓ |

### 6. 需要修复

1. **run_repobench_all.sh 缺少 StarCoder checkpoints** — 脚本只有 Qwen，需要添加 5 个 StarCoder（CKPT_BASE 不同：`m2_full_starcoder`）
2. **PID 等待逻辑已过时** — 不阻塞但属于无用代码，可删除
3. conda 激活已包含 ✓，不会重复 UniXcoder 的问题

### 7. 当前 GPU 状态

- GPU 0: 80.4/97.9 GB, 100% util
- GPU 1: 68.2/97.9 GB, 100% util

两块 GPU 都在跑，需等 D062 eval 释放 GPU 1 后才能启动。

### 8. 预估运行时间

没有找到之前的 repobench 运行日志（PID 158952 被 kill 前无输出）。粗估：每个 checkpoint 跑 4 splits × 2 difficulty + 1000 bootstrap，batch_size=32，大约 **15-30 分钟/checkpoint**。

- Qwen 7 个 × ~20min ≈ **2-3.5 小时**
- StarCoder 5 个 × ~20min ≈ **1.5-2.5 小时**
- **总计约 3.5-6 小时**（单 GPU 串行）

---
