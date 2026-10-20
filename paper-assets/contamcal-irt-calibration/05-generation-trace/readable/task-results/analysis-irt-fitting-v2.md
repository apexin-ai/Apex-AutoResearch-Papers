# analysis irt fitting v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt-fitting-v2_20260520T031009_result.json`
- **Structured JSON:** [`77a4958ab1bdd6164df6.json`](../../sessions/77/77a4958ab1bdd6164df6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已启动并在运行（PID 265452）。

```
IRT fitting: 已启动
tmux session: irt_fitting_mmlu_v3
PID: 265452 (python fit_irt_2pl_gamma.py)
PyMC: 已安装 (conda base, python 3.12)
命令: python fit_irt_2pl_gamma.py --benchmark mmlu --data-dir irt_data_v3/ --output-dir results/irt/ --method advi --draws 1000 --seed 42
预计运行时间: ~30-60min (ADVI, 25×14042)
监控: tail /root/runs/contamcal-irt-calibration/irt_fitting_mmlu_v3.log
Registry: irt_fitting_mmlu_v3 (PREPARING)
```

---
