# verify weight decay check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_weight_decay_check_20260520T074348_result.json`
- **Structured JSON:** [`89eda7b2b0066ccb124e.json`](../../sessions/89/89eda7b2b0066ccb124e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：代码实际值是 `weight_decay=0.01`，不是论文写的 0.05。**

具体来源：`/root/distill_sparse_swiglu/src/train.py` 共 5 处 AdamW 初始化（行 98、206、324、420、538），全部硬编码 `weight_decay=0.01`。没有通过 argparse 覆盖——值直接写死在代码里。训练日志中也无 weight_decay 的打印记录。

**论文与代码不一致：论文写 5×10⁻²（0.05），代码实际用 1×10⁻²（0.01）。** 需要修正论文或确认哪个是正确值。

---
