# cpu rho max verify

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_rho_max_verify_20260521T120007_result.json`
- **Structured JSON:** [`a48e160a4dc88acf10ec.json`](../../sessions/a4/a48e160a4dc88acf10ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the analysis:

---

## Abstract ρ_max 核实结果

### 当前 Abstract 写法
> Quality estimation signals correlate with oracle F1 ($\rho$ up to 0.45, AUROC up to 0.82)

### 实际 ρ 值汇总

**Table 1 (N=8, seed=42, primary)**

| Config | Signal | ρ |
|--------|--------|---|
| CoNLL (Qwen) | EM | **0.451** ← Table 1 最高 |
| CoNLL (Qwen) | SJ | 0.436 |
| CoNLL (LLaMA) | SJ/EM | 0.431 |

→ 0.451 四舍五入 = 0.45，Abstract 对 N=8 primary 是准确的。

**Table robustness (N=16, LLaMA CoNLL, 3-seed mean ± σ)**

| Signal | ρ |
|--------|---|
| SJ | **0.474 ± 0.009** |
| EM | **0.473 ± 0.010** |
| VC | 0.470 ± 0.006 |
| FK | 0.467 ± 0.009 |

**Individual seed 最高值 (unified_rho_full.json, N=16)**

| Config | Signal | ρ |
|--------|--------|---|
| LLaMA CoNLL seed42 | SJ | **0.4836** ← 全局最高 |
| LLaMA CoNLL seed42 | EM | 0.4818 |
| LLaMA CoNLL seed456 | EM | 0.4752 |

**特殊情况（不宜放 Abstract）**
- WNUT-17 VC full-set: ρ=0.724（但 conditional ρ=0.038，被 zero/non-zero boundary 驱动）
- SciERC 6+ entities 子集: SJ ρ=0.547（stratified subset）

### 结论

| 范围 | ρ_max | Abstract "0.45" 是否准确 |
|------|-------|--------------------------|
| N=8 primary (Table 1) | 0.451 | ✅ 准确 |
| N=16 3-seed mean (Tab robustness) | **0.474** | ❌ 偏低 |
| N=16 单 seed 最高 | **0.484** | ❌ 偏低 |

审稿人提到的 "EM 0.472 (LLaMA CoNLL)" 应该指的是 Tab robustness 中 EM 3-seed mean = 0.473。

### 修正建议

**方案 A**（保守，限定 N=8）: 不改，但需在 Abstract 中明确 "at N=8"，避免被认为隐瞒 N=16 结果。

**方案 B**（推荐）: 改为 `$\rho$ up to 0.47`，覆盖 N=16 三种子均值 0.474，四舍五入准确。Abstract 不需要区分 N=8/N=16，"up to" 应覆盖论文中所有正式报告的值。

**方案 C**（最精确）: 改为 `$\rho$ up to 0.48`，覆盖单 seed 最高值 0.484，但论文正文表格报的是 3-seed mean 0.474，用 0.48 可能反而过高。

推荐 **方案 B: "ρ up to 0.47"**。

---
