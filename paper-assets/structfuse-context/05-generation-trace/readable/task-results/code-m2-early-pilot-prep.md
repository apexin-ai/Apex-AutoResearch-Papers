# code m2 early pilot prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m2-early-pilot-prep_20260513T014145_result.json`
- **Structured JSON:** [`2424505cc5113a3d3628.json`](../../sessions/24/2424505cc5113a3d3628.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部步骤完成。汇总报告：

---

```
=== 磁盘状态 ===
/root/autodl-tmp/: 59G free (34% used)

=== M1 进度 ===
PID: 577864 存活 (已运行 05:02:37)
已完成 repos: 24/131（含 skip_log.jsonl 共 5596 文件）
最近产出: oauthlib__oauthlib, cantools__cantools (09:50)

=== 训练数据生成结果 ===
train_random.jsonl:    2672 行 (278.3MB)
train_embedding.jsonl: 2672 行 (318.6MB)
train_dataflow.jsonl:  2672 行 (277.1MB)
val.jsonl:              746 行 (47.4MB)
dataflow_graph.json:   155390 entries (42.5MB)
基于 24 个 repos 的 5613 个有效 extraction
（15 train repos / 4 val repos, max_per_repo=200 cap 后 3418→2672+746）

=== 三策略差异统计 ===
random MD5:    65d9de27ab1daf6eac719144021e73d6 (avg_pool=36.4, min=4, max=50)
embedding MD5: 800adcd21ac1e0dea8b951fece5289e2 (avg_pool=36.4, min=4, max=50)
dataflow MD5:  7e23fe43575dd4b444502d38af8629a0 (avg_pool=33.9, min=2, max=50)
三策略是否有差异: YES — 全部不同
91.8% 的 instance 的 embedding vs dataflow pool 有差异

=== Dataflow fallback 统计 ===
dataflow_graph.json 结构: dict{instance_id::file → [connected instance_id::file]}
155390 entries, 100% 有连接（avg=2.0, max=322）
注: graph 是双向邻接表，不区分 dataflow/callgraph 层级——
    差异体现在 build 阶段: positive_files 只含直接 dataflow，
    full_connected 含 call graph。dataflow 策略排除 full_connected
    作为 negatives，所以 avg_pool 更小（33.9 vs 36.4）

=== train.py CUDA_VISIBLE_DEVICES ===
未找到硬编码，无需修复

=== Wrapper 脚本 ===
路径: /root/structfuse/run_m2_early_pilot.sh
策略参数映射:
  random    → --hard-negative-strategy random
  embedding → --hard-negative-strategy embedding_distance
  dataflow  → --hard-negative-strategy dataflow_aware + --dataflow-graph-file
就绪状态: YES
```

---
