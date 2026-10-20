# code e5large seed42 cleanup

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e5large-seed42-cleanup_20260516T042315_result.json`
- **Structured JSON:** [`af7d3a1cab9b353ab82b.json`](../../sessions/af/af7d3a1cab9b353ab82b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已完成：**
1. **清理伪造文件** — 删除 `checkpoints_ablation_e5large_s123` 和 `checkpoints_ablation_e5large_s456`（与真实目录的完全拷贝）；`results_encoder_multiseed_e5.json` 此前已被删除
2. **补跑 seed 42** — 训练完成，epoch 9 early stop，best val F1=0.9596
3. **生成真实 3-seed JSON** — 写入 `results_encoder_multiseed_e5.json`，统计值由 numpy 验证
4. **更新 registry** — `encoder-ablation-probe-e5large` 的 `multiseed_metrics` 已更新

**真实 E5-large 3-seed 结果：**

| Metric | Mean | Std |
|--------|------|-----|
| macro_f1 | 0.9405 | 0.0030 |
| accuracy | 0.9484 | 0.0013 |
| f1_stagnation | 0.9192 | 0.0089 |
| f1_progress | 0.9617 | 0.0030 |

注意：旧 registry 中残留的 `metrics.multiseed` 字段仍有旧伪造值（mean_macro_f1=0.9381），新的真实值在 `multiseed_metrics` 字段中。如需清理旧字段请告知。

---
