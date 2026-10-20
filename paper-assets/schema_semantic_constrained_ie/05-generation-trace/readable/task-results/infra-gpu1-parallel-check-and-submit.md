# infra gpu1 parallel check and submit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu1_parallel_check_and_submit_20260513T221926_result.json`
- **Structured JSON:** [`3823d00f9d7bc3377ee2.json`](../../sessions/38/3823d00f9d7bc3377ee2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 1 显存状态

| 指标 | 值 |
|------|-----|
| 已用 | 16,489 MiB |
| 总量 | 97,887 MiB |
| 剩余 | **~81,398 MiB (79.5 GB)** |
| 利用率 | 83% |
| 进程 | PID 126473, 占 16,480 MiB |

## 并行建议

**可以并行。** GPU 1 剩余 ~79.5GB，远超 20GB 阈值。即使加载一个 7B 模型（~16GB）做 unconstrained baseline 推理，总占用也只到 ~33GB，GPU 1 仍有大量余量。

两个推理进程共享 GPU 会有 30-50% 速度下降，但总吞吐高于串行。建议主 Agent 在 GPU 1 上提交 unconstrained baseline，指定 `CUDA_VISIBLE_DEVICES=1`。

---
