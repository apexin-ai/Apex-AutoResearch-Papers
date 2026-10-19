# check bm25 watcher and phase1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bm25_watcher_and_phase1_20260514T202819_result.json`
- **Structured JSON:** [`0728f90e3a62ec105c44.json`](../../sessions/07/0728f90e3a62ec105c44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## 1. Watcher tmux sessions — 存活，正在等待

| Session | 状态 | 监控对象 |
|---------|------|----------|
| `bm25_starcoder_watcher` | ✅ 存活 | PID 519791 — 实际运行 `run_m2_full_starcoder_resume.sh`（已跑 ~2.5h） |
| `bm25_qwen_watcher` | ✅ 存活 | PID 337267 — 实际运行 `run_m2_full_qwen.sh`（已跑 ~9h） |

两个 watcher 都在阻塞等待前序训练完成，尚未启动 BM25 训练。

## 2. BM25 数据文件 — 完整

| 文件 | 大小 | Records |
|------|------|---------|
| train_bm25_s42.jsonl | 1.48 GB | 11,308 |
| train_bm25_s43.jsonl | 1.46 GB | 11,236 |
| train_bm25_s44.jsonl | 1.53 GB | 11,264 |
| val_bm25_s42.jsonl | 361 MB | 2,980 |
| val_bm25_s43.jsonl | 331 MB | 3,052 |
| val_bm25_s44.jsonl | 310 MB | 3,024 |

6 个文件全部存在，train ~11K records、val ~3K records，符合预期。

## 3. 训练脚本 — 参数正确

两个脚本关键参数一致：

| 参数 | StarCoder | Qwen |
|------|-----------|------|
| MODEL_PATH | `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b` ✅ | `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B` ✅ |
| GPU | `${1:-0}` ✅ | `${1:-0}` ✅ |
| s42 | epochs=3, patience=0（无 early stopping）✅ | 同 ✅ |
| s43/s44 | epochs=2, patience=2 ✅ | 同 ✅ |
| 其他 | batch_size=8, num_negatives=7, max_seq_len=2048, lr=2e-5, LoRA, gradient_ckpt | 同 |

## 4. 问题

无。Phase 1 数据完整，脚本参数正确，watcher 正常等待前序任务完成后将自动启动 BM25 训练。

---
