# diagnose steering 107 qwen L14

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_steering_107_qwen_L14_20260522T151136_result.json`
- **Structured JSON:** [`f1bb9198b0914db3682e.json`](../../sessions/f1/f1bb9198b0914db3682e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**steering_107_qwen_L14 是 false positive failure**，进程正常完成并输出了完整结果 JSON。被 cron 标记失败是因为没写 W&B metrics（与 L13、L18 同样原因）。

**实验结果：negative。** 所有 6 个 alpha 均无显著 steering 效果：
- 最低 Fisher p = 0.68（alpha=-10），远不显著
- 所有 alpha 的定向 flip (p2c, c2p) 均为 0
- 尽管 probe accuracy 达 70.2%，steering 未能因果性地改变 answer routing

已将 conclusion 更新为 `negative`，补充了 metrics 和 notes。

---
