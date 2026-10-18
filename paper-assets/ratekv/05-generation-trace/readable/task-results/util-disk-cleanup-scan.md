# util disk cleanup scan

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_util_disk_cleanup_scan_20260514T134956_result.json`
- **Structured JSON:** [`870a817d2a165f676dcb.json`](../../sessions/87/870a817d2a165f676dcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下。

---

## westd-37397 磁盘扫描报告

**总量** 250G | **已用** 152G | **可用** 99G | **需要** ~140G（Qwen2.5-72B）

### 空间占用明细

| 路径 | 大小 | 状态 |
|------|------|------|
| `prov_grounded_uie/outputs/` | **68G** | 另一个项目的训练 checkpoint |
| `.hf_cache/Qwen/Qwen3-8B/` | **16G** | 非 ratekv 在用模型 |
| `.hf_cache/Qwen/Qwen2.5-7B/` | 15G | **在用 - 不能删** |
| `models/LLM-Research/Meta-Llama-3.1-8B/` | 15G | **在用 - 不能删** |
| `models/mistralai/` | 14G | **在用 - 不能删** |
| `.hf_cache/ms_deberta/` | **9G** | prov_grounded_uie 的 NLI 模型 |
| `.hf_cache/models--cross-encoder--nli-deberta-v3-large/` | **7.6G** | prov_grounded_uie 的 NLI 模型 |
| `models/Qwen2.5-1.5B/` + `.hf_cache/models--Qwen--Qwen2.5-1.5B/` + `.hf_cache/Qwen/Qwen2.5-1.5B/` | **~3-6G** | 非在用，可能有硬链接重复 |
| `.hf_cache/datasets/` | 0.7G | 小，保留无妨 |
| `ratekv/` | 7.4M | 无大文件 |

### 清理建议

| 优先级 | 可删目录 | 释放空间 | 风险 |
|--------|----------|----------|------|
| **P0** | `prov_grounded_uie/` 整个目录 | **~68G** | 需确认该项目已不再需要 |
| **P1** | `.hf_cache/Qwen/Qwen3-8B/` | **~16G** | ratekv 未使用 |
| P2 | `.hf_cache/ms_deberta/` + `models--cross-encoder--nli-deberta-v3-large/` | **~17G** | 属于 prov_grounded_uie，随 P0 一起清 |
| P3 | Qwen2.5-1.5B（三处副本） | **~3-6G** | ratekv 未使用 |

### 结论

- **删 P0 + P1** 即可释放 **~84G**，总可用 ~183G，足够放 Qwen2.5-72B
- 仅删 **P0**（prov_grounded_uie）就有 ~167G，已够用
- Gemma-2-9B 未在磁盘上找到，可能尚未开始下载
- `Meta-Llama-3___1-8B` 和 `Meta-Llama-3.1-8B` 内容相同（硬链接），只占 15G 实际空间

---
