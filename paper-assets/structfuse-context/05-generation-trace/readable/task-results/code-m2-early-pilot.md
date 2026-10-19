# code m2 early pilot

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m2_early_pilot_20260513T014059_result.json`
- **Structured JSON:** [`8d3a778d048d166bcf4a.json`](../../sessions/8d/8d3a778d048d166bcf4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练确认在运行。GPU 4 使用率 100%，显存 9.2GB/24GB，无 OOM。

---

**汇报**

### 1. 训练数据统计
| 指标 | 值 |
|------|------|
| 参与 repo 数 | 23 (15 train / 4 val) |
| 总 extractions | 5,591 |
| train instances | 2,670（每策略相同） |
| val instances | 748 |
| 策略差异率 | 91.8%（embedding vs dataflow） |
| train_random.jsonl | 241 MB |
| train_embedding.jsonl | 273 MB |
| train_dataflow.jsonl | 238 MB |
| val.jsonl | 85 MB |

### 2. 训练提交
- tmux session: `m2_early_pilot`
- PID: 795739
- GPU: cuda:4（100% 利用率，9.2GB/24GB）

### 3. 参数调整（相对原始任务）
因 24GB 单卡 OOM，做了以下调整：
- `batch_size`: 8 → **2**
- `num_negatives`: 7 → **3**
- `max_seq_length`: 2048 → **1024**
- 模型使用本地缓存 `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`（AutoDL HuggingFace 不可达）
- `WANDB_MODE=offline`（未配置 API key）

### 4. 预计运行时间
- 每策略 ~4005 steps（2670 × 3 epochs / batch 2）
- 3 策略顺序训练，预计总计 **4-8 小时**

### 5. 磁盘剩余
- `/root/autodl-tmp/`: **54GB free** / 169GB total（69% 已用）

---
