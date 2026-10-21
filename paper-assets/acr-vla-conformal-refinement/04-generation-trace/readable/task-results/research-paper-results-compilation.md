# research paper results compilation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-results-compilation_20260515T200332_result.json`
- **Structured JSON:** [`a324bab48b4f8188dd4f.json`](../../sessions/a3/a324bab48b4f8188dd4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成 `results_tables.md` 并注册（`art_20260515_9c36f1`）。包含 5 张表：

1. **Table 1 — Object 6-way**: obs_only 19% 领先，argmin/VLA-only/VLA-mean 均 12%，perdof 11%，scalar 9%。含 10-task 逐任务 SR。
2. **Table 2 — Spatial 6-way**: obs_only 和 perdof 并列 35%，argmin 34%，scalar/VLA-mean 32%，VLA-only 30%。含逐任务 SR。
3. **Table 3 — Spatial Magnitude Sweep**: 5 个 norm 点（0.03–0.3），perdof vs obs_only。obs_only 0.03 为 7/10 partial（RUNNING），perdof 0.2 为 6/10 partial（killed）。含完整逐任务分解。
4. **Table 4 — Object Magnitude**: obs_only 0.1=19%, 0.2=22% 为 FINAL，其余 7 个实验 RUNNING（1–2/10 tasks）。
5. **Table 5 — Seed=43 Progress**: VLA-only DONE 12%（与 seed=42 一致），其余 5 个实验 RUNNING（2–6/10 tasks）。

---
