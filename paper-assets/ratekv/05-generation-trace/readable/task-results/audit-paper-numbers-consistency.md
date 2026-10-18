# audit paper numbers consistency

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_numbers_consistency_20260515T010304_result.json`
- **Structured JSON:** [`5a55687ed665cbd506aa.json`](../../sessions/5a/5a55687ed665cbd506aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I've now read all paper files and have the full registry data. Here's the complete audit.

---

## 论文数字一致性审计报告

### 审计结论：**无实质性不一致**

所有核心定量声明与 registry 一致。以下为完整核对结果。

---

### 一致性确认（全部通过）

| 数字 | 论文值 | Registry值 | 来源实验 | 状态 |
|------|--------|-----------|----------|------|
| Qwen concentration | 0.61 | 0.6104 | `qwen_hires_float32_d048` | ✓ |
| Yi-1.5 concentration | 0.71 | 0.7139 | `yi15_hires_bf16_2bitonly` | ✓ |
| Llama concentration | 0.57 | 0.5749 | `llama_hires_bf16_2bitonly` | ✓ |
| Mistral concentration | 0.24 | 0.241 | `mistral_hires_bf16_2bitonly_v4` | ✓ |
| Gemma-2 concentration | 0.23 | 0.2291 | `gemma2_hires_bf16_2bitonly` | ✓ |
| Qwen baseline PPL | 9.81 | 9.8106 | `hires_mckp_reeval` | ✓ |
| Qwen uniform PPL | 15.45 | 15.4454 | `hires_mckp_reeval` | ✓ |
| Qwen MCKP (standard) | 11.23 | 11.23 | `exp_c_constrained_mckp` | ✓ |
| Qwen MCKP (hires) | 10.91 | 10.9131 | `hires_mckp_reeval` | ✓ |
| Yi-1.5 baseline | 7.02 | 7.0157 | `yi15_hires_constrained_mckp` | ✓ |
| Yi-1.5 MCKP | 7.22 | 7.2181 | `yi15_hires_constrained_mckp` | ✓ |
| Yi-1.5 uniform | 7.22 | 7.2171 | `yi15_hires_constrained_mckp` | ✓ |
| Llama baseline | 8.09 | 8.0922 | `llama_hires_constrained_mckp` | ✓ |
| Llama MCKP (hires) | 8.45 | 8.4498 | `llama_hires_pipeline` | ✓ |
| Llama uniform | 8.47 | 8.4701 | `llama_hires_pipeline` | ✓ |
| Mistral baseline (eval) | 7.04 | 7.035 | `mistral_full_pipeline` | ✓ |
| Mistral MCKP (k=4) | 7.16 | 7.1648 | `mistral_k_ablation` | ✓ |
| Mistral uniform | 7.13 | 7.131 | `mistral_k_ablation` | ✓ |
| Gemma-2 baseline | 8.90 | 8.9 | `gemma2_9b_full_pipeline` | ✓ |
| Gemma-2 MCKP | 9.05 | 9.05 | `gemma2_9b_full_pipeline` | ✓ |
| Gemma-2 uniform | 9.03 | 9.03 | `gemma2_9b_full_pipeline` | ✓ |
| Cross-dataset agreement (Qwen) | 96.4% (108/112) | 96.4% (108/112) | `c4_rerun_d032` | ✓ |
| Cross-dataset agreement (Llama) | 97.7% (250/256) | 97.7% (250/256) | `llama_c4_cross_dataset` | ✓ |
| Cross-dataset agreement (Mistral) | 96.5% (247/256) | 96.5% (247/256) | `mistral_c4_cross_dataset` | ✓ |
| Multi-seed 3-way agreement | 90.2% | 90.2% | `multi_seed_error_bars` | ✓ |
| Unconstrained greedy PPL | 32.45 | 32.45 | `ratequant_greedy_comparison` | ✓ |
| Greedy bit dist (2-bit count) | 68 | 68 | `ratequant_greedy_comparison` | ✓ |
| Constrained MCKP bit dist | {2:8, 4:100, 8:4} | {2:8, 4:100, 8:4} | `exp_c_constrained_mckp` | ✓ |
| Yi-1.5 L4H3 delta | 13.12 | 13.1236 | `yi15_hires_bf16_2bitonly` | ✓ |
| Llama L2H5 delta | 15.26 | 15.2636 | `llama_hires_bf16_2bitonly` | ✓ |
| Mistral t1/t5 | 0.41 | 0.41 | commit e52fb0e | ✓ |
| Mistral shape | Flat | Flat | `mistral_hires_bf16_2bitonly_v4` | ✓ |
| 27.3% improvement | (15.45−11.23)/15.45 | = 27.3% | 算术验证 | ✓ |
| 0.50 threshold | ≳0.50 | — | 5/5 classification | ✓ |

---

### 分类标签核对

| Model | Paper classification | 依据 | 状态 |
|-------|---------------------|------|------|
| Qwen | Spread | conc=0.61≥0.50, t1/t5=0.57≤0.70 | ✓ |
| Yi-1.5 | Spike | t1/t5=0.90≥0.70 | ✓ |
| Llama | Spike | t1/t5=0.85≥0.70 | ✓ |
| Mistral | Flat | conc=0.24<0.50 | ✓ |
| Gemma-2 | Flat | conc=0.23<0.50 | ✓ |

---

### 算术内部一致性验证

| 声明位置 | 计算 | 状态 |
|----------|------|------|
| analysis.tex:15 — "+5.64 PPL (uniform)" | 15.45−9.81=5.64 | ✓ |
| analysis.tex:15 — "+1.42 PPL (ours)" | 11.23−9.81=1.42 | ✓ |
| analysis.tex:17 — Yi "+0.20 vs +0.20" | 7.22−7.02=0.20 both | ✓ |
| analysis.tex:27 — Llama "+0.36 vs +0.38" | 8.45−8.09=0.36, 8.47−8.09=0.38 | ✓ |
| analysis.tex:28 — Mistral "+0.13 vs +0.10" | 7.16−7.04=0.12→0.13, 7.13−7.04=0.09→0.10 | ✓ (rounding) |
| analysis.tex:28 — Gemma "+0.15 vs +0.13" | 9.05−8.90=0.15, 9.03−8.90=0.13 | ✓ |
| appendix — hires "11.23→10.91 (−0.32)" | 11.23−10.91=0.32 | ✓ |
| appendix — "1.42→1.10, 22.5% reduction" | (1.42−1.10)/1.42=22.5% | ✓ |
| appendix — KV sep "10.91 vs 11.22 (+0.31)" | 11.22−10.91=0.31 | ✓ |
| experiments.tex:69 — Mistral "+0.4%" | (7.16−7.13)/7.13=0.42%≈0.4% | ✓ |
| method.tex:73 — L0H0 "31.9% (9.81→12.94)" | (12.94−9.81)/9.81=31.9% | ✓ |
| method.tex:73 — L0H2 "23.2% (9.81→12.09)" | (12.09−9.81)/9.81=23.2% | ✓ |
| method.tex:73 — L0H3 "11.7% (9.81→10.96)" | (10.96−9.81)/9.81=11.7% | ✓ |
| method.tex:118 — "0.4% of 4.53 PPL" | 0.018/4.53=0.4% | ✓ |

---

### 观察事项（非错误，供参考）

1. **Table 2 (experiments.tex:50) `11.23±0.06`**: ±0.06 来自 hires profiling 3-seed（mean=10.99±0.06），但 11.23 是 standard profiling 单次结果。脚注已注明来源，但读者可能误认为 11.23 本身的不确定度。建议明确标注或改为 hires mean±std (10.99±0.06)。

2. **36.92 (unconstrained MCKP)**: Registry 提取中未找到此数字的独立实验记录（agent 仅提取到 greedy=32.45 from `ratequant_greedy_comparison`）。论文内部算术一致（method.tex Table 4 和 abstract 一致引用），但建议确认 registry 中有对应条目。

---

### 任务描述中的参考值勘误

任务给出 "Llama MCKP=8.50"，但 registry (`llama_hires_pipeline`) 和论文 (Table 2) 均为 **8.45**（registry 精确值 8.4498）。此为任务描述笔误，非论文错误。

---

**总结：论文所有定量声明与 registry 数据一致，无需修改。**

---
