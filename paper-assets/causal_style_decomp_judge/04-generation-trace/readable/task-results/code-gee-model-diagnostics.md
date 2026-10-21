# code gee model diagnostics

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gee_model_diagnostics_20260521T060943_result.json`
- **Structured JSON:** [`905274e9e67c969a4f27.json`](../../sessions/90/905274e9e67c969a4f27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。脚本 `csd_pipeline/gee_diagnostics.py` 已在服务器上运行成功。

---

### 结果摘要

**TABLE A: Correlation Structure Comparison**
- |ΔQIC| < 0.001 且 Max|ΔCoef| < 0.02（所有 6 cells），Exchangeable 和 Independence 结果实质等价——预期中，因为 cluster size = 2
- α 范围 [-0.25, +0.11]，within-pair correlation 较弱

**TABLE B: GEE Coefficients (Exchangeable)**

| Judge | Axis | Style OR | Style p | Orig OR | Orig p |
|-------|------|----------|---------|---------|--------|
| GPT-4o | Formality | 2.58 | 0.002 | 2.32 | 0.006 |
| GPT-4o | Verbosity | **11.34** | 1.1e-8 | 0.45 | 0.062 |
| GPT-4o | Register | 1.88 | 0.027 | 2.21 | 0.005 |
| Qwen3-32B | Formality | 4.20 | 0.0002 | 4.70 | 5.2e-5 |
| Qwen3-32B | Verbosity | **13.10** | 2.6e-9 | 0.49 | 0.096 |
| Qwen3-32B | Register | 1.91 | 0.046 | 5.72 | 8.5e-8 |

- Verbosity 的 style effect 最强（OR~11-13），originality 不显著
- Formality 两个 effect 均显著
- Register 的 originality effect 在 Qwen3-32B 上极强（OR=5.72）

**TABLE C: Interaction (Formality)**
- 两个 judge 的 style×originality interaction 均不显著（p=0.53, 0.32），两个 effect 可视为独立

---
