# exp-002: Contamination Detection Signal Pipeline

Computes 4 contamination detection signals for each model-benchmark pair:

- **S1 (Embedding)**: FAISS + sentence-transformers cosine similarity between benchmark items and SFT training data
- **S2 (Min-K%++)**: Token-level membership inference with z-score normalization against a reference model
- **S3 (ConStat)**: Performance gap between original and paraphrased benchmark items
- **S4 (Self-Critique)**: YES/NO entropy collapse on model's self-evaluation of its own answers

## Usage

```bash
# Single signal
python compute_signals.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter \
  --benchmark gsm8k \
  --signal s2 \
  --output-dir /root/autodl-tmp/exp002/outputs/Qwen2.5-0.5B_d005_s42 \
  --batch-size 8

# All signals
python compute_signals.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter \
  --benchmark mmlu \
  --signal all \
  --output-dir /root/autodl-tmp/exp002/outputs/Qwen2.5-0.5B_d005_s42
```

## Output format

Per-signal JSON files: `signal_{name}_{benchmark}.json`

```json
[
  {"item_id": "gsm8k_0001", "signal": "s2_minkpp", "score": 0.847, "metadata": {...}},
  ...
]
```

## Signal-specific arguments

| Signal | Extra args | Notes |
|--------|-----------|-------|
| S1 | `--sft-data-dir` | Auto-infers dosage from adapter path |
| S2 | `--ref-model-path`, `--k-percent` | Auto-infers d000 reference if not set |
| S3 | `--original-eval-paths`, `--paraphrase-eval-paths` | Requires pre-computed eval results |
| S4 | (none) | Uses model to generate answers + self-critique |
