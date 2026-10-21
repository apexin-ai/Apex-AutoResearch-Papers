TSR COLLAPSE MECHANISM ANALYSIS REPORT
=======================================
Date: 2026-05-26
Data: 16 eval conditions, 3200 episodes total

1. TSR DROP PATTERN: MONOTONIC DECREASE
- Pi0.5 Base: 75.5%
- SDF λ=0.005 best checkpoint (10-16K): 7.8%
- SDF λ=0.005 @ 30K: 6.8% ± 2.1%
- SDF λ=0.01 @ 30K: 6.5% ± 1.0%
- LoRA Baseline @ 30K: 7.1% ± 1.0%
- Drop: ~68% for ALL conditions (SDF and LoRA identical)

Per-task at best checkpoint:
- Choco Pudding: 22-36% (most resilient)
- Orange Juice: 0-4%
- Milk: 0%
- BBQ Sauce: 0%

2. FAILURE MODE BREAKDOWN
                    Success  UnsafeSucc  SafeFail  CollFail
Pi0.5 Base          25.8%    49.8%       0.5%      24.0%
SDF λ=0.005         2.2%     5.0%        49.8%     43.0%
SDF λ=0.01          1.8%     4.8%        51.2%     42.2%
LoRA Baseline       1.9%     5.2%        47.5%     45.4%

CRITICAL: Safe failure rate 0.5% → ~50% (100x increase)
Both SDF and LoRA show identical pattern → NOT SDF-specific

3. DISPLACEMENT ANALYSIS
Obstacle displacement: Base 0.143m → SDF 0.059m → LoRA 0.060m
EE displacement (SDF only): mean 0.5m, 0% frozen episodes
Robot moves substantially but undirectedly

4. MECHANISM: COMPOSITE
Component 1: Catastrophic forgetting of task semantics
- TSR drops immediately, monotonically
- LoRA baseline confirms SDF loss not the cause
- 3/4 tasks collapse to ~0% even at early checkpoints

Component 2: Learned collision avoidance (retained)
- Safe failure rate jumps 100x
- Robot not frozen (EE disp ~0.5m)
- Obstacle displacement halved

CONCLUSION: Catastrophic forgetting of task-specific grasping/placing
semantics, NOT conservative avoidance. LoRA fine-tuning on safety data
disrupts pre-trained task policy regardless of SDF loss presence.

Figures: /root/colliforce-vla/figures/
Script: /root/colliforce-vla/scripts/analysis_tsr_collapse.py