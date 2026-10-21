# exp step2 cron resolve

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_step2-cron-resolve_20260522T010447_result.json`
- **Structured JSON:** [`03ff905fca6e761db3a1.json`](../../sessions/03/03ff905fca6e761db3a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Step 2 v2 最终状态：成功完成

进程已结束，日志有 `Step 2 complete` 标记，结果文件已生成（20K）。

### 结果汇总

| Dataset | High K_eff ASR | Low K_eff ASR | Mann-Whitney p | hypothesis_holds |
|---------|---------------|---------------|----------------|-----------------|
| **mmlu** | 0.2457 | 0.1438 | 1.0000 | — |
| **arc_challenge** | 0.1228 | 0.0780 | 1.0000 | false |

**结论：实验成功运行完成，但假设未得到统计支持。**

两个数据集的趋势方向一致——high K_eff panel 的 ASR 都高于 low K_eff panel（mmlu: 0.246 vs 0.144, arc: 0.123 vs 0.078），说明更独立的 panel 确实更容易被攻击成功。但 Mann-Whitney p=1.0 表明在仅 3 vs 3 panel 的样本量下，差异完全不显著。`hypothesis_holds=false`。

结果文件：`/root/cert_manip_resist_eval/artifacts/results/results_step2_keff_contrast_20260522_010347.json`

---
