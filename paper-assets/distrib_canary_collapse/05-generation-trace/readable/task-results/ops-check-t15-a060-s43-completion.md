# ops check t15 a060 s43 completion

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-t15-a060-s43-completion_20260523T200140_result.json`
- **Structured JSON:** [`c6ed64a040126ff9681e.json`](../../sessions/c6/c6ed64a040126ff9681e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不在当前 session，无需删除。

---

**实验结果：`scale_14b_t15_a060_s43_fp32` — SUCCESS**

- 进程 749427 已退出
- 产出 16 个 generation（gen_0 ~ gen_15），超过预期的 15 个，全部有完整 metrics.json + all_metrics.json
- 关键指标（gen_15）：perplexity 68.88, mauve 0.029, distinct_3 0.566, effective_rank 100.88
- Perplexity 从 gen_0 的 19.83 涨至 68.88（ratio 3.47x），mauve 从 0.033 降至 0.029
- Registry 已更新为 DONE/success

**其他 5 个实验均在运行中：**

| PID | 已运行时间 |
|--------|------------|
| 750075 | 17h 12m |
| 781724 | 10h 55m |
| 780907 | 11h 01m |
| 796624 | 7h 29m |
| 762806 | 15h 06m |

---
