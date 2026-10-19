# ops plan013 dataflow retry prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan013-dataflow-retry-prep_20260513T080207_result.json`
- **Structured JSON:** [`bfb81dbb50c4e031a6bc.json`](../../sessions/bf/bfb81dbb50c4e031a6bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建完毕，语法校验通过。

**汇总：**

| 项目 | 状态 |
|------|------|
| **脚本路径** | `/root/structfuse/run_plan013_dataflow_retry.sh`（已创建，语法 OK） |
| **降参数配置** | batch=2, neg=3, seq=2048（原 batch=4, neg=5 OOM） |
| **dataflow 数据文件** | `dataflow_graph.json`（61MB）✓，`train_dataflow.jsonl`（320MB）✓ |
| **embedding 训练进度** | Epoch 2/2, step 1000, GPU 24GB 占用，LR 8.02e-06 持续下降，预计快完成 |

脚本未启动，等你确认 embedding 完成后再提交。

---
