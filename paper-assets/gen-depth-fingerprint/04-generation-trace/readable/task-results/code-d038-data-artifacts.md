# code d038 data artifacts

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d038-data-artifacts_20260516T124846_result.json`
- **Structured JSON:** [`ace177add45fbdda0bdc.json`](../../sessions/ac/ace177add45fbdda0bdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个 artifacts 已生成并验证。汇总如下：

---

## 产出汇总

### 1. Per-Generator Binary F1 (`8gen_logo_results.json`)

| Generator | Binary F1 | 95% CI | 3-class F1 |
|---|---|---|---|
| pythia-1b | **0.7888** | [0.776, 0.804] | 0.8516 |
| qwen3-0.6b | 0.7594 | [0.744, 0.774] | 0.8235 |
| qwen3-1.7b | 0.7584 | [0.744, 0.773] | 0.8075 |
| pythia-2.8b | 0.7282 | [0.714, 0.743] | 0.8065 |
| olmo-2-1b | 0.6860 | [0.671, 0.702] | 0.7651 |
| qwen3-8b | 0.6497 | [0.635, 0.665] | 0.6845 |
| llama-3.2-3b | 0.6224 | [0.602, 0.643] | 0.7434 |
| mistral-7b-v0.3 | 0.4876 | [0.468, 0.506] | 0.6283 |
| **OVERALL** | **0.6851** | | **0.7638** |

### 2. Pooled Spearman ρ (`8gen_pooled_rho.json`, sorted by |ρ|)

| Feature | Pooled ρ | Balanced ρ |
|---|---|---|
| hapax_ratio | **-0.6405** | -0.6288 |
| ttr | -0.6249 | -0.6130 |
| entropy_mean | -0.5978 | -0.5954 |
| entropy_min | -0.4037 | -0.3992 |
| entropy_std | -0.1567 | -0.1692 |
| entropy_max | +0.0608 | +0.0595 |
| tail_decay | -0.0413 | -0.0422 |

排序不变：hapax_ratio > ttr > entropy_mean 仍是 top-3。

### 3. Per-Gen Spearman Median (`8gen_per_gen_spearman.json`)

| Feature | Median ρ |
|---|---|
| hapax_ratio | -0.6624 |
| ttr | -0.6428 |
| entropy_mean | -0.6146 |
| entropy_min | -0.3981 |
| entropy_std | -0.1739 |
| entropy_max | +0.0858 |
| tail_decay | -0.0665 |

### 4. Degeneration Rates (`degeneration_rates.json`)

| Generator | d0 | d1 | d2 | d3 | d4 | total |
|---|---|---|---|---|---|---|
| qwen3-0.6b | 0 | 23.5 | 62.7 | 73.0 | 80.5 | 45.4 |
| pythia-1b | 0 | 17.4 | 59.5 | 75.2 | 82.8 | 44.4 |
| qwen3-1.7b | 0 | 14.6 | 61.2 | 75.7 | 81.3 | 44.4 |
| olmo-2-1b | 0 | 13.2 | 48.2 | 69.2 | 79.8 | 40.6 |
| llama-3.2-3b | 0 | 11.4 | 43.5 | 65.0 | 74.2 | 37.2 |
| pythia-2.8b | 0 | 9.2 | 43.9 | 63.5 | 76.4 | 36.5 |
| qwen3-8b | 0 | 8.6 | 37.1 | 56.0 | 64.2 | 30.7 |
| mistral-7b-v0.3 | 0 | 7.0 | 24.3 | 41.3 | 51.8 | 24.4 |

### 5. rp-LOFO (`rp_lofo_results.json`)

- **Test A** (Llama rp=1.1): 3-class F1=0.4168, binary F1=0.5182. Confusion matrix + per-class included.
- **Test B** (Llama rp=1.0 filtered, n=2937): 3-class F1=0.7155, binary F1=0.6210. Per-class: gen-0=0.943, gen-1=0.565, gen-2+=0.639. Confusion matrix included.

---
