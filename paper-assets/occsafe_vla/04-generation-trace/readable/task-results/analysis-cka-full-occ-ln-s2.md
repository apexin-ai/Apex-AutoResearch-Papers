# analysis cka full occ ln s2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_full_occ_ln_s2_20260525T031418_result.json`
- **Structured JSON:** [`4affa74ff38cb6ca6820.json`](../../sessions/4a/4affa74ff38cb6ca6820.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。CKA 分析已在提交时瞬间跑完（~2秒），结果已注册。

**结论：s0 DINOv2 CKA=0.640 确认为 seed-specific outlier。**

三个 seed 的 DINOv2 CKA 对比：
- s0: 0.640 (异常)
- s1: 0.965 (正常)
- s2: **0.9651** (正常)

产出文件在 `/root/autodl-tmp/analysis/cka_full_occ_ln_s2/`（cka_results.json, cka_analysis.pdf, cka_analysis.png）。

---
