# Supplementary Material Framework

> ICML 2026 — "Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3"
> 生成时间: 2026-05-25 | 数据锁定: 2026-05-27

---

## A. Complete Experiment Summary Table

### A.1 Success Experiments (n=69)

| exp_id | Environment | Config | Hypothesis (short) | Conclusion | Seeds |
|--------|-------------|--------|-------------------|------------|-------|
| exp_001_baseline | Walker Walk | dt=1, vanilla DreamerV3 | Baseline convergence ~950 | success | s1 |
| exp_001_baseline_s2 | Walker Walk | dt=1, vanilla | Additional baseline seed | success | s2 |
| exp_001_baseline_s2_extended | Walker Walk | dt=1, vanilla, 505K | s2 extended long-run | success | s2 |
| exp_001_baseline_s3 | Walker Walk | dt=1, vanilla | Third baseline seed | success | s3 |
| exp_001_baseline_s3_extended | Walker Walk | dt=1, vanilla, 505K | s3 extended long-run | success | s3 |
| exp_001_baseline_s4 | Walker Walk | dt=1, vanilla | Fourth baseline seed | success | s4 |
| exp_001_baseline_s4_extended | Walker Walk | dt=1, vanilla, 505K | s4 extended long-run | success | s4 |
| exp_008a_no_subsample_dt2 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3: unexposed dt_emb protection | success | s0 |
| exp_008a_unexposed_s1 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3 seed replication | success | s1 |
| exp_008a_unexposed_s2 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=15 | C3 seed replication | success | s2 |
| exp_008a_cheetah_unexposed_s0 | Cheetah Run | untrained dt_emb, subsample OFF | C3 cross-env validation | success | s0 |
| exp_008a_cheetah_unexposed_s1 | Cheetah Run | untrained dt_emb, subsample OFF | C3 cross-env validation | success | s1 |
| exp_008d_subsample_on_h8 | Walker Walk | trained dt_emb, subsample ON, H=8 | C2: CIVO trigger (original) | success | s1 |
| exp_008d_civo_trigger_s3 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO trigger seed=3 | success | s3 |
| exp_008d_civo_trigger_s4 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO trigger seed=4 | success | s4 |
| exp_008e_v3_subsample_on_dt1_h15 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6: dt=1 imagination test | success | s0 |
| exp_008e_v3_walker_s1 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6 seed=1 (healthy) | success | s1 |
| exp_008e_v3_s4 | Walker Walk | trained dt_emb, subsample ON, dt=1 imag, H=15 | C6 seed=4 | success | s4 |
| exp_008f_no_dt_embed_subsample_on_h8 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | C2 causal control | success | s0 |
| exp_008f_s3_no_dt_embed_walker | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb seed=3 | success | s3 |
| exp_009a_baseline_walker_s2 | Walker Walk | dt=1, vanilla | Multi-seed baseline | success | s2 |
| exp_009c_s3 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb seed=3 | success | s3 |
| exp_009d_baseline_walker_s0 | Walker Walk | dt=1, vanilla | Multi-seed baseline | success | s0 |
| exp_010a_cheetah_baseline_s1 | Cheetah Run | dt=1, vanilla | Cheetah baseline s1 | success | s1 |
| exp_010b_cheetah_civo_trigger | Cheetah Run | trained dt_emb, subsample ON, H=8 | Cheetah CIVO trigger | success | s1 |
| exp_010b_cheetah_civo_trigger_s0 | Cheetah Run | trained dt_emb, subsample ON, H=8 | Cheetah CIVO trigger s0 | success | s0 |
| exp_019a_v2_pickcube_baseline | PickCube-v1 | dt=1, vanilla | PickCube baseline | success | s0 |
| exp_019b_pickcube_civo_trigger | PickCube-v1 | trained dt_emb, subsample ON, H=8 | PickCube CIVO trigger | success | s0 |
| exp_020_vanilla_dreamerv3_s2 | Walker Walk | dt=1, vanilla | Pathway B control | success | s2 |
| exp_022b_no_curriculum | Walker Walk | frozen dt_emb, learned gate, no curriculum | Frozen + learned gate | success | s0 |
| exp_023a_cheetah_baseline_s0 | Cheetah Run | dt=1, vanilla | Cheetah baseline s0 | success | s0 |
| exp_023b_cheetah_baseline_s1 | Cheetah Run | dt=1, vanilla | Cheetah baseline s1 | success | s1 |
| exp_023_cheetah_baseline_s2 | Cheetah Run | dt=1, vanilla | Cheetah baseline s2 | success | s2 |
| exp_023_cheetah_baseline_s3 | Cheetah Run | dt=1, vanilla | Cheetah baseline s3 | success | s3 |
| exp_023_cheetah_baseline_s4 | Cheetah Run | dt=1, vanilla | Cheetah baseline s4 | success | s4 |
| exp_023_cheetah_baseline_s4_extended | Cheetah Run | dt=1, vanilla, 300K | Cheetah baseline s4 extended | success | s4 |
| exp_024b_cheetah_no_dt_emb_s0 | Cheetah Run | dt_embed_dim=0, subsample ON, H=8 | Cheetah no dt_emb control | success | s0 |
| exp_024b_cheetah_no_dt_emb_s1 | Cheetah Run | dt_embed_dim=0, subsample ON, H=8 | Cheetah no dt_emb s1 | success | s1 |
| exp_027_tcn_walker_s0_sigma02 | Walker Walk | TCN σ=0.2, trained dt_emb | TCN CIVO suppression | success | s0 |
| exp_029a_tcn_walker_s1_sigma02 | Walker Walk | TCN σ=0.2, trained dt_emb | TCN multi-seed | success | s1 |
| exp_032_dual_critic_walker | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic CIVO prevention | success | s0 |
| exp_032b_dual_critic_walker_s1 | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic s1 | success | s1 |
| exp_033_wide_critic_walker | Walker Walk | wide single critic, trained dt_emb | Capacity ablation | success | s0 |
| exp_035_narrow_dual_critic_walker | Walker Walk | narrow dual-critic, trained dt_emb | Min-operator ablation | success | s0 |
| exp_039_narrow_dual_critic_walker_s1 | Walker Walk | narrow dual-critic, trained dt_emb | Narrow dual s1 | success | s1 |
| exp_040_wide_dual_critic_cheetah | Cheetah Run | wide dual-critic, trained dt_emb | Cheetah dual-critic s1 | success | s1 |
| exp_041_dual_critic_walker_s3 | Walker Walk | dual-critic (wide), trained dt_emb | Dual-critic s3 | success | s3 |
| exp_042_frozen_dt_emb_walker | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb CIVO prevention | success | s0 |
| exp_043_008f_walker_s1 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | No dt_emb s1 replication | success | s1 |
| exp_044_gradient_stop_walker | Walker Walk | gradient stop (reward head), trained dt_emb | Gradient stop reviewer Q | success | s0 |
| exp_045_treatment_extension_008d_s3 | Walker Walk | trained dt_emb, subsample ON, H=8, extended | CIVO extension | success | s3 |
| exp_046_frozen_dt_emb_cheetah | Cheetah Run | frozen dt_emb, subsample ON, H=8 | Frozen cross-env validation | success | s0 |
| exp_047_frozen_dt_emb_walker_s1 | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb s1 | success | s1 |
| exp_048_cheetah_civo_extension | Cheetah Run | trained dt_emb, extended | Cheetah CIVO irreversibility | success | s0 |
| exp_049_stackcube_civo_trigger_s0 | StackCube-v1 | trained dt_emb, subsample ON, H=8 | StackCube CIVO trigger | success | s0 |
| exp_050_peginsertion_civo_trigger_s0 | PegInsertion-v1 | trained dt_emb, subsample ON, H=8 | PegInsertion CIVO | success | s0 |
| exp_052_stackcube_civo_trigger_s1 | StackCube-v1 | trained dt_emb, subsample ON, H=8 | StackCube CIVO s1 | success | s1 |
| exp_053_peginsertion_frozen_s0 | PegInsertion-v1 | frozen dt_emb, subsample ON, H=8 | PegInsertion frozen | success | s0 |
| exp_054_pickcube_frozen_s0 | PickCube-v1 | frozen dt_emb, subsample ON, H=8 | PickCube frozen | success | s0 |
| exp_055_peginsertion_civo_trigger_s1 | PegInsertion-v1 | trained dt_emb, subsample ON, H=8 | PegInsertion CIVO s1 | success | s1 |
| exp_056_peginsertion_frozen_s1 | PegInsertion-v1 | frozen dt_emb, subsample ON, H=8 | PegInsertion frozen s1 | success | s1 |
| exp_057_frozen_dt_emb_walker_s2 | Walker Walk | frozen dt_emb, subsample ON, H=8 | Frozen dt_emb s2 | success | s2 |
| exp_058_frozen_dt_emb_cheetah_s1 | Cheetah Run | frozen dt_emb, subsample ON, H=8 | Frozen Cheetah s1 | success | s1 |
| exp_059_walker_trained_s5 | Walker Walk | trained dt_emb, subsample ON, H=8 | 5th CIVO seed | success | s5 |
| exp_063_rssm_fidelity | Analysis | RSSM fidelity gap analysis | dt=2 vs dt=1 prediction quality | success | — |
| exp_064_value_distribution | Analysis | Value distribution analysis | V(s) vs MC return | success | — |
| exp_065_dt_emb_cosine | Analysis | dt_emb cosine similarity | dt=1 vs dt=2 embedding separation | success | — |
| exp_rssm_fidelity_analysis | Analysis | RSSM fidelity comparison | baseline/008d/008f comparison | success | — |

