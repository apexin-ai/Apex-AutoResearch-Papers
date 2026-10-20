# code gemma lofo supplement

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma_lofo_supplement_20260521T014657_result.json`
- **Structured JSON:** [`61fa4ff7e9442a582181.json`](../../sessions/61/61fa4ff7e9442a582181.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是结果汇总：

---

## LOFO θ Validation 结果

### 代码位置
- **新建脚本**: `/root/autodl-tmp/gen-depth-contamination/scripts/lofo_theta_validation.py`
- **输出目录**: `results/lofo_theta_validation/`
  - `lofo_theta_results.json` — 完整数据
  - `lofo_theta_table.tex` — LaTeX 表格

### Gemma-2-2B 数据
数据完整可用，来源：`artifacts/exp_gemma2b_depth_bootstrap_ci.json`

### Per-family K* at θ=0.60

| Family | K* | 1v2 ci_lower | margin |
|--------|-----|-------------|--------|
| Qwen-rw | 2 | 0.6859 | +0.086 |
| Pythia | 2 | 0.6454 | +0.045 |
| OLMo | 2 | 0.6045 | +0.005 |
| Qwen-cont | 2 | 0.6015 | +0.002 |
| Qwen-7B | 2 | 0.6080 | +0.008 |
| **Gemma-2B** | **1** | **0.5882** | **-0.012** |

### LOFO θ̂ Range 表格

| Left-out | θ_low | θ_high | Width | θ̂(mid) | θ=0.60? |
|----------|-------|--------|-------|---------|---------|
| Qwen-rw | 0.5511 | 0.5882 | 0.0371 | 0.5696 | NO |
| Pythia | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
| OLMo | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
| Qwen-cont | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
| Qwen-7B | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |
| **Gemma-2B** | 0.5795 | 0.6015 | 0.0220 | 0.5905 | **YES** |
| All 6 | 0.5795 | 0.5882 | 0.0087 | 0.5838 | NO |

### 关键发现

1. **Gemma-2-2B 是 binding constraint**: 其 1v2 ci_lower=0.5882 将全集 K*=2 共识范围上界从 0.6015 压缩到 0.5882，θ=0.60 落在共识范围外。

2. **θ̂ 稳定性**: LOFO θ̂ midpoint 范围 [0.5696, 0.5905]，mean=0.5826 ± 0.0063。所有 6 个 LOFO 子集都产生有效共识范围。

3. **Framing 影响**: θ=0.585 可使全部 6 族（含 Gemma）达成 K*=2 共识。θ=0.60 仅在去掉 Gemma 时成立（5/6 原始模型）。

4. **论文调整建议**: 可以将 Gemma 定位为 borderline case（1v2 ci_lower 仅低于 θ 1.2pp），LOFO θ̂ 的窄波动（±0.63pp）仍然支持 K*=2 作为 robust boundary 的 claim。

---
