# infra gpu cleanup random

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-cleanup-random_20260513T233244_result.json`
- **Structured JSON:** [`22d1cb1d5bcb669f5f59.json`](../../sessions/22/22d1cb1d5bcb669f5f59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Random baseline 已经在 GPU 3 上运行了，无需重新启动。

**汇报：**

| 项目 | 结果 |
|------|------|
| Kill | 指定 PID (29514/29893/31124/31486/31844/28839) 已不存在，kill 静默完成 |
| GPU 0 | PID 27689 — v4a (sparsity=0.1)，28929 MiB |
| GPU 1 | PID 28083 — v4b (sparsity=0.2)，28929 MiB |
| GPU 2 | PID 28452 — v4c (sparsity=0.3)，28929 MiB |
| **GPU 3** | **PID 32192 — mvp_v4_random_r2 (random masking, sparsity 0.1-0.3)，17031 MiB，已运行 ~7.5 min** |

Random baseline (PID 32192) 在 07:29 启动，`--masking_method random --sparsity_levels 0.1,0.15,0.2,0.25,0.3`，输出到 `/root/autodl-tmp/pacs/profiling_output_v4_random_r2`，日志在 `/tmp/mvp_v4_random_r2.log`。

四张 GPU 全部在工作，无需额外操作。需要我注册 registry 记录吗？

---
