# fix chart data correction

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_chart-data-correction_20260516T150919_result.json`
- **Structured JSON:** [`8a2569fce4677a715e48.json`](../../sessions/8a/8a2569fce4677a715e48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复结果汇总

### 过滤统计

| 数据集 | 过滤前 | eval (b=0) | 过滤后 |
|--------|--------|------------|--------|
| ρ=0.4 (adaptive_fix_seed42) | 51,913 | 25,922 | **25,991** |
| ρ=0.6 (contamination_60_seed42_r2) | 24,412 | 325 | **24,087** |

### 修正后的统计值

| 指标 | ρ=0.4 | ρ=0.6 |
|------|-------|-------|
| b\* mean | 1.425 (std=1.941) | 1.402 (std=1.964) |
| α\_eff binding rate | 38.2% | 33.4% |
| ESS binding rate | 34.4% | 36.3% |

### 生成文件

| 文件 | PDF | PNG |
|------|-----|-----|
| `bstar_distribution_rho_comparison` | 22,187 B | 73,426 B |
| `alpha_eff_binding_rate_rho_comparison` | 22,540 B | 198,033 B |
| `bstar_trajectory_adaptive_fix` | 248,653 B | 407,383 B |

路径：`westd-47453:/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/`

ρ=0.4 之前报告 N=51,913 实际约一半是 eval 记录（b=0.0, ess=4.0, loss=unweighted_loss），过滤后 N=25,991。bstar_trajectory PDF 从 0 bytes 修复为 248KB。

---
