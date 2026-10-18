# check gemini part2 progress

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gemini_part2_progress_20260519T205843_result.json`
- **Structured JSON:** [`e35e151f36d000181268.json`](../../sessions/e3/e35e151f36d000181268.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemini Dim2 BCS-controlled 实验状态

**进程状态**: 🟢 Alive（PID 622986，最新日志 05:00:32，持续 API 调用中）

**已完成数据** (5376 lines):

| 条件 | 行数 | Batches | 每 batch 样本数 |
|------|------|---------|----------------|
| count_8_low | 2400 | 25/25 ✅ | 96 |
| count_8_high | 2400 | 25/25 ✅ | 96 |
| count_16_low | 576 | 3/? (seeds 0,1,2 各192行，均完整) | 192 |
| count_16_high | 0 | 0 | — |
| count_40_* | 0 | 0 | — |
| count_80_* | 0 | 0 | — |

**进度**: 已完成 53 batches。若 part2 共 60 batches（count_8×50 + count_16×10），剩余 7 batches（count_16_low 2个 + count_16_high 5个）= 1344 行。

**速度估算**:
- 运行时间: ~3 小时（01:59 → 05:00），产出 5376 行
- 速率: ~30 行/分钟
- 剩余 1344 行 → **预计 ~45 分钟完成**（约 05:45）

**最近日志**: 全部 200 OK，无报错，~2秒/请求，运行稳定。

---
