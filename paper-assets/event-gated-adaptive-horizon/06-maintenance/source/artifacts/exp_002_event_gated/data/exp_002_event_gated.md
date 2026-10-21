Experiment: Event-Gated Adaptive Horizon on DMC Walker Walk
Server: autodl-rtx6000 (RTX PRO 6000 x2)
GPU: cuda:1
PID: 9764 (main), 9769 (python)
Logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1
Log file: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1.log
Steps: 500000
Seed: 1
Config: defaults + dmc_proprio
gate_enabled: True
gate_max_dt: 8, tau annealing 5.0->0.5 over 200K steps
curriculum: phase1=50K (gate off), phase2=150K (ramp up)
Started: 2026-05-13 10:04 UTC