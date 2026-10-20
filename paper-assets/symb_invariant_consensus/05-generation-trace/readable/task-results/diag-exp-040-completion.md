# diag exp 040 completion

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-040-completion_20260519T105944_result.json`
- **Structured JSON:** [`669e692710ef36f57e35.json`](../../sessions/66/669e692710ef36f57e35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-040 诊断结果

| 项目 | 值 |
|------|------|
| 状态 | **成功完成** (FULL_MVP_DONE) |
| SICA | 85.7% (514/600) |
| SC | 85.0% (510/600) |
| **Δ** | **+0.7pp** |
| Extraction rate | 99.7% |
| Contradiction rate | 0.4% |
| Wall time | 1032.2 min (~17.2h) |
| GPU 1 | **已释放** (0MiB) |
| vLLM port 8001 | **已停止** |

结论：**negative**。Qwen3-14B (non-thinking) 在 PW-600 上 SC 已达 85%，Δ 仅 +0.7pp，确认 capability trap — 高能力模型 SICA 增益极小。Registry 已更新为 DONE。

---
