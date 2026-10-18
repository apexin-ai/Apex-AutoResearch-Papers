# infra verify gpu usage

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-gpu-usage_20260515T143732_result.json`
- **Structured JSON:** [`9cd9fe44caae162a81b2.json`](../../sessions/9c/9cd9fe44caae162a81b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练进程都在运行：

| 任务 | PID | Config | GPU | 状态 |
|------|-----|--------|-----|------|
| baseline_seed42 | 23289 | `configs/baseline.yaml` | GPU 0 | 运行中，CPU 21.6% |
| imm_d03_l05_seed42 | 23434 | `configs/imm_anchor.yaml` | GPU 1 | 运行中，CPU 21.3% |

**GPU 状态**：
- GPU 0 (RTX PRO 6000, 98GB): 559MiB 占用，GPU-Util 0%，35°C
- GPU 1 (RTX PRO 6000, 98GB): 3MiB 占用，GPU-Util 0%，30°C

两个进程刚启动约 1 分钟（22:36 启动），显存占用还很低，GPU 利用率为 0%——可能正在初始化/加载模型阶段。如果持续几分钟后 GPU-Util 仍为 0% 且显存不增长，需要排查。

---
