# ops check cuda0 unknown process

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_cuda0_unknown_process_20260521T162101_result.json`
- **Structured JSON:** [`791ec11f0c9081f138b8.json`](../../sessions/79/791ec11f0c9081f138b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 占用 49175MiB / 100% 利用率，但 nvidia-smi 显示 **"No running processes found"**。

这是 **orphan 显存占用**（无 PID 关联）的情况。

根据硬约束：nvidia-smi 无 PID 时不尝试 kill 任何进程，只有容器重启能释放。

### 汇报

| 项目 | cuda:0 | cuda:1 |
|------|--------|--------|
| 显存占用 | 49175 MiB / 97887 MiB (50%) | 0 MiB |
| GPU 利用率 | 100% | 0% |
| 进程 PID | 无 | 无 |

**结论**：cuda:0 存在 orphan 显存占用（~48GB），无活跃进程可杀。GPU-Util 显示 100% 但无进程，属于驱动层残留。需要**重启容器**才能释放。

---
