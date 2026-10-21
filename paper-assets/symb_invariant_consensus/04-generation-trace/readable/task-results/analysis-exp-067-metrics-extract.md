# analysis exp 067 metrics extract

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-067-metrics-extract_20260519T120836_result.json`
- **Structured JSON:** [`33b55c526d672a945844.json`](../../sessions/33/33b55c526d672a945844.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-067 结果** (Mistral-7B-Instruct-v0.3, FOLIO-204, seed=789, K=12):

| Metric | Value |
|---|---|
| SC | 54.41% (111/204) |
| SICA | 53.92% (110/204) |
| Δ (SICA − SC) | −0.49 pp |
| n | 204 |
| McNemar b/c | 6 / 5 |
| McNemar exact p | 1.0000 |

SICA 略低于 SC，差异完全不显著 (p=1.0)。discordant pairs 极少 (b+c=11)，两种方法在绝大多数问题上一致 (a+d=193/204)。

---
