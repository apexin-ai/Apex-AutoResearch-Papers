# eval baseline 245eps

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline-245eps_20260514T080744_result.json`
- **Structured JSON:** [`7e2df0efcbad770e47e1.json`](../../sessions/7e/7e2df0efcbad770e47e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 245-ep Baseline Results (11 tasks)

| Baseline | Mean Score | 90% CI | Success | Death | SimRatio |
|---|---|---|---|---|---|
| always-internal | **-39.07** | [-44.89, -33.37] | 0.131 | 0.429 | 0.000 |
| always-deterministic | **-9.47** | [-13.66, -5.11] | 0.241 | 0.163 | 1.000 |
| oracle | **-6.58** | [-10.65, -2.43] | 0.253 | 0.143 | 0.962 |
| random | **-22.38** | [-27.75, -17.09] | 0.184 | 0.278 | 0.524 |

与 194 eps 对比（方向一致，数值微调）：
- always-int: -37.16 → -39.07（新增 eps 偏差）
- always-det: -11.64 → -9.47（改善）
- oracle: -9.03 → -6.58（改善）
- random: -23.75 → -22.38

**处理细节**：`episode_summary.jsonl` 只有 194 行（旧数据），脚本优先读它而忽略 245 行的 `episodes.jsonl`。已从 `episodes.jsonl` 重建全部 summary 文件（旧文件备份为 `.bak194`）。

结果已写入 `results/baseline_245eps/`，registry 已更新为 `plan-003-baseline-245eps`。

---
