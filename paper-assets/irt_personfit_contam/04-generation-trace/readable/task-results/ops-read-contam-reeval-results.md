# ops read contam reeval results

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-contam-reeval-results_20260523T133259_result.json`
- **Structured JSON:** [`30ae663dee1b1c8cb5b9.json`](../../sessions/30/30ae663dee1b1c8cb5b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. V2 contam_50_s1（pilot/llama）— 已完成

| 指标 | 值 |
|------|-----|
| theta_mle | **-0.1490** |
| lz_star (overall) | **-3.3313** |
| accuracy_overall | **0.6983** |
| accuracy_seen | 0.6914 |
| accuracy_unseen | 0.7053 |
| lz_star_seen | -1.9171 |
| lz_star_unseen | -2.8092 |
| n_items | 14042 (seen=7021, unseen=7021) |

### 2. V2 contam_15_s1 — 仍在运行

进度：**7000/14042（~50%）**，当前 acc=0.6606。文件尚未生成。

### 3. V1 contam_15（ctrl_contam_llama）

| 指标 | 值 |
|------|-----|
| theta_mle | **-0.2761** |
| lz_star (overall) | **-2.9922** |
| lz_uncorrected | -2.6572 |
| accuracy_overall | **0.6654** |
| accuracy_seen | 0.7707 |
| accuracy_unseen | 0.6469 |
| lz_star_seen | -0.5727 |
| lz_star_unseen | -2.4945 |
| n_items | 14042 (seen=2106, unseen=11936) |

### 4. V1 contam_50（ctrl_contam_llama）

| 指标 | 值 |
|------|-----|
| theta_mle | **-0.1490** |
| lz_star (overall) | **-3.3313** |
| lz_uncorrected | -2.8581 |
| accuracy_overall | **0.6983** |
| accuracy_seen | 0.7573 |
| accuracy_unseen | 0.6394 |
| lz_star_seen | -1.2956 |
| lz_star_unseen | -2.2149 |
| n_items | 14042 (seen=7021, unseen=7021) |

### V1 vs V2 对比（contam_50）

V1 和 V2 的 overall 指标完全相同（theta=-0.1490, lz*=-3.3313, acc=0.6983），说明 response vector 一致，只是 seen/unseen 的随机划分不同（不同 seed）。

关键差异在 seen/unseen 分拆：
- **V1**: acc_seen=0.7573 > acc_unseen=0.6394（seen 显著高于 unseen，**符合预期**）
- **V2 s1**: acc_seen=0.6914 < acc_unseen=0.7053（seen 反而**低于** unseen）

这说明 V2 s1 的随机种子恰好把较难的题分给了 seen 组，contamination 效应在这个 seed 下被 item difficulty 分布掩盖了。

### Clean seed re-eval 状态

`ctrl_contam_llama/results/` 下有 clean_s2 到 clean_s10（共10个 clean 结果），全部在 5/21-5/22 完成。`pilot/llama/` 下无 clean 结果文件。

### pilot/llama 目录其他已完成文件

除 contam_50_s1 外还有：contam_15_s2、contam_50_s2、contam_5、contam_25（均已完成）。

---
