# analyze eval supp reconvla k2 spatial s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-reconvla-k2-spatial-s42_20260523T083410_result.json`
- **Structured JSON:** [`4304458fa8e9d4ca0f24.json`](../../sessions/43/4304458fa8e9d4ca0f24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验日志都已读取完毕。

```
实验: eval-supp-reconvla-k2-spatial-s42
状态: 正常完成 (return_code=0)
整体 SR: 160/200 = 80.0%
trigger_rate: N/A (reconvla 模式无 trigger_rate)
各 task SR:
  1. between_plate_and_ramekin  → 95.0% (19/20)
  2. next_to_ramekin            → 100.0% (20/20)
  3. from_table_center          → 100.0% (20/20)
  4. on_cookie_box              → 95.0% (19/20)
  5. in_top_drawer              → 75.0% (15/20)
  6. on_ramekin                 → 0.0% (0/20)
  7. next_to_cookie_box         → 95.0% (19/20)
  8. on_stove                   → 75.0% (15/20)
  9. next_to_plate              → 80.0% (16/20)
  10. on_wooden_cabinet         → 85.0% (17/20)
备注: K=2 reconvla 得到 80%，高于预期的 ~78.5% VLA-only baseline。centroid bug 假设（K=2 argmin 退化为 K=1）下仍拿到 80%，说明 CRM correction 本身就提供了改进，但幅度不大（~1.5pp over VLA-only）。这没有达到预期的"完全等于 K=1"——80% > 78.5%，CRM correction 仍有少量贡献。

实验: eval-supp-adapt-tau025-spatial-s43
状态: 正常完成 (return_code=0)
整体 SR: 160/200 = 80.0%
trigger_rate: 19.4% (mean_unc=0.1845, conformal_threshold=0.25)
各 task SR:
  1. between_plate_and_ramekin  → 95.0% (19/20)
  2. next_to_ramekin            → 95.0% (19/20)
  3. from_table_center          → 95.0% (19/20)
  4. on_cookie_box              → 100.0% (20/20)
  5. in_top_drawer              → 70.0% (14/20)
  6. on_ramekin                 → 0.0% (0/20)
  7. next_to_cookie_box         → 100.0% (20/20)
  8. on_stove                   → 80.0% (16/20)
  9. next_to_plate              → 85.0% (17/20)
  10. on_wooden_cabinet         → 80.0% (16/20)
备注: tau=0.25 adaptive CRM seed43 也是 80%。trigger_rate 19.4% 表示只在约 1/5 的 step 触发 CRM correction（max_correction_norm=0.2）。与 seed42 的 full reconvla 80% 一致，说明 adaptive 模式用更少的 intervention（19.4% vs 100%）达到了相同效果。
```

---
