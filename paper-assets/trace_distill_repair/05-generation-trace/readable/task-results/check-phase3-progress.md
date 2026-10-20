# check phase3 progress

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase3_progress_20260515T105708_result.json`
- **Structured JSON:** [`e6a8d4980e6ef765ca97.json`](../../sessions/e6/e6a8d4980e6ef765ca97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 3 Repair Comparison 状态

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE (PID 116942, 运行 33m36s) |
| **进度** | **18/33 实例已完成** (54.5%) |
| **预估剩余** | ~28 分钟 (按 ~1.9 min/instance) |

### 当前结果（从日志观察）

所有实例 `success=False` (test_execution 全部失败)，judge 分数低 (0-2 范围)。

summary.json 是 18:06 的旧快照（31 实例的上一轮），当前 33 实例的运行尚未生成最终 summary。从旧 summary 看：

| Condition | Avg Input Tokens | Avg Output Tokens | Success Rate | Avg Judge |
|-----------|-----------------|-------------------|-------------|-----------|
| no_trace | 1,067 | 2,363 | 0% | 0.0 |
| full_trace | 13,532 | 2,933 | 0% | 0.0 |
| structural_filtered | 1,333 | 2,696 | 0% | 0.0 |
| line_filtered | 2,274 | 2,660 | 0% | 0.0 |

### 异常

- **所有 condition 的 success rate 都是 0%**，test execution 全部失败
- 评估方法显示 114 次 `line_overlap_fallback` + 10 次 `empty_response`，说明测试执行环境可能有系统性问题
- judge 分数在日志中出现 1-2 的值，但 summary 显示 0.0（可能 summary 统计逻辑有差异）
- Token 使用符合预期：full_trace 远高于其他条件（13.5k vs 1-2.3k）

**关键问题**：0% success rate 是系统性测试执行失败，不是模型能力问题。建议等运行完成后检查测试执行的具体错误信息。

---
