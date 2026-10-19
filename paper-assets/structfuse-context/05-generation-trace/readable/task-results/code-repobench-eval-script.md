# code repobench eval script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repobench_eval_script_20260516T051646_result.json`
- **Structured JSON:** [`1790157030282a971eb3.json`](../../sessions/17/1790157030282a971eb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据加载正常。Python 有 5 个候选，Java 有 6-9 个候选。脚本完成：

- 文件：`/root/structfuse/evaluation/eval_repobench.py`
- `--help` 正常打印
- dry-run 验证数据加载成功（python_cff 16k, python_cfr 8k, java_cff 16k, java_cfr 8k 测试样本）
- RepoBench-R 每例候选数较少（5~9），与 pool50 评估不同，这里直接在原始候选池上做 retrieval ranking

---