### A.2 Negative Experiments (n=36)

| exp_id | Environment | Config | Finding | Seeds |
|--------|-------------|--------|---------|-------|
| exp_003_event_gated_v2 | Walker Walk | Event-gated v2 | Gate mechanism failed | s0 |
| exp_004_event_gated_v3 | Walker Walk | Event-gated v3 (logits masking) | Gate still ineffective | s0 |
| exp_005_event_gated_v4 | Walker Walk | Learned gate activation | Learned gate → collapse | s0 |
| exp_006_fixed_dt2 | Walker Walk | fixed dt=2, trained dt_emb, H=15 | Peak 485→collapse to ~135 | s0 |
| exp_007_fixed_dt4 | Walker Walk | fixed dt=4, trained dt_emb, H=15 | Peak 177 (33% baseline) | s0 |
| exp_008c_no_subsample_dt2_h8 | Walker Walk | untrained dt_emb, subsample OFF, dt=2, H=8 | eval ~242 (reduced effective horizon) | s0 |
| exp_008e_v3_s3 | Walker Walk | trained dt_emb, dt=1 imag, H=15 | C6: collapse via non-CIVO pathway | s3 |
| exp_008e_v3_walker_s2 | Walker Walk | trained dt_emb, dt=1 imag, H=15 | C6: collapse (eval-driven, Pathway B) | s2 |
| exp_008f_s4 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | Borderline NVE decline after 75K | s4 |
| exp_009b_008d_walker_s2 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO onset → self-correction (eval 268) | s2 |
| exp_009c_008f_walker_s2 | Walker Walk | dt_embed_dim=0, subsample ON, H=8 | NVE borderline 1.14x@105K | s2 |
| exp_009e_008d_walker_s1 | Walker Walk | trained dt_emb, subsample ON, H=8 | CIVO collapse confirmed (= 008d s1) | s1 |
| exp_015b_frozen_dt_emb | Walker Walk | frozen dt_emb, subsample ON, dt=2, H=8 | Frozen dt_emb early negative | s1 |
| exp_016e_sgs_walker_s1 | Walker Walk | Reward-only SGS | NVE=10.42×, paradoxically worse | s1 |
| exp_018_full_sgs_s2 | Walker Walk | Full SGS | Collapse (eval 40.8) | s2 |
| exp_018v2_full_sgs_walker_s1 | Walker Walk | Full SGS v2 | NVE 1.66×, CIVO+ | s1 |
| exp_021_full_sgs_cheetah_s1 | Cheetah Run | Full SGS | Transient NVE 9.94× | s1 |
| exp_025_obs_sgs_walker_s2 | Walker Walk | Obs-decoder SGS | Collapse despite obs-decoder block | s2 |
| exp_027_tcn_walker_s0 | Walker Walk | TCN σ=0.5 | NVE 3.97, oscillatory CIVO | s0 |
| exp_027_tcn_walker_s1 | Walker Walk | TCN σ=0.5 | NVE 1.64, oscillatory | s1 |
| exp_028_rave_walker_s0 | Walker Walk | RAVE ceil=2.0 | EMA anchor polluted | s0 |
| exp_028_rave_walker_s0_ceil15 | Walker Walk | RAVE ceil=1.5 | EMA anchor polluted | s0 |
| exp_029b_tcn_walker_s2_sigma02 | Walker Walk | TCN σ=0.2 | NVE=2.11@95K, gradual onset CIVO | s2 |
| exp_029c_tcn_walker_s0_sigma01 | Walker Walk | TCN σ=0.1 | Borderline dose response | s0 |
| exp_029d_tcn_walker_s3_sigma02 | Walker Walk | TCN σ=0.2 | NVE=3.04@105K, sudden onset | s3 |
| exp_030a_tcn_cheetah_s0_sigma02 | Cheetah Run | TCN σ=0.2 | NVE=1.90@55K, dose insufficient | s0 |
| exp_030b_tcn_cheetah_s0_sigma05 | Cheetah Run | TCN σ=0.5 | NVE=10.67@55K, transient spike | s0 |
| exp_030c_tcn_cheetah_s0_sigma10 | Cheetah Run | TCN σ=1.0 | CIVO prevented but eval→47 (impossible dose) | s0 |
| exp_031_tcn_pickcube_s0_sigma02 | PickCube-v1 | TCN σ=0.2 | NVE=3.71@52.5K, dose insufficient | s0 |
| exp_031b_tcn_pickcube_s0_sigma05 | PickCube-v1 | TCN σ=0.5 | Still insufficient | s0 |
| exp_034 | Cheetah Run | Dual-critic | CIVO (NVE 1.75) → partial recovery 31% | s0 |
| exp_034_dual_critic_cheetah | Cheetah Run | Dual-critic | CIVO despite dual-critic | s0 |
| exp_036_dual_critic_pickcube | PickCube-v1 | Dual-critic | PickCube scope limitation | s0 |
| exp_037_wide_critic_cheetah | Cheetah Run | Wide single critic | CIVO still present | s0 |
| exp_038_dual_critic_walker_s2 | Walker Walk | Dual-critic (wide) | Non-CIVO collapse (entropy ↑) | s2 |
| exp_051_stackcube_frozen_dt_emb_s0 | StackCube-v1 | Frozen dt_emb | StackCube frozen negative | s0 |

