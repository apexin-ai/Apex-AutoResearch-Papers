# code irt fitting prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_irt-fitting-prep_20260519T221016_result.json`
- **Structured JSON:** [`9600d776072dd4edb199.json`](../../sessions/96/9600d776072dd4edb199.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。脚本位于 `/root/contamcal-irt-calibration/analysis/fit_irt_2pl_gamma.py`。

**测试结果**：
- `--help` 正常
- ARC 100 items + ADVI 500 draws → 完整运行，产出 `gamma_summary.csv`、`gamma_histogram.png`、`theta_summary.csv`
- ADVI fitting 耗时 ~9s（100 items）

**注意**：
- 实际数据在 `analysis/irt_data/` 目录（非任务描述的 `irt_data_v3`），格式匹配
- MMLU 有 14042 items（20 respondents），ARC 有 1172 items（21 respondents）
- 现有 Stan 模型用全局 γ，此脚本用 per-item γ_i
- PyMC 6.0.0 + arviz 1.1.0 已安装
- ADVI quick test 中 0/100 items 的 γ 显著（符合预期——ADVI 精度低+仅 100 items）

**用法示例**：
```bash
# ARC 全量 ADVI
python analysis/fit_irt_2pl_gamma.py --benchmark arc --method advi

# MMLU 1000 items NUTS
python analysis/fit_irt_2pl_gamma.py --benchmark mmlu --max-items 1000 --method nuts

# MMLU 1000 items ADVI (快)
python analysis/fit_irt_2pl_gamma.py --benchmark mmlu --max-items 1000 --method advi
```

---
