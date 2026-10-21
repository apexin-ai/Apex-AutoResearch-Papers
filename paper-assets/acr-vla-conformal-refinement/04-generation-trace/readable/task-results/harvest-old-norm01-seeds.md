# harvest old norm01 seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_old-norm01-seeds_20260521T035537_result.json`
- **Structured JSON:** [`4443699b95e9415a1095.json`](../../sessions/44/4443699b95e9415a1095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。

**结果**:
- 扫描 4 台服务器，修正 1 条 registry：`seed60` killed → success (SR=0.15，JSON 在 bjb2-28827 上完好)
- 其余 failed/killed 实验无可恢复 JSON，确认为真正失败
- **obs_only norm01 现有 18 个 unique seeds**，mean SR = **15.7% ± 2.2%**，95% CI [14.7%, 16.7%]，与 ROADMAP ~15.0% 一致
- 另有 seed66/67 仍在运行，seed76/77 在准备中

报告已写入 `artifacts/harvest_norm01_report.md`。

---
