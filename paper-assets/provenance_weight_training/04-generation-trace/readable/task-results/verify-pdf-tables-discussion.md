# verify pdf tables discussion

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_pdf_tables_discussion_20260523T051234_result.json`
- **Structured JSON:** [`edea1d159b83e6be118d.json`](../../sessions/ed/edea1d159b83e6be118d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 论文验证结果

### 表格编号（从 main.aux 确认）
| Label | 编译后编号 | 正确？ |
|-------|-----------|--------|
| `tab:alpha_corr` | **Table 11** | ✓ |
| `tab:alpha_corr_perseed` | **Table 12** | ✓ |

### Discussion §6 内容检查

**r=0.80 vs r=0.706 区分**：正确。discussion.tex 第70-71行明确写了：
- `r(α_eff, q̄) = 0.80` → proxy-to-proxy (detector score) correlation
- `r(α_eff, true real fraction) = 0.706` → proxy-to-ground-truth
- 并解释了 gap 来源（thresholding noise in r_i）

引用也正确：r=0.80 指向 Table 12 (`tab:alpha_corr_perseed`)，r=0.706 指向 Table 11 (`tab:alpha_corr`)。

### `\placeholder` 宏
**已全部清除**，grep 无匹配。

---

## 训练状态

| 实验 | Step | 进度 | Loss | 
|------|------|------|------|
| rho03_adaptive_seed456_r2 | 2941/6103 | 48% | ~3.06 |
| rho03_uniform_seed456 | 4268/6103 | 70% | ~1.76 |
| bs8_nmin4_adaptive_seed123_r2 | 3426/6103 | 56% | ~2.19 |
| bs8_nmin4_uniform_seed123_r2 | 3490/6103 | 57% | ~2.24 |

4 GPU 全部在跑（80-100% utilization）。所有实验正常推进。

---
