# ops check maven status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_maven_status_20260519T134808_result.json`
- **Structured JSON:** [`300f7f9ff9a6bb2ecd6a.json`](../../sessions/30/300f7f9ff9a6bb2ecd6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 进程：RUNNING
PID 610111 仍在运行，正在执行第 3 个 random_batch seed（seed44 推测），当前在 Batch 16/18，rendering prompts 阶段。

### GPU：忙
NVIDIA RTX PRO 6000 Black (98GB), 已用 94.2GB/97.9GB, VLLM::EngineCore 占用。

### 实验进度：进行中（4/5+ arms 已完成）

已完成的 arms 及 metrics（gold_count = 2491）：

| Arm | Precision | Recall | F1 | Pred Count | Latency |
|-----|-----------|--------|----|------------|---------|
| **single_pass** | **0.2866** | 0.1618 | **0.2068** | 1,406 | 56s |
| sdgd_zero (18 batches) | 0.0911 | **0.1907** | 0.1233 | 5,212 | 522s |
| random_batch_s42 (18 batches) | 0.0898 | 0.1517 | 0.1129 | 4,208 | 538s |
| random_batch_s43 (18 batches) | 0.0829 | 0.1975 | 0.1168 | 5,936 | 552s |

### SDGD Zero 图分解统计
- 168 nodes, 2110 edges, 18 colors
- τ = 0.319, k = 1.0
- Batch sizes: [39, 20, 16, 12, 12, 10, 10, 8, 8, 6, 6, 6, 5, 4, 2, 2, 1, 1]
- Merge expansion ratio: 1.006（几乎无重复预测）

### 关键发现
**single_pass 全面优于 sdgd_zero 和 random_batch**。分解后 recall 有提升（+2.9pp），但 precision 崩溃（0.287→0.091），pred_count 膨胀 3.7 倍（1406→5212），F1 反而下降 8.4pp。random_batch 表现更差，说明不是 DAG 分解的问题，而是多批次推理本身导致 over-prediction。

---
