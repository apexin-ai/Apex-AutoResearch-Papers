# infra gpu check urgent

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check-urgent_20260515T110004_result.json`
- **Structured JSON:** [`7165b3d34cf592b5de96.json`](../../sessions/71/7165b3d34cf592b5de96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**双卡正常，无需重启。**

| 任务 | 状态 | 进度 | GPU 显存 |
|------|------|------|----------|
| openvla-trained-extract (GPU 0) | 运行中 | [4/10] `put_both_moka_pots_on_the_stove` 100% 即将保存 | 16.4 GB |
| openvla-untrained-extract (GPU 1) | 运行中 | [4/10] `put_both_moka_pots_on_the_stove` 100% 即将保存 | 16.4 GB |

GPU 利用率瞬时 0% 是因为两个任务都刚跑完第 4 个 demo 的全部 20794 steps，正处于保存 .h5 文件的 I/O 阶段（上一个 .h5 约 5.8 GB）。进程 CPU 占用正常（901%/998%），两个 tmux session 都在。

---
