# launch 70b lora docred restart

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_70b_lora_docred_restart_20260521T123028_result.json`
- **Structured JSON:** [`a17a41d6c86c3560aa69.json`](../../sessions/a1/a17a41d6c86c3560aa69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在稳步运行但 loss 没有打到控制台。这是 transformers 5.8.1 + `report_to="none"` 的行为——metrics 不输出到 tqdm bar。训练本身正常（GPU1 100%，~31s/step）。

有两个选择：
1. **继续当前训练**，loss 在 epoch 1 结束时（step 382，约 3.3h 后）保存到 `trainer_state.json`
2. **重启并修改** `report_to=["tensorboard"]` 使 loss 写入 TB logs，这样可以实时查看

训练刚跑了 13 步（<1%），重启代价不大。要我改成 tensorboard 报告并重启吗？

---
