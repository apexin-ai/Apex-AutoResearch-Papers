# diagnose phase diagram t20 a060 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase_diagram_t20_a060_s43_fp32_20260521T192541_result.json`
- **Structured JSON:** [`60126085e7c524b86e04.json`](../../sessions/60/60126085e7c524b86e04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败原因**: 磁盘满 (`No space left on device`, os error 28)。westd-17855 数据盘 350G 已 100% 占满，仅剩 1.2M。gen_3 训练跑完了 5000/5000 steps 但 `model.save_pretrained()` 写 safetensors 时失败。

**进度**: gen_0–gen_2 完整可用，gen_3 checkpoint 损坏（36KB/~800MB），gen_4–gen_19 未开始。

**重试方案**: 需先在 westd-17855 释放 ≥34GB 空间（或迁移到其他服务器），删除损坏的 gen_3，从 gen_2 续跑。

---