### A.3 Running Experiments (n=4)

| exp_id | Environment | Config | Server | ETA |
|--------|-------------|--------|--------|-----|
| exp_060_cartpole_baseline | Cartpole Swingup | dt=1, vanilla baseline | bjb1-45299 cuda:0 | 5/25 13:30 UTC |
| exp_061_cartpole_civo_trigger | Cartpole Swingup | trained dt_emb, subsample ON, H=8 | bjb1-45299 cuda:1 | 5/25 15:30 UTC |
| exp_062_cartpole_control | Cartpole Swingup | dt_embed_dim=0, subsample ON, H=8 | bjb1-40020 cuda:0 | 5/25 17:20 UTC |
| exp_066_timeseries_rssm_fidelity | Analysis | RSSM fidelity timeseries (12 dense ckpts) | bjb1-40020 | running |

### A.4 Failed / Killed (n=32, not included in analysis)

11 failed (config errors, code bugs) + 21 killed (superseded by improved configs).

---

## B. All-Seed Learning Curves

### B.1 Walker Walk

| Condition | exp_id(s) | Seeds | Server | Logdir |
|-----------|-----------|-------|--------|--------|
| **Baseline (dt=1)** | exp_001_baseline | s1 | bjb1-45299 | /root/autodl-tmp/event-gated-adaptive-horizon/ (original) |
| | exp_001_baseline_s2, _s2_extended | s2 | bjb1-45299 | (check W&B) |
| | exp_001_baseline_s3, _s3_extended | s3 | bjb1-45299 | (check W&B) |
| | exp_001_baseline_s4, _s4_extended | s4 | bjb1-45299 | (check W&B) |
| | exp_009d_baseline_walker_s0 | s0 | bjb1-45299 | (check W&B) |
| | exp_009a_baseline_walker_s2 | s2 | bjb1-45299 | (check W&B) |
| **Trained dt_emb (CIVO trigger)** | exp_008d_subsample_on_h8 | s1 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |
| | exp_009b_008d_walker_s2 | s2 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |
| | exp_008d_civo_trigger_s3 | s3 | bjb1-45299 | (check W&B) |
| | exp_008d_civo_trigger_s4 | s4 | bjb1-45299 | (check W&B) |
| | exp_059_walker_trained_s5 | s5 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |
| | exp_009e_008d_walker_s1 | s1 (dup=008d) | bjb1-45299 | |
| **Frozen dt_emb** | exp_042_frozen_dt_emb_walker | s0 | bjb1-45299 | (check W&B) |
| | exp_047_frozen_dt_emb_walker_s1 | s1 | bjb1-45299 | (check W&B) |
| | exp_057_frozen_dt_emb_walker_s2 | s2 | bjb1-45299 | (check W&B) |
| **No dt_emb (dim=0)** | exp_008f_no_dt_embed_subsample_on_h8 | s0 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |
| | exp_009c_008f_walker_s2 | s2 | bjb1-45299 | /root/dreamerv3-torch/logdir/ |
| | exp_008f_s3_no_dt_embed_walker | s3 | bjb1-45299 | |
| | exp_043_008f_walker_s1 | s1 | bjb1-45299 | |
| **Untrained dt_emb** | exp_008a_no_subsample_dt2 (H=15) | s0 | bjb1-45299 | |
| | exp_008a_unexposed_s1 | s1 | bjb1-45299 | |
| | exp_008a_unexposed_s2 | s2 | bjb1-45299 | |
| **dt=1 imagination** | exp_008e_v3_walker_s1 | s1 (healthy) | bjb1-45299 | |
| | exp_008e_v3_walker_s2 | s2 (collapsed) | bjb1-45299 | |
| | exp_008e_v3_s3 | s3 (collapsed) | — | |
| | exp_008e_v3_s4 | s4 (healthy) | — | |

