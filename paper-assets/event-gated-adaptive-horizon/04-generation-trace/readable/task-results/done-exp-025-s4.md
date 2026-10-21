# done exp 025 s4

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_done_exp_025_s4_20260520T015904_result.json`
- **Structured JSON:** [`d8f22dc2532f86ac2a31.json`](../../sessions/d8/d8f22dc2532f86ac2a31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE/negative，cron 已删除。

**结果摘要**：
- **Final step**: 215K（超过 210K 目标）
- **CIVO 比预期更严重**：peak ve_ratio=**6.06@75K**（eval 从 179@25K 暴跌到 34@75K），远超之前已知的 2.15@65K
- **后半程自然恢复**：ve_ratio 从 6.06 逐步衰减到 0.14@215K，eval 恢复到 241.5
- **结论 negative**：SGS 未能阻止 CIVO onset，后期恢复是 value 自然衰减驱动，非 SGS 机制生效

---
