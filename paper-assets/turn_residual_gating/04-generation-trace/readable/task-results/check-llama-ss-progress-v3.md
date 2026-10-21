# check llama ss progress v3

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama_ss_progress_v3_20260524T111453_result.json`
- **Structured JSON:** [`aec2fe4212009b6fbc4b.json`](../../sessions/ae/aec2fe4212009b6fbc4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Llama SS 训练状态汇报：**

| 项目 | 状态 |
|------|------|
| 进程 PID | 158507，已运行 3h57m |
| GPU | RTX PRO 6000 (98GB)，占用 57GB，利用率 67% |
| 当前进度 | **Step 1450 / 3000**（Epoch 1），48.3% |
| Loss | ~0.91（NTP 为主，GAR 极小） |
| Gate 均值 | 0.92–0.94，深层(L24-L30)明显低于浅层 |
| SS ratio | 0.300，间歇触发 |
| 预估剩余 | 按当前速率（~367 steps/h），还剩 ~4h13m 完成 |

训练正常推进，无异常。

---
