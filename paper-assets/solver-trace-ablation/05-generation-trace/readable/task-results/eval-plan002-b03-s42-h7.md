# eval plan002 b03 s42 h7

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan002-b03-s42-h7_20260515T004256_result.json`
- **Structured JSON:** [`79f0951c165662eab861.json`](../../sessions/79/79f0951c165662eab861.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。plan002-additive-b03-s42 eval 结果：

| 指标 | 值 |
|------|-----|
| PR | 18/100 (18%) |
| Mean ISR | 0.0257 ± 0.0742 |
| Proved-only ISR | 0.1427 |
| H7 | 0/18 (0%) |
| H1 | 14/18 (77.8%) |
| Genuine | 4/18 (22.2%) |

Checkpoint 已被清理但 eval 结果此前已产出（`outputs/eval_sta_plan002_additive_b03.json`），H7 分类通过 `classify_h7.py` 完成。注意该实验 conclusion=negative，eval PR 从训练末期的 55% 大幅下降至 18%，泛化能力弱。

---
