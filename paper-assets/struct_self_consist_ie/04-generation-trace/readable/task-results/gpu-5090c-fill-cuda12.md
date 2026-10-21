# gpu 5090c fill cuda12

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090c_fill_cuda12_20260521T130200_result.json`
- **Structured JSON:** [`97f8b3c547e0dd556784.json`](../../sessions/97/97f8b3c547e0dd556784.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动，vLLM 正在加载模型。

---

**已完成实验指标汇总：**

| 指标 | SciERC N=16 s42 | CoNLL N=16 s123 |
|------|-----------------|-----------------|
| greedy_f1 | 0.663 | 0.908 |
| oracle_f1 | 0.809 | 0.963 |
| oracle_headroom | 0.146 | 0.055 |
| ρ(FK→F1) cond | 0.128 | 0.391 |
| ρ(SJ→F1) cond | 0.326 | 0.417 |
| logprob ρ cond | 0.160 | 0.373 |
| structural > surface | ✓ (+0.128) | ✓ (+0.010) |
| verdict | **MARGINAL** | **PASS** |

**新启动实验：**

| GPU | exp_id | PID | 内容 |
|-----|--------|-----|------|
| cuda:1 | exp_e2_pretrained_conll_s123 | 321281 | Qwen2.5-7B-Instruct (未微调) CoNLL, seed=123 |
| cuda:2 | exp_e2_pretrained_conll_s456 | 321549 | Qwen2.5-7B-Instruct (未微调) CoNLL, seed=456 |

**当前 5090-c 全部 4 GPU 满载：**
- cuda:0: exp_fewnerd_n16_s123 (RUNNING)
- cuda:1: exp_e2_pretrained_conll_s123 (刚启动)
- cuda:2: exp_e2_pretrained_conll_s456 (刚启动)
- cuda:3: exp_e2_pretrained_fewnerd_s123 (RUNNING)

---
