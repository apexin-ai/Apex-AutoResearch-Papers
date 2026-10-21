# ops investigate dead experiments

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-dead-experiments_20260518T185629_result.json`
- **Structured JSON:** [`f260dd8d897e589476b3.json`](../../sessions/f2/f260dd8d897e589476b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 实验 1: c1_ablation_bce_kl_targets_s123_v2 — **COMPLETED**

| Metric | Seed 123 (v2) | Seed 42 (参考) |
|--------|--------------|---------------|
| Final loss | 0.0537 | — |
| **WikiText-2 PPL** | **9.32** | 11.71 |
| Eval sparsity | 0.615 | 0.50 |
| Agreement | 0.979 | 0.834 |

Checkpoint: `predictor_bce_kl_targets.pt` (145M) 已保存。

Seed 123 结果显著优于 seed 42: PPL 低 2.39, agreement 高 14.5pp, 且 sparsity 更高。

---

### 实验 2: kl_sparsity45_s42_eval_teal_uniform — **COMPLETED**

| Task | Metric | Value |
|------|--------|-------|
| wikitext2 | PPL | 10.9488 |
| arc_challenge | acc_norm | 0.3763 |
| winogrande | acc | 0.6361 |
| mmlu | acc | 0.3063 |
| gsm8k | exact_match | 0.0273 |

Results JSON 已保存到 `results/benchmark/kl_sparsity45_s42_eval_teal_uniform/results.json`。

---

### westd-34887 GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 66995 / 97887 MiB | 100% | **kl_sparsity35_s42_eval_teal_uniform 运行中** (pid 47633, ~8min elapsed) |
| cuda:1 | 0 / 97887 MiB | 0% | 空闲 |

`kl_sparsity35_s42_eval_teal_uniform` (pid 47628/47633) 仍在运行，刚启动约8分钟，预计还需 30-40 分钟完成全部 5 个 benchmark。

---
