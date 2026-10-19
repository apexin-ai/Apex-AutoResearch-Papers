# code m2 dryrun prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m2_dryrun_prep_20260512T210208_result.json`
- **Structured JSON:** [`6f82e069acc60bb559a7.json`](../../sessions/6f/6f82e069acc60bb559a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

M1 运行 30h，689 JSON 文件（约 55% 完成），进程正常。

---

## M2 训练准备 + Dry-run 总结

### 1. 训练代码验证 ✓

训练脚本在 `/root/structfuse/training/train.py`，dry-run（1 epoch, MVP 数据）成功：

| 指标 | step 50 | step 100 | step 200 | Final |
|------|---------|----------|----------|-------|
| train_loss | 0.4874 | 0.5203 | 0.6318 | 0.3110 |
| val_loss | - | 0.2757 | 0.1906 | 0.1231 |
| recall@1 | - | 75.6% | 79.5% | 89.0% |

Checkpoint 保存正常（best + final），已清理。

**正确的 CLI 参数名**（与任务描述中不同）：
- `--learning-rate`（非 `--lr`）
- `--hard-negative-strategy`（非 `--strategy`）
- `--train-file` / `--val-file`（必填，非 positional）

### 2. M1→训练数据管线 ✓

创建了 `scripts/build_m1_training_data.py`。

**发现并修复了关键 bug**：原始 `build_p2b_data.py` 和初版脚本中，`non_pos` 排除了整个 `connected_set`，然后 dataflow 策略又用同一个 `connected_set` 做过滤——结果是 no-op，导致 embedding ≡ dataflow。

修复方案：分成两层连通性：
- `positive_files`（直接 dataflow 连接）→ 用于定义训练正例和排除 non_pos
- `full_connected`（positive_files + call graph）→ 用于 dataflow_aware 负例过滤

### 3. train_dataflow vs train_embedding

| | MD5 | 大小 |
|--|-----|------|
| random | `034c8c...` | 87.0MB |
| embedding | `930c4a...` | 104.6MB |
| **dataflow** | **`b6f970...`** | **94.2MB** |

**三策略 MD5 全部不同 ✓**。67.4% 的实例在 embedding 和 dataflow 间有不同负例池。全量数据（222 repo 含大型项目）时比例更高。

### 4. M2 就绪状态

M1 完成后执行：
```bash
# Step 1: 构建训练数据
python scripts/build_m1_training_data.py \
  --extraction-dir /root/autodl-tmp/structfuse/m1_extraction/ \
  --repos-dir /root/autodl-tmp/structfuse/m1_repos/ \
  --output-dir /root/autodl-tmp/structfuse/m1_training_data/

# Step 2: 训练 (3策略 × 3种子 = 9 runs)
python training/train.py \
  --train-file /root/autodl-tmp/structfuse/m1_training_data/train_dataflow.jsonl \
  --val-file /root/autodl-tmp/structfuse/m1_training_data/val.jsonl \
  --output-dir /root/autodl-tmp/structfuse/checkpoints/m2_dataflow_s42 \
  --model-name models/Qwen/Qwen2.5-Coder-3B \
  --batch-size 2 --learning-rate 2e-5 --num-negatives 3 \
  --max-seq-length 512 --use-lora --gradient-checkpointing \
  --num-epochs 3 --hard-negative-strategy dataflow_aware --seed 42 \
  --dataflow-graph-file /root/autodl-tmp/structfuse/m1_training_data/dataflow_graph.json
```

### 5. 约束遵守
- 只用 cuda:4 ✓（train.py 顶部硬编码）
- M1 进程未触碰（PID 577864 正常运行，30h elapsed）✓
- Dry-run checkpoint 已清理 ✓
- 磁盘：81GB 剩余 ✓

---
