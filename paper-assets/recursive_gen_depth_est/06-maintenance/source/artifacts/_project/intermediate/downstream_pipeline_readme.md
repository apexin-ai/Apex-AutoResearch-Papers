## Downstream Benchmark Pipeline (Plan_024)

### Scripts (all at /root/autodl-tmp/recursive_gen_depth_est/scripts/)

1. **downstream_score_data.py** — Train RF on labeled features (20K samples, 4 depths) → predict depth on C4 10K wild features → output scored JSONL
   - RF val accuracy: 77.4%
   - Input: data/features_all.jsonl + results/wild_features/c4_10k_features.csv + data/wild/c4_10k.jsonl
   - Output: data/downstream/c4_scored.jsonl

2. **downstream_filter.py** — Filter by predicted depth
   - strict: d0-d1 only
   - moderate: d0-d2
   - unfiltered: all (baseline)
   - random: same size as strict, random sample (control)

3. **downstream_finetune.py** — LoRA fine-tune Pythia-410M (EleutherAI/pythia-410m)
   - LoRA r=8, alpha=16, dropout=0.05, target=query_key_value
   - lr=5e-5, 3 epochs, bs=4×4 grad_accum, max_len=512
   - Output: checkpoints/downstream/{condition}/

4. **downstream_eval.sh** — lm-eval-harness (v0.4.11) evaluation
   - Tasks: hellaswag, arc_easy, piqa
   - Evaluates base + 4 fine-tuned conditions
   - Output: results/downstream_eval/

5. **run_downstream_full.sh** — End-to-end orchestration

### Verification
- All --help pass ✓
- Dry-run scoring (10 samples) pass ✓  
- Dry-run filtering pass ✓
- lm-eval 0.4.11 installed ✓
- peft 0.7.1 installed ✓

### To Run
```bash
# Full pipeline
bash scripts/run_downstream_full.sh

# Or step-by-step
python scripts/downstream_score_data.py          # CPU, ~5s
python scripts/downstream_filter.py              # CPU, ~1s
python scripts/downstream_finetune.py --data_path data/downstream/c4_strict.jsonl  # GPU
bash scripts/downstream_eval.sh                  # GPU
```