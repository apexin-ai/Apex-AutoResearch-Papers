# package supplementary results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_package_supplementary-results_20260528T073505_result.json`
- **Structured JSON:** [`7d56e346593d34068f65.json`](../../sessions/7d/7d56e346593d34068f65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个文件已生成并注册：

### 生成文件

| 文件 | 行数 | 说明 |
|------|------|------|
| `tau_sweep_results.csv` | 55 行 | SmolVLA + Pi05，τ=0.05–0.90，含 delta_vs_vla_only |
| `bonus_seeds_results.csv` | 65 行 | 4 benchmark × 4 method，seeds s42–s49 |
| `pi05_cross_vla_results.csv` | 33 行 | Pi05 去重后的 canonical 结果，4 benchmark × 3 mode × 3 seeds |
| `supplementary_summary.md` | 完整汇总 | 含 τ-sweep 表格、bonus seeds mean±std、K-sweep、CRM always-on ablation |

### 各类数据量

| 类别 | 有效实验数 | 状态 |
|------|-----------|------|
| A. τ-sweep | 55 (有 SR 值) / 81 总 | 充足 |
| B. Bonus seeds | 65 (有 SR 值) / 115 总 | 部分 incomplete（见下） |
| C. Pi05 cross-VLA | 33 canonical | 充足 |
| D. K-sweep | 23 有 SR / 38 总 | 多数 K=20 实验缺 SR |
| E. CRM always-on | 23 有 SR / 24 总 | 充足 |

### 数据缺口

- **Bonus seeds / long / adaptive**: s42/s45/s46 均无 SR — **incomplete**
- **Bonus seeds / object / adaptive**: 仅 1 个有效实验 (s42)
- **Bonus seeds / object & long / crm_obs_only**: 各仅 1 个有效实验
- **Pi05 / long / crm_obs_only**: 仅 s44 一个 seed
- **K-sweep K=20**: 仅 smolvla/object 有 SR，其余均为 None
- **CRM always-on / smolvla / long / s45**: SR 为 None

---
