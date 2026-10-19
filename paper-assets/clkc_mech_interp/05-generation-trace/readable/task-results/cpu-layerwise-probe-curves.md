# cpu layerwise probe curves

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_layerwise-probe-curves_20260522T132052_result.json`
- **Structured JSON:** [`c6517df200aa083ceedc.json`](../../sessions/c6/c6517df200aa083ceedc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完毕。

## 输出

**文件路径**: `/root/clkc_mech_interp/data/layerwise_probe_curves.json`（服务器 westd-41302）

## 数据摘要

### Residual Stream Probe

| Model | Direction | Peak Layer | Peak Bal. Acc |
|-------|-----------|-----------|---------------|
| **Llama-3.1-8B** (32 layers) | EN→EN | 28 | 0.7757 |
| | ZH→ZH | 13 | 0.7206 |
| | EN→ZH | 5 | 0.5956 |
| | ZH→EN | 15 | 0.7059 |
| **Qwen3-8B** (36 layers) | EN→EN | 24 | 0.7500 |
| | ZH→ZH | 14 | 0.7262 |
| | EN→ZH | 23 | 0.6726 |
| | ZH→EN | 18 | 0.7321 |

### MLP Probe

| Model | Direction | Peak Layer | Peak Bal. Acc |
|-------|-----------|-----------|---------------|
| **Llama-3.1-8B** (32 layers) | EN→EN | 16 | 0.8051 |
| | ZH→ZH | 7 | 0.7463 |
| | EN→ZH | 18 | 0.6875 |
| | ZH→EN | 15 | 0.7500 |
| **Qwen3-8B** (36 layers) | EN→EN | 14 | 0.7738 |
| | ZH→ZH | 2 | 0.7500 |
| | EN→ZH | 22 | 0.6964 |
| | ZH→EN | 8 | 0.7381 |

## JSON 结构

包含 5 个顶层 key：
- `llama31` — residual stream 逐层 balanced accuracy (32 layers × 4 directions)
- `llama31_mlp` — MLP 逐层 balanced accuracy
- `qwen3` — residual stream 逐层 balanced accuracy (36 layers × 4 directions)
- `qwen3_mlp` — MLP 逐层 balanced accuracy
- `qwen3_bootstrap_ci` — Qwen3 n=2000 bootstrap 逐层均值 + 95% CI

每个 model entry 包含 `directions`（layer→accuracy 映射）和 `peaks`（peak_layer, peak_acc）。

---
