# exp r7n2 data size ablation fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r7n2-data-size-ablation-fix_20260516T011633_result.json`
- **Structured JSON:** [`154b642c2ac21f49d685.json`](../../sessions/15/154b642c2ac21f49d685.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，模型路径修复生效。当前状态：

- **Seed 42** 第一个 scale 已完成（Balanced acc: 0.5000, Internal recall: 1.0000）
- **Seed 43** 正在训练中（13/42 steps, ~31%）
- 模型加载正常：`Loading checkpoint shards: 100%|██████████| 2/2`

**注意**：日志开头有 wandb 报错 `No API key configured`，但脚本似乎捕获了异常继续运行，训练本身不受影响。如果需要 wandb 日志记录，后续需要在服务器上执行 `wandb login`。

---
