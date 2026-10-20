# code exp46 efficiency

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp46_efficiency_20260522T061556_result.json`
- **Structured JSON:** [`8dea3012be210fe0a06f.json`](../../sessions/8d/8dea3012be210fe0a06f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp46 完成。结果：

| | DisPeD (DeBERTa+BiGRU) | Qwen3-8B (3-shot) |
|---|---|---|
| **Latency** | 13.12 ± 1.61 ms | 318.53 ± 26.80 ms |
| **Throughput** | 76.19 conv/s | 3.14 conv/s |
| **GPU Memory** | 868 MB | 16,096 MB |
| **Parameters** | 186.73M | 8.19B |

**Speedup: DisPeD is 24.3x faster** than Qwen3-8B LLM-as-judge, using 18.5x less GPU memory and 44x fewer parameters. Tested on 100 conversations (50 IID + 50 DD OOD), same GPU (RTX PRO 6000 Blackwell).

Script: `scripts/exp46_inference_efficiency.py`
Results: `results/exp46_inference_efficiency.json` (on server)
Registry: exp46 → DONE (success)

---
