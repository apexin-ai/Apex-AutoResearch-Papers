# ops extract s42v2 d102 correct values

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract-s42v2-d102-correct-values_20260523T102904_result.json`
- **Structured JSON:** [`297cf35598ce25ee519c.json`](../../sessions/29/297cf35598ce25ee519c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the comparison:

---

## D102 源文件 vs Registry 对比

### scale_14b_t10_a050_s42_fp32_v2

源文件：`westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t10_a050_s42_fp32_14b/analysis/5method_leadlag.json`

| 指标 | Registry (L9925-9931) | D102 源文件 | 匹配? |
|------|----------------------|-------------|-------|
| PermG fwd (FDR) | 4/8 | 4/8 | ✓ |
| PermG rev (FDR) | 2/8 | 2/8 | ✓ |
| **DiffXCorr fwd (FDR)** | **8/8** | **4/8** | **✗ 错误** |
| DiffXCorr rev (FDR) | (未记录) | 4/8 | - |
| **Threshold (3sigma)** | **1/8** | **2/8** | **✗ 错误** |
| TY | NaN | 0/8 | ~合理 |
| K≥3 | 3/8 | 3/8 | ✓ |
| K≥4 | (未记录) | 0/8 | - |

### scale_14b_t10_a075_s42_fp32_v2

源文件：`westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t10_a075_s42_fp32_14b/analysis/5method_leadlag.json`

| 指标 | Registry (L9760-9767) | D102 源文件 | 匹配? |
|------|----------------------|-------------|-------|
| PermG fwd (FDR) | 5/8 | 5/8 | ✓ |
| PermG rev (FDR) | 0/8 | 0/8 | ✓ |
| **DiffXCorr fwd (FDR)** | **8/8** | **6/8** | **✗ 错误** |
| DiffXCorr rev (FDR) | (未记录) | 6/8 | - |
| Threshold (3sigma) | 0/8 | 0/8 | ✓ |
| **TY** | **NaN** | **3/8** | **✗ 错误** |
| K≥3 | 5/8 | 5/8 | ✓ |
| K≥4 | (未记录) | 2/8 | - |

---

## 结论

Reviewer #141 确认正确。两个实验的 **DiffXCorr fwd 都被错误记录为 8/8**：
- a050_s42 v2: 实际 **4/8**（非 8/8）
- a075_s42 v2: 实际 **6/8**（非 8/8）

根因：Registry 录入时使用了未 FDR 校正的 `significant` 字段（或 raw count），而非 `significant_fdr` / `diff_xcorr_fdr_forward_sig`。

额外发现：
- a050 的 Threshold 也错（registry 1/8 → 实为 2/8）
- a075 的 TY 不是 NaN，实际是 **3/8**（α=0.75 > 0.50，不受 C003 禁用限制）

---
