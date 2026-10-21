# audit w38 gpu01

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_w38-gpu01_20260527T194331_result.json`
- **Structured JSON:** [`ce41cc2cff79a7d63459.json`](../../sessions/ce/ce41cc2cff79a7d63459.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。w38 全部 4 个 GPU 状态正常，无未注册进程。

**修复内容：**
- `eval_openvla_random_k095_long_seed42_v3`：补全 gpu=cuda:0, pid=272022
- `eval_openvla_attn_k075_long_seed42_v3`：补全 gpu=cuda:1, pid=266221

**确认正常运行：**
- cuda:2: L2norm k=0.5 s44 (PID 557458, 36m) — 已注册，pid=557449 是 bash wrapper
- cuda:3: Attn k=0.5 s43 (PID 541249, 1h4m) — 已注册，pid=541240 是 bash wrapper

两个 OV 实验已跑 7h+，接近完成。无异常进程。

---
