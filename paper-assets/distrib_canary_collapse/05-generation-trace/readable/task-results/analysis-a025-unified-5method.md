# analysis a025 unified 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a025_unified_5method_20260516T185900_result.json`
- **Structured JSON:** [`a2f8ab48d16abb4b519a.json`](../../sessions/a2/a2f8ab48d16abb4b519a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Metric | Seed 43 | Seed 44 | Total (/16) |
|--------|---------|---------|-------------|
| Perm Granger FDR sig | 0/8 | 0/8 | **0/16** |
| TY sig (p<0.05) | 0/8 | 2/8 | 2/16 (cross-seed 不一致) |
| Robust consensus ≥3/5 | 0/8 | 0/8 | **0/16** |

**关键发现**: α=0.25 完全 sub-threshold，与预期一致。与 α=0.75 形成清晰对比。

**注意**: `a025_s42` 目录不存在，只有 s43/s44 两个 seed，结果为 /16 而非 /24。若需完整 /24 需补跑 seed 42。

产出文件:
- `results/alpha_sweep/a025_s43/analysis/5method_leadlag.json`
- `results/alpha_sweep/a025_s44/analysis/5method_leadlag.json`
- `results/alpha_sweep/a025_3seed_unified_summary.txt`

---
