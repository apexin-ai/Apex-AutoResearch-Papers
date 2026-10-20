# ssh conll freeform prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_conll_freeform_prep_20260522T090955_result.json`
- **Structured JSON:** [`9bf3a29d588fbc3c30d6.json`](../../sessions/9b/9bf3a29d588fbc3c30d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: GPU 状态

**autodl-5090**

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 0% | 2/32G | **空闲** |
| 1 | 0% | 2/32G | **空闲** |
| 2 | 72% | 29.7/32G | conll_pretrained_n64_s42 — 75% (165k/221k), **ETA ~20min** |
| 3 | 0% | 2/32G | **空闲** |

**autodl-5090-c**

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 87% | 30.1/32G | fewnerd_n32_s42 (fine-tuned, N=32) |
| 1 | 78% | 30.1/32G | fewnerd_pretrained_n16_s42 |
| 2 | 0% | 0/32G | **空闲** |
| 3 | 81% | 29.8/32G | fewnerd_pretrained_n32_s42 |

### 已完成实验 — MV 指标

**conll_pretrained_n16_seed42** (Qwen2.5-7B-Instruct):
- greedy=0.5986, MV_strict=0.6320, **Δ_SC=+3.34pp**, oracle=0.7282
- δ_degen=25.5%, α_crit=0.299, α_crit_eff=0.402

**scierc_pretrained_n64_seed42** (Qwen2.5-7B-Instruct):
- greedy=0.2432, MV_strict=0.2717, **Δ_SC=+2.85pp**, oracle=0.5017
- δ_degen=0.0%, α_crit=0.122, α_crit_eff=0.122

### 仍在运行（无 samples.jsonl）
- conll_pretrained_n64_seed42 — ~20min
- fewnerd_n32_seed42, fewnerd_pretrained_n16_seed42, fewnerd_pretrained_n32_seed42 — 全在 5090-c

---

### Part 2: CoNLL Free-Form Ablation

**已经完成，无需重跑。** 数据在 `output/review_round9_experiments/freeform_conll/`：

- 4 seeds (42/123/456/789), N=8, T=1.0, model=qwen3-8b-conll2003-merged, `use_grammar=False`
- 3453 instances/seed, parse rate ~79-81%
- 论文 appendix 已引用这些结果（§CoNLL NER free-form results）

关键数字（与论文一致）：
- LP range median: 0.058±0.007
- LP-selected F1: 0.896 vs greedy 0.904 (Δ=-0.77pp)
- QE: SJ ρ=0.461, EM ρ=0.471, LP ρ=0.326

**实现机制**：`sampling.py` 的 `run_sampling_pipeline` 已有 `use_grammar` 参数（默认 True），设 False 即为 free-form。`run_mvp_pilot.py` 未暴露此 flag，但已有单独脚本生成了数据。

**可用 GPU**：autodl-5090 cuda:0/1/3 均空闲，5090-c cuda:2 空闲。如果需要额外实验（如 pretrained model free-form 或不同 N），随时可以启动。

---
