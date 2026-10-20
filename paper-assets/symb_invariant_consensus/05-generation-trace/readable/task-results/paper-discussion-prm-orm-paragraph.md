# paper discussion prm orm paragraph

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_discussion-prm-orm-paragraph_20260525T053441_result.json`
- **Structured JSON:** [`fc9e9690b15b04c801ec.json`](../../sessions/fc/fc9e9690b15b04c801ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无错误。

最终 discussion.tex 新增两段（~195 words）：
1. **PRM/ORM 机制段**：解释 trained verifier 通过训练目标引入条件独立的验证信号，打破 M→T→A→C chain，使 $I(V(T);Y)$ 突破 $I(A;Y)$ 上界。引用了 `cobbe2021gsm8k`（ORM 开创工作）和 `khalifa2023grace`（discriminator-guided decoding）。将本文 cross-arch NLI escape 定位为同一原理的 zero-shot 实例。
2. **验证策略谱段**：从 self-extraction（无外部信号）到 PRM（密集监督）的连续谱，本文方法居中间。指向 lightweight trained verification 作为未来方向。

---
