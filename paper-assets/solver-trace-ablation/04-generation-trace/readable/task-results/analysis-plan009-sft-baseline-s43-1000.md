# analysis plan009 sft baseline s43 1000

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan009-sft-baseline-s43-1000_20260515T131712_result.json`
- **Structured JSON:** [`75f51e8daa3ff50ad7b2.json`](../../sessions/75/75f51e8daa3ff50ad7b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新，status=DONE, conclusion=success。

**总结：plan009-sft-baseline-s43-1000 完成**

| 指标 | s43 | s42 |
|------|-----|-----|
| prove_rate | 11% | 13% |
| mean_isr | 0.0699 | 0.0738 |
| final_loss | 0.0167 | 0.0168 |
| runtime | 1585s | 1415s |
| proved_only_isr | 0.6352 | — |

s43 与 s42 高度一致，SFT baseline 跨 seed 稳定。只有 answer_type=true 的题能 prove（11/34=32.4%），false 和 unknown 全部 0/66，符合 SFT 预期。GPU 0 已空闲（s44 训练仍在 GPU 1 运行）。

---
