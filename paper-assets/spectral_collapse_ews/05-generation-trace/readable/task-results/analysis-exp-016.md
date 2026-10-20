# analysis exp 016

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_016_20260522T183111_result.json`
- **Structured JSON:** [`e8158cf7045939ffff8d.json`](../../sessions/e8/e8158cf7045939ffff8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**exp_016 结果**: Type III trajectory 确认 (conclusion=success)。seed44 的 SLV 从 2366.68 → 2505.25 (+5.86%)，gen2 起严格单调上升。

**3-seed Gen10 统计** (r=0.3):
| 指标 | Mean ± Std |
|------|-----------|
| SLV (log_det) | 2508.24 ± 2.94 |
| eff_rank | 521.11 ± 0.20 |
| ppl | 13.344 ± 0.036 |
| distinct4 | 0.295 ± 0.155 |
| SLV 总变化 | +5.98% ± 0.12% |

谱指标 CV < 0.3%，3 seeds 高度一致。distinct4 跨 seed 方差大但不影响 Type III 分类。r=0.3 三 seed 验证完成，registry 已更新为 DONE，报告已保存并注册。

---
