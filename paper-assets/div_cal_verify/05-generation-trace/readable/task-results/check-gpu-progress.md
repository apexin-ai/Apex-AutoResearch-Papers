# check gpu progress

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-progress_20260513T231511_result.json`
- **Structured JSON:** [`169fb97f04fd916ee7f1.json`](../../sessions/16/169fb97f04fd916ee7f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新汇报：

- **cuda:0**: medium_rgds_seed42 — **Gen 5/7**, 正在训练 (Step 3/5 Training student)，GPU 40%, 显存 80/98 GB
- **cuda:1**: rgds_seed456 — **已完成**。medium_external 已自动启动（06:56:26），正在初始化加载模型阶段，GPU 尚未开始计算

**Chain 队列：**
- cuda:0: medium_rgds (Gen 5/7 进行中) → medium_random50
- cuda:1: ~~rgds_seed456~~ (完成) → **medium_external** (刚启动，加载模型中) → medium_random50

---
