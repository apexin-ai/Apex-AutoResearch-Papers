# diagnose eval argmin object seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-argmin-object-seed44-r2_20260516T153021_result.json`
- **Structured JSON:** [`f175d7c6ed34c6b158ee.json`](../../sessions/f1/f175d7c6ed34c6b158ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验没有失败。** 它完整运行了全部 10 个 task × 10 rollouts = 100 次评估后正常退出。

### 根因

EXIT_CODE=129 (SIGHUP) 发生在实验**已经完成并保存结果之后**。日志最后几行清楚显示：

1. 打印了 "Overall success rate (reconvla): 13.0% (13/100)"
2. 打印了 "Results saved to logs/eval_object_reconvla_seed44.json"
3. 之后才出现 EXIT_CODE=129

这是 tmux/nohup session 在主进程退出后收到 SIGHUP 的典型现象（可能是 tmux session 被关闭或终端断开），不影响实验结果。

### 实验结果

- **所有 10/10 task 全部完成**，100 个 rollout 全部跑完
- **输出文件完整** (1486 bytes, 包含所有 per-task 结果)
- **Overall success rate: 13.0% (13/100)**

Per-task breakdown:
| Task | Success Rate |
|------|-------------|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 10% |
| bbq_sauce | 20% |
| ketchup | 10% |
| tomato_sauce | 10% |
| butter | 0% |
| milk | 10% |
| chocolate_pudding | 50% |
| orange_juice | 20% |

### 建议

**不需要重试 (r3)**。实验已完整完成，结果文件有效可用。

---
