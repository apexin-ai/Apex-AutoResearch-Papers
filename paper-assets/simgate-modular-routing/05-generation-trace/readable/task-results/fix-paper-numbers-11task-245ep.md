# fix paper numbers 11task 245ep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper-numbers-11task-245ep_20260514T081613_result.json`
- **Structured JSON:** [`8e0991d3004d2d1d3a2f.json`](../../sessions/8e/8e0991d3004d2d1d3a2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成。

## 修改清单

### 1. paper_framing.md — 已保存
| 原值 (30-task/249-ep) | 新值 (11-task/245-ep) | 出现位置 |
|---|---|---|
| ~99% | ~90% | Core Insight, Differentiation, Story Spine, Reviewer #4 |
| Δ_full=+38.33 | +29.60 [A] | Core Insight, C1, Story Spine, Headline |
| Δ_nd=+0.48 | +2.84 [A] | Core Insight, C1, Story Spine, Headline |
| DAF=98.75% | 90.41% [A] | Core Insight, C1, Headline |
| r=0.9864 | 0.9698 [A] | Core Insight, C1, Headline |
| p<0.0001 | p=8.12e-07 [A] | Core Insight, C1, Headline |
| 30 tasks / 249 eps | 11 tasks / 245 eps [A] | 全文 |
| Δ_nd/Δ_full=1.3% | 9.6% [A] | Core Insight, C1, Story Spine |
| 102/1/146 | 86/9/150 [A] | C1 |
| find-non-living-thing n=5, Δ=-6.80 | n=40, Δ=+9.58 [A] | C1, Core Insight |
| 5 outlier tasks (详细描述) | 单一 key exception: find-non-living-thing | Core Insight, C1 |
| 25/30 DAF≥95% | 移除（用 key exception 替代） | C1 |
| 93/102=91.2% death_asymmetry | 移除（无 11-task 等价数据） | C1 |
| "negligible" | "small but non-negligible" | C1, Story Spine |
| Data Provenance Note (引用 death_decomposition_report.json) | 删除，替换为数据源权威声明 | 文件末尾 |
| — | 新增 Robustness Check 段（30-task 数字标注 [B]） | 新增段落 |

### 2. paper_provenance.yaml — 已保存 (v12→v13)
| Claim | 变更 |
|---|---|
| 顶层 data_authority | death_decomposition_report.json (30/249) → plan-012-full (11/245) |
| C003 | DAF 0.9875→0.9041, text ~99%→~90% |
| C006 | Δ_full 38.33→29.60, Δ_nd 0.48→2.84 |
| C010 | r 0.9864→0.9698, p <0.0001→8.12e-07 |
| C015 | 102/1/146→86/9/150, 百分比相应更新 |
| C023 | 25/30 DAF≥95% → 10/11 death-dominated, sole exception find-non-living-thing |
| C024 | 全部数字回退到 11-task |
| C025 | Δ_nd 0.48→2.84, 1.3%→9.6%, "negligible"→"small but non-negligible" |
| C028 | 同 C015 |
| C031 | 93/102=91.2% → 86 det-preferred, DAF=90.41%（无细分） |
| C035 | 0.9875→0.9041 |
| C040 | 38.33→29.60, 0.48→2.84 |
| C046 | 25/30→10/11, 移除 measure-melting-point-unknown 异常值 |
| C053 | 0.9864→0.9698 |
| C071 | 5-outlier→单一 key exception (n=40, Δ=+9.58) |
| C072 | 同 C071 对齐 |
| 所有 claims | source 字段统一为 plan-012-full (11 tasks / 245 eps) |

### 3. artifacts/paper_data_tables.md — 服务器上不存在，跳过

### 4. ROADMAP.md — 已验证，数字已是 11-task/245-ep，无需修改

---
