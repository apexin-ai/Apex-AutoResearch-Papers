# analysis 15B para aligned batch and simsweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_15B_para_aligned_batch_and_simsweep_20260515T230421_result.json`
- **Structured JSON:** [`fcd9685f1e592ab2f776.json`](../../sessions/fc/fcd9685f1e592ab2f776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部更新为 DONE+success。汇总：

---

## 任务 1: exp_001_eval_15B_s123_para_aligned_batch → DONE

**1.5B s123 para_aligned eval 结果：**

| Dosage | MMLU | GSM8K | ARC | HumanEval |
|--------|------|-------|-----|-----------|
| d000 | 0.6111 | 0.5921 | 0.7547 | 0.1538 |
| d005 | 0.6140 | 0.5439 | 0.7475 | 0.0769 |
| d025 | 0.6145 | 0.5482 | 0.7504 | 0.1923 |
| d100 | 0.6290 | 0.5307 | 0.7834 | 0.2308 |

注：para_aligned 版本 GSM8K 仅 228 items，HumanEval 仅 26 items（释义子集）。MMLU 6596 items。d100 在 MMLU 和 ARC 上有明显提升（contamination effect），GSM8K 反而下降。

## 任务 2: exp_004_sim_sweep_v7 → DONE

Registry 原本没有 `exp_004_sim_sweep_v7`（只有 `exp_004_sim_sweep_extreme_gamma`），两个都已完成：

- **主 sweep (v7)**: 16 conditions (AUC={0.55,0.65,0.8,0.9} × N={8,20,50,100}), gamma_true=0.5, 160 runs。CI95 coverage 80-100%（均值 94%），gamma bias 极小（<0.025）。
- **Extreme gamma sweep**: 8 conditions (gamma={2.0,4.0} × AUC={0.7,0.9} × N={20,50}), 80 runs, 11.1h。gamma=2.0 完美恢复（CI95=100%），gamma=4.0 轻微负偏（-0.10 to -0.23），CI95=90-100%。结论：经验数据中的 coverage collapse 是 model misspecification，不是极端参数值导致。

---
