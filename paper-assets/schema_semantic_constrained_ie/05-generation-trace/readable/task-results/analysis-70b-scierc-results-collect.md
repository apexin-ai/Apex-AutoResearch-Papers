# analysis 70b scierc results collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_70b_scierc_results_collect_20260518T132952_result.json`
- **Structured JSON:** [`be81de26943e2016fca7.json`](../../sessions/be/be81de26943e2016fca7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。汇总：

## 70B SciERC 结果

| 指标 | Unconstrained | Constrained (OntoCoDec) |
|------|:---:|:---:|
| ET_pct | 0% | 0% |
| RV_pct | 0.6% | **0%** |
| DR_pct | 6.5% | **0%** |
| CF_count | 0 | 86 (3.66%) |
| E_F1 | 0.3517 | 0.3514 |
| E_P | 0.3009 | 0.3007 |
| E_R | 0.4232 | 0.4226 |
| R_F1 | 0.1122 | 0.1124 |
| R_P | 0.0929 | 0.0932 |
| R_R | 0.1417 | 0.1417 |
| Parse failures | 0/551 | 0/551 |

**关键发现：**
- OntoCoDec 在 70B 上完全消除了 RV 和 DR 违规（6.5% → 0%），F1 几乎无损（差异 < 0.001）
- 70B 模型 scale 本身已消除 ET 违规（unconstrained 也是 0%），但 DR 仍有 6.5%
- Constrained 引入了 86 个 CF (cross-field consistency) 违规

## Registry 更新完成

- **spec.command 修复**：4 个实验全部已补齐 `--data_path`, `--constraints_path`, `--output_path`, `--skip_on_error`
- **SciERC 状态**：两个实验均已 → DONE (success)，metrics 和 notes 已录入
- **DocRED**：westd-16980 仍在运行（~42min elapsed），spec 已修复，等完成后再收集结果

---
