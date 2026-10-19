# ops add bm25 to supplement scripts

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_add-bm25-to-supplement-scripts_20260515T165118_result.json`
- **Structured JSON:** [`857bfe4ae894143ce99e.json`](../../sessions/85/857bfe4ae894143ce99e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过，diff 确认三处修改正确。

---

## 报告

### 1. BM25 数据文件确认（6/6 ✓）

| 文件 | 大小 |
|------|------|
| `train_bm25_s42.jsonl` | 1.4G |
| `train_bm25_s43.jsonl` | 1.4G |
| `train_bm25_s44.jsonl` | 1.5G |
| `val_bm25_s42.jsonl` | 345M |
| `val_bm25_s43.jsonl` | 317M |
| `val_bm25_s44.jsonl` | 296M |

### 2. 脚本修改

**实际架构**：任务描述中的 `run_m2_s42_supplement.sh` 和 `watch_and_chain_starcoder_s42.sh` 并非独立脚本——两个 watcher 都调用同一个共享脚本 `run_m2_s42_supplement.sh`（通过 `--encoder` 参数区分）。因此只需修改 supplement 脚本一个文件。

**修改位置**：`/root/structfuse-context/run_m2_s42_supplement.sh`（备份: `.bak.pre_bm25`）

**Diff 三处新增**：
1. **+82行**: `run_bm25_training()` 函数定义（格式与 `run_training()` 完全一致，strategy 固定为 `bm25`，seed 通过参数传入）
2. **+10行**: Qwen 段追加 `run_bm25_training "Qwen" ... 43 44`
3. **+10行**: StarCoder 段追加 `run_bm25_training "StarCoder" ... 42 43 44`

BM25 训练参数与已有 runs 完全一致：batch_size=8, num_negatives=7, max_seq_length=2048, lr=2e-5, temperature=0.07, hard_negative_ratio=0.5, eval_steps=500, **num_epochs=2, early_stopping_patience=2**。

### 3. 完整执行链

**Qwen**:  
主链完成 → watcher PID(watch_and_chain_qwen_s42.sh) 触发 → `run_m2_s42_supplement.sh --encoder qwen` → embed_s42 → dataflow_s42 → **bm25_s43 → bm25_s44**

**StarCoder**:  
主链完成 → watcher PID 20226(watch_and_chain_starcoder_s42.sh) 触发 → `run_m2_s42_supplement.sh --encoder starcoder` → embed_s42 → dataflow_s42 → **bm25_s42 → bm25_s43 → bm25_s44**

### 4. bash -n 语法检查: **SYNTAX OK**

---
