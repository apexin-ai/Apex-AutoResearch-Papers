# code exp29 inference efficiency

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp29-inference-efficiency_20260520T153941_result.json`
- **Structured JSON:** [`f02485f23587e306c4a5.json`](../../sessions/f0/f02485f23587e306c4a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp29 完成。

**结果总结**：

| Model | Latency (ms) | Throughput (conv/s) | Params | AA OOD F1 |
|---|---|---|---|---|
| **DeBERTa+BiGRU (ours)** | **12.12 ± 1.22** | **82.5** | 186.7M | **0.972** |
| TF-IDF+LR | 0.43 ± 0.05 | 2,345 | 10K | 0.261 |
| Qwen3-8B 3-shot | 902 | 1.11 | 8B | 0.661 |
| Qwen3-8B zero-shot | 3,229 | 0.31 | 8B | 0.0 |
| GPT-4o (est.) | 2,000-5,000 | 0.2-0.5 | ~200B+ | N/A |

- GPU 显存：862 MB（RTX PRO 6000 Blackwell）
- **vs LLM judge**: 266x faster than Qwen3-8B, 165-413x faster than GPT-4o API
- **vs TF-IDF**: TF-IDF 28x faster but OOD F1 仅 0.261（完全无法泛化）

结果已保存到 `results/exp29_inference_efficiency.json`，registry 和 artifact 已注册。

---
