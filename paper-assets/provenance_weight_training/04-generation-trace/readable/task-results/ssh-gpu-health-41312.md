# ssh gpu health 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_health_41312_20260517T201514_result.json`
- **Structured JSON:** [`1e0e6cde35e91b5f74b4.json`](../../sessions/1e/1e0e6cde35e91b5f74b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 — westd-41312

| GPU | 利用率 | 显存占用 | PID | 实验 | 进度 | 状态 |
|-----|--------|----------|-----|------|------|------|
| **0** | 100% | 46,539 / 97,887 MiB (48%) | 125995 | `qwen06b_uniform_seed42` | 3364/6103 (55%) | 🟢 运行中，预计剩余 ~1h36m |
| **1** | 100% | 75,023 / 97,887 MiB (77%) | 115525 | `ess_only_seed456` | 3492/8477 (41%) | 🟢 运行中，预计剩余 ~25m |
| **2** | 100% | 75,023 / 97,887 MiB (77%) | 115021 | `ess_only_seed123` | 4105/8477 (48%) | 🟢 运行中，预计剩余 ~23m |
| **3** | 78% | 75,023 / 97,887 MiB (77%) | 125367 | `random_reweight_seed456` | 8009/8477 (94%) | 🟢 即将完成，预计剩余 ~2m24s |

### 总结

- **4 张 GPU 全部在用**，均有 python 训练进程
- 所有实验均在正常运行中，**无异常/无完成**
- `random_reweight_seed456`（GPU3）马上完成（94%），约 2-3 分钟后结束
- `ess_only_seed456` 和 `ess_only_seed123`（GPU1/2）约 25 分钟内完成
- `qwen06b_uniform_seed42`（GPU0）最慢，还需约 1.5 小时（速度 ~2.10s/it）

---
