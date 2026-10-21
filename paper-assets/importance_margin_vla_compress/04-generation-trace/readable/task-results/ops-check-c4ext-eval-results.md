# ops check c4ext eval results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-c4ext-eval-results_20260521T025331_result.json`
- **Structured JSON:** [`382cd228d85c3130241e.json`](../../sessions/38/382cd228d85c3130241e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程被 kill，未跑完。日志分析如下：

**已完成**：
- Task 0 ("pick up the alphabet soup and place it in the basket"): **0/50 (0.0%)**
- Task 1 ("pick up the cream cheese and place it in the basket"): 跑到 Ep 41/50 时中断

**未完成**：Task 2-9 全未跑。

**关键数据**：
- 总计 91 个 episode 全部 FAIL，0 个 SUCCESS
- 每个 episode 都跑满 280 步超时，说明模型动作完全不对（没有提前完成任务的情况）

**结论**：OpenVLA Smart Compress M=128 VTC-only 20K checkpoint 在 libero_object 上 success rate 为 **0%**（基于已完成的 91 episodes）。模型表现极差，即使跑完剩下的 episodes 结果也不会有意义改善。

**建议**：不需要重跑这个 eval。0/91 已经足够说明 20K checkpoint 的 VTC-only 方案不 work。需要排查训练是否有问题，或者 VTC-only 方案本身不可行。

---
