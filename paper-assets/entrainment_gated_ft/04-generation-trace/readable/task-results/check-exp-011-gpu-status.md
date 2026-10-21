# check exp 011 gpu status

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp-011-gpu-status_20260519T154533_result.json`
- **Structured JSON:** [`6317e8c700241e2248d4.json`](../../sessions/63/6317e8c700241e2248d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PID 474289 存活**，已运行 1h09m49s。

| 项目 | 状态 |
|------|------|
| **已完成模型** | 11 个 JSON（共 16 个） |
| **当前正在跑** | HGRN2 的某个 hybrid 变体（loglikelihood 96%，即将完成） |
| **GPU 利用率** | 38%，显存 6465 MiB |
| **预计剩余** | 还剩 5 个模型，按每个 ~6min 估算约 30min 完成 |

已完成的 11 个模型（按时间倒序）：
1. `HGRN2-pure` (23:39)
2. `RetNet-hybrid-3-1` (23:33)
3. `RetNet-hybrid-6-1` (23:27)
4. `RetNet-hybrid-12-1` (23:20)
5. `RetNet-hybrid-24-1` (23:13)
6. `RetNet-pure` (23:07)
7. `GatedDeltaNet-hybrid-3-1` (23:01)
8. `GatedDeltaNet-hybrid-6-1` (22:56)
9. `GatedDeltaNet-hybrid-12-1` (22:49)
10. `GatedDeltaNet-hybrid-24-1` (22:42)
11. `GatedDeltaNet-pure` (22:31)

网络不可达（HF Hub），但数据集全部命中本地缓存，不影响评估。

---
