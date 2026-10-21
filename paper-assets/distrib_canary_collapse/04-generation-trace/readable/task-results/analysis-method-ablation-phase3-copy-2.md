# analysis method ablation phase3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_method_ablation_phase3_20260518T225001_result.json`
- **Structured JSON:** [`8f383a2c40ca35db5390.json`](../../sessions/8f/8f383a2c40ca35db5390.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 3 完成。7×5 BH FDR-corrected 矩阵：

| alpha | n | naive | diff | threshold | permG | TY |
|-------|---|-------|------|-----------|-------|-----|
| 0.00 | 24 | 96% | 33% | 46% | 0% | 0% |
| 0.10 | 8 | 100% | 12% | 38% | 0% | 0% |
| 0.25 | 16 | 100% | 62% | 38% | 0% | 0% |
| 0.50 | 24 | 100% | 88% | 83% | 0% | 0% |
| 0.60 | 8 | 100% | 100% | 75% | 100% | 50% (bf16) |
| 0.75 | 24 | 100% | 96% | 100% | 83% | 0% |
| 1.00 | 32 | 100% | 100% | 100% | 75% | 59% |

关键发现：

1. **α=0.10 确认为盲区** — 和 α=0.00 一样，robust methods (permG/TY) 均为 0%

2. **permG 在 α=0.50-0.60 之间存在阶跃跳变** — 从 0% (α≤0.50) 直接跳到 100% (α=0.60) / 83% (α=0.75)。α=0.50 的 50% raw significance 全部被 FDR 翻转（12 个 flip），说明 p-values 集中在临界附近

3. **TY 在 α≤0.75 后全部为 0%（FDR 后）**，仅 α=1.00 有 59%，再次确认 C003

4. **多 seed 修正了 Phase 2 的单 seed 估计** — α=0.25 diff 从 25%→62%（新 seed 影响大），α=0.25 TY 从 38%→0%（seed 不稳定）

5. **α=0.60 bf16 单 seed 需谨慎解读** — permG=100%、TY=50% 可能受 bf16 精度和 seed 方差影响

产出文件：
- 服务器: `results/method_ablation_phase3_panel.json` + `results/method_ablation_phase3_report.md`
- 本地: `artifacts/method_ablation_phase3/method_ablation_phase3_summary.md` (已注册 art_20260518_d2036c)

---
