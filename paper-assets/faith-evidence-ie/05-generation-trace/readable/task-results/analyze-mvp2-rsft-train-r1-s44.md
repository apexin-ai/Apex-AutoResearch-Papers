# analyze mvp2 rsft train r1 s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mvp2_rsft_train_r1_s44_20260515T073356_result.json`
- **Structured JSON:** [`49e78e0a6d3e4f8a7556.json`](../../sessions/49/49e78e0a6d3e4f8a7556.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。分析报告如下：

---

## mvp2_rsft_train_r1_s44 分析报告

### 训练状态
- **完成**，EXIT_CODE=0，无报错
- 训练时间：~1h52m，3 epochs，510 steps
- train_loss=0.6138

### Task Eval Metrics

| Metric | Step 170 (~Epoch 1) | Step 510 (Epoch 3, Final) | Pass 标准 |
|--------|---------------------|---------------------------|-----------|
| **rel_f1 (F1)** | 0.0448 | **0.0509** | > 0.4057 |
| **evi_f1** | 0.7545 | **0.7798** | > 0.798 |
| ign_f1 | 0.0448 | 0.0509 | - |
| EDCR | 0.6181 | 0.6030 | - |
| preds | 812 | 771 | - |

### HF Trainer Eval

| Metric | Epoch 2 | Epoch 3 |
|--------|---------|---------|
| eval_loss | 0.7590 | 0.7625 |
| mean_token_accuracy | 0.8291 | 0.8290 |

### Pass 判定：**FAIL**
- rel_f1 = 0.0509 << 0.4057（相对 SFT baseline 下降 87%，灾难性退化）
- evi_f1 = 0.7798 < 0.798（差 0.0182，未达标）

### Checkpoint
`/root/autodl-tmp/rsft_output_s44/` — adapter_model.safetensors (528MB)，含 5 个中间 checkpoint (350/400/450/500/510)

### 结论：**NEGATIVE**
RSFT 训练严重破坏了 relation extraction 能力（rel_f1 从 0.4057 降到 0.0509），evidence F1 虽有改善趋势但仍未达标。seed=44 的 variance run 确认了 RSFT r1 方案的根本问题不是随机性导致的。

---
