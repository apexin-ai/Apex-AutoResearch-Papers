# analysis mistral bit dist check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral_bit_dist_check_20260514T100413_result.json`
- **Structured JSON:** [`a64d50cf023bab233665.json`](../../sessions/a6/a64d50cf023bab233665.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**怀疑确认：l0_heuristic_corrected 的 Mistral MCKP 实际用了 18 个 2-bit head，不是 16 个。**

### 证据链

**文件**: `/root/ratekv/mistral_hires_results.json`

l0_heuristic_corrected 脚本硬编码引用的 `mckp_ppl: 7.323` 来自这个文件。该文件的 MCKP 求解配置为 `max_2bit=18`：

| Bit width | Head 数量 |
|-----------|----------|
| 2-bit     | **18**   |
| 4-bit     | 235      |
| 16-bit    | 3        |
| **总计**  | **256** (32层 × 8 KV heads) |

PPL = **7.3231** — 精确匹配 k_ablation 的 k=18 结果。

### 对比验证

**文件**: `/root/ratekv/mistral_hires_constrained16_results.json`

后续已做了修正实验，在同一 hires profile 上用 `max_2bit=16` 重新求解：

| 约束 | 2-bit heads | PPL |
|------|-------------|-----|
| max_2bit=18（原始，有 bug） | 18 | 7.3231 |
| max_2bit=16（修正后） | 16 | **7.3106** |

差异 = -0.0125 PPL。修正后 k=16 的 MCKP PPL 应为 **7.3106**，不是 7.3231。

### 根因

`run_l0_heuristic_corrected.py` 中 Mistral 配置 `k=16`（L0 heuristic 用 16 个 2-bit head），但 MCKP 参考值来自 `mistral_hires_results.json`，该文件求解时用的是 `max_2bit=18`。两边的约束不一致。

---
