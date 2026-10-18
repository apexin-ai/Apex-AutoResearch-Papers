# check 14b progress

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_14b_progress_20260520T030354_result.json`
- **Structured JSON:** [`bd003b6266e74e4b79ec.json`](../../sessions/bd/bd003b6266e74e4b79ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 14B 实验状态：

| 实验 | GPU | 状态 | 运行时间 | 当前阶段 | 进度 |
|------|-----|------|---------|---------|------|
| qwen25_14b_temp09 | GPU 0 (92%, 32G) | **RUNNING** | 24h 4m | Phase 3.3b: Generate d3 | ~75% |
| qwen25_14b_topk50 | GPU 1 (93%, 32G) | **RUNNING** | 22h 4m | Phase 3.3b: Generate d3 | ~75% |

两个实验进度一致：已完成 d0→d2 的 LoRA 微调和生成，当前都在最后一个生成阶段（用 LoRA(d2) 生成 d3 的 5000 samples）。模型权重已加载完毕，正在执行文本生成。

剩余 Phase 4 (特征提取) + Phase 5 (分类) 都是轻量阶段，预计今天内完成。

---
