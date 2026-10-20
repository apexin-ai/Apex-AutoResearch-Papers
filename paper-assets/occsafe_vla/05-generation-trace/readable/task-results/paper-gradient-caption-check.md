# paper gradient caption check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_gradient_caption_check_20260525T112650_result.json`
- **Structured JSON:** [`5c4de10689bf102a6fb0.json`](../../sessions/5c/5c4de10689bf102a6fb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**(a) 图中实际包含的 conditions：** Vanilla, Full OCC, Random OCC, Detach — 共 4 个。

**(b) 修改内容：** 数量 "four" 不变（确实是 4 个），但修正了条件列表：`Full OCC+LN` → `Random OCC`（Full OCC+LN 不在图中，Random OCC 在图中）。

**(c) 修改后的 caption 全文：**

> Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a) Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1–13% of Vanilla. (b) Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c) Action–auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d) Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.

---
