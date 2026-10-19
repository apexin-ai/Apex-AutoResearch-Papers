# eval swebench restart 100instances

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_swebench-restart-100instances_20260515T184352_result.json`
- **Structured JSON:** [`22eecd4cd19ba6c7cc60.json`](../../sessions/22/22eecd4cd19ba6c7cc60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已启动并在 GPU 上运行。汇总报告：

**1. Kill 确认**
- PID 58268 已终止（SIGTERM 成功，无需 SIGKILL）
- eval 子进程已清理

**2. 新 eval 进程**
- PID: **61318**
- 日志: `/root/autodl-tmp/structfuse/logs/swebench_eval_100.log`
- 已加载 100 instances，random_s42 开始评估中
- GPU 0 使用 62.5GB / 97.9GB

**3. 3 个代表性 checkpoint（每策略一个）**
- `random_s42` — 随机负采样
- `embedding_distance_s43` — embedding 距离采样
- `dataflow_aware_s43` — 数据流感知采样

**4. BM25 baseline**
- `eval_swebench.py` **不支持 BM25 模式**。脚本强制要求 `--checkpoint-path`（neural retriever），无 BM25/lexical/keyword 相关代码
- 如需 BM25 baseline，需要单独实现一个 BM25 retriever 并集成到 eval pipeline，或写独立脚本

**5. 预计 ETA**
- ~131s/instance × 100 instances = ~3.6h / checkpoint
- 3 checkpoints 串行 ≈ **10.9 小时**（加上模型加载 ~11h 总计）
- 预计完成时间：~2026-05-16 13:45 CST

---
