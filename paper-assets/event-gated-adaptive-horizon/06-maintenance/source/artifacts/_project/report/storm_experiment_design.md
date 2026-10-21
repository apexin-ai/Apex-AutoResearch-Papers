# STORM Cross-Architecture Experiment Design

## 1. Hypothesis

**Primary**: CIVO is not RSSM-specific — it manifests in any imagination-based actor-critic that combines trained temporal conditioning with pure-imagination value estimation.

**Operationalized**: A transformer world model (STORM) with trained dt-embedding + multi-rate data exposure will produce NVE > 2.0× and eval collapse on Walker Walk, replicating the DreamerV3 CIVO pattern.

**Alternative (if negative)**: CIVO requires the RSSM's recurrent bottleneck architecture. The transformer's parallel attention mechanism may resist the co-adaptation dynamics that drive CIVO in DreamerV3.

**Why this matters for the paper**: Current paper claims CIVO is structural to "any imagination-based actor-critic" (analysis.tex ¶4), but all evidence comes from DreamerV3/RSSM. A single cross-architecture confirmation would substantially strengthen the contribution; a null result would precisely narrow the scope to RSSM architectures.

---

## 2. Phase 1: Baseline Verification (dt=1)

### Goal
Confirm STORM DMC adaptation produces a healthy Walker Walk baseline, prerequisite for all CIVO experiments.

### Configuration

| Parameter | Value |
|-----------|-------|
| Environment | DMC Walker Walk (proprioceptive, 24-dim obs, 6-dim action) |
| Architecture | STORM transformer WM (2-layer, 8-head, 512-dim) + discrete categorical latent (32×32) |
| dt-conditioning | None (Phase 1 = standard STORM) |
| Steps | 500K environment steps |
| Seed | 0 |
| Imagination horizon | 15 steps (config default) |
| Eval | 10 episodes greedy, every 10K steps |
| WM lr | 3e-4, Agent lr | 3e-5 |
| γ=0.997, λ=0.95 | |

### Launch command

```bash
export CUDA_VISIBLE_DEVICES=<N> && export MUJOCO_EGL_DEVICE_ID=<N>
cd /root/autodl-tmp/event-gated-adaptive-horizon/storm_dmc
python -u train_dmc.py -n storm_baseline_s0 -seed 0 -config_path config/dmc_walker.yaml
```

### Success criteria

| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| eval_return_mean@500K | ≥ 600 | 80% of DreamerV3 baseline (787.7). STORM's original Atari results suggest competitive but not identical performance. |
| Learning curve | Monotonically increasing with plateaus OK | No mid-training collapse |
| value_mean | Tracks eval_return (v/e ratio ∈ [0.5, 2.0]) | Healthy critic estimation |
| model_loss | Converging/stable by 100K | World model learning |

### Monitoring metrics
- `train/episode_return` — environment interaction performance
- `eval/return_mean`, `eval/return_std` — greedy evaluation
- `value_mean` — critic estimate (compute v/e ratio manually)
- World model losses (obs reconstruction, reward, KL)

### Failure scenarios and responses

| Outcome | Action |
|---------|--------|
| eval < 200 at 500K (< 25% DreamerV3) | **Debug**: Check obs scaling, action clipping, terminated/truncated handling. Compare STORM loss curves to Atari reference. |
| eval 200-400 (25-50% DreamerV3) | **Tune**: Try larger transformer (4-layer), longer warmup, adjusted lr. If still low → Scenario C. |
| eval 400-600 (50-80% DreamerV3) | **Marginal**: Proceed to Phase 2 with caution. CIVO signal may be harder to detect against a weaker baseline. |
| eval ≥ 600 | **Pass**: Proceed to Phase 2. |
| Training divergence (NaN, loss explosion) | **Debug**: Gradient clipping, lr warmup, check for numerical issues in MLP encoder/decoder. |

### Estimated GPU-hours
4-6 hours on 1× RTX PRO 6000 (500K steps with transformer model).

---

## 3. Phase 2: CIVO Isolation (requires Phase 1 pass)

### Code changes needed
Phase 2 requires implementing dt-conditioning in STORM. The modifications mirror DreamerV3's dt-embedding approach:

1. **DtEmbedding module** (`sub_models/dt_embedding.py`):
   - Learned embedding: `nn.Embedding(max_dt+1, embed_dim)` with `requires_grad=True`
   - Frozen variant: same architecture with `requires_grad=False`
   - Concatenated to transformer input alongside latent + action

2. **Transformer model** (`sub_models/transformer_model.py`):
   - Stem input changes from `stoch_dim + action_dim` to `stoch_dim + action_dim + dt_embed_dim`
   - Imagination loop passes dt values to embedding

3. **Replay buffer** (`replay_buffer.py`):
   - Add temporal subsampling: sample dt=2 transitions by skipping consecutive frames
   - Store dt values alongside obs/action/reward/done

4. **Training loop** (`train_dmc.py`):
   - Imagination at dt=2 with dt embedding
   - CLI flags: `--dt_embed_dim`, `--dt_embed_mode {trained,frozen,removed}`, `--subsample_max_dt`, `--imag_horizon`

