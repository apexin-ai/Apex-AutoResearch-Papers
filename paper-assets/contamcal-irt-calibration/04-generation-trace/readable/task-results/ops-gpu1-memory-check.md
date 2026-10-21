# ops gpu1 memory check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu1-memory-check_20260514T235612_result.json`
- **Structured JSON:** [`6b6f16af45246aa9c417.json`](../../sessions/6b/6b6f16af45246aa9c417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**0.5B 显存高于 1.5B 的原因是 batch-size 差异：**

| | 0.5B (GPU 1, 21794 MiB) | 1.5B (GPU 2, 14714 MiB) |
|---|---|---|
| **batch-size** | **4** | **1** |
| grad-accum | 4 | 16 |
| effective batch | 16 | 16 |
| max-seq-length | 2048 (默认) | 2048 (默认) |
| 量化 | 无 | 无 |
| 精度 | bf16 | bf16 |

**核心原因**：1.5B 任务用 `--batch-size 1 --grad-accum 16`，而 0.5B 用 `--batch-size 4 --grad-accum 4`。batch-size=4 意味着同时在 GPU 上保存 4 条序列的 activation（每条 2048 tokens），activation memory 随 batch-size 线性增长。

对于 0.5B 模型，模型参数本身很小（~1GB bf16），但 batch-size=4 × seq_len=2048 的 activation 占了 ~20GB。1.5B 模型参数更大（~3GB bf16）但 batch-size=1 大幅减少了 activation memory，所以总显存反而低。

**修复建议**：如果要节省 GPU 1 显存，将 0.5B 也改为 `--batch-size 1 --grad-accum 16`（保持相同 effective batch size），预计显存降至 ~5-8GB。

---
