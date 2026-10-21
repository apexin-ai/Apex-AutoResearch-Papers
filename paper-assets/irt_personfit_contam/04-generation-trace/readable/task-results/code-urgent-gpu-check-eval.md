# code urgent gpu check eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent-gpu-check-eval_20260521T062322_result.json`
- **Structured JSON:** [`3230658f61c21c23b509.json`](../../sessions/32/3230658f61c21c23b509.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个子实验 DONE，父实验 metrics 已更新。最终汇总：

---

## Mistral Controlled Contamination — 完整结果

| | **clean** | **contam_15** | **contam_50** |
|---|---|---|---|
| **lz\*** | **+5.42** | **-1.38** | **-3.15** |
| **Δlz\*** (vs clean) | — | **-6.80** | **-8.57** |
| acc_overall | 0.514 | 0.595 | 0.673 |
| acc_seen | N/A | 0.744 | 0.752 |
| acc_unseen | 0.514 | 0.569 | 0.594 |
| theta_mle | -1.157 | -0.713 | -0.303 |
| lz\*_seen | N/A | -1.084 | -1.370 |
| lz\*_unseen | +5.42 | -0.096 | -0.997 |

**关键发现**：contamination 导致 lz\* 从 +5.42 大幅下降至 -1.38/-3.15，Δlz\* 达 -6.80/-8.57，信号极强。seen items 上 acc 显著高于 unseen (74-75% vs 57-59%)，且 lz\*_seen 一致为负值（aberrant pattern）。

**GPU 现状**：
- GPU 0: GRPO 相关进程
- GPU 1, 3: eval 完成后可释放（进程可能仍驻留）
- GPU 2: GRPO 主进程 (PID 73689)
- **GRPO**: 3293/7021 (47%), ~2.07s/step, ETA ~2h10m

---