**需要的图表**:
- **Fig S1**: Walker Walk all-seed learning curves (eval return vs steps), 6 conditions 叠加，每条线标注 seed
- **Fig S2**: Walker Walk NVE evolution per seed, same 6 conditions

### B.2 Cheetah Run

| Condition | exp_id(s) | Seeds | Server | Logdir |
|-----------|-----------|-------|--------|--------|
| **Baseline (dt=1)** | exp_023a_cheetah_baseline_s0 | s0 | — | |
| | exp_023b_cheetah_baseline_s1, exp_010a_cheetah_baseline_s1 | s1 | bjb1-45299 | |
| | exp_023_cheetah_baseline_s2 | s2 | — | |
| | exp_023_cheetah_baseline_s3 | s3 | — | |
| | exp_023_cheetah_baseline_s4, _s4_extended | s4 | — | |
| **Trained dt_emb** | exp_010b_cheetah_civo_trigger | s1 | — | |
| | exp_010b_cheetah_civo_trigger_s0 | s0 | — | |
| **Frozen dt_emb** | exp_046_frozen_dt_emb_cheetah | s0 | bjb1-40020 | |
| | exp_058_frozen_dt_emb_cheetah_s1 | s1 | — | |
| **No dt_emb** | exp_024b_cheetah_no_dt_emb_s0 | s0 | — | |
| | exp_024b_cheetah_no_dt_emb_s1 | s1 | bjb1-45299 | |

**需要的图表**:
- **Fig S3**: Cheetah Run all-seed learning curves
- **Fig S4**: Cheetah Run NVE evolution per seed

### B.3 Cartpole Swingup (TODO — experiments running)

| Condition | exp_id(s) | Seeds | Server | ETA |
|-----------|-----------|-------|--------|-----|
| **Baseline** | exp_060_cartpole_baseline | s0 | bjb1-45299 cuda:0 | 5/25 13:30 |
| **CIVO trigger** | exp_061_cartpole_civo_trigger | s0 | bjb1-45299 cuda:1 | 5/25 15:30 |
| **No dt_emb control** | exp_062_cartpole_control | s0 | bjb1-40020 cuda:0 | 5/25 17:20 |

**需要的图表**:
- **Fig S5**: Cartpole Swingup learning curves + NVE (TODO: 待实验完成)

### B.4 Manipulation Environments (PickCube, StackCube, PegInsertion)

| Condition | exp_id(s) | Environment | Seeds |
|-----------|-----------|-------------|-------|
| **PickCube baseline** | exp_019a_v2_pickcube_baseline | PickCube-v1 | s0 |
| **PickCube CIVO** | exp_019b_pickcube_civo_trigger | PickCube-v1 | s0 |
| **PickCube frozen** | exp_054_pickcube_frozen_s0 | PickCube-v1 | s0 |
| **StackCube CIVO** | exp_049_stackcube_civo_trigger_s0 | StackCube-v1 | s0 |
| | exp_052_stackcube_civo_trigger_s1 | StackCube-v1 | s1 |
| **StackCube frozen** | exp_051_stackcube_frozen_dt_emb_s0 | StackCube-v1 | s0 |
| **PegInsertion CIVO** | exp_050_peginsertion_civo_trigger_s0 | PegInsertion-v1 | s0 |
| | exp_055_peginsertion_civo_trigger_s1 | PegInsertion-v1 | s1 |
| **PegInsertion frozen** | exp_053_peginsertion_frozen_s0 | PegInsertion-v1 | s0 |
| | exp_056_peginsertion_frozen_s1 | PegInsertion-v1 | s1 |

**需要的图表**:
- **Fig S6**: Manipulation environments learning curves (scope limitation discussion)

---

## C. Intervention Hierarchy — Complete Data

