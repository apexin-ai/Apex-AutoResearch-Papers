# urgent b8 status and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_b8_status_and_eval_20260522T155959_result.json`
- **Structured JSON:** [`30cf66519bd7b3642d1c.json`](../../sessions/30/30cf66519bd7b3642d1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果：

## B=8 Eval 结果汇总

| Dataset | Adaptive PPL | Uniform PPL | Δ(A−U) |
|---------|-------------|-------------|--------|
| **Holdout** | 17.65 | 17.69 | **−0.04** |
| **OWT** | 18.33 | 18.36 | **−0.03** |
| **Wiki** | 15.32 | 15.34 | **−0.02** |

**Adaptive 在所有三个 eval 集上均优于 Uniform**，但差距很小（Δ ≈ −0.02 ~ −0.04）。

### Batch-size 趋势对比

| Batch Size | Δ(adaptive−uniform) avg |
|-----------|------------------------|
| B=4 | −0.020 |
| **B=8** | **−0.03** |
| B=16 | −0.068 |

B=8 的 Δ≈−0.03 落在 B=4 (−0.020) 和 B=16 (−0.068) 之间，**确认 adaptive 优势随 batch size 单调递增**，符合 batch-size amplification 假设。

---
