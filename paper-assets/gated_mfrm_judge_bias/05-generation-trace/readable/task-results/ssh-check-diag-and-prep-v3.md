# ssh check diag and prep v3

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-diag-and-prep-v3_20260525T153021_result.json`
- **Structured JSON:** [`725ffa48269b92d92444.json`](../../sessions/72/725ffa48269b92d92444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `diagnosis_and_v3_results.txt`。汇总：

---

**Part 1: 诊断实验**

| Method | tau | rho | R-hat | ESS |
|--------|-----|-----|-------|-----|
| Raw Average (500 items) | 0.838 | 0.949 | N/A | N/A |
| Variant A: c_n=0 (pure MFRM) | 0.824 | 0.934 | 1.006 | 1304 |
| Variant B: tighter prior (HN 0.3) | 0.794 | 0.926 | 1.008 | 1121 |
| N=16 G-MFRM (excl gpt-4-turbo) | 0.817 | 0.935 | 1.013 | 680 |
| exp-020 v2 joint_gmfrm (500 items) | 0.794 | 0.926 | 1.002 | 1240 |

关键发现：
- 去掉 c_n 后 tau 从 0.794 升到 0.824 — contamination gating 在 500 items 上确实损害排名
- Tighter prior 无改善
- 排除 gpt-4-turbo 后 tau 升到 0.817

**Part 2: exp-020 v3 (I=317 filtered items)**

| | v2 (I=500) | v3 (I=317) | Delta |
|--|-----------|-----------|-------|
| G-MFRM tau | 0.794 | 0.809 | **+0.015** |
| G-MFRM rho | 0.926 | 0.929 | +0.002 |
| raw_avg tau | 0.838 | 0.824 | -0.015 |

- 收敛良好：R-hat=1.0086, ESS=1677, divergences=0
- 过滤到 317 items 后 G-MFRM tau 改善了 +0.015
- G-MFRM vs raw 的 gap 从 -0.044 缩小到 -0.015
- c_n 值整体变大（exposure 信号更集中），尤其 gpt-4-0613 (3.775→4.263) 和 gpt-4-turbo (3.756→4.015)

---
