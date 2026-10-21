# fix fig claim evidence margin

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fig_claim_evidence_margin_20260523T203825_result.json`
- **Structured JSON:** [`dbae9896c0de194dc711.json`](../../sessions/db/dbae9896c0de194dc711.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个问题都已修复：

1. **左侧裁切** — 去掉 `bbox='tight'`，改用 `fig.subplots_adjust(left=0.01)` + `bbox_inches=None` 手动控制边距。"Training-Associated" 和 "Inherited Instruction-" 现在完整显示。

2. **Evidence 行2 补充 "6/8"** — `"empty ranks first"` → `"empty ranks first in 6/8"`。

---
