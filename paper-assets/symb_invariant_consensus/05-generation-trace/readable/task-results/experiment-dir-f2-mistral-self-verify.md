# experiment dir f2 mistral self verify

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-f2-mistral-self-verify_20260520T162059_result.json`
- **Structured JSON:** [`c2549e34bae21695beae.json`](../../sessions/c2/c2549e34bae21695beae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入。总结：

**Dir-F2 Self-Verification 结果 (30 题 pilot)**

| 指标 | 值 |
|------|-----|
| SC accuracy | 16/30 (53.3%) |
| Original SICA accuracy | 16/30 (53.3%) |
| **Self-filtered SICA accuracy** | **16/30 (53.3%)** |
| Constraint keep rate | 63.2% (750/1187) |
| McNemar p (filt vs SC) | 1.0 |
| McNemar p (filt vs orig) | 1.0 |
| Gains / Losses vs original | +0 / -0 |

Mistral-7B 自验证滤掉了 36.8% 的 constraints，但对 accuracy 零影响——0 gains, 0 losses。与此前 CoT prompt 版本（keep rate 42.4%，accuracy 下降 1 题）对比，无论 prompt 风格如何，同模型无法逃逸自身 bias。这是 Method Exhaustion Table 的一个清晰数据点。

---
