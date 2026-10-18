# diag w2 check full profiles

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_w2_check_full_profiles_20260515T050552_result.json`
- **Structured JSON:** [`6bc5df35c85c5188ead8.json`](../../sessions/6b/6bc5df35c85c5188ead8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral 完成。结果非常明确。

## 结果

### Profile 可用性

| Model | Full {2,4,8} Profile | File |
|-------|---------------------|------|
| Qwen-2.5-7B | ✓ | `hires_profiles.json` |
| Mistral-7B-v0.3 | ✓ | `mistral_ppl_profiles_hires.json` |
| Llama-3.1-8B | ✗ | 仅 `*_2bitonly_profiles.json` |
| Yi-1.5-9B | ✗ | 仅 `*_2bitonly_profiles.json` |
| Gemma-2-9B | ✗ | 仅 `*_2bitonly_profiles.json` |

### Mistral Full-Profile Unconstrained 结果（刚跑完）

| Solver | PPL | 2-bit | 4-bit | 8-bit | 16-bit | 2-bit% | Catastrophic? |
|--------|-----|-------|-------|-------|--------|--------|---------------|
| Greedy | **6.39** | 42 | 207 | 0 | 7 | 16.4% | No |
| MCKP | **6.41** | 43 | 213 | 0 | 0 | 16.8% | No |

Baseline PPL = 5.87。

### 对比旧 2bitonly 结果

| Solver | Old PPL | New PPL | Old 2-bit% | New 2-bit% |
|--------|---------|---------|------------|------------|
| Greedy | 47.85 | **6.39** | 85.9% | 16.4% |
| MCKP | 47.85 | **6.41** | 85.9% | 16.8% |

旧结果是 catastrophic（8x baseline），新结果接近 baseline（1.09x）。差异根源：有了 4-bit 选项后，solver 把 207/256 heads 分到 4-bit（delta≈0），只有 42 heads 需要 2-bit。

### 缺失模型估算

需要用 `hires_quant_profiler.py` 重新 profiling（64 seq × 2048 tok, {2,4,8} 三轮）：

| Model | Total Heads | Evals Needed | Est. Time |
|-------|-------------|-------------|-----------|
| Llama-3.1-8B | 256 (32L×8H) | 768 | ~4-6h |
| Yi-1.5-9B | 192 (48L×4H) | 576 | ~3-5h |
| Gemma-2-9B | 336 (42L×8H) | 1008 | ~5-7h |

三个模型可以串行跑（共享 GPU），总计 ~12-18h。需要启动 profiling 吗？

---
