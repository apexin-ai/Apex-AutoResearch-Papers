# diag gpu check 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-check-10894_20260528T181642_result.json`
- **Structured JSON:** [`006e42f1b731c789aba4.json`](../../sessions/00/006e42f1b731c789aba4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **可见 GPU**：1 张（仅 cuda:0）
- **型号**：NVIDIA RTX PRO 6000 Blackwell Server Edition
- **显存**：97,887 MiB（~96GB），已用 0 MiB
- **GPU 利用率**：0%
- **进程**：无任何进程在跑，GPU 完全空闲

注意：`nvidia-smi -L` 只列出 1 张 GPU，但约束 C001 说 westd-10894 有 cuda:0-3 共 4 张。可能是 `CUDA_VISIBLE_DEVICES` 限制了可见范围，或者硬件配置有变化。

---
