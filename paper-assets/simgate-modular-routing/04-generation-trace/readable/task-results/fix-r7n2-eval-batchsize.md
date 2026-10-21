# fix r7n2 eval batchsize

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_r7n2-eval-batchsize_20260516T031315_result.json`
- **Structured JSON:** [`b472bc9693564e169963.json`](../../sessions/b4/b472bc9693564e169963.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **`per_device_eval_batch_size`** 从 `args.batch_size`(4) → 硬编码 `2`（第342行）
2. **`generation_eval` batch_size** 已是 2（第376、384行，无需改）
3. Kill 了旧进程 929751 及两个残留子进程（930111、930385），释放 ~14GB 显存
4. 新进程 PID 930638 运行中，GPU0 占用 10GB/32GB，训练 epoch 1 接近完成（~93%）
5. GPU1 未动

---
