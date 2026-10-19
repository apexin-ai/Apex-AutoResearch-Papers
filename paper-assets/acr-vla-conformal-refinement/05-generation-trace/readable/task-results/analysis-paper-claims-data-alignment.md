# analysis paper claims data alignment

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-claims-data-alignment_20260517T111825_result.json`
- **Structured JSON:** [`d878303872ddba31e759.json`](../../sessions/d8/d878303872ddba31e759.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/paper_data_alignment.md` 并注册。核心发现：

**Claim 1 (pipeline improvement)**: ✅ 充分。6v6 seeds, p=0.0074, d=1.21 全部 registry 验证通过。

**Claim 2 (magnitude interaction)**: ⚠️ 部分。趋势清晰但 Figure 2 低 norm 端 (0.03, 0.05) 双方法仅 1 seed，无法加 error bars，且无 RUNNING 实验覆盖。perdof default 也仅 1 seed。

**Claim 3 (per-DOF negative result)**: ⚠️ 部分。所有 spatial 数据单 seed。perdof spatial norm=0.3 实际 26%，低于论文声称的 "30-35%" 范围。

**数据错误**: scalar CRM seed42 paper_framing 写 15%，registry 实为 9%。VLA-mean seed44/45 已完成但 paper_framing 未更新。

**关键建议**: 8 张空闲 GPU 应优先补 Figure 2 低 norm 端 (0.03/0.05) 的 multi-seed 数据和 perdof default 额外 seed。

---
