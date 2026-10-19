# ops check plan013v2 status

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-plan013v2-status_20260521T120837_result.json`
- **Structured JSON:** [`5aabf835b04cc1059bcc.json`](../../sessions/5a/5aabf835b04cc1059bcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰了。汇报如下：

## 状态

**进程存活** — PID 47972 已运行 11h12m，正在执行 `probing_controls_v2.py`。

## 进度

8 层中已完成 4 层（0, 12, 16, 20），剩余 4 层（24, 27, 4, 8）。每层耗时 ~2-3.5 小时，预计还需 **8-14 小时**完成。

已完成层的结果：

| Layer | CV AUROC | Perm AUROC | Selectivity |
|-------|----------|------------|-------------|
| 0     | 0.6304   | 0.5007     | +0.1297     |
| 12    | 0.6389   | 0.4977     | +0.1411     |
| 16    | 0.6801   | 0.5038     | +0.1764     |
| 20    | 0.7211   | 0.5006     | +0.2205     |

趋势正常：deeper layers → higher selectivity，permutation baseline 在 ~0.50 符合预期。

## Registry 状态不一致

`conclusion=failed` 是错误标记。进程正在正常运行且产出合理结果。建议将 registry 的 `conclusion` 字段清除或改为 `pending`。

## 建议

1. 不要干预，让它跑完（预计还需半天左右）
2. 修正 registry 中 `conclusion=failed` 的错误标记
3. 完成后结果应写入 `results/probing_controls_v2.csv`（当前仅输出到 `/tmp/probing_v2.log`，需确认脚本最终是否写 CSV）

---
