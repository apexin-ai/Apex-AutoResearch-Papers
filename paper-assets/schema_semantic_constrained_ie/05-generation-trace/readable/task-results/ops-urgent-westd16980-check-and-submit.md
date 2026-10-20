# ops urgent westd16980 check and submit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_westd16980_check_and_submit_20260516T060652_result.json`
- **Structured JSON:** [`ce1fa4986af5812ec4b9.json`](../../sessions/ce/ce1fa4986af5812ec4b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 被 w5_qwen_docred_lora_constrained_eval 占用，无法提交 w7_llama_scierc_ft_grammar_only。

---

## 产出汇总

### 1. 实验状态

| 实验 | PID | 状态 | 进度 | GPU |
|------|-----|------|------|-----|
| w6_mistral_scierc_constrained | 334612 (死亡) | **DONE** | 551/551 (100%) | GPU 0 已释放 |
| w5_qwen_docred_lora_constrained_eval | 321568 (存活, 4h12m) | RUNNING | 685/998 (~69%) | GPU 1 (83%, 17GB) |

### 2. w6_mistral_scierc_constrained Metrics + Delta

| 指标 | Unconstrained | Constrained | Delta |
|------|--------------|-------------|-------|
| ET% | 1.50% | **0%** | **-1.50pp** |
| RV% | 0% | 0% | 0 |
| DR% | 56.94% | **13.40%** | **-43.54pp** |
| E_F1 | 0.2728 | 0.2746 | +0.18pp |
| R_F1 | 0.0366 | 0.0367 | +0.01pp |
| Parse fail | 0% | 0% | 0 |

**结论**: OntoCoDec 在 Mistral zero-shot 上消除了 ET，大幅降低 DR (-43.54pp)，F1 不受损。残余 DR 13.4% 远高于 FT 模型 (~1-2%)，符合 zero-shot regime 语义约束不足的预期。

### 3. w5_qwen_docred_lora_constrained_eval

仍在运行，685/998 (~69%)，~14s/sample，ETA ~1.2h。baseline (unconstrained) 已知: E_F1=82.15, R_F1=40.86, DR=0.76%。完成后需再次提取。

### 4. FT Ablation 提交

- **w7_qwen_scierc_ft_grammar_only**: 已提交 GPU 0，tmux session `w7_qwen_ft_grammar`，PID 337069，模型加载中。Registry → RUNNING。
- **w7_llama_scierc_ft_grammar_only**: GPU 1 被占用，**待 w5_qwen_docred 完成后提交**。

---
