# analysis qwen7b n3 bootstrap ci

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen7b-n3-bootstrap-ci_20260521T001734_result.json`
- **Structured JSON:** [`fe9760345060baf5dd9f.json`](../../sessions/fe/fe9760345060baf5dd9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen-7B n=3 BCa Bootstrap CI 结果

### 数据源

| Seed | MMLU 来源 | ARC 来源 |
|------|----------|---------|
| s0 | eval_qwen7b_mmlu_arc_s0 (success) | 同左 |
| s42 | eval_qwen7b_s42_cqa1_v2 MMLU 部分 (D162 确认 Δ=-1.82pp) | eval_qwen7b_arc_s42 (success) |
| s123 | eval_qwen7b_s123_cqa1_v2 (success) | 同左 |

### Per-seed Δ(d000→d100)

| Seed | MMLU Δ(pp) | ARC Δ(pp) |
|------|-----------|----------|
| s0 | -1.03 | -1.88 |
| s42 | -1.82 | -2.90 |
| s123 | +0.00 | -2.47 |

### BCa Bootstrap CI (B=10000, seed=42)

| Benchmark | n | Mean Δ | 95% BCa CI | CI∋0 | Pattern |
|-----------|---|--------|-----------|------|---------|
| **MMLU** | 3 | **-0.95pp** | **[-1.82, -0.34]** | No | V-recovery |
| **ARC** | 3 | **-2.42pp** | **[-2.90, -2.08]** | No | V-recovery |

**Direction consistency: ✓** — 两个 benchmark 均为 negative。

### n=2→n=3 关键变化

- CI 方法从 t(df=1) 升级为 BCa bootstrap，CI 宽度大幅收窄
- MMLU: [-12.16, +10.37] → **[-1.82, -0.34]**（CI 排除 0，n=2 时包含 0）
- ARC: [-5.90, +0.61] → **[-2.90, -2.08]**（CI 排除 0，n=2 时包含 0）
- 两个 benchmark CI 均排除 0 → contamination 对 Qwen-7B 的 negative effect 在 family level 统计显著

### Family-level 判断

Mean 显著为负但幅度 <3pp，结合 per-seed dose-response 曲线均呈 V 形（dip then partial/full recovery）→ **V-recovery**。s123 完全恢复(0.00pp)、s0 部分恢复(-1.03pp)、s42 部分恢复(-1.82pp)，恢复程度因 seed 而异。

---
