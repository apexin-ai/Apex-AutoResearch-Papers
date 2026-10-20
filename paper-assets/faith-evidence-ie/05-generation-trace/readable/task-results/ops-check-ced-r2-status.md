# ops check ced r2 status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-ced-r2-status_20260514T111940_result.json`
- **Structured JSON:** [`474694bd36b9d9187bd3.json`](../../sessions/47/474694bd36b9d9187bd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CED r2 训练状态报告

### 1. 进程状态
PID 39551 **存活**，已运行 21 分 48 秒，状态 `Ss+`。

### 2. GPU 状态
4 卡均有显存占用，但瞬时利用率 0%（采样时恰好在 generation/reward 计算阶段）：

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 0% | 12,847 / 32,607 MiB |
| 1 | 0% | 11,805 / 32,607 MiB |
| 2 | 0% | 11,463 / 32,607 MiB |
| 3 | 0% | 11,691 / 32,607 MiB |

显存占用 ~12GB/卡，模型已加载，训练正在进行。

### 3. 训练进度
**Step 14 / 378**（3.7%），已运行约 19 分钟。

最新 metrics（step 10）：
| 指标 | 值 |
|------|-----|
| loss | 0.3427 |
| reward | 0.284 |
| format_reward | 0.138 |
| f1_reward | 0.007 |
| ced_reward | 0.139 |
| KL | 4.80 |
| clipped_ratio | 45.3% |

⚠️ **Step 5 有异常**：loss=286M, KL=3.7B，但 step 10 已恢复正常。可能是首次 gradient accumulation 的数值问题。

### 4. Checkpoint
**无 checkpoint**。`--save_steps 20`，当前 step 14，预计 step 20 时生成第一个 checkpoint。

### 5. 结论
**训练正在正常进行**。当前 step 14/378，平均 ~76s/step，预估剩余时间 **约 7.7 小时**（预计完成时间 ~次日凌晨 2:40）。需关注 step 5 的异常 loss 是否复发——建议 step 20 checkpoint 生成后再检查一次 metrics 趋势。

---
