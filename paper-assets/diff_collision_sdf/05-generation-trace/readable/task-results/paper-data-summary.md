# paper data summary

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_data_summary_20260524T160934_result.json`
- **Structured JSON:** [`3a6fdbd1da241329864a.json`](../../sessions/3a/3a6fdbd1da241329864a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件：`artifacts/_project/report/paper_data_summary.md`（art_20260524_7c4cb0）

包含 4 个数据表：
1. **Table 1** — Pi0.5+A1 3-seed × 2-lambda 矩阵，仅 s0 10K 有数据（TSR 47-49%, CAR 56-58%），s1/s2 TBD
2. **Claim 1 Fake Safety** — A1-LoRA 99.6% fake safe, LoRA 99.4%, Pi0.5 baseline 98.2%；Pi0.5+A1 是唯一 0% frozen 的方法
3. **Claim 3 Oracle** — GT SDF refinement 仍 96-98% fake safe，CAR 反而比无 refine baseline 更低（73-77% vs 82%）
4. **Scatter 数据** — 17 个数据点含 marker 建议，Pi0.5+A1 是唯一 Pareto-improving 方向

末尾列出 5 项待补充数据（seed 1/2 eval、Full-FT fake_safe_rate 等）。

---
