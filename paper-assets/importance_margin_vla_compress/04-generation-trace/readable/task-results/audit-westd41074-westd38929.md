# audit westd41074 westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd41074_westd38929_20260527T104740_result.json`
- **Structured JSON:** [`2d1bbe46caf8ac2e75f0.json`](../../sessions/2d/2d1bbe46caf8ac2e75f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### westd-41074 — 4/4 GPU 全部存活

| GPU | 利用率 | 显存 | 进程 | PID |
|-----|--------|------|------|-----|
| 0 | 11% | 10.9/97.9 GB | π0.5 Random k=0.9 strict v2 | 356361 |
| 1 | 19% | 10.4/97.9 GB | π0.5 Random k=0.5 strict v2 | 356612 |
| 2 | 51% | 10.9/97.9 GB | π0.5 Attn k=0.95 strict | 433293 |
| 3 | 53% | 10.8/97.9 GB | π0.5 L2norm k=0.85 strict v2 | 433369 |

GPU2 仍在运行（51% 利用率），**不需要重部署**。

### westd-38929 — 4/4 GPU 全部存活

| GPU | 利用率 | 显存 | 进程 | PID |
|-----|--------|------|------|-----|
| 0 | 71% | 16.4/97.9 GB | OV Long 实验 | 112587 |
| 1 | 62% | 15.8/97.9 GB | OV Long 实验 | 949447 |
| 2 | 58% | 16.1/97.9 GB | OV Long 实验 | 950007 |
| 3 | 66% | 16.0/97.9 GB | OV Long 实验 | 968309 |

两台服务器 8 个 GPU 全部正常运行，无需干预。

---
