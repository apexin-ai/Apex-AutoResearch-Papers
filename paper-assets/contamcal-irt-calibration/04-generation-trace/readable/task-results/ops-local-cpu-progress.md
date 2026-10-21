# ops local cpu progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_local-cpu-progress_20260514T092850_result.json`
- **Structured JSON:** [`b16936064da94690b5aa.json`](../../sessions/b1/b16936064da94690b5aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### exp-004 sim sweep v2 (PID 411032)
- **状态**: 运行中，已运行 2h17m，进程状态 S (sleeping)
- **进度**: **45/120 seeds (37.5%)**，5/12 conditions 有数据
  - auc0.55_n20: 10/10 done
  - auc0.55_n50: 10/10 done
  - auc0.55_n100: 7/10
  - auc0.8_n20: 10/10 done
  - auc0.8_n50: 8/10 (当前正在跑)
- **预估剩余**: ~26 小时（平均 ~20.7 min/seed），预计 5/15 ~11:00 完成

### exp-005 noise prop v3 (PID 426335)
- **状态**: 运行中，已运行 1h03m，进程状态 S (sleeping)
- **进度**: **5/25 fits 已保存**，当前在 σ_e=0.3 seed=42 的 analytic ME 模型（4 chains 已完成，即将写入第 6 个 fit）
  - σ_e=0.1: 5/5 seeds done
  - σ_e=0.3: seed=42 进行中
- **预估剩余**: ~11.5 小时（平均 ~35.5 min/fit），预计今晚 ~21:00 完成

---
