# code plan 012 analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-012-analysis_20260514T004217_result.json`
- **Structured JSON:** [`17967598e4682b742a7d.json`](../../sessions/17/17967598e4682b742a7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。脚本运行正常，输出完整。

**修改总结：**

| 项目 | 旧版 | 新版 |
|------|------|------|
| Bootstrap 95% CI | 无 | delta_full, delta_nd, death_avoidance_fraction 均有 |
| Death-only Δ | 不计算 | `delta_death_only` = 81.64 (聚合) |
| CLI `--data_dirs` | 逗号分隔 | 空格分隔 `nargs='+'` |
| CLI `--output` | 单文件路径 | 输出目录（含 report.json + paper_table.json + summary.csv） |
| CSV 输出 | 无 | summary.csv |
| pearsonr fallback | subprocess 调 python3（脆弱） | 纯 Python 实现（regularized incomplete beta） |
| 死代码 `aggregate_results` | 保留 | 删除 |

**Dry-run 结果（26 tasks, 153 episodes）：**
- Δ_full = +44.61, 95% CI [36.37, 52.75]
- Δ_nd = +0.7, 95% CI [-1.33, 2.6]
- Death avoidance fraction = 98%, CI [94.2%, 103.1%]
- Pearson r = 0.982, p < 0.000001
- 一键命令可用：`python src/death_decomposition.py --data_dirs results/plan_c results/prescreening results/research --output results/decomposition_final/`

---
