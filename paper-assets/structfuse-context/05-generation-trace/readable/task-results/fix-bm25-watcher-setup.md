# fix bm25 watcher setup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bm25_watcher_setup_20260514T181354_result.json`
- **Structured JSON:** [`0cfb564ddcddd56dfeef.json`](../../sessions/0c/0cfb564ddcddd56dfeef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

**Watcher 汇报：**

| Watcher | tmux session | 监控 PID | GPU | BM25 脚本 |
|---|---|---|---|---|
| StarCoder | `bm25_starcoder_watcher` | 519791 | cuda:1 | `/root/structfuse/scripts/run_m2_full_bm25_starcoder.sh` |
| Qwen | `bm25_qwen_watcher` | 337267 | cuda:0 | `/root/structfuse/scripts/run_m2_full_bm25_qwen.sh` |

**Qwen 链主脚本 PID：337267**（`bash run_m2_full_qwen.sh`，父进程 300284，当前正在跑 random_s44）

两个 watcher 均已确认在 watching 状态，GPU 上只有训练进程（504138 on GPU0, 519805 on GPU1），watcher 不占 GPU。

---
