# DocRED Constrained Eval Readiness Report

**Date**: 2026-05-15
**Status**: ✅ ALL CHECKS PASSED — Ready for immediate submission

## 1. Model Verification

| Model | Path | Status |
|-------|------|--------|
| Qwen3-8B LoRA DocRED merged | `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/` | ✅ Complete (config.json, 4× safetensors, tokenizer) |
| Llama-3.1-8B LoRA DocRED merged | `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` | ✅ Complete (config.json, 4× safetensors, tokenizer) |

## 2. Data Verification

| File | Path | Status |
|------|------|--------|
| DocRED dev set | `data/docred/dev.json` (4.3MB) | ✅ Exists |
| DocRED ontology constraints | `data/docred/ontology_constraints_docred.json` (64KB) | ✅ Exists |

## 3. Script Verification

- Entry point: `run_constrained_extraction.py`
- Key args: `--mode full_s1 --dataset docred --model_path <path> --data_path <path> --constraints_path <path> --output_path <path> --device <gpu> --batch_size 1 --max_new_tokens 4096`
- `--max_samples 0` = run all (998 samples)

## 4. Dry-Run Results (2-sample each)

| Model | Samples | JSON Parse | Entities | Relations | Status |
|-------|---------|------------|----------|-----------|--------|
| Qwen | 2/2 | ✅ | ✅ Valid types | ✅ Valid DocRED relations | **PASS** |
| Llama | 2/2 | ✅ | ✅ Valid types | ✅ Valid DocRED relations | **PASS** |

## 5. Ready-to-Submit Commands

### Qwen constrained eval (cuda:1)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_docred_lora_constrained_eval.jsonl --device cuda:1 --batch_size 1 --max_new_tokens 4096"
```

### Llama constrained eval (cuda:0)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096"
```

## 6. GPU Allocation Note

Currently running unconstrained evals:
- cuda:0: Llama unconstrained (PID 303525)
- cuda:1: Qwen unconstrained (PID 304006)

Each GPU has ~80GB free (17/98GB used), so constrained eval can coexist on the same GPU if needed, or wait for unconstrained to finish and reuse the same GPU.

## 7. Issues Found

**None.** All prerequisites verified. Commands can be submitted immediately when GPUs are available.
