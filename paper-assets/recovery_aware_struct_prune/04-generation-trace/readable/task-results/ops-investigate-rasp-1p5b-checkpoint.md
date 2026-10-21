# ops investigate rasp 1p5b checkpoint

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate_rasp_1p5b_checkpoint_20260518T163841_result.json`
- **Structured JSON:** [`3e98496115742923525d.json`](../../sessions/3e/3e98496115742923525d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**checkpoint 完整可用。**

- `checkpoint-100/model.safetensors`: 2.91 GB, 339 tensors, 1.45B 参数 — 文件完整，可正常加载
- 崩溃发生在保存 **optimizer state** 阶段（`torch.save(self.optimizer.state_dict())`），模型权重在此之前已成功保存
- completions 也完整保存了全部 100 步（10 个 parquet 文件）
- 缺少 `optimizer.pt` 和 `scheduler.pt`，意味着无法从此 checkpoint **继续训练**，但用于推理/评估完全没有问题

**不需要重跑。** 模型权重完好，可以直接用于下游实验。

---
