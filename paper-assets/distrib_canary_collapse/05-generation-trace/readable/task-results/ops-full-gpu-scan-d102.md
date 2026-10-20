# ops full gpu scan d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-scan-d102_20260523T020540_result.json`
- **Structured JSON:** [`c2ce690d40af7bae4a61.json`](../../sessions/c2/c2ce690d40af7bae4a61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 6 个实验仍在运行，没有 DEAD PID。**

| PID | 实验 | GPU | 运行时间 | GPU利用率 | 显存 |
|-----|------|-----|---------|----------|------|
| 679656 | t15_a060_v2 | cuda:0 | 12h 58m | 100% | 31.5 GiB |
| 680095 | t15_a050_v3 | cuda:1 | 12h 58m | 95% | 31.5 GiB |
| 719178 | t10_a075_s43 | cuda:2 | 5h 43m | 99% | 27.7 GiB |
| 719252 | t10_a060_s43 | cuda:3 | 5h 43m | 98% | 27.7 GiB |
| 738796 | t10_a045_s43 | cuda:4 | 1h 18m | 100% | 31.3 GiB |
| 680608 | t15_a045 | cuda:5 | 12h 58m | 99% | 31.5 GiB |

6 块 GPU 全部占满（每块 ~98GB），利用率 95-100%。没有已完成的实验，因此无需执行 D102 分析或 registry 更新。

---
