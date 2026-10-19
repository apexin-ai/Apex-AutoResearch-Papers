# code full m2 data build

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-m2-data-build_20260513T151943_result.json`
- **Structured JSON:** [`12b27a2cf44ca53741a1.json`](../../sessions/12/12b27a2cf44ca53741a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进度正常，已到第 10+ 个 repo，速度稳定。

**状态总结：**

| 项目 | 状态 |
|------|------|
| M1 数据 | 44,173 instances, 15,897 有效 extraction |
| Repos 目录命名 | 已修复（双下划线），和 M1 数据匹配 |
| 模型路径 | Qwen2.5-Coder-3B 就绪 |
| 依赖 | torch 2.10+cu128, transformers 4.57.6, rank_bm25 OK |
| 磁盘 | 153GB 可用（估计输出 ~4GB，充足） |
| 进程 | PID 58008, seed 42 正在处理 ~120 repos |

**预计时间：** ~120 repos × 3 seeds，每 seed ~1.5-2 小时，总计 ~5-6 小时。

**输出目录：** `/root/autodl-tmp/structfuse/full_m2_training_data/`
- `train_random_s{42,43,44}.jsonl`
- `train_embedding_distance_s{42,43,44}.jsonl`
- `train_dataflow_aware_s{42,43,44}.jsonl`
- `val_*_s{42,43,44}.jsonl`
- `dataflow_graph.json`

**轮询进度：**
```bash
tail -20 /tmp/build_full_m2.log
ps -p 58008 -o pid= 2>/dev/null && echo "RUNNING" || echo "DONE"
ls -lh /root/autodl-tmp/structfuse/full_m2_training_data/*.jsonl 2>/dev/null
```

---
