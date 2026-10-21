# check sdgd v2 kill or wait

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_sdgd_v2_kill_or_wait_20260515T154656_result.json`
- **Structured JSON:** [`aa29ae8f492f66980adb.json`](../../sessions/aa/aa29ae8f492f66980adb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 决策: **WAIT_2MIN**

per_type 当前在 **batch 60/66**（正在处理第 60 个，54% 完成），每 batch 约 20 秒，预计 **2-3 分钟内完成全部实验**。

---

### 已完成 mode 结果

| Mode | F1 | Precision | Recall | Latency | Batches |
|------|-----|-----------|--------|---------|---------|
| single_pass | **0.4451** | 0.5631 | 0.3679 | 79s | 1 |
| random_batch | 0.3007 | 0.3307 | 0.2758 | 494s | 8 |
| sdgd_zero | 0.2407 | 0.3244 | 0.1913 | 261s | 4 |
| per_type | *running* | — | — | — | 60/66 |

### per_type 进度
- 已完成: 59/66 batch
- 当前: batch 60，54% processed
- 剩余: ~6 batch，预计 2-3 min

### GPU 状态
- 利用率: 14%
- 显存占用: 94221 MiB

### 建议
**不要终止。** 剩余 6 个 batch 约 2-3 分钟即可跑完，等它自然结束后收集完整 per_type 结果。single_pass 以 F1=0.4451 领先，per_type 的完整结果是关键对比数据。

---