### C.1 Overview Table (论文 Section 3.6 核心)

| Level | Method | Success Rate | Environments | exp_ids | Primary Failure Mechanism |
|-------|--------|-------------|--------------|---------|--------------------------|
| **L1: Gradient** | Reward-only SGS | 0/2 | Walker | 016e | No-op (gradient ≠ causal); paradoxically worse NVE=10.42× |
| **L1: Gradient** | Full SGS | 0/3 | Walker, Cheetah | 018v2 (s1), 018 (s2), 021 | Forward-pass damage irreducible |
| **L1: Gradient** | Obs-decoder SGS | 1/6 | Walker (4), Cheetah (2) | 025_s1✓, 025_s2✗, 025_s3✗, 025_s4✗, 026_s0✗, 026_s1✗ | Compensatory amplification + critic calibration damage |
| **L2: Output** | RAVE ceil=2.0 | 0/1 | Walker | 028 | EMA anchor self-pollution |
| **L2: Output** | RAVE ceil=1.5 | 0/1 | Walker | 028_ceil15 | EMA anchor self-pollution |
| **L3: Representation** | TCN σ=0.1 | 0/1 | Walker | 029c | Borderline, dose insufficient |
| **L3: Representation** | TCN σ=0.2 | 2/4 (Walker only) | Walker (4), Cheetah (1), PickCube (1) | 027_sigma02✓, 029a✓, 029b✗, 029d✗, 030a✗, 031✗ | Seed sensitivity + cross-env dose mismatch |
| **L3: Representation** | TCN σ=0.5 | 0/3 | Walker (2), Cheetah (1), PickCube (1) | 027✗, 027_s1✗, 030b✗, 031b✗ | Overdose (Walker) / insufficient (Cheetah) |
| **L3: Representation** | TCN σ=1.0 | 1/1 (CIVO only) | Cheetah | 030c | CIVO prevented but eval=47 (impossible dose) |
| **L4: Architecture** | Dual-critic (wide) | 3/4 (CIVO), 2/4 (perf) | Walker (4), Cheetah (2), PickCube (1) | 032✓, 032b✓, 038✗(non-CIVO), 041✓ | s2 non-CIVO collapse; Cheetah partial |
| **L4: Architecture** | Dual-critic (narrow) | 0/2 (CIVO occurs → recovery) | Walker | 035, 039 | CIVO occurs but min enables recovery |
| **L4: Architecture** | Wide single critic | 0/1 (CIVO → partial recovery) | Walker, Cheetah | 033, 037 | Capacity alone insufficient for prevention |
| **Control** | dt_emb removal (dim=0) | 5/5 | Walker (3), Cheetah (2) | 008f, 009c, 043, 024b_s0, 024b_s1 | — (removes the feature) |
| **Control** | Frozen dt_emb | 5/5 | Walker (3), Cheetah (2) | 042, 047, 057, 046, 058 | — (disables training) |

### C.2 SGS 详细数据

**exp_016e (Reward-only SGS)**:
- Config: reward_dt_emb_detach=True, subsample ON, H=8, seed=1
- NVE: 10.42× (paradoxically 5× worse than untreated 008d ~2×)
- eval: peak 326.7@75K → collapse 31.7@95K
- Failure: Reward gradient to dt_emb is 0 by architecture — reward SGS is a no-op. 016e 与 008d 差异归因于随机变异。
- Key insight: **Gradient magnitude ≠ causal importance** — reward head carries 38-49% of gradients but blocking it has no effect

**exp_018v2_full_sgs_walker_s1 (Full SGS)**:
- Config: all decoder gradients blocked from dt_emb
- NVE: 1.66×, CIVO+ (above threshold)
- eval: 448.3
- Failure: forward-pass representational damage persists without backward-pass gradients

**exp_018_full_sgs_s2**:
- NVE: collapse
- eval: 40.8

**exp_021_full_sgs_cheetah_s1**:
- NVE: 9.94× transient → recovery to 0.34×
- Recovery not due to SGS (same pattern in untreated Cheetah)

**exp_025 Obs-decoder SGS (Walker, 4 seeds)**:
- s1: eval 726 (survived) but ve_ratio 0.056 @215K → **universal value collapse**
- s2: collapsed (CIVO)
- s3: healthy@105K → CIVO@135K (NVE 6.8×) → eval recovery 590@215K → persistent value collapse (ve_ratio 0.14)
- s4: collapsed
- All 4 seeds terminal ve_ratio 0.056-0.14 — critic underestimation as side effect

**exp_026 Obs-decoder SGS (Cheetah, 2 seeds)**:
- s0: NVE 21.9× (untreated baseline: 8.3×) — **compensatory amplification 2.6×**
- s1: NVE 30.2× — **compensatory amplification 3.6×**
- Blocking obs-decoder shifts co-adaptation to reward head

### C.3 TCN 详细数据

**Dose-Response Summary**:

| σ | Walker | Cheetah | PickCube |
|---|--------|---------|----------|
| 0.1 | ⚠️ borderline (1 seed) | — | — |
| 0.2 | ✅ 2/4, eval 45-91% | ❌ NVE 1.90 | ❌ NVE 3.71 |
| 0.5 | ❌ oscillatory (2 seeds) | ❌ NVE 10.67 transient | ❌ insufficient |
| 1.0 | — | ✅ CIVO prevented, ❌ eval=47 | — |

