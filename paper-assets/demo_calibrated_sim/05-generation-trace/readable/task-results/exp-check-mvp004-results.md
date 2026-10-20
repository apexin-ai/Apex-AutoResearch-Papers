# exp check mvp004 results

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_check-mvp004-results_20260512T153442_result.json`
- **Structured JSON:** [`1d3a1739607be7d1b1c4.json`](../../sessions/1d/1d3a1739607be7d1b1c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个 variant 已完成。以下是完整结果。

## MVP-004 完整结果（6 variants, n=19-20）

| Variant | Politeness Rate | Question Rate | Completion Rate | n |
|---------|:-:|:-:|:-:|:-:|
| **baseline** (uncalibrated) | 55.9% | 4.4% | 36.8% | 19 |
| aave_target | 46.8% | 1.5% | 10.0% | 20 |
| indian_english_target | 46.0% | 1.4% | 15.0% | 20 |
| overcorrected | 60.5% | 1.8% | 26.3% | 19 |
| **single_dim_question** | 41.6% | 6.5% | 25.0% | 20 |
| **single_dim_politeness** | 63.4% | 2.1% | 20.0% | 20 |

## H-Gate 判定

| Gate | Passed | Detail |
|------|:------:|--------|
| **H1** | **PASS** | baseline politeness=55.9% > 30% threshold |
| **H2** | **FAIL** | 所有 3 个 calibrated variants 的 politeness improvement% 均未达到 30% 阈值：aave=25.4%, indian=27.6%, overcorrected=-10.0% |
| **H3** | **FAIL** | 所有 3 个 calibrated variants completion 均低于 retention threshold (29.5%)：aave=10%, indian=15%, overcorrected=26.3% |

**Overall: FAIL** (1/3 gates passed)

## 新 variant 结果解读

- **single_dim_question**: question_rate 从 baseline 4.4% 提升到 6.5%（方向正确但幅度有限），但 politeness 大幅下降到 41.6%，completion 降至 25%
- **single_dim_politeness**: politeness 从 baseline 55.9% 提升到 63.4%（最高），question_rate 控制在 2.1%，但 completion 也降至 20%

## 进程状态

- PID 111195 (python): **已退出**
- PID 110596 (vLLM): **仍在运行** — 需要手动清理以释放 cuda:2

---
