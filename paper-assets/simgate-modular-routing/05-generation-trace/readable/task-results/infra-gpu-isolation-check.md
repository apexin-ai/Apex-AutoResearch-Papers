# infra gpu isolation check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-isolation-check_20260513T064942_result.json`
- **Structured JSON:** [`b32fae7e10f1cc091c06.json`](../../sessions/b3/b32fae7e10f1cc091c06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 隔离正确，无冲突。**

| 角色 | 父 PID | 实际计算 PID | CUDA_VISIBLE_DEVICES | 物理 GPU | GPU UUID |
|------|--------|-------------|---------------------|----------|----------|
| GPU0 Phase 1 | 20296 | 20301 | `0` | GPU 0 | `GPU-30234404...` |
| GPU1 Phase 1 | 55775 | 55780 | `1` | GPU 1 | `GPU-5576d2e7...` |

- PID 20301 独占 GPU 0，占用 15720 MiB / 32607 MiB
- PID 55780 独占 GPU 1，占用 15466 MiB / 32607 MiB
- 两个进程分别绑定不同物理 GPU，无交叉

---
