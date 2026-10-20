# ssh verify gpu0 conflict

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-gpu0-conflict_20260514T021301_result.json`
- **Structured JSON:** [`ab50f955187e34b14356.json`](../../sessions/ab/ab50f955187e34b14356.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### PID 存活状态

| PID | 状态 | 说明 |
|-----|------|------|
| 544511 (v3 原始) | **已死** | 不存在 |
| 544942 (v3 父) | **已死** | 不存在 |
| 582850 (v4 新) | **存活** | 运行 6 分钟，正在跑 `lifespan-longest-lived,measure-melting-point-unknown-substance --episodes 20 --gpu_id 0` |

### GPU 进程分布

| GPU | UUID | 占用显存 | PID | 归属 |
|-----|------|---------|-----|------|
| GPU0 | `GPU-3023...` | 28013/32607 MiB | **583838** (VLLM) | plan-001b-gpu0-**v4** 的子进程（PPID 582855 → 582850） |
| GPU1 | `GPU-5576...` | 28013/32607 MiB | **558609** (VLLM) | 另一个任务：`find-non-living-thing --gpu_id 1`（PPID 557852），与 GPU0 无关 |

### 结论：**无冲突**

- v3 进程（PID 544511）已经死了，GPU0 上只有 v4 一个进程在跑。
- GPU1 上的 558609 是另一个独立任务（`find-non-living-thing --gpu_id 1`），不涉及 GPU0。
- v4 正在正常推理中（日志显示持续的 prompt processing，速度约 2000+ toks/s input, ~90 toks/s output）。
- 不需要 kill 任何进程。

---
