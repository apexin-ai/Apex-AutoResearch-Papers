# code exp two sided v2

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_two_sided_v2_20260520T085412_result.json`
- **Structured JSON:** [`ee7c6db79b0f2e8b1131.json`](../../sessions/ee/ee7c6db79b0f2e8b1131.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 artifacts registered. Here's the summary:

## 结果

**v2 flagged 57/60 (95.0%)** — 比 v1 (56/60, 93.3%) 甚至略高。

### 核心发现

修正 θ 估计（benchmark-specific MLE）+ 使用参数化 bootstrap 经验零分布 + BH-FDR 控制后，flagging rate **没有下降**。这说明 v1 的高 flagging rate 不是全局 θ 偏移的 artifact，而是 **4PL IRT 模型本身无法拟合 LLM 的 response patterns**。

lz* 值极端（MMLU/HellaSwag 上 |lz*| = 8-36），1000 次 bootstrap 复制从未产生如此极端的值（p_emp = 0.000）。

### 3 个未被 flag 的 cell
- Yi-Lightning × arc_c (lz*=1.66, p=0.095)
- 360GPT2-Pro × humaneval (lz*=1.50, p=0.125)  
- Yi-Lightning × humaneval (lz*=1.35, p=0.178)

### Gemini-1.5 × MMLU
- 100% accuracy → θ_bench=4.0 (boundary), lz*=31.8, p_emp=0.000, **flagged**

### 方法论意义
全局 θ vs benchmark-specific θ 的 calibration gap 确实存在（mean gap ±0.2-0.4），但这不是主因。主因是 LLM 违反 4PL 假设（局部独立性、单维性），即使在单个 benchmark 内也存在系统性 misfit。

### 产出文件
- `src/two_sided_detection_v2.py` — 完整 pipeline
- `artifacts/phase_b_two_sided_v2/` — 5 个输出文件（personfit_matrix_v2.csv, empirical_pvalues.csv, two_sided_summary_v2.json, lz_star_heatmap_v2.png, analysis_report.md）

---
