# analysis llama bias ratio scp

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-bias-ratio-scp_20260520T115825_result.json`
- **Structured JSON:** [`a6f54b3fc890257f9964.json`](../../sessions/a6/a6f54b3fc890257f9964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

直接在 westd-16639 上计算完成，无需 scp。结果：

| Model | N | Errors | BR_err | Wrong% | BR_cor | Gold% | SICA | SC | Delta |
|-------|---|--------|--------|--------|--------|-------|------|------|-------|
| LLaMA-3.1-8B | 204 | 78 | 2.66 | 72.7% | 2.86 | 74.1% | 0.6176 | 0.6618 | -0.0441 |

细节：
- **Incorrect 组** (n=78): gold 权重占比 27.3%，non-gold 占 72.7%，BR_err=2.66
- **Correct 组** (n=126): gold 权重占比 74.1%，non-gold 占 25.9%，BR_cor=2.86
- SICA 比 SC 低 4.4 个点 (0.6176 vs 0.6618)，Delta=-0.0441

---
