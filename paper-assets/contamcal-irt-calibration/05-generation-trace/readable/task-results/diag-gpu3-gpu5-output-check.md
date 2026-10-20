# diag gpu3 gpu5 output check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu3_gpu5_output_check_20260514T153057_result.json`
- **Structured JSON:** [`8f7801a342f6159ed538.json`](../../sessions/8f/8f7801a342f6159ed538.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

---

### Part A: 0.5B d025 aligned eval — ❌ 失败（从未执行）

Batch 脚本按顺序跑: d000 → d000_para → d005 → d005_para → d100，在 d100 的 GSM8K (492/1319, 37%) 处超时 `EXIT_CODE=124`。**d025 排在 d100 后面，从未被执行。** 输出目录为空。

需要单独重跑 d025 aligned eval。

### Part B: 3B d100 aligned eval — ✅ 成功

| Benchmark | Score |
|-----------|-------|
| MMLU | 64.17% (9011/14042) |
| GSM8K | 69.67% (919/1319) |
| ARC-Challenge | 83.96% (984/1172) |
| HumanEval | 12.20% (20/164) |

运行时间 ~3h16m (20:06→23:22)，3 个输出文件完整。

### Part C: GPU 状态

| GPU | Memory | Util | Status |
|-----|--------|------|--------|
| 0 | 14367/24564 MiB | 32% | 占用 |
| 1 | 5889/24564 MiB | 50% | 占用 |
| 2 | 9763/24564 MiB | 98% | 占用 |
| **3** | **0/24564 MiB** | **0%** | **空闲** |
| 4 | 8985/24564 MiB | 69% | 占用 |
| 5 | 8293/24564 MiB | 36% | 占用（其他进程） |

**仅 GPU 3 空闲。** GPU 5 虽然 d025 eval 已退出，但有其他进程在使用 8.3GB 显存。

---
