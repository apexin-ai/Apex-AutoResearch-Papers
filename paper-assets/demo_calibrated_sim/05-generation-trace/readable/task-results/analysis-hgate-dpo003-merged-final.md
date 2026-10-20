# analysis hgate dpo003 merged final

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_hgate-dpo003-merged-final_20260513T060551_result.json`
- **Structured JSON:** [`b86bd8ad553571152c99.json`](../../sessions/b8/b86bd8ad553571152c99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。以下是完整结论。

---

## hgate-dpo003-merged 最终结果：Plan A (DPO 校准) = **FAIL**

### 4 Runs 汇总

| Run | Baseline Politeness | Baseline Completion | H1 | H2 | H3 |
|-----|---|---|---|---|---|
| 1 | 0.475 | 27.8% | PASS | FAIL | FAIL |
| 2 | 0.466 | 15.0% | PASS | FAIL | PASS |
| 3 | 0.532 | 40.0% | PASS | FAIL | FAIL |
| 4 | 0.534 | 35.0% | PASS | FAIL | FAIL |

### Aggregate
- **H1 PASS (4/4)**: baseline politeness 均 ≥30%
- **H2 FAIL (0/4)**: 平均 politeness gap 变化 = **-10.3%**（需 ≥+30%）。12 个 variant 检查中 10 个 gap 反而扩大了，2 个略有缩小但远不到 30%
- **H3 FAIL (3/4)**: 平均 baseline completion = **29.4%** < 29.6% 阈值；calibrated variants 的 completion 大幅下降

### 核心失败原因

**H2 是致命问题**：DPO 训练没有缩小 politeness gap，反而扩大了。calibrated variants（aave/indian_english/overcorrected）的 politeness 比 baseline 更高（例如 run_1: baseline=0.475, aave=0.609, indian=0.577）。DPO 把模型往"更礼貌"的方向推了，但对所有方言 variant 推得更多，导致 gap 反向增大。

**H3 是次要问题**：calibrated variants 的 task completion 严重下降（部分低至 10%），说明 DPO 训练在增加礼貌的同时损害了任务完成能力。

### 结论

D011 此前基于 2/4 runs 的判定正确。完整 4 runs 数据确认：**Plan A（DPO 校准方法）FAIL**，conclusion=negative，已写入 registry。

---
