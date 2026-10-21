# ops verify 8gen rho

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-8gen-rho_20260516T172140_result.json`
- **Structured JSON:** [`e3261f91ea97464d0eb5.json`](../../sessions/e3/e3261f91ea97464d0eb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 8gen_pooled_rho.json (8 generators, N=37058)

| Feature | ρ (pooled) | ρ (balanced) |
|---------|-----------|-------------|
| hapax_ratio | **-0.641** | -0.629 |
| ttr | **-0.625** | -0.613 |
| entropy_mean | **-0.598** | -0.595 |
| entropy_min | -0.404 | -0.399 |
| entropy_std | -0.157 | -0.169 |
| entropy_max | +0.061 | +0.060 |
| tail_decay | -0.041 | -0.042 |

Generators: pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-0.6b, qwen3-1.7b, qwen3-8b, llama-3.2-3b, mistral-7b-v0.3

## pooled_rho_fix.json (6 generators, N=27529)

| Feature | ρ (pooled) | ρ (per-gen median) |
|---------|-----------|-------------------|
| hapax_ratio | **-0.647** | -0.662 |
| ttr | **-0.630** | -0.643 |
| entropy_mean | **-0.610** | -0.620 |
| entropy_min | -0.406 | -0.397 |
| entropy_std | -0.200 | -0.209 |
| entropy_max | +0.050 | +0.076 |
| tail_decay | -0.040 | -0.080 |

Generators: olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b, qwen3-8b (缺 llama-3.2-3b, mistral-7b-v0.3)

## 差异分析

| Feature | 8gen pooled | fix pooled | Δ |
|---------|------------|-----------|---|
| hapax_ratio | -0.641 | -0.647 | +0.006 |
| ttr | -0.625 | -0.630 | +0.005 |
| entropy_mean | -0.598 | -0.610 | +0.012 |
| entropy_min | -0.404 | -0.406 | +0.002 |
| entropy_std | -0.157 | -0.200 | +0.043 |
| entropy_max | +0.061 | +0.050 | +0.011 |
| tail_decay | -0.041 | -0.040 | -0.001 |

主要差异来源：
1. **样本量不同**：8gen 有 37058 样本（含 llama-3.2-3b + mistral-7b-v0.3），fix 只有 27529 样本（6 gen）
2. **entropy_std 差距最大**（Δ=0.043）：新增的两个 generator 拉低了 entropy_std 与 depth 的相关性
3. 核心 feature（hapax_ratio, ttr, entropy_mean）差异很小（<0.012），结论稳健

---
