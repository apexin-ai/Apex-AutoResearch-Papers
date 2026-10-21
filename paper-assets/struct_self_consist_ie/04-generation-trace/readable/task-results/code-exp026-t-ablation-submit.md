# code exp026 t ablation submit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp026_t_ablation_submit_20260518T152445_result.json`
- **Structured JSON:** [`154a797ee7dc44efb73c.json`](../../sessions/15/154a797ee7dc44efb73c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部完成，registry 已更新为 DONE。

## 结果摘要

推理已有（`output/exp_026_t05/t08/t12/samples.jsonl`，每个 551 instances x N=8 + logprobs，模型 `qwen3-8b-scierc-merged-v2` = ft_002_v2）。5-signal 分析已跑完，输出到各目录的 `all_signals_5signal.json`。

**NER 5-signal（full split, rho）**

| Signal | T=0.5 | T=0.8 | T=1.2 |
|--------|-------|-------|-------|
| SJ | 0.26 | 0.36 | 0.38 |
| FK | 0.23 | 0.25 | 0.34 |
| LP | 0.22 | 0.25 | 0.20 |
| EM | 0.29 | 0.29 | 0.34 |
| VC | 0.38 | 0.38 | 0.40 |

**RE 5-signal（full split, rho）**

| Signal | T=0.5 | T=0.8 | T=1.2 |
|--------|-------|-------|-------|
| SJ | 0.18 | 0.27 | 0.26 |
| FK | 0.13 | 0.20 | 0.35 |
| LP | 0.28 | 0.33 | 0.29 |
| EM | 0.10 | 0.20 | 0.12 |
| VC | 0.28 | 0.40 | 0.40 |

趋势：结构信号（SJ, FK, EM）随温度升高而增强（更多样本多样性 → 更好的信号区分度），LP 信号相对稳定但 conditional 下高温退化。

---
