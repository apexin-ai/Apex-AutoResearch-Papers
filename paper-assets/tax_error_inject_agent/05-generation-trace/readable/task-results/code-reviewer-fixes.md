# code reviewer fixes

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reviewer-fixes_20260514T051654_result.json`
- **Structured JSON:** [`a6ea5185f77cd31802c6.json`](../../sessions/a6/a6ea5185f77cd31802c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个修复均已完成并验证通过：

1. **formatter.py** — 创建完整文件，action 输出已包裹 `&lt;action>...&lt;/action>` 标签，编译通过。
2. **context.py** — C4_ObservationMasking 已从 per-step mask_prob=0.3 改为每条轨迹最多 mask 2 步且跳过 step 0。功能验证：10 步轨迹仅 mask 了 step 2 和 step 7，step 0 未被 mask，断言全部通过。

---
