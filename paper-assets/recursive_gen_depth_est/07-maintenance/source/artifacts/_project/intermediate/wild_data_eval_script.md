Remote: gpu-6000pro-2:/root/autodl-tmp/recursive_gen_depth_est/scripts/wild_data_eval.py

Usage:
  /root/miniconda3/bin/python3.12 scripts/wild_data_eval.py \
    --input results/wild_features/c4_10k_features.csv,results/wild_features/fineweb_10k_features.csv

Options:
  --train_features: default data/features_all.jsonl
  --output_dir: default results/wild_eval/
  --n_estimators: default 200
  --seed: default 42