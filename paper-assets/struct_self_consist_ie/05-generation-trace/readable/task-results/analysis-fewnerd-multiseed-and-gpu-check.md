# analysis fewnerd multiseed and gpu check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd_multiseed_and_gpu_check_20260518T114906_result.json`
- **Structured JSON:** [`8bdf1a5f1c8be0fbb120.json`](../../sessions/8b/8bdf1a5f1c8be0fbb120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是汇总报告。

---

## GPU 状态

| GPU | 状态 | 任务 | 详情 |
|-----|------|------|------|
| cuda:0 | **空闲** | — | 2MiB / 32607MiB |
| cuda:1 | **运行中** | LLaMA Few-NERD LoRA 训练 | 15% (3622/24708), 30878MiB, **预计剩余 ~10h** |
| cuda:2 | **空闲** | — | 2MiB / 32607MiB |
| cuda:3 | **空闲** | — | 2MiB / 32607MiB |

**可用 GPU: cuda:0, cuda:2, cuda:3**（3张空闲）

tmux sessions: `llama_fewnerd`(训练中), `fewnerd_s456`(已完成), `exp_011_ood_conll_to_scierc`, `exp_017_llama_conll_n16_r1024`, `exp_017_llama_conll_n16_s456_r1024`

---

## Qwen Few-NERD 多种子分析结果

两个 seed 的推理和分析**都已完成**（`results.json` 包含完整 5-signal 指标），无需重新运行分析脚本。

### 核心指标对比

| 指标 | seed=123 | seed=456 | 跨seed稳定性 |
|------|----------|----------|-------------|
| **greedy_macro_f1** | 0.7480 | 0.7486 | ±0.0003 |
| **oracle_macro_f1** | 0.8772 | 0.8751 | ±0.0011 |
| **headroom_pp** | 12.92 | 12.65 | ±0.13 |
| **degeneracy_rate%** | 9.37% | 8.24% | ±0.57 |
| **zero_f1_rate%** | 11.88% | 11.82% | ±0.03 |
| **lp_range_median** | 0.0632 | 0.0693 | ±0.003 |

### Selection F1 (LP-based selection)

| 指标 | seed=123 | seed=456 |
|------|----------|----------|
| **lp_sel_f1** | 0.7624 | 0.7623 |
| **lp_delta_pp** | **+1.44** | **+1.37** |
| LP bootstrap p-value | 0.0 (sig) | 0.0 (sig) |
| LP bootstrap 95% CI | [+1.26, +1.61] | [+1.19, +1.55] |

**LP 是唯一在 Few-NERD 上正向的 selection signal**，两个 seed 一致。其他 signal (SJ/FK/EM/VC) 在 seed=123 上负向，seed=456 上也负向。

### QE Spearman (global)

| Signal | seed=123 | seed=456 |
|--------|----------|----------|
| LP | 0.4223 | 0.4206 |
| SJ | 0.3203 | 0.3268 |
| FK | 0.3420 | 0.3361 |
| EM | 0.3230 | 0.3078 |
| VC | 0.3633 | 0.3943 |

---

## CoNLL 多种子状态

- **exp_002_conll_n8_seed123**: 推理+分析完成，`full_signal_analysis.json` 存在
  - greedy_f1=0.9077, oracle_f1=0.9476, headroom=3.99pp, degeneracy=63.0%, LP_delta=-0.77pp
- **exp_002_conll_n8_seed456**: 推理+分析完成，`full_signal_analysis.json` 存在

---

## 关键发现

1. **Few-NERD 跨 seed 高度稳定**：greedy F1 差异仅 0.0006，LP delta 差异仅 0.07pp，bootstrap 均显著
2. **LP selection 在 Few-NERD 上一致正向**（+1.4pp），与 CoNLL（-0.77pp）形成鲜明对比
3. **Few-NERD degeneracy 远低于 CoNLL**（~9% vs ~63%），解释了 LP signal 在 Few-NERD 上更有效
4. **3张 GPU 空闲**（cuda:0/2/3），可立即分配新任务

---
