# diagnose mistral distortion zero

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mistral_distortion_zero_20260515T185328_result.json`
- **Structured JSON:** [`5689b0d8c72b242f4fd7.json`](../../sessions/56/5689b0d8c72b242f4fd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结论

### 1. Solver 选中的 2 个 2-bit heads
- **L24,H7** → `['quant', 2]`
- **L25,H0** → `['quant', 2]`

### 2. 这些 head 在 profile 中的原始 distortion
| Head | hires 2-bit d2 (原始) | monotonicity 后 d2 |
|------|----------------------|-------------------|
| L24H7 | -0.001051 | 0.0 (被 clamp) |
| L25H0 | -0.000532 | 0.0 (被 clamp) |

### 3. 根因

**`mistral_profiling_results.json`（标准 profile）的 4-bit 和 8-bit distortion 全部为 0.0。** 256 个 head 无一例外。

完整因果链：
1. `run_yi_mistral_downstream_k2.py` 的 `load_merged_profiles()` 将 hires 的 2-bit 数据与 standard 的 4-bit/8-bit 数据合并
2. Standard profile 的 4-bit = 0.0, 8-bit = 0.0 → 合并后所有 head 的 4-bit/8-bit distortion 均为 0
3. `enforce_monotonicity` 要求 d2 >= d4 >= d8 >= 0，将负的 d2（如 L24H7 的 -0.001051）也 clamp 到 0.0
4. Solver 将 254 head 放在 4-bit（d=0.0）+ 2 head 放在 2-bit（d=0.0）→ total_distortion = 0.0

对比：`mistral_c4_profiling_results.json`（C4 校准集）的 4-bit/8-bit 全部非零（256/256），是正常的。只有 `mistral_profiling_results.json` 和 `mistral_ppl_profiles_hires.json` 的 4-bit/8-bit 全零。

### 4. 修复建议

**方案 A（推荐）**：重新用 WikiText 校准集对 Mistral 做 4-bit/8-bit profiling，生成正确的 `mistral_profiling_results.json`

**方案 B（快速）**：在 `run_yi_mistral_downstream_k2.py` 中将 Mistral 的 standard profile 路径换成 `mistral_c4_profiling_results.json`（C4 校准集有正确数据），然后重跑 downstream eval。但需注意校准集不一致的问题。

---