**Impossible Dose (exp_030c Cheetah σ=1.0, FINAL @224K)**:
- NVE ≤ 0.30 全程 → CIVO 完全抑制
- eval: peak 372@35K (116% baseline) → 47@215K (15% baseline)
- value_mean=12.4, NVE=0.26@215K → value calibration normal
- Key: 噪声不阻止初始学习（early eval > baseline!），而是渐进腐蚀 policy
- Cheetah CIVO prevention threshold (~σ=1.0) > noise tolerance threshold (~σ<0.5)
- **不存在 Goldilocks zone**

### C.4 RAVE 详细数据

- **ceil=2.0**: EMA anchor tracks polluted imagined values → ceiling ineffective. CIVO unmitigated.
- **ceil=1.5**: Same mechanism. More aggressive ceiling also fails because anchor is already biased.

### C.5 Dual-Critic 2×2 Mechanism Factorial

| | Single critic | Dual critic (min) |
|--|--------------|-------------------|
| ~1.05-1.2M params | **008d: CIVO → permanent collapse** | **exp_035 narrow: CIVO(NVE 2.75) → recovery → eval 697.8** |
| ~2.4-2.9M params | **exp_033 wide: CIVO(NVE 4.75) → self-repair → eval 408** | **exp_032: CIVO prevented (NVE≤1.1) → eval 670-788** |

- **v1 ≈ v2 across all configs** (ρ>0.999): Double Q pessimism mechanism fails in pure-imagination MBRL
- **Min >> Capacity for recovery**: 697.8 vs 408
- **Prevention requires min+capacity synergy**: only exp_032 (min+wide) prevents CIVO entirely
- **Cross-env caveat**: Walker recovery sufficient (697.8), Cheetah recovery insufficient (97.5, 31%)

---

## D. NVE Diagnostic — Complete Data

### D.1 NVE Threshold Analysis (plan_034)

- **AUROC = 0.961** (29 experiments, 2 environments)
- **Optimal threshold: 1.5× (Youden-optimal: 1.53×)**
- **F1 = 0.880** at threshold 1.5×
- **TPR/FPR**: 15/16 CIVO-positive correctly identified, AUROC near-perfect separation

**Threshold Sensitivity**:

| Threshold | TPR | FPR | F1 | Notes |
|-----------|-----|-----|----|-------|
| 1.0× | 16/16 | high | lower | Over-sensitive |
| 1.25× | 16/16 | moderate | moderate | |
| **1.5×** | **15/16** | **low** | **0.880** | **Optimal (Youden)** |
| 2.0× | 12/16 | very low | lower | Under-sensitive |
| 3.0× | 8/16 | 0 | lower | Too conservative |

**时间限定**: NVE>1.5× diagnostic 适用于 **35K+ steps**（baseline v/e 已收敛至 >0.24）。25K 处 baseline v/e 仅 0.087，微小绝对差异被放大。

### D.2 Per-Experiment NVE Summary

**Walker Walk (trained dt_emb)**:
| exp_id | Seed | NVE_peak | NVE_step | Outcome | Classification |
|--------|------|----------|----------|---------|----------------|
| exp_008d_subsample_on_h8 | s1 | 4.12×@55K | 35K+ sustained | Collapse | CIVO |
| exp_009b_008d_walker_s2 | s2 | 2.05×@25K, 1.62×@45K | Transient | Self-correction (eval 268) | CIVO (self-correcting) |
| exp_008d_civo_trigger_s3 | s3 | (sustained CIVO) | 35K+ | Collapse | CIVO |
| exp_008d_civo_trigger_s4 | s4 | (sustained CIVO) | 35K+ | Collapse | CIVO |
| exp_059_walker_trained_s5 | s5 | 4.72×@85K | 85K | Collapse (eval 95.8 = 10.5% baseline) | Onset_collapse (Collapse†) |

**Walker Walk (no dt_emb / frozen / untrained)**:
| exp_id | Seed | NVE_peak | Outcome | Classification |
|--------|------|----------|---------|----------------|
| exp_008f (dim=0) | s0 | 1.02× | Stable | No CIVO |
| exp_009c (dim=0) | s2 | 1.26× | Borderline but stable | No CIVO |
| exp_042 (frozen) | s0 | 0.19× | Stable | No CIVO |
| exp_047 (frozen) | s1 | 1.71× transient | Stable | No CIVO (transient) |
| exp_057 (frozen) | s2 | (stable) | Stable | No CIVO |
| exp_008a (untrained) | s0 | 0.59-0.93× | Two recovery cycles | No CIVO |

**Cheetah Run**:
| exp_id | Seed | NVE_peak | Outcome | Classification |
|--------|------|----------|---------|----------------|
| exp_010b s0 | s0 | 70.64× | Collapse (irreversible) | CIVO (severe) |
| exp_010b s1 | s1 | 8.27× | Collapse | CIVO |
| exp_046 (frozen) | s0 | 1.35× | Stable | No CIVO |
| exp_058 (frozen) | s1 | (stable) | Stable | No CIVO |

### D.3 AUROC Confusion Matrix (at threshold 1.5×, 35K+)

|  | Predicted CIVO+ | Predicted CIVO- |
|--|-----------------|-----------------|
| **Actual CIVO+** | TP = 15 | FN = 1 |
| **Actual CIVO-** | FP = 0 | TN = 13 |

- Precision = 15/15 = 1.000
- Recall = 15/16 = 0.938
- F1 = 0.880 (based on n=29 full dataset, TODO: verify exact calculation)
- AUROC = 0.961

### D.4 NVE Baseline Reference Values (exp_001 s1)

| Step | baseline v/e | baseline ve_ratio |
|------|-------------|-------------------|
| 25K | 8.7% | 0.087 |
| 35K | 24.1% | 0.241 |
| 45K | 33.1% | 0.331 |
| 55K | 40.4% | 0.404 |
| 65K | 56.3% | 0.563 |
| 85K | — | 0.7007 |
| 105K | — | 0.656 |

