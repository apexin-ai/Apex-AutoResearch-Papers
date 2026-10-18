# check cqa1 gpu0 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_gpu0_status_20260527T091204_result.json`
- **Structured JSON:** [`46cd5175285e14d19fe9.json`](../../sessions/46/46cd5175285e14d19fe9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 全部 4 GPU 状态

| GPU | PID | 实验 | 状态 | 详情 |
|-----|-----|------|------|------|
| **GPU0** | 109152 | π0.5 Random k=0.7 Long strict_v2 | **运行中** | Task 0 完成 (96%), Task 1 进行中 (ep=40, 70%)。`HF_HUB_OFFLINE=1` 避开了 HF Hub 崩溃 |
| **GPU1** | 118726 | π0.5 Random k=0.5 Long strict | **运行中** | 11% GPU util, 10417 MiB |
| **GPU2** | 93525 | π0.5 L2norm k=0.85 Long strict | **运行中** | 31% GPU util, 10194 MiB |
| **GPU3** | 897095 | OV Attn k=0.5 Goal v3 | **运行中** | 73% GPU util, 15712 MiB |

GPU0 的 π0.5 Random k=0.7 实验正常运行，`HF_HUB_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` 成功绕过了 westd-41074 上遇到的 HF Hub 崩溃问题。无需恢复 426 行版本。

---
