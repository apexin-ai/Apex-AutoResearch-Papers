# ops westd41074 deploy pi05 random k07

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-deploy-pi05-random-k07_20260521T090923_result.json`
- **Structured JSON:** [`9064ca0452c9a6f21f4e.json`](../../sessions/90/9064ca0452c9a6f21f4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，GPU 3 已占用 7.1 GB，模型加载成功（gradient checkpointing 已启用，即将开始 eval）。

## 总结

**部署信息**：
- **实验**: eval_pi05_random_k07_object_seed42
- **GPU**: 3 (7.1 GB occupied)
- **PID**: 51513
- **Log**: `/tmp/eval_pi05_random_k07_seed42.log`

**westd-41074 全部 GPU 状态**：

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 9.9 GB | 0% | π0.5 random k=0.3 (PID 914719) |
| 1 | 10.4 GB | 17% | π0.5 L2norm k=0.3 (PID 936652) |
| 2 | 28.6 GB | 0% | M96 train (PID 68539) |
| 3 | 7.1 GB | 6% | **π0.5 random k=0.7 (PID 51513)** ← 新部署 |

4 块 GPU 全部在用。

---
