# gpu status all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-status-all-servers_20260524T003306_result.json`
- **Structured JSON:** [`1931e01102cb009380cf.json`](../../sessions/19/1931e01102cb009380cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 服务器 | GPU | 显存 | Util | PID | 实验 | 状态 |
|--------|-----|------|------|-----|------|------|
| cqa1-33015 | 0 | 10314 MiB | 29% | 459609 | pi05 random k0.9 object seed42 | 运行中 |
| cqa1-33015 | 1 | 10324 MiB | 32% | 541798 | pi05 random k0.95 object seed42 | 运行中 |
| cqa1-33015 | 2 | 10264 MiB | 24% | 467663 | pi05 random k0.7 object seed42 | 运行中 |
| cqa1-33015 | 3 | 1 MiB | 0% | — | — | 空闲 |
| westd-41074 | 0 | 1 MiB | 0% | — | — | 空闲 |
| westd-41074 | 1 | 1 MiB | 0% | — | — | 空闲 |
| westd-41074 | 2 | 10614 MiB | 56% | 242422 | pi05 random k0.85 spatial seed42 | 运行中 |
| westd-41074 | 3 | 1 MiB | 0% | — | — | 空闲 |
| westd-38929 | 0 | 1 MiB | 0% | — | — | 空闲 |
| westd-38929 | 1 | 5104 MiB | 29% | 432791 | xvla l2norm k0.5 long(libero_10 d3) seed43 | 运行中 |
| westd-38929 | 2 | 1 MiB | 0% | — | — | 空闲 |
| westd-38929 | 3 | 4371 MiB | 1% | 469773 | xvla random k0.5 goal seed43 | 运行中 |
| westd-27271 | 0 | 15964 MiB | 64% | 486402 | openvla l2norm k0.5 goal seed42 | 运行中 |
| westd-27271 | 1 | 1 MiB | 0% | — | — | 空闲 |

**汇总：14 GPU 中 7 块运行中，7 块空闲。**

运行中的实验：
- **Pi0.5 pruning eval**（cqa1 × 3 + westd-41074 × 1）：random 模式，k=0.7/0.9/0.95 object + k=0.85 spatial
- **X-VLA pruning eval**（westd-38929 × 2）：l2norm k0.5 long + random k0.5 goal，seed43
- **OpenVLA pruning eval**（westd-27271 × 1）：l2norm k0.5 goal，seed42

---
