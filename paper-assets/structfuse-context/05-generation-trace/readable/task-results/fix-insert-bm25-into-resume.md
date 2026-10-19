# fix insert bm25 into resume

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_insert_bm25_into_resume_20260514T180458_result.json`
- **Structured JSON:** [`6af409b86ad41a5e4198.json`](../../sessions/6a/6af409b86ad41a5e4198.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，汇报结果：

### 1. StarCoder resume 脚本
**无需修改** — RUNS 数组已包含 `"bm25:42:3"` 在 `"random:44:2"` 之后（第3项）。循环体中有 bm25 专用分支，使用 `BM25_DATA_DIR` 和 `BM25_OUTPUT_BASE`。

### 2. Qwen 脚本已修改
在嵌套循环 `done` 之后、结束 echo 之前插入了 bm25_s42 训练块。由于 bash 已预读循环体，bm25_s42 会在所有循环 run（6个）结束后执行。

- 语法验证：**SYNTAX_OK**
- python 调用数：2（循环内1个 × 6次迭代 + bm25块1个 = 7 训练 run）
- "ALL 9 RUNS" → "ALL 7 RUNS"

### 3. BM25 数据路径确认
- `train_bm25_s42.jsonl`：`/root/autodl-tmp/structfuse/full_m2_training_data/` (1.4GB) ✓
- `val_bm25_s42.jsonl`：同目录 (361MB) ✓
- StarCoder resume 脚本已配置 `BM25_DATA_DIR` 指向该目录
- Qwen 脚本的 `DATA_DIR` 也指向该目录

### 4. 模型路径确认
- StarCoder：`/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b`（resume 脚本内所有 run 统一使用，含 bm25）
- Qwen：`/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`（bm25 块使用 `${MODEL}` 变量，与其他 run 一致）

### 5. bm25_s42 训练参数
| 参数 | StarCoder (已有) | Qwen (新增) |
|------|-----------------|-------------|
| epochs | 3 | 3 |
| seed | 42 | 42 |
| early-stopping-patience | 2 | 2 |
| output-dir | `full_m2_outputs/bm25_starcoder_s42` | `full_m2_outputs/bm25_s42` |
| wandb-run-name | `m2_full_sc2_bm25_s42` | `m2_full_bm25_s42` |
| 其他参数 | 与同脚本其他 run 一致 | 与同脚本其他 run 一致 |

**注意**：Qwen 的 bm25_s42 将在当前循环全部跑完（dataflow_aware_s44 之后）才执行，无法插入到 random_s44 和 embedding_distance_s43 之间（循环体已被 bash 预读）。

---
