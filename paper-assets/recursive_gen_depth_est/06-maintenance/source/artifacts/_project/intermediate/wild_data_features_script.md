Remote: gpu-6000pro-2:/root/autodl-tmp/recursive_gen_depth_est/scripts/wild_data_features.py

Usage:
  /root/miniconda3/bin/python3.12 scripts/wild_data_features.py \
    --input data/wild/c4_10k.jsonl,data/wild/fineweb_10k.jsonl \
    --device cuda:0

Options:
  --input: JSONL file(s), comma-separated
  --output_dir: default results/wild_features/
  --model_path: default /root/autodl-tmp/models/pythia-1.4b
  --trunc_len: default 507
  --dry_run: process only 10 samples