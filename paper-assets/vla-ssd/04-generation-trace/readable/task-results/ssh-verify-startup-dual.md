# ssh verify startup dual

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_startup_dual_20260521T211204_result.json`
- **Structured JSON:** [`b978d804d224ea507e50.json`](../../sessions/b9/b978d804d224ea507e50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均启动成功：

| 实验 | PID | GPU | 显存 | 运行时间 | 状态 |
|------|-----|-----|------|----------|------|
| openvla_long_cf_trained | 579760 | cuda:0 | 15313 MiB, 85% util | 2m54s | Phase 6 counterfactual, 600/5000 |
| openvla_long_untrained_v1 | 580167 | cuda:1 | 15593 MiB, 72% util | 0m44s | Phase 1 representation extraction, Task 1/10, 600/5000 |

- PID 存活 ✓
- GPU 占用正常 ✓
- 日志正常输出，无 error/traceback ✓

---
