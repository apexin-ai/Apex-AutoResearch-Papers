# ssh verify nrollouts and monitor seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-nrollouts-and-monitor-seed45_20260516T201913_result.json`
- **Structured JSON:** [`ca924dcd90124a912af4.json`](../../sessions/ca/ca924dcd90124a912af4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务 A: n_rollouts 验证

3 个实验全部在 **bjb1-32546** 上，均已正确指定 `--n_rollouts 10`：

| 实验 | PID | 启动时间 | n_rollouts | 状态 |
|------|-----|----------|------------|------|
| vla-only-seed46 | 295478 | 今天 02:38 | 10 ✓ | OK |
| perdof-norm03-seed45 | 306318 | 今天 04:18 | 10 ✓ | OK |
| perdof-norm02-seed46 | 306518 | 今天 04:18 | 10 ✓ | OK |

bjb2-28827 上未发现这 3 个实验。**无需干预。**

## 任务 B: obs-only-seed45 (norm02)

**未完成，9/10 tasks done，第 10 个 task 刚开始。**

运行位置：bjb1-32546，PID 233553，started May16

已完成 9 个 task 的结果：

| Task | SR |
|------|----|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 10% (1/10) |
| bbq_sauce | 40% (4/10) |
| ketchup | 10% (1/10) |
| tomato_sauce | 10% (1/10) |
| butter | 10% (1/10) |
| milk | 20% (2/10) |
| chocolate_pudding | 40% (4/10) |

当前累计：14/90 = **15.6%**（9 tasks）。最后 1 个 task（orange_juice）刚进入，预计 ~1h 内完成。

---
