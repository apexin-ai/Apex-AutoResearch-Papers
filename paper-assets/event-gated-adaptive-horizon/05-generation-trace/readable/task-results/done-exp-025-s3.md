# done exp 025 s3

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_done_exp_025_s3_20260520T004706_result.json`
- **Structured JSON:** [`6dc92fb2b13e841b1eb6.json`](../../sessions/6d/6dc92fb2b13e841b1eb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**VE ratio trajectory @ key checkpoints:**

| Step | eval_return | value_mean | ve_ratio |
|------|------------|------------|----------|
| 105K | 818.58 | 460.09 | 0.5621 |
| 135K | 66.95 | 365.96 | 5.4659 |
| 145K | 43.75 | 298.05 | **6.8121** (peak) |
| 155K | 92.25 | 244.70 | 2.6524 |
| 165K | 109.21 | 198.70 | 1.8194 |
| 175K | 193.92 | 160.46 | 0.8274 |
| 185K | 339.27 | 131.81 | 0.3885 |
| 195K | 376.11 | 109.14 | 0.2902 |
| 205K | 158.72 | 92.01 | 0.5797 |
| 215K | 590.17 | 80.55 | 0.1365 |

**Registry 更新:** status=DONE, conclusion=negative, metrics 已写入。
**Cron 已删除。**

注：没有 210K 的数据点，最终步数为 215K。eval_return 在末段恢复到 590 但 value_mean 持续衰减到 80.6，ve_ratio=0.14x 表明 value 网络已严重低估——从 CIVO 过渡到了 value collapse。

---
