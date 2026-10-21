# ssh check p50 spatial status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-p50-spatial-status_20260520T070317_result.json`
- **Structured JSON:** [`b19c48fc98a91a108f97.json`](../../sessions/b1/b19c48fc98a91a108f97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 实验 | 状态 | 说明 |
|------|------|------|
| **seed42** (bjb2-40593) | **FAILED** — 进程已死，跑到 task 3/10 后中断 | Log 停在 14:56 (UTC+8)，无错误信息，无输出 JSON。进程被 kill 或 OOM。已完成 3 个 task: 70%, 100%, 0% |
| **seed43-r2** (bjb1-32546) | **FAILED** — 启动即失败 | 参数错误：`--threshold 0.074855` → 应为 `--adaptive_threshold`。exit code=2 |
| **seed44-r2** (bjb2-28827) | **FAILED** — 启动即失败 | 同上，`--threshold` 拼写错误 |

三个实验全部失败，无一产出结果 JSON。

## 需要重新提交

1. **seed42**: 命令参数正确（用了 `--adaptive_threshold`），但进程异常中断。需排查是否 OOM 或被手动 kill，然后在 bjb2-40593 上重跑。
2. **seed43**: 修复参数 `--threshold` → `--adaptive_threshold`，重新提交。
3. **seed44**: 同 seed43，修复参数后重新提交。

---
