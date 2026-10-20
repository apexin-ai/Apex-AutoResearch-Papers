Experiment: π0.5 Attn k=0.75 Long strict
Server: westd-41074, GPU0
tmux session: pi05_attn_k075
Log: /root/autodl-tmp/importance_margin_vla_compress/eval_pi05_attn_k075_long_seed42_strict_w41.log
Command: CUDA_VISIBLE_DEVICES=0 python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0
Hypothesis: lenient=51.8%, 补全 Attn strict cliff curve 中间段
Started: 2026-05-27 20:24 UTC