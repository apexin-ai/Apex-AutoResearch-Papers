# ops db64 teal global reeval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_db64-teal-global-reeval_20260516T210825_result.json`
- **Structured JSON:** [`69bd22de20b771dc3bb6.json`](../../sessions/69/69bd22de20b771dc3bb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态清晰了。汇报如下：

## d_b Sweep 进度总结

| d_b | 训练 | per_token Eval | GPU | 位置 |
|-----|------|----------------|-----|------|
| 64  | ✅ 完成 | ✅ PPL=10.158 | — | checkpoint 已存在 |
| 256 | 🔄 Step 750/1000 | 待训练完自动跑 | GPU 0 | db_sweep.sh 主流程 |
| 512 | 🔄 Step 50/1000 | — | GPU 1 | 并行单独启动 |

**关键发现：**
- `run_db_sweep.sh` 跑在 GPU 0，是顺序执行（train→eval→下一个 d_b）。完成 d_b=256 后会自动做 per_token eval。
- d_b=512 被单独并行启动在 GPU 1（`db_sweep_512_parallel.log`）。
- **两个 GPU 都满载，无法立即跑 teal_global eval。**

**时间估算：**
- d_b=256 训练剩余 ~250 steps，预计 ~8-10 分钟后完成。之后 sweep 脚本会自动跑 per_token eval。
- d_b=512 训练剩余 ~950 steps，预计 ~35-40 分钟后完成。

**计划：**
1. 等 d_b=256 训练+per_token eval 完成后，GPU 0 空出来，可以在 GPU 0 上跑所有 teal_global eval（d_b=64, 256, 512）。
2. 或者等 d_b=512 完成后用 GPU 1。

注意：sweep 脚本在 d_b=256 eval 之后还会尝试在 GPU 0 上训练 d_b=512（虽然 GPU 1 已经在跑了）。这可能会造成冲突，需要关注。

要我设个定时检查（~10分钟后）来看 d_b=256 是否训练完毕，然后立即启动 teal_global eval？

---
