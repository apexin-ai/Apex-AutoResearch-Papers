# check server status and cleanup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-status-and-cleanup_20260515T041456_result.json`
- **Structured JSON:** [`b8eca01ff1712f317b1c.json`](../../sessions/b8/b8eca01ff1712f317b1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态报告已写入 memory.md。汇总：

### 1. m1_reextract_v2
运行中，32/60h (~53%)，all.jsonl 44,173 行。有少量 CodeQL query 失败/超时（非致命）。ETA **May 16 ~16:00**。

### 2. PID 465668
已自行退出，无需清理。

### 3. M2 训练链
- **Qwen (GPU0)**: embedding_distance_s43 step 1000/2810, R@1=0.5446@step500。已完成 3/~8 subruns，ETA **May 16 ~14:30**
- **StarCoder (GPU1)**: random_s43 step 1900/2810, R@1=0.4912@step1500。已完成 1/~8 subruns，ETA **May 17 ~00:00**

### 4. plan_003 SWE-bench
eval_swebench.py **不存在**，/root/structfuse 内无任何 swebench 相关脚本。12 个 repos 已预克隆。LLM API 依赖无法确认（脚本未创建）。

### 5. 磁盘
根分区 20G 可用 (34%)，数据盘 81G 可用 (68%)，checkpoints 占 64G。

---