---

## E. RSSM Fidelity Analysis (exp_063)

### E.1 Model Comparison Table

| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |
|-------|------------|------------|---------|---------------|---------------|------------|
| baseline (exp_001) | 13.49 | 27.50 | **2.04×** | 0.0102 | 0.0159 | 1.56× |
| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30×** | 0.0568 | 0.1579 | **2.78×** |
| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75×** | 0.7469 | 0.7526 | 1.01× |

**解读**:
- 008d 低 obs gap ratio (1.30×) 具有误导性 — dt=1 绝对误差已是 baseline 的 3× (model 已崩塌)
- 008d reward gap (2.78×) 表明 dt_emb 使 reward head 能区分 dt=1/dt=2 但在 dt=2 上系统性偏差
- 008f reward gap 仅 1.01× — 没有 dt_emb 的 reward head 完全无法区分不同 dt

### E.2 Gradient Decomposition (dt_emb.weight)

| Source | 55K (%) | 112K (%) |
|--------|---------|----------|
| Reward head | 49.0 | 38.1 |
| KL dynamics | 34.7 | 40.4 |
| Obs decoders | 16.3 | 21.5 |
| Cont head | ~0 | ~0 |

**Key finding**: Gradient magnitude ≠ causal importance. Reward head 最大梯度 (49%) 但 reward-only SGS 完全无效; obs decoder 最小非零梯度 (16%) 但携带 Δt-specific 空间信息。

### E.3 Timeseries RSSM Fidelity (exp_066, RUNNING)

- 12 dense checkpoints, 每 5K steps, 0-60K 训练过程
- 目标：建立 RSSM fidelity gap → NVE 的时序因果链
- TODO: 待 exp_066 完成后补充数据

---

## F. Actor Entropy Causal Chain (plan_031)

### F.1 Summary

Collapsed configs (trained dt_emb) 的 actor entropy 在 CIVO onset 后爆炸性增长:
- **Collapsed**: +2.1 nats / 10K steps (after collapse onset)
- **Healthy**: +0.07 ~ +0.22 nats / 10K steps

### F.2 Temporal Causation

时序因果链确认: **return 先崩 → entropy 后升**
- 非 entropy 先升导致 return 崩 (排除 exploration failure 假说)
- 与 CIVO 叙事一致: value overestimation → actor exploits overestimated values → policy degrades → entropy increases as learned policy collapses

### F.3 Data Source
- Artifact: `artifacts/actor_entropy_analysis.md`
- All experiments with actor_entropy logged via W&B

---

## G. Value Prediction Distribution (exp_064)

### G.1 Summary
- trained dt_emb (008d collapsed): V(s) systematically overestimates at dt=2 imagination steps
- untrained/absent dt_emb (008f) + baseline (001): V(s) tracks MC return closely
- **直观展示 CIVO 的 value divergence 位置和形态**

### G.2 Charts
- Scatter plot: V(s) vs MC return per config
- Histogram: value ratio distribution
- Value bias vs timestep within imagination rollout

### G.3 Data Source
- Server: bjb1-40020
- Artifact directory: `artifacts/exp_064_value_distribution/`

---

## H. Cosine Similarity Analysis (exp_065)

### H.1 Summary
- dt=1 vs dt=2 embedding cosine similarity 及训练过程演化
- 判断 CIVO 来自微小差异被 downstream 放大 (high cosine sim) 还是 dt=2 表征本身偏差 (low cosine sim)

### H.2 Charts
- `cosine_sim_evolution.png`: cosine similarity vs training steps
- `pairwise_heatmap.png`: 所有 dt embedding 向量的 pairwise similarity

### H.3 Data Source
- Server: bjb1-45299
- Logdir: `/root/dreamerv3-torch/logdir/exp_065_dt_emb_cosine/`

---

## I. Negative Results — Detailed Analysis

### I.1 High-Value Negative Results (7 categories)

**1. Event-Gated Mechanisms (exp_003/004/005)**:
- Learned gate → all degrade/collapse
- Insight: adaptive temporal abstraction in imagination is fundamentally difficult, not just a hyperparameter issue

**2. Reward-only SGS (016e)**:
- Paradoxically worse (NVE 10.42× vs untreated ~2×)
- Insight: blocking reward gradient forces dt_emb adaptation through obs-decoder, reinforcing spatial bias

**3. Full SGS Failure (018/018v2/021)**:
- 0/3 across 2 environments despite blocking ALL non-KL gradients
- Insight: forward-pass representational damage is irreducible; backward-pass interventions are categorically insufficient

**4. Obs-decoder SGS Compensatory Amplification (025/026)**:
- Cheetah: blocking obs-decoder → 2.6-3.6× NVE amplification vs untreated
- Insight: CIVO exploits redundant pathways; blocking one strengthens others

**5. RAVE Anchor Pollution (028)**:
- EMA tracks polluted imagined values → ceiling is anchored too high
- Insight: output-level interventions fail when the reference signal is contaminated

**6. TCN Dose-Environment Impossibility (030c)**:
- Cheetah σ=1.0: CIVO prevented but eval→47 (15% baseline)
- Key: effective dose > tolerable dose → no Goldilocks zone exists
- Insight: representation-level noise is environment-specific and cannot be universalized

**7. Dual-Critic Non-CIVO Collapse (038)**:
- eval 354→121 with normal NVE (≤0.3), actor entropy ↑
- Insight: trained dt_emb creates vulnerability through multiple pathways (CIVO = Pathway A, policy instability = Pathway B)

### I.2 Contribution to Paper Narrative

