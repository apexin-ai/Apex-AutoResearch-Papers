# infra verify vllm after kill

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-vllm-after-kill_20260515T162747_result.json`
- **Structured JSON:** [`d208886e4d15c2c13af6.json`](../../sessions/d2/d208886e4d15c2c13af6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据拿到。

## 验证报告

| 检查项 | 结果 | 详情 |
|--------|------|------|
| vLLM /health | **PASS** | HTTP 200 OK |
| running requests ≤ 12 | **PASS** | `num_requests_running` = **12**（正好等于 v3 正常并发数） |
| waiting 队列 = 0 | **PASS** | `num_requests_waiting` = **0**（capacity=0, deferred=0） |
| KV cache 已回落 | **PASS** | `kv_cache_usage_perc` = **39.1%**（健康水位） |
| v3 进程 PID 129992 存活 | **PASS** | 状态 `Sl`，已运行 35m48s，命令 `python -u run_full_mvp.py --mode vllm --k 12 ...` |
| 5 个诊断进程已死 | **PASS** | PID 131729/132125/132208/132230/132280 全部不存在（ps 返回空） |

**6/6 PASS。** vLLM 恢复正常，v3 实验稳定运行中。注意 `num_preemptions_total=18`，说明之前确实发生过抢占，现在已消退。

---
