# ops gpu conflict check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_conflict_check_20260515T195421_result.json`
- **Structured JSON:** [`8f38fd00e3fa2fadf188.json`](../../sessions/8f/8f38fd00e3fa2fadf188.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### cuda:0 实际占用

| GPU | UUID (前8位) | 占用 PID | 显存 | 利用率 |
|-----|-------------|---------|------|--------|
| 0 | 7717ada7 | 236779 (plan_001 子进程) | 16278/32607 MiB | 74% |
| 1 | 19de3485 | 246982 + 247244 | 12126 + 8366 MiB | 77% |
| 2 | 5e7d7885 | 245108 | 28816/32607 MiB | 97% |
| 3 | 80915638 | 234494 | 20084/32607 MiB | 32% |

**cuda:0 无冲突。** 只有 plan_001 的子进程 (PID 236779) 在 GPU 0 上。plan_011 的 PID 246041 已不存在。

### plan_001_flat_nli_seed43 状态

- **仍在训练中**，进度 481/507 steps（~95%），epoch 2.84/3.0
- 已运行 1h30m，预计还剩 ~2 分钟
- 最新 checkpoint: checkpoint-450
- Epoch 2.0 eval: loss=0.7535, mean_token_accuracy=0.8300
- 最新 train metrics (step 480): loss=0.6003, mean_token_accuracy=0.8523, entropy=0.6433

### 结论

- plan_001 即将完成（~2min），独占 GPU 0，无冲突
- plan_011 (PID 246041) 已终止，GPU 1 上运行的是其他进程 (PID 246982, 247244)

---