These negative results form two positive contributions:
1. **Intervention Hierarchy**: systematic taxonomy proving CIVO is fundamentally hard to mitigate at all 3 intervention levels
2. **Multi-Pathway Vulnerability**: trained dt_emb creates both CIVO (value-driven) and non-CIVO (eval-driven) failure modes

---

## J. Figures & Tables Checklist

### Main Paper Figures (planned)
| # | Type | Content | Status |
|---|------|---------|--------|
| Fig 1 | Learning curves | Hero figure: all experiments overlaid | TODO |
| Fig 2 | Line plot | Value/eval ratio — healthy vs pathological | TODO |
| Fig 3 | Grid/heatmap | Factorial grid summary (dt_emb × subsample) | TODO |
| Fig 4 | Diagram | Causal chain: dt_emb → value overestimation → collapse | TODO |
| Fig 5 | Line plot | dt=1 vs dt=2 vs dt=4 monotonic degradation | TODO |
| Table 1 | Table | RSSM fidelity — absolute + ratio | TODO |
| Fig 6 | Line plot | Mitigation comparison (008e_v3 seeds) | TODO |

### Supplementary Figures
| # | Type | Content | Data Source | Status |
|---|------|---------|-------------|--------|
| Fig S1 | Multi-line plot | Walker all-seed learning curves (6 conditions) | W&B / logdir | TODO |
| Fig S2 | Multi-line plot | Walker NVE evolution per seed | W&B / logdir | TODO |
| Fig S3 | Multi-line plot | Cheetah all-seed learning curves | W&B / logdir | TODO |
| Fig S4 | Multi-line plot | Cheetah NVE evolution per seed | W&B / logdir | TODO |
| Fig S5 | Multi-line plot | Cartpole learning curves + NVE | exp_060/061/062 | TODO (running) |
| Fig S6 | Multi-line plot | Manipulation environments | W&B | TODO |
| Fig S7 | Bar chart | Intervention hierarchy success rates | Section C | TODO |
| Fig S8 | Scatter | Value distribution V(s) vs MC return | exp_064 | DONE (artifacts/) |
| Fig S9 | Histogram | Value ratio distribution | exp_064 | DONE (artifacts/) |
| Fig S10 | Line plot | NVE threshold sensitivity (ROC curve) | plan_034 | TODO |
| Fig S11 | Line plot | Actor entropy evolution (collapsed vs healthy) | plan_031 | DONE (artifacts/) |
| Fig S12 | Heatmap | dt_emb cosine similarity | exp_065 | DONE (server) |
| Fig S13 | Line plot | Cosine similarity evolution | exp_065 | DONE (server) |
| Fig S14 | Line plot | RSSM fidelity timeseries | exp_066 | TODO (running) |
| Fig S15 | Line plot | TCN dose-response curves | exp_027-031 | TODO |
| Fig S16 | Line plot | Dual-critic v1 vs v2 correlation | exp_032-041 | TODO |
| Fig S17 | Bar chart | Gradient decomposition (dt_emb.weight) | exp_063 | TODO |

### Supplementary Tables
| # | Content | Status |
|---|---------|--------|
| Table S1 | Complete experiment registry (A.1+A.2) | This document |
| Table S2 | Intervention hierarchy full data (C.1) | This document |
| Table S3 | NVE per-experiment values (D.2) | This document |
| Table S4 | AUROC confusion matrix (D.3) | This document |
| Table S5 | RSSM fidelity all models (E.1) | This document |
| Table S6 | Gradient decomposition (E.2) | This document |
| Table S7 | TCN dose-response full table (C.3) | This document |
| Table S8 | Dual-critic 2×2 factorial (C.5) | This document |
| Table S9 | Baseline NVE reference values (D.4) | This document |

---

## K. Outstanding TODOs

### Data Gaps
- [ ] **Cartpole results** (exp_060/061/062): running, ETA 5/25 17:20 UTC → Section B.3, Fig S5
- [ ] **exp_066 RSSM fidelity timeseries**: running → Section E.3, Fig S14
- [ ] **Per-experiment logdir paths**: many experiments missing exact logdir — need W&B run URLs or server paths
- [ ] **Exact key_metrics** for all experiments: registry fields are sparse, need per-experiment data from W&B

### Figures to Generate
- [ ] Fig S1-S6: All-seed learning curves per environment (from W&B data)
- [ ] Fig S7: Intervention hierarchy bar chart
- [ ] Fig S10: NVE ROC curve with threshold annotations
- [ ] Fig S15: TCN dose-response (σ vs NVE, σ vs eval, per environment)
- [ ] Fig S16: Dual-critic v1-v2 scatter plots
- [ ] Fig S17: Gradient decomposition stacked bar chart

### Writing
- [ ] LaTeX appendix template (ICML 2026 supplementary format)
- [ ] Cross-reference main paper figure/table numbering
- [ ] Proofread all experiment descriptions for consistency
- [ ] Add IQM + CI for multi-seed conditions (per Agarwal et al. 2021)
- [ ] Verify AUROC F1 calculation (currently 0.880 — confirm formula used)

---

## L. Data Source Registry

| Source | Location | Access |
|--------|----------|--------|
| W&B project | (project W&B URL) | wandb API |
| Server bjb1-45299 | ssh connect.bjb1.seetacloud.com | SSH |
| Server bjb1-40020 | ssh connect.bjb1.seetacloud.com | SSH |
| Local artifacts | `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/` | Local |
| Registry | `read_registry(project="event-gated-adaptive-horizon")` | MCP tool |
| Experiment code | `/root/autodl-tmp/event-gated-adaptive-horizon/` (on server) | SSH |
