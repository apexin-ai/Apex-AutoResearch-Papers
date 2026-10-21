# ops post restart status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-status-check_20260522T020914_result.json`
- **Structured JSON:** [`76dafef7315a3b8c82f0.json`](../../sessions/76/76dafef7315a3b8c82f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU（4× RTX 5090，全部活跃）

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 82% | 21.5/32.6 GB |
| 1 | 85% | 30.4/32.6 GB |
| 2 | 85% | 30.4/32.6 GB |
| 3 | 81% | 21.5/32.6 GB |

### 进程（全部存活）

| PID | 运行时间 | 任务 |
|-----|----------|------|
| 63490 | 12h22m | DS CWM repo s456 v2 eval |
| 94100 | 4h35m | Qwen3-8B CWM repo s123 eval |
| 96722 | 4h04m | Qwen CWM s456 eval (bash wrapper) |
| 100824 | 2h51m | DS CWM repo s123 v2 eval |

### Eval 进度（总计约 9784 样本）

| Eval | 已完成 | 进度 |
|------|--------|------|
| DS CWM s456 v2 | 9744 | **99.6%** |
| Qwen3-8B CWM s123 | 3272 | 33.4% |
| Qwen3-8B CWM s456 | 2760 | 28.2% |
| DS CWM s123 v2 | 2212 | 22.6% |

### DS s456 v2 分析（9744 样本，接近完成）

| 指标 | 值 |
|------|-----|
| Overall accuracy | 56.14% |
| **Unparseable** | **57.0%** (5552/9744) |
| Parseable-only accuracy | 32.47% |
| F1-macro | 50.63% |
| Fail recall | 42.05% |
| Pass recall | 61.36% |

**注意**：DS s456 的 unparseable 率高达 57%，严重拖累整体性能。parseable 样本的准确率仅 32.47%，表现远低于预期。DS s456 还差约 40 样本即完成。

---
