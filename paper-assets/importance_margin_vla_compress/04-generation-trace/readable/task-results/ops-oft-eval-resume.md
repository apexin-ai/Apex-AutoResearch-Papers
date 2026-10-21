# ops oft eval resume

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_oft-eval-resume_20260520T124527_result.json`
- **Structured JSON:** [`023a6bc64c2d89cdbb1c.json`](../../sessions/02/023a6bc64c2d89cdbb1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Sweep 已在运行，覆盖了所有需要的 k 值。** 不需要再提交新任务。

## 当前状态

**Smoke test**: 通过 (ALL_CHECKS_PASSED)

**GPU 1 (PID 418848)** 正在跑 OFT pruning sweep，依次执行 k=`0.95, 0.9, 0.7, 0.5, 0.3`：
- 当前在 k=0.95, Task 2/10（~8.5 eps/min）
- k=0.7 和 k=0.5 在队列中，会自动执行

**已完成的 OFT 结果**（之前单独跑的）：
| k | Success Rate |
|---|---|
| 0.95 | **0.0%** (0/500) |
| 0.90 | **0.0%** (0/500) |

**需要注意**：k=0.95 只剪掉 5% token（512→486），却得到 0% 成功率，极为异常。当前 sweep 重跑 k=0.95 也在 Task 1 得到 0/50。这可能意味着 random pruning 在 OFT 上的实现有 bug，或 OFT 模型对 token 剪枝极其敏感。

**预计时间**：sweep 每个 k 约 60 min（10 tasks × 50 eps），当前 k=0.95 还剩 ~48 min，之后 4 个 k 值 ~4 小时。总计约 **5 小时**后全部完成。

**其他 GPU**：
- GPU 0: smart compress m128 eval（进行中）
- GPU 2/3: smart compress m96/m64 训练（进行中）

---
