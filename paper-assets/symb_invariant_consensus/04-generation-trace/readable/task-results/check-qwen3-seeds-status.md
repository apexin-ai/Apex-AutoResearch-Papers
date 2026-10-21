# check qwen3 seeds status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen3-seeds-status_20260524T014343_result.json`
- **Structured JSON:** [`a8587dace0ddfc2bd676.json`](../../sessions/a8/a8587dace0ddfc2bd676.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen3-14B PW 种子状态

**GPU**: GPU 0/2/3 占用 ~88GB (vLLM serving), GPU 1 空闲。3 个 vLLM 实例 (port 8020/8021/8022) + 3 个 `run_full_mvp.py` 进程均在运行中。

| Seed | 状态 | 进度 | SC% | SICA% |
|------|------|------|-----|-------|
| 42 (exp033) | 已完成 | 600/600 | 85.00 | 85.67 |
| 123 | 运行中 | 263/600 (43.8%) | - | - |
| 456 | 运行中 | 265/600 (44.2%) | - | - |
| 789 | 运行中 | 267/600 (44.5%) | - | - |

**时间估算**: 三种子于今日 02:06 启动，已运行 ~7.6h，完成 ~44%。按当前速率 (~35 problems/h/seed)，剩余 ~335 problems，预计还需 **~9.5h**，约今日 **19:30** 左右完成。

---
