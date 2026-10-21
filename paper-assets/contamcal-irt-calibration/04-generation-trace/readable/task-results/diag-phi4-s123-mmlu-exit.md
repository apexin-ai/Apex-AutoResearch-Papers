# diag phi4 s123 mmlu exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phi4-s123-mmlu-exit_20260520T151627_result.json`
- **Structured JSON:** [`5757dd36ab9bdaed4779.json`](../../sessions/57/5757dd36ab9bdaed4779.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Cron 误报，进程仍在正常运行。**

| Dosage | 状态 | Accuracy |
|--------|------|----------|
| d000_s123 | ✅ 完成 | **76.31%** (10716/14042) |
| d005_s123 | ✅ 完成 | **75.92%** (10661/14042) |
| d025_s123 | 🔄 进行中 | log 显示 98% (13829/14042) |
| d050_s123 | ⏳ 未开始 | — |
| d100_s123 | ⏳ 未开始 | — |

- PID 360893 存活，cuda:2 上运行
- 结果输出到 `/root/contamcal-irt-calibration/results/mmlu_eval/phi4/` （不是 `eval_results_v2/`）
- d025 马上完成，之后还有 d050 和 d100 两个 dosage，每个约 12-13 分钟，预计还需 ~30 分钟全部跑完

---
