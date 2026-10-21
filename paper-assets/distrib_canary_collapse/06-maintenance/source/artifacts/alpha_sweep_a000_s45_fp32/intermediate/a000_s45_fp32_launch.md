Experiment: alpha_sweep_a000_s45_fp32
Server: westd-17855, cuda:2
PID: 448944
Started: 2026-05-21 14:04 CST

Parameters:
- model: EleutherAI/pythia-410m
- seed: 45
- synthetic_ratio: 0.0 (null, no contamination)
- bf16: false (fp32)
- num_generations: 10
- steps_per_gen: 5000
- data: wikitext103_5k

Notes:
- Required HF_HUB_OFFLINE=1 to bypass HF Hub network timeout on AutoDL
- 4th null seed for FPR confidence interval narrowing
- Log: /root/autodl-tmp/distrib_canary_collapse/logs/a000_s45_fp32.log