### Configurations

**Config A (CIVO trigger)**:

| Parameter | Value | DreamerV3 equivalent |
|-----------|-------|---------------------|
| dt_embed_dim | 32 | gate_dt_embed_dim=32 |
| dt_embed_mode | trained | (default trained) |
| subsample_max_dt | 2 | gate_subsample_max_dt=2 |
| imag_dt | 2 | gate_fixed_dt=2 |
| imag_horizon | 8 | imag_horizon=8 |
| steps | 500K | (105K in DreamerV3 due to faster convergence) |
| seed | 0 | |

**Config B (causal control)**:

| Parameter | Value | DreamerV3 equivalent |
|-----------|-------|---------------------|
| dt_embed_dim | 0 | gate_dt_embed_dim=0 |
| subsample_max_dt | 2 | gate_subsample_max_dt=2 |
| imag_dt | 2 | gate_fixed_dt=2 |
| imag_horizon | 8 | imag_horizon=8 |
| steps | 500K | |
| seed | 0 | |

**Config C (frozen control, optional)**:

Same as Config A but `dt_embed_mode=frozen` (`requires_grad=False`).

### Scenario Determination

**Scenario A — CIVO confirmed in STORM**:
- Config A: NVE > 2.0× sustained after 35K steps + eval collapse (< 30% of Phase 1 baseline)
- Config B: NVE < 2.0× (healthy)
- Optional: Config C (frozen) also NVE < 2.0×

**Scenario B — CIVO absent in STORM**:
- Config A: NVE < 2.0× throughout, no eval collapse
- Config A eval within 70% of Phase 1 baseline
- Interpretation: CIVO may require RSSM's recurrent bottleneck

**Scenario C — Inconclusive**:
- Config A: NVE elevated but not crossing 2.0× clearly
- OR: Config B also shows elevated NVE (confounded by STORM adaptation issues)
- OR: Phase 1 baseline too weak for meaningful CIVO isolation (eval < 400)

### NVE Computation
Same formula as DreamerV3 experiments:
```
NVE_t = (v/e)_{config,t} / (v/e)_{baseline,t}
```
- `v`: mean imagined critic value
- `e`: mean evaluation return
- `baseline`: Phase 1 baseline at corresponding step
- Window: 35K+ steps (same as DreamerV3)
- Threshold: NVE ≥ 2.0× = CIVO-positive

### Estimated GPU-hours per config
4-6 hours × 3 configs = 12-18 GPU-hours total for Phase 2.

---

## 4. Paper Impact by Scenario

### Scenario A (CIVO confirmed) → Strongest paper upgrade
Pre-written text: `artifacts/storm_scenario_a_text.md` (8 sections)

| Section | Change |
|---------|--------|
| Abstract | +1 sentence: "Cross-architecture validation on STORM confirms CIVO is not specific to RSSM-based dynamics." |
| Introduction | Contribution 1 expanded: "cross-architecture validation on a transformer world model confirms the phenomenon is not RSSM-specific" |
| Discussion ¶4 | Rewrite: claim "manifests across RSSM and transformer dynamics architectures" (currently hedged) |
| Discussion ¶5 | STORM onset data added to complexity boundary |
| Limitations | Narrowed: "two architectures tested" (was "sole architecture") |
| Related Work | Optional: cite Zhang et al. 2023 in closing sentence |
| Table 1 | +3 rows (STORM baseline, trained, frozen) |
| Appendix | New subsection: STORM DMC adaptation details |

### Scenario B (CIVO absent) → Interesting null result, scope refinement
Pre-written text: `artifacts/storm_scenario_b_text.md` (7 sections)

| Section | Change |
|---------|--------|
| Discussion ¶4 | Rewrite: CIVO narrows to RSSM-specific. Two hypotheses for transformer resistance. |
| Limitations | Updated: "confirmed RSSM-specific, transformer resistance observed" |
| Appendix | New subsection: STORM results + architecture comparison |
| Abstract/Intro | No change (current text doesn't claim cross-architecture) |

### Scenario C (inconclusive) → Minimal changes
Pre-written text: `artifacts/storm_scenario_c_text.md` (2 sections)

| Section | Change |
|---------|--------|
| Limitations | +1 sentence: STORM attempt, baseline instability |
| Appendix | New subsection: "Transformer World Model Attempt" (transparency) |

---

## 5. Timeline and Dependencies

```
Phase 1 (baseline):     [Day 1-2]  ~6h GPU + analysis
  ↓ (pass/fail gate)
Phase 2 code:           [Day 2-3]  ~4h coding (no GPU)
Phase 2 experiments:    [Day 3-4]  ~18h GPU (3 configs)
  ↓
Analysis + paper edits: [Day 4-5]  ~2h
```

**Critical path**: Phase 1 baseline quality. If baseline fails (Scenario C), total GPU cost is ~6h and paper changes are minimal.

**Parallel opportunity**: Phase 2 code can be written while Phase 1 runs, so Phase 2 experiments can start immediately after Phase 1 passes.
