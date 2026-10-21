# analysis coverage boost exec

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_coverage-boost-exec_20260516T191034_result.json`
- **Structured JSON:** [`983103776a24937da683.json`](../../sessions/98/983103776a24937da683.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 项 Coverage Boost 分析全部完成：

| Task | 产出 | 状态 |
|------|------|------|
| **A: n_min 消融 → Claim 1** | paper_framing.md Claim 1 新增 n_min auto-compute 证据（含 n_min=1/2/4 消融数据） | ✅ |
| **B: Grid-b 位移 CSV** | `artifacts/grid_b_shift.csv` — 20 行，3 seeds × b∈{0.1-5.0}，含 delta_ppl 和 pct_shift | ✅ registered (art_20260516_332bc1) |
| **C: Golden Ratio → Claim 3** | paper_framing.md Claim 3 新增 τ=1−ρ/2 经验规则（2 验证点 + ρ=0.2 预测） | ✅ |
| **D: τ×ρ 部分网格表** | `artifacts/tau_rho_grid.csv` — 9 行（ρ=0.4×6 + ρ=0.6×3），含 exp_id 溯源 | ✅ registered (art_20260516_196973) |

---
