# code mf1 lofo power calibration v2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf1_lofo_power_calibration_v2_20260522T105348_result.json`
- **Structured JSON:** [`c26ae5c01e2510ce1a8d.json`](../../sessions/c2/c26ae5c01e2510ce1a8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF1 完成。核心发现：

| | Full | Random Subsample | LOFO | Power Effect | Composition Effect |
|---|---|---|---|---|---|
| Remove Mistral (ref 1080→533) | 31.32% | 30.91±2.07% | 22.47% | −0.41pp (5%) | −8.44pp (95%) |
| Remove Llama-3 (foc 807→492) | 31.32% | 32.24±1.42% | 24.06% | +0.91pp (−13%) | −8.17pp (113%) |

**结论**：C% 下降几乎完全由 composition effect（family-specific removal）驱动，power effect（样本量减少）可忽略不计。随机移除同等数量模型时 C% 基本不变（Mistral: −0.4pp; Llama-3 甚至 +0.9pp），但定向移除特定 family 导致 8-9pp 的下降。LOFO observed 值远低于 random subsample 的 95% range，确认这不是统计波动。

输出文件在 `artifacts/mf1_lofo_power_calibration/`:
- `mf1_lofo_power_calibration.py` — 完整可复现脚本
- `power_calibration_results.csv` — 汇总结果
- `power_calibration_reps.csv` — 400 次 per-rep 详细数据
- `power_calibration_report.md` — 分析报告

---
