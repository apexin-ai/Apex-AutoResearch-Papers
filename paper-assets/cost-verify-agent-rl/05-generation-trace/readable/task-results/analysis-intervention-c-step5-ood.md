# analysis intervention c step5 ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_intervention_c_step5_ood_20260521T232303_result.json`
- **Structured JSON:** [`366d69c392db7574602d.json`](../../sessions/36/366d69c392db7574602d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

**结果摘要**:

| 指标 | 值 |
|---|---|
| OOD success rate | 10.45% (14/134) |
| reward_mean@134 | 1.045 |
| response_length | 6266 tokens |
| action_is_valid | 63.7% |
| action_is_effective | 99.0% |
| num_actions | 45.0 |

结论：**negative**。Step 5 (pre-collapse) 的 OOD 泛化已经很差（10.45%），response length 6266 已明显膨胀，action_is_valid 仅 63.7% 表明格式退化。这说明 hard cap 在 collapse 之前就已经未能保持 OOD 迁移能力，与 intervention-c-hard-cap 整体 negative 的结论一致。

---
