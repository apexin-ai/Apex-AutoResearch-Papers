# research ft ablation prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ft_ablation_prep_20260516T054250_result.json`
- **Structured JSON:** [`db17dee1aedef921f3d0.json`](../../sessions/db/db17dee1aedef921f3d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。汇总如下：

---

## 确认结果

### 1. LoRA merged 路径（已确认存在）

| Model | Path | Size |
|-------|------|------|
| Qwen3-8B LoRA SciERC | `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged/` | ~15GB, 4 shards |
| Llama-3.1-8B LoRA SciERC | `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/` | ~15GB, 4 shards |

### 2. Mode 支持（已确认）

`run_constrained_extraction.py` line 602-604:
```
--mode choices=["unconstrained", "grammar_only", "semantic_only", "full_s1", "full_s2"]
```
`grammar_only` 和 `semantic_only` 均为有效选项。

### 3. 已有 FT baseline metrics

**Qwen3-8B LoRA SciERC** (w5_lora_scierc_*)

| Metric | unconstrained | full_s1 | delta |
|--------|:---:|:---:|:---:|
| E_F1 | 0.6705 | 0.6705 | 0 |
| R_F1 | 0.4386 | 0.4377 | -0.0009 |
| DR% | 1.95% | 0% | **-1.95pp** |
| RV% | 0% | 0% | 0 |
| ET% | 0% | 0% | 0 |
| CF% | 0% | 1.18% | +1.18pp |

**Llama-3.1-8B LoRA SciERC** (w5_llama_lora_scierc_*)

| Metric | unconstrained | full_s1 | delta |
|--------|:---:|:---:|:---:|
| E_F1 | 0.6776 | 0.6776 | 0 |
| R_F1 | 0.4545 | 0.4547 | +0.0002 |
| DR% | 1.11% | 0.09% | **-1.02pp** |
| RV% | 0% | 0% | 0 |
| ET% | 0% | 0% | 0 |
| CF% | 0% | 0.46% | +0.46pp |

### 4. 四个实验命令

**注意：两个 GPU 当前均被占用**（GPU0: PID 334612 ~15GB, GPU1: PID 321568 ~17GB）。需要等当前任务结束后再提交。

每个实验约 25-45 min，可 2 并行（每 GPU 一个）。

| exp_id | model | mode | gpu |
|--------|-------|------|-----|
| w7_qwen_scierc_ft_grammar_only | Qwen3-8B LoRA | grammar_only | cuda:0 |
| w7_qwen_scierc_ft_semantic_only | Qwen3-8B LoRA | semantic_only | cuda:0 |
| w7_llama_scierc_ft_grammar_only | Llama-3.1-8B LoRA | grammar_only | cuda:1 |
| w7_llama_scierc_ft_semantic_only | Llama-3.1-8B LoRA | semantic_only | cuda:1 |

命令模板（以 w7_qwen_scierc_ft_grammar_only 为例）：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_grammar_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096"
```

**完整 4 条命令：**

**Round 1**（并行，Qwen on GPU0 + Llama on GPU1）：
```bash
# w7_qwen_scierc_ft_grammar_only — cuda:0
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_grammar_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096"

# w7_llama_scierc_ft_grammar_only — cuda:1
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_llama_scierc_ft_grammar_only.jsonl --device cuda:1 --batch_size 1 --max_new_tokens 4096"
```

**Round 2**（Round 1 结束后并行）：
```bash
# w7_qwen_scierc_ft_semantic_only — cuda:0
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_semantic_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096"

# w7_llama_scierc_ft_semantic_only — cuda:1
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_llama_scierc_ft_semantic_only.jsonl --device cuda:1 --batch_size 1 --max_new_tokens 4096"
```

### 5. 预期对比矩阵（完成后）

每个模型将有 4 行：

| mode | DR% | RV% | ET% | E_F1 | R_F1 |
|------|-----|-----|-----|------|------|
| unconstrained | baseline | — | — | — | — |
| grammar_only | **w7 new** | — | — | — | — |
| semantic_only | **w7 new** | — | — | — | — |
| full_s1 | existing | — | — | — | — |

这将揭示 grammar 层和 semantic 层在 FT 模型上各自的单独贡献。

---
