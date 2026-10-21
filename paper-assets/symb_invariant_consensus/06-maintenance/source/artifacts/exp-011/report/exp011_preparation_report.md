# exp-011 Preparation Report

## Status: READY TO LAUNCH

## Model
- **Path**: `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- **Size**: 14GB (4 safetensors shards)
- **Files**: config.json, tokenizer.json, generation_config.json, 4x model shards — complete

## Dataset (D012)
- ProofWriter D5: 30 problems (`data/proofwriter_30.json`)
- FOLIO: 30 problems (`data/folio_30.json`)
- Total: 60 problems ✓

## Launch Command
```bash
# One-liner (background with log):
nohup bash /root/symb_invariant_consensus/scripts/run_exp011_llama8b.sh > /tmp/exp011.log 2>&1 &

# Or foreground:
bash /root/symb_invariant_consensus/scripts/run_exp011_llama8b.sh
```

## Script Parameters
| Parameter | Value |
|-----------|-------|
| Model | LLaMA-3.1-8B-Instruct |
| K | 12 |
| Temperature | 0.7 |
| max_tokens | 8192 |
| max-model-len | 8192 |
| gpu_memory_utilization | 0.90 |
| vLLM port | 8002 |
| Seed | 42 |
| Output | `results/exp011_llama8b/exp011_results.json` |

## GPU
- **Hardware**: NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB VRAM)
- **Current status**: 100% busy (exp-002 K-ablation running, 83.5/98GB used)
- **exp-011 estimate**: LLaMA-8B fp16 ≈ 16GB + KV cache ≈ 25-30GB total (well within 98GB)

## Runtime Estimate
- vLLM startup: ~30-60s
- Pipeline (60 problems × K=12): ~60-90 min
- Total: ~1-1.5 hours

## Prerequisites Before Launch
1. exp-002 must finish (GPU fully released)
2. No other vLLM on port 8002

## Potential Issues
- None identified. All files, paths, and dependencies verified.
