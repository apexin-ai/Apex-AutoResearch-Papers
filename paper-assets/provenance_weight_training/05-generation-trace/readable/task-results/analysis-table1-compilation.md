# analysis table1 compilation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table1_compilation_20260516T011300_result.json`
- **Structured JSON:** [`19c7a66b27da5aa1eeaf.json`](../../sessions/19/19c7a66b27da5aa1eeaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入并注册 (`art_20260516_3b775e`)。

**验证摘要**：所有 PPL 数字与 registry 完全一致。关键结果：

- **最优方法**：Grid b=0.5 (mean 17.6463, Δ=−0.0475) 略优于 Adaptive τ=0.8 (mean 17.6508, Δ=−0.0430)
- seed456 grid b≥2.0 三组因 checkpoint resume artifact 已排除，对应行只报 2 seeds
- τ sweep 最优点在 τ=0.8，n_min 最优点在 n_min=2
- ρ=0.6 还有 3 个实验 RUNNING（adaptive/grid b=0.5/ESS-only）

LaTeX 代码已包含三张表（main、τ sweep、n_min ablation），可直接粘贴到论文。PPL 在 LaTeX 中统一保留 3 位小数，Δ 保留 3 位。

---
