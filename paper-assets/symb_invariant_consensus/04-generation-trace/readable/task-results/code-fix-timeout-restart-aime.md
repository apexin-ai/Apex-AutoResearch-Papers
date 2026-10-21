# code fix timeout restart aime

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-timeout-restart-aime_20260515T131209_result.json`
- **Structured JSON:** [`eb5357eaff47d979cc39.json`](../../sessions/eb/eb5357eaff47d979cc39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 修复内容（constraint_extractor.py）
| Fix | 修改 | 效果 |
|-----|------|------|
| HTTP timeout | `OpenAI(timeout=120.0)` | 单次请求 120s 超时，不再无限等待 |
| Future timeout | `future.result(timeout=180)` + `as_completed(timeout=600)` | 单 trace 180s、整体 batch 600s 超时 |
| 并发限制 | `Semaphore(6)`, `max_workers=6` | 从 12 降到 6 并发，减轻 vLLM 压力 |
| 健康检查 | `check_vllm_health()` | 每 batch 前检测 vLLM 存活 |

### Smoke Test 结果（k=4, 1 题）
- Extraction 26s 完成，**没有 hang**
- 4/4 traces 都有结果（2 有约束，2 因 max_tokens=2048 截断返回空）
- Pipeline 总耗时 121.7s

### AIME v2 实验已启动
- **tmux session**: `sica_aime30_v2`
- **PID**: 121139
- **日志**: `~/runs/symb_invariant_consensus/sica_aime30_v2.log`
- 30 题 AIME，k=12，max-tokens=10240

---
