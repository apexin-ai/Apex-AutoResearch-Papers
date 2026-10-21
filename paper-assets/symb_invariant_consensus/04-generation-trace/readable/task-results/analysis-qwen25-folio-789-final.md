# analysis qwen25 folio 789 final

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen25-folio-789-final_20260522T105335_result.json`
- **Structured JSON:** [`6417a10b0083d7f5c425.json`](../../sessions/64/6417a10b0083d7f5c425.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个进程都还活着：
- PID 510872（vLLM）— ALIVE
- PID 555317（Guard）— ALIVE  
- PID 576920（收割脚本）— ALIVE

收割脚本还在跑，但 seed=789 的 `results.json` 已经生成了（201 题）。收割脚本可能在等其他 seed 或执行后续汇总。

**总结：** SICA 在 4 个 seeds 上平均比 SC 低 1.24 pp（73.80 vs 75.04），没有一个 seed 上 SICA 胜出。seed=789 少了 3 题（201/204）。

---
