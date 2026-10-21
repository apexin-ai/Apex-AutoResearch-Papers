# fix docred lora restart tb

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_docred_lora_restart_tb_20260521T124132_result.json`
- **Structured JSON:** [`d119ccb53265ac1688d2.json`](../../sessions/d1/d119ccb53265ac1688d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 20 数据到了：

| Step | Loss | Grad Norm | LR |
|------|------|-----------|----|
| 10 | 0.1472 | 0.1431 | 2e-6 |
| 20 | 0.1499 | 0.1574 | 3e-6 |

Loss 从 0.1472→0.1499 微升，这是正常的——当前处于 warmup 阶段（LR 在爬升），loss 在 warmup 结束前不会明显下降。grad_norm 稳定在 0.14-0.16，梯度健康。训练一切正常。

---
