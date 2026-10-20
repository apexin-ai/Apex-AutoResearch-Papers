# FewRel Formal Study Launch Commands

Server: cqa1-38874 | Project: /root/schema-dag-extraction

## Step 0: Qwen3 Embedding Computation (prerequisite, ~2 min GPU)

```bash
cd /root/schema-dag-extraction
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python3 src/compute_type_embeddings.py \
    --types configs/fewrel_relation_types.json \
    --model /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ \
    --output artifacts/fewrel_qwen3_embeddings.pt \
    --batch-size 8 \
    --dtype bfloat16
```

Notes:
- Output: `{PID: tensor}` dict (e.g. `{"P931": tensor, ...}`)
- `run_fewrel_formal.py` auto-remaps PID keys to relation names via `pid2name`
- Text template: `"{PID}: {relation_name}"` (e.g. `"P931: place served by transport hub"`)
- 80 relation types, dim depends on Qwen3 hidden size

## Step 1: Exp1 - Count Curve (count={1,4,8,16,32,64,80})

### Dry run (verify batch config, no GPU)
```bash
python3 src/run_fewrel_formal.py \
    --mode exp1 --use_all --dry_run
```

### Full run
```bash
nohup python3 src/run_fewrel_formal.py \
    --mode exp1 --use_all \
    --embeddings_path artifacts/fewrel_qwen3_embeddings.pt \
    --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ \
    > artifacts/fewrel_formal/exp1_run.log 2>&1 &
echo $!
```

- 110 batches (80 solo + 5x6 random), ~13200 inferences
- Est. GPU time: ~330 min @ 1.5s/sample

## Step 2: Exp2 - BCS Controlled (count={8,16})

### Dry run
```bash
python3 src/run_fewrel_formal.py \
    --mode exp2 --use_all --dry_run \
    --embeddings_path artifacts/fewrel_qwen3_embeddings.pt
```

### Full run
```bash
nohup python3 src/run_fewrel_formal.py \
    --mode exp2 --use_all \
    --embeddings_path artifacts/fewrel_qwen3_embeddings.pt \
    --model_path /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/ \
    > artifacts/fewrel_formal/exp2_run.log 2>&1 &
echo $!
```

- 54 batches (2 count levels x (1 low + 1 high + 25 random))
- Est. GPU time: ~TBD (depends on samples per batch)

## Step 3: Analysis

```bash
python3 src/analyze_fewrel_results.py \
    --predictions_path artifacts/fewrel_formal/predictions_exp1.json \
    --sim_matrix_path artifacts/fewrel_formal/relation_sim_matrix.pt \
    --output_dir artifacts/fewrel_formal/analysis_exp1

python3 src/analyze_fewrel_results.py \
    --predictions_path artifacts/fewrel_formal/predictions_exp2.json \
    --sim_matrix_path artifacts/fewrel_formal/relation_sim_matrix.pt \
    --output_dir artifacts/fewrel_formal/analysis_exp2
```

## Monitoring

```bash
# Check if running
ps aux | grep run_fewrel_formal

# Tail log
tail -f artifacts/fewrel_formal/exp1_run.log

# Check output files
ls -la artifacts/fewrel_formal/
```

## Execution Order

1. Compute Qwen3 embeddings (Step 0) -- GPU needed, ~2 min
2. Dry-run exp1 + exp2 to verify batch configs
3. Run exp1 (Step 1) -- ~5.5 hours GPU
4. Run exp2 (Step 2) -- after exp1 completes (same GPU)
5. Analyze results (Step 3)
