# cleanup stale preparing registry

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_stale-preparing-registry_20260516T161914_result.json`
- **Structured JSON:** [`6c16bef9e2460f6fd9bb.json`](../../sessions/6c/6c16bef9e2460f6fd9bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果：**
- 48 个 PREPARING 实验全部推进到 DONE
- 其中 39 个已有 conclusion（24 success + 4 negative + 6 failed + 5 killed）
- 9 个无 conclusion 的实验标记为 killed（vanilla_sft_aligned_v1/v2 被 v4 pipeline 取代；v4-*-r3 被 r2 成功版取代；llama31-* 已由 3way batch 完成；inject10 eval-r2 OOM 放弃）
- Registry 中 PREPARING 数量：**0**

---
