# ops westd gpu fill

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_gpu_fill_20260517T185106_result.json`
- **Structured JSON:** [`943b8f4ff8ad24a9c3fe.json`](../../sessions/94/943b8f4ff8ad24a9c3fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都已利用。最终结果总结：

---

## Task A: cuda:0 — qwen25_14b_scale_003 ✅ 已启动

- **14B 模型**：完整 (8/8 shards, `/root/autodl-tmp/models/Qwen2.5-14B/`)
- **脚本**：从 gpu-6000pro-2 SCP 传输，MD5 校验通过
- **状态**：模型加载中 (579 weight shards)，Phase 2 (d0 generation) 开始
- **配置**：FP16, d0-d3, 5000 samples/depth, nucleus p=0.95, seed=42
- **预计运行时间**：10-15 小时

## Task B: Proto gpt2xl 20K subsample ✅ 完成

| 指标 | 20K subsample | 全量 (60K train) | 差异 |
|------|--------------|-----------------|------|
| Accuracy | **67.13%** | 68.35% | -1.22% |
| MAE | 0.3888 | — | — |
| mean_pairwise_AUC | **0.8977** | 0.8926 | +0.0051 |

20K subsample 性能损失极小，AUC 甚至略高于全量训练。结果保存在 `results/learned_estimator/prototypical_gpt2xl.json`。

---
