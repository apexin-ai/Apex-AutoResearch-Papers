# ops verify gemma2 start v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gemma2-start-v2_20260518T181249_result.json`
- **Structured JSON:** [`fefe1d7508528e2d617b.json`](../../sessions/fe/fefe1d7508528e2d617b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**启动正常，正在初始化阶段。**

状态：
- **PID 49193**：存活
- **Chat template**：`Set Gemma chat template on tokenizer` — fallback 正确触发
- **模型加载**：权重 464/464 已完成加载到 CPU（耗时 ~20s）
- **cuda:1 显存 3MiB**：正常 — 9B 模型刚完成 CPU 加载，还没到 quantize + LoRA 注入 + `.to(device)` 阶段，GPU 显存尚未分配

没有任何 error/warning（`torch_dtype` deprecated 是 transformers 版本提示，无影响）。等模型移到 GPU 后 cuda:1 显存会跳到 ~15-20GiB。

---
