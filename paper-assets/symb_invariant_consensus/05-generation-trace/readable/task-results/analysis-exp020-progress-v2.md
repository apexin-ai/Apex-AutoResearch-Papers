# analysis exp020 progress v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp020-progress-v2_20260517T094515_result.json`
- **Structured JSON:** [`cbf516ea717941d6ffeb.json`](../../sessions/cb/cbf516ea717941d6ffeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据汇总：

**PROGRESS: 51/204 (25%)** | SICA: 64.7% | SC: 68.6% | DELTA: -3.9pp | ETA: ~96min

详细：
- 已处理 51 个问题，开始于 17:13，当前 17:46（33 min elapsed）
- **SICA: 64.7% (33/51)**, **SC: 68.6% (35/51)**, SICA 落后 SC 3.9pp
- Extraction rate: 93.5%，但日志显示多个 `finish_reason=length` 的 trace 提取失败（answer=NONE）
- GPU: 100% 利用率, 88309 MiB 显存占用，运行正常
- 按当前速率 (~0.65 min/problem)，剩余 153 个问题预计还需 **~96 分钟**

注意：当前 SICA < SC，delta 为负。`finish_reason=length` 导致部分 trace 无法提取答案，可能拖累 SICA 表现。

---
