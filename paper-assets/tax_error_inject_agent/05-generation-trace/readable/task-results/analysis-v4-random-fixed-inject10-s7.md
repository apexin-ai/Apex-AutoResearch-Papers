# analysis v4 random fixed inject10 s7

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject10-s7_20260515T215623_result.json`
- **Structured JSON:** [`ad3872598b99c4150c53.json`](../../sessions/ad/ad3872598b99c4150c53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总：

| 指标 | s7 值 | s1 参考 |
|------|-------|---------|
| final_loss | 0.2352 | 0.3096 |
| train_loss_avg | 0.4209 | 0.4238 |
| final_token_acc | 0.9066 | 0.8902 |
| total_steps | 1635 | 1635 |
| epochs | 3 | 3 |
| runtime | 3512s (~58min) | — |
| memory | 18.15 GiB | — |

s7 的 final_loss 比 s1 更低、token_acc 更高，训练完全正常。checkpoint 路径：`v1-20260516-045440/checkpoint-1635`。

---
