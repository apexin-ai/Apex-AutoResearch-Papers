# ops verify resume step counter

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_resume_step_counter_20260524T180601_result.json`
- **Structured JSON:** [`6297c912c1fe7113fa22.json`](../../sessions/62/6297c912c1fe7113fa22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：max_steps=50005 是绝对计数，不需要修改。**

启动命令确认 `--resume true --resume_step 20000 --max_steps 50005`。源码逻辑：

- `log_step = resume_step(20000) + gradient_step_idx` 
- 终止条件：`log_step == max_steps(50005)` → `gradient_step_idx == 30005` 时停止
- 总训练步数：20000（已完成） + 30005（新增） = 50005 步

进度条显示 `1/50005` 是因为 tqdm total 设为 max_steps 但从 0 开始计数，视觉上会有误导（最终停在 30005/50005），但**实际训练步数是正确的**。

训练无需干预，继续运行即可。

---
