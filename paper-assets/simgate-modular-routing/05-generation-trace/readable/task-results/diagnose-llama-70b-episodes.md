# diagnose llama 70b episodes

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama-70b-episodes_20260524T135459_result.json`
- **Structured JSON:** [`7b37a81d36e4ab6d4aae.json`](../../sessions/7b/7b37a81d36e4ab6d4aae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**判定：成功完成。**

- 11 tasks × 20 episodes = 220 episodes，2070 labeled steps，全部到位
- 进程正常退出，无报错
- Registry 已更新为 ANALYZING，metrics 已写入
- 诊断报告已注册

Label 分布要点：det-preferred 占 30.5%，int-preferred 几乎为 0（仅 2/220），no-preference 占 68.6%。det-preferred 主要来自 death_asymmetry（internal 策略死亡而 deterministic 存活）。

---
