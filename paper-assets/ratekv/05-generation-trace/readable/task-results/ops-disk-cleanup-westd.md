# ops disk cleanup westd

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_westd_20260515T163311_result.json`
- **Structured JSON:** [`8d457a0d6bed73669ef0.json`](../../sessions/8d/8d457a0d6bed73669ef0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有保留模型完好。

## 清理完成

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 227G (91%) | 183G (73%) |
| 可用 | 24G | **68G** |
| **释放** | | **44G** |

### 删除内容
| 目录 | 大小 |
|------|------|
| `.hf_cache/._____temp/` (Phi-3 不完整下载) | 18G |
| `.hf_cache/Qwen/Qwen2.5-14B/` | 28G |
| `/tmp/grpo_*` (其他项目测试输出) | ~8G |
| `.hf_cache/microsoft/` (空目录) | 0 |
| pip cache | <1G |

### 保留的模型（均完好）
Qwen2.5-7B (15G), Llama-3.1-8B (30G), Mistral-7B-v0.3 (14G), Yi-1.5-9B (17G), Gemma-2-9B (35G), Pythia-1.4B (5.5G)

68G 可用空间足够下载 Phi-3 (~26GB) + CodeLlama (~13GB)。另外注意 `prov_grounded_uie/` 占 68G（outputs/ 中的训练 checkpoint），如果确认不再需要可以进一步释放。

---
