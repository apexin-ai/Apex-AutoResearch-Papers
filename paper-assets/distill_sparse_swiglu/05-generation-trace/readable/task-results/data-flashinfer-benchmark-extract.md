# data flashinfer benchmark extract

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_flashinfer_benchmark_extract_20260519T175139_result.json`
- **Structured JSON:** [`d3ff47a87fd91a74be6b.json`](../../sessions/d3/d3ff47a87fd91a74be6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。数据保存在 `results/benchmark/flashinfer_benchmark.json`，已注册为 artifact `art_20260519_4bed22`。

**数据概要**（28 条记录，LLaMA-3.1-8B，RTX PRO 6000 Blackwell）：

| 配置 | sparse_50 加速比 | sparse_30 加速比 |
|------|-----------------|-----------------|
| BS=1, SL=512 | 1.035x | 0.890x |
| BS=1, SL=2048 | 1.051x | 0.861x |
| BS=8, SL=512 | 1.126x | 0.899x |
| BS=8, SL=2048 | 1.109x | 0.902x |

- `mask_multiply` 模式几乎无加速（~0.98x），符合预期（仍做全尺寸 matmul）
- `sparse_50` 在所有配置下都有正向加速（3.5%-12.6%）
- `sparse_30` 因 gather 开销反而变慢（~10%），仅剪掉 30% 不足以抵消索引开销
- predictor 开销极小：BS=1 时 2.4-3.2ms，BS=8 时 4.9-14.4ms
- `flashinfer_30/50` 模式因 masks 未正确加载被跳过（v2 实验停留在 PREPARING）

---
