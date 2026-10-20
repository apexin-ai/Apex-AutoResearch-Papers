# check all running metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_running_metrics_20260514T040636_result.json`
- **Structured JSON:** [`439d09e8b200074f8734.json`](../../sessions/43/439d09e8b200074f8734.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。三个实验全部存活，汇总：

| 实验 | step | eval_return | 状态 |
|------|------|-------------|------|
| **008a** | 65K (eval 中) | @55K=487.9 | 65K eval 正在执行，结果未出。train@64K=557 暗示可能回升 |
| **008c** | 68K | @65K=240.9 | plateau 确认，10K 步零增长 |
| **008d** | 40K | @35K=146.3 | train@40K=119 持续下滑，崩塌预警；45K eval 未到达 |

**关键待定**：008a 的 65K eval 是核心决策点，预计 30-40 分钟后出结果。008d 的 45K eval 预计 ~50 分钟后到达，将确认是否崩塌。

---
