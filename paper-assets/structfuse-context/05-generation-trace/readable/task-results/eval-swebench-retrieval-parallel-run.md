# eval swebench retrieval parallel run

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_swebench-retrieval-parallel-run_20260515T183320_result.json`
- **Structured JSON:** [`9a6cdf9e41da2291fec0.json`](../../sessions/9a/9a6cdf9e41da2291fec0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动并在运行中。

**状态汇总：**

1. **PID**: 58268，正在评估第一个 checkpoint `random_s42`（300 instances）
2. **GPU 0 显存**：已从 51GB → 62.5GB used（模型加载了约 11.5GB），34.7GB free — 训练 + eval 并行无压力
3. **GPU 1**：54.5GB used，未受影响（StarCoder 训练继续）
4. **进度**：SWE-bench Lite 数据集已从离线缓存加载（300 instances），checkpoint shards 加载完成，开始逐 instance 评估

脚本会依次评估 6 个 checkpoints：random_s42 → random_s43 → random_s44 → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s43。已完成的会自动跳过（检测 summary.json）。

结果输出目录：`/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/&lt;run_name>/`

日志：`/root/autodl-tmp/structfuse/logs/swebench_eval_all.log`

---
