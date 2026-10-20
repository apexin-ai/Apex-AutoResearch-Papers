# diagnose reeval flat nli s43 protocol

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_reeval_flat_nli_s43_protocol_20260516T022754_result.json`
- **Structured JSON:** [`4b02d31a33f6a9d6277b.json`](../../sessions/4b/4b02d31a33f6a9d6277b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 核实结果

### 协议对比

| 参数 | reeval_flat_nli_s43 | eval_flat_nli_s44 |
|------|-------------------|------------------|
| 模型 | Qwen3-4B (full precision) | Qwen3-4B (full precision) |
| 量化 | **无**（无 4-bit/bnb 日志） | **无** |
| SFT adapter | ✓ `/root/autodl-tmp/sft_output` | ✓ `/root/autodl-tmp/sft_output` |
| LoRA adapter | `rsft_output_flat_nli_s43/checkpoint-507` | `rsft_output_flat_nli_s44/checkpoint-507` |
| **推理 batch 数** | **62** | **247** |
| **推断 batch_size** | **16** (985/62≈15.9) | **4** (985/247≈3.99) |
| 总耗时 | 3515.8s (56.71s/batch) | 10580.1s (42.83s/batch) |
| 文档数 | 985 | 985 |

### 结论

**Reviewer 的量化假说不成立**——两个 eval 都是 full precision，没有 `--no-quantize` 差异。

**真正的协议不一致是 batch_size：s43 用了 batch_size=16，s44 用了 batch_size=4。** 这完美解释了 2.8x 的耗时差异（batch 数量差 4x，但大 batch 单步更慢，净效果约 3x 加速）。

不同 batch_size 可能因 padding 和 attention 行为差异影响生成结果。**建议用 batch_size=4 重跑 s43 eval 以确保跨 seed 可比性**，或者确认 batch_size=16 对结果无实质影响（对比两次 s43 eval 的 metrics）。

补充：`eval_flat_nli_seed44.log` 和 `eval_flat_nli_seed45.log` 都用了 247 batches（batch_size=4），但 seed44 在 batch 12 被 Terminated，seed45 在 batch 208 截断。这些是早期未完成的 run。

---
