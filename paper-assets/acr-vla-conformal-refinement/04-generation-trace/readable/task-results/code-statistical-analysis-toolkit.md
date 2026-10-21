# code statistical analysis toolkit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_statistical-analysis-toolkit_20260515T135827_result.json`
- **Structured JSON:** [`df5e7deb37d404723341.json`](../../sessions/df/df5e7deb37d404723341.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，dry-run 全部通过：

- **Fisher test**: obs_only_0.1 vs argmin p=0.18（6-task partial 数据量不足，尚未显著），obs_only_0.2 vs argmin p=0.06（接近显著）
- **Bootstrap CI**: obs_only_0.1 mean=13.3% [3.3, 25.0]，argmin mean=6.7% [0.0, 16.7]
- **Magnitude curve**: 图已生成，obs_only 在 norm≥0.2 时稳定优于 perdof 和 argmin baseline
- **Comparison table**: 6 种方法对比表含 Fisher p-values

文件位置：
- 脚本: `src/analysis/statistical_tests.py`
- 图: `artifacts/magnitude_curve_draft.png` + `.pdf`

---
