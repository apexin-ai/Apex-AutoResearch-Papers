# analysis icc neff estimation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_icc_neff_estimation_20260521T045230_result.json`
- **Structured JSON:** [`19b9e2e2c830b81c3278.json`](../../sessions/19/19b9e2e2c830b81c3278.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**α=0.50 (3 seeds)**：
- 三个 seed 的 PermG 二进制结果**完全一致**：`[1,1,1,0,1,1,1,0]`（6/8 sig）
- 6 个 canary→distinct 对全部显著，2 个 canary→mauve 对全部不显著
- **ICC(1,1) = 1.0**（SS_within = 0，无 seed 间分歧）
- **N_eff = 24 / (1 + 7×1.0) = 3.0**（每个 seed 仅贡献 1 个独立观测）
- 一致 pair：8/8，不一致：0/8

**α=0.00 null (3 seeds)**：
- 三个 seed 全部 0/8，ICC 退化（全零，无方差）

已保存至 `artifacts/icc_neff_analysis.json` 并注册 (`art_20260521_14d974`)。

---
