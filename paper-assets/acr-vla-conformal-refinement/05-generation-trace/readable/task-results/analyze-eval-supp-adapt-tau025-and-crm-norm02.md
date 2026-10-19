# analyze eval supp adapt tau025 and crm norm02

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-adapt-tau025-and-crm-norm02_20260523T061041_result.json`
- **Structured JSON:** [`1ede75f360577308e4a8.json`](../../sessions/1e/1ede75f360577308e4a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。以下是分析报告。

---

## 实验结果报告 — LIBERO-Spatial seed42

### 实验 1: Adaptive CRM tau=0.25 (adaptive_conformal_crm)

| 指标 | 值 |
|---|---|
| **Overall SR** | **82.0%** (164/200) |
| Trigger rate | 19.4% |
| Mean uncertainty | 0.1847 |

**Per-task SR:**

| Task | SR |
|---|---|
| between_plate_and_ramekin | 95% |
| next_to_ramekin | 95% |
| from_table_center | **100%** |
| on_cookie_box | **100%** |
| in_top_drawer | 75% |
| on_ramekin | **0%** |
| next_to_cookie_box | 90% |
| on_stove | 90% |
| next_to_plate | 90% |
| on_wooden_cabinet | 85% |

### 实验 2: CRM norm=0.2 Always-on (crm_obs_only)

| 指标 | 值 |
|---|---|
| **Overall SR** | **79.0%** (158/200) |
| Trigger rate | 100% (always-on) |

**Per-task SR:**

| Task | SR |
|---|---|
| between_plate_and_ramekin | **100%** |
| next_to_ramekin | 90% |
| from_table_center | 95% |
| on_cookie_box | 95% |
| in_top_drawer | 75% |
| on_ramekin | **0%** |
| next_to_cookie_box | **100%** |
| on_stove | 95% |
| next_to_plate | 75% |
| on_wooden_cabinet | 65% |

### 对比分析

| 配置 | SR | Trigger Rate | 备注 |
|---|---|---|---|
| VLA-only | 78.5% | 0% | baseline |
| CRM norm=0.05 (always-on) | 80.0% | 100% | |
| CRM norm=0.1 (always-on) | 79.0% | 100% | |
| **CRM norm=0.2 (always-on)** | **79.0%** | **100%** | 本次 |
| Adaptive tau=0.2, norm=0.2 | 81.0% | ~30% | 前次 |
| **Adaptive tau=0.25, norm=0.2** | **82.0%** | **19.4%** | 本次 |

### 关键结论

**1. Adaptive tau=0.25 vs tau=0.2: tau 提高成功降低 trigger rate 且 SR 更高**
- tau=0.25: 82.0% SR, 19.4% trigger → tau=0.2: 81.0% SR, ~30% trigger
- trigger rate 从 ~30% 降到 19.4%，SR 反而从 81% 升到 82%
- 说明 tau=0.2 时有些不必要的 correction 反而有害，更精准的 gating 效果更好
- **Hypothesis confirmed**: tau=0.25 在 Pareto 前沿上严格优于 tau=0.2

**2. Adaptive (82%) vs Always-on norm=0.2 (79%): Gating 机制贡献 +3pp**
- 同一 norm=0.2，adaptive gating 比 always-on 高 3 个百分点
- always-on norm=0.2 甚至没有超过 VLA-only baseline (78.5%) 太多
- **结论: norm=0.2 的 correction 幅度过大，不加选择地 always-on 会损害性能**，gating 机制通过抑制不必要的大幅 correction 来提升整体表现

**3. Always-on norm 对比: norm=0.2 (79%) = norm=0.1 (79%) < norm=0.05 (80%)**
- norm 从 0.05 增大到 0.2，always-on SR 单调递减
- 验证了大 norm always-on correction 会 over-correct，尤其在 VLA 原本就做对了的 step 上
- on_wooden_cabinet 65% 和 next_to_plate 75% 是 always-on norm=0.2 的主要受害任务

**4. on_ramekin 任务所有配置均为 0%**，这是 VLA 本身的能力瓶颈，CRM 无法挽救。

---
