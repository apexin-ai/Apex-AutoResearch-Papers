# diag gpu check 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-check-34685_20260528T181636_result.json`
- **Structured JSON:** [`5eedd600af62545030be.json`](../../sessions/5e/5eedd600af62545030be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-34685 GPU 状态：**

- **可见 GPU**：1 张（仅 GPU 0）
- **型号**：NVIDIA RTX PRO 6000 Blackwell Server Edition
- **显存**：97,887 MiB（~96GB），已用 0 MiB
- **GPU 利用率**：0%
- **进程**：无任何进程在跑，GPU 完全空闲

注意：项目约束 C001 写的是 cuda:0-3（4张），但实际只可见 1 张 GPU。可能其余 GPU 被其他容器/分区隔离，或配置有变化。

---
