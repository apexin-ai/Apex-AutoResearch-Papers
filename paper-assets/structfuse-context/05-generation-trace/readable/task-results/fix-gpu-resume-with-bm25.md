# fix gpu resume with bm25

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu_resume_with_bm25_20260514T175853_result.json`
- **Structured JSON:** [`760a74a2c6dd94a81d07.json`](../../sessions/76/760a74a2c6dd94a81d07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件相同。现在汇总完整状态。

---

## 汇报

### 1. GPU 状态

| GPU | 状态 | 进程 | 显存 |
|-----|------|------|------|
| cuda:0 | **忙** (99%) | Qwen random_s44 (epoch 1/2, 1408 batches) | 49292 / 97887 MiB |
| cuda:1 | **空闲** (0%) | 无 — StarCoder random_s43 OOM 崩溃 | 3 / 97887 MiB |

OOM 原因：`m2_full_starcoder` tmux session 和 `starcoder_s42_watcher` 同时在 GPU 1 启动了两份训练，显存冲突。random_s43 checkpoint 目录为空，需完全重跑。

### 2. StarCoder resume 脚本修改（已完成）

文件：`/root/structfuse/run_m2_full_starcoder_resume.sh`

修改内容：
- 新增变量 `BM25_DATA_DIR` 和 `BM25_OUTPUT_BASE`
- RUNS 数组在 `random:44:2` 后插入 `bm25:42:3`
- 循环内新增条件：BM25 使用 `full_m2_training_data` 目录和 `full_m2_outputs/bm25_starcoder_s42/` 输出路径
- 更新 header/footer 中的 run 计数 (8→9)

新序列：`random_s43 → random_s44 → bm25_s42 → embedding_s42 → embedding_s43 → embedding_s44 → dataflow_s42 → dataflow_s43 → dataflow_s44`

### 3. StarCoder 模型路径
`/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`

### 4. Qwen 状态和训练序列

当前序列（`m2_qwen_s43` tmux）：
- random_s43 ✓（recall@1=0.5554, val_loss=0.4638）
- **random_s44** ← 进行中（epoch 1）
- embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s43 → dataflow_aware_s44（待跑）

已创建独立 BM25 Qwen 脚本：`/root/structfuse/run_m2_bm25_qwen_s42.sh`（3 epochs, 输出到 `full_m2_outputs/bm25_qwen_s42/`）

### 5. 建议的提交命令

**cuda:1 StarCoder（立即提交）：**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_full_starcoder_resume.sh"
```

**cuda:0 Qwen BM25（等当前 Qwen 队列跑完后提交）：**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && bash run_m2_bm25_qwen_s42.sh"
```

**提交前建议**：先清理冲突的 tmux sessions（`m2_full_starcoder`, `starcoder_s42_watcher`），避免再次出现两个进程抢同一张卡的问题：
```bash
tmux kill-session -t m2_full_starcoder; tmux kill-session -t starcoder_s42_watcher
```

---
