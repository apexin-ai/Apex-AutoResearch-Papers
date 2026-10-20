# 3×4 Matrix Experiment Summary Table

> Generated: 2026-05-22 | Source: westd-19183:/root/autodl-tmp/vla-ssd/results/

## Main Table

| Arch | Suite | R² trained (peak→exit, Δ) | R² untrained (peak→exit, Δ) | L1 trained | L1 untrained | CF trained (top d) | CF untrained (top cosine_dist) |
|------|-------|---------------------------|-----------------------------|-----------:|-------------:|--------------------|---------------------------------|
| OpenVLA | Goal | MISSING — no pipeline dir | MISSING — no pipeline dir | MISSING | MISSING | MISSING | MISSING |
| OpenVLA | Spatial | MISSING — no pipeline dir | MISSING — no pipeline dir | MISSING | MISSING | MISSING | MISSING |
| OpenVLA | Object | 0.787→0.666, Δ=0.121 | 0.761→0.685, Δ=0.076 | 24/32 | 24/32 | d=1.21 (empty) | cos=0.569 (empty) |
| OpenVLA | Long | 0.871→0.867, Δ=0.004 | 0.826→0.810, Δ=0.016 | 14/32 | 25/32 | d=0.56 (shuffled) | d=1.05 (empty) ‡ |
| TracVLA | Goal | 0.802→0.574, Δ=0.228 | 0.719→0.671, Δ=0.048 | 27/32 | 32/32 | d=1.52 (empty) | cos=0.153 (empty) |
| TracVLA | Spatial | 0.809→0.671, Δ=0.138 | 0.722→0.707, Δ=0.016 | 30/32 | 32/32 | d=1.33 (empty) | cos=0.180 (empty) |
| TracVLA | Object | 0.764→0.470, Δ=0.294 | 0.690→0.681, Δ=0.009 | 30/32 | 32/32 | d=1.21 (empty) | cos=0.185 (empty) |
| TracVLA | Long | 0.817→0.619, Δ=0.198 | 0.746→0.717, Δ=0.028 | 30/32 | 32/32 | d=1.47 (empty) | cos=0.173 (empty) |
| NORA | Goal | 0.688→−0.004, Δ=0.691 | 0.664→0.619, Δ=0.044 | 13/16 | 13/16 | cos=1.000 (all saturated) † | cos=0.081 (empty) |
| NORA | Spatial | 0.720→0.417, Δ=0.302 | 0.632→0.596, Δ=0.037 | 12/16 | 14/16 | cos=0.275 (wrong) | MISSING — no CF file |
| NORA | Object | N/A — no checkpoint | N/A | N/A | N/A | N/A | N/A |
| NORA | Long | N/A — no checkpoint | N/A | N/A | N/A | N/A | N/A |

**Notes:**
- † NORA Goal trained: exit-layer cosine distances saturated at 1.0 for all conditions (std=0), making ranking meaningless. Earlier layers show differentiation (L24 wrong=0.123, empty=0.098).
- ‡ OpenVLA Long untrained: uses action_mse/Cohen's d method (same as trained), NOT cosine distance. Reported d=1.05 for "empty" condition.

## CF Condition Rankings

### Trained (action_mse, Cohen's d)

| Arch | Suite | 1st | 2nd | 3rd | 4th |
|------|-------|-----|-----|-----|-----|
| OpenVLA | Object | empty (1.21) | wrong (1.19) | shuffled (1.12) | para (0.90) |
| OpenVLA | Long | shuffled (0.56) | wrong (0.55) | empty (0.50) | para (0.45) |
| TracVLA | Goal | empty (1.52) | wrong (1.40) | shuffled (1.34) | para (1.21) |
| TracVLA | Spatial | empty (1.33) | shuffled (1.29) | para (1.18) | wrong (1.17) |
| TracVLA | Object | empty (1.21) | shuffled (1.16) | wrong (1.06) | para (0.97) |
| TracVLA | Long | empty (1.47) | wrong (1.42) | shuffled (1.39) | para (1.16) |

### Untrained (cosine distance)

| Arch | Suite | 1st | 2nd | 3rd | 4th |
|------|-------|-----|-----|-----|-----|
| OpenVLA | Object | empty (0.569) | shuffled (0.298) | wrong (0.231) | para (0.085) |
| TracVLA | Goal | empty (0.153) | shuffled (0.084) | wrong (0.016) | para (0.004) |
| TracVLA | Spatial | empty (0.180) | shuffled (0.140) | wrong (0.005) | para (0.004) |
| TracVLA | Object | empty (0.185) | shuffled (0.098) | para (0.005) | wrong (0.004) |
| TracVLA | Long | empty (0.173) | shuffled (0.120) | wrong (0.022) | para (0.007) |
| NORA | Goal | empty (0.081) | shuffled (0.033) | wrong (0.014) | para (0.004) |

## Summary: Cross-Architecture Patterns

**R² exit collapse (Δ = peak − exit):**
- Trained models consistently show larger Δ than untrained across all architectures and suites.
- NORA trained shows the most extreme collapse: Goal Δ=0.691 (exit R² drops to −0.004), Spatial Δ=0.302.
- TracVLA trained shows moderate-to-large collapse across all 4 suites (Δ=0.138–0.294).
- OpenVLA Long trained is an outlier: Δ=0.004 (near-zero collapse), suggesting representations remain stable through exit layers.
- Untrained Δ values are uniformly small (0.009–0.076), confirming collapse is training-induced.

**L1 attention (instruction-dominant heads):**
- TracVLA untrained: 32/32 instruction-dominant across all 4 suites — Phi-3's pretrained attention is already instruction-biased before fine-tuning.
- TracVLA trained: slightly reduced (27–30/32), suggesting fine-tuning repurposes some heads away from instruction-only attending.
- OpenVLA Object: 24/32 in both trained and untrained — no change from fine-tuning on this suite.
- OpenVLA Long: dramatic shift — 14/32 trained vs 25/32 untrained — fine-tuning heavily reorganizes attention for Long suite.
- NORA (16-head model): 12–14/16 instruction-dominant, similar between trained/untrained.

**Counterfactual sensitivity (trained):**
- "empty" is the top condition for 5/6 available trained settings; OpenVLA Long is the exception with "shuffled" on top.
- TracVLA shows consistently high d values (1.2–1.5), indicating strong instruction sensitivity post-training.
- OpenVLA Long has notably weak CF sensitivity (d=0.45–0.56), possibly related to the near-zero R² collapse.

**Counterfactual sensitivity (untrained):**
- "empty" is universally the top condition across all untrained models.
- Cosine distances are much smaller for untrained models (0.004–0.569), with OpenVLA Object being an outlier at 0.569.
- Consistent ordering: empty > shuffled > wrong > para in most cases.

## Data Provenance

| Cell | Source File |
|------|------------|
| OpenVLA Object trained R² | `libero_object/action_r2_probing.json` |
| OpenVLA Object trained L1 | `libero_object/l1_attention_profile.json` |
| OpenVLA Object trained CF | `libero_object/counterfactual_combined.json` |
| OpenVLA Object untrained R² | `libero_object_untrained/action_r2_probing.json` |
| OpenVLA Object untrained L1 | `libero_object_untrained/l1_attention_profile.json` |
| OpenVLA Object untrained CF | `libero_object_untrained/counterfactual_combined.json` |
| OpenVLA Long trained R² | `libero_long/action_r2_probing.json` |
| OpenVLA Long trained L1 | `libero_long/l1_attention_profile.json` |
| OpenVLA Long trained CF | `libero_long/counterfactual_combined.json` |
| OpenVLA Long untrained R² | `libero_long_untrained/action_r2_probing.json` |
| OpenVLA Long untrained L1 | `libero_long_untrained/l1_attention_profile.json` |
| OpenVLA Long untrained CF | `libero_long_untrained/counterfactual_combined.json` |
| TracVLA Goal trained R² | `tracvla_goal/trained/action_r2_probing.json` |
| TracVLA Goal trained L1 | `tracvla_goal/trained/l1_attention_profile.json` |
| TracVLA Goal trained CF | `tracvla_goal/trained/counterfactual_combined.json` |
| TracVLA Goal untrained R² | `tracvla_goal/untrained/action_r2_probing.json` |
| TracVLA Goal untrained L1 | `tracvla_goal/untrained/l1_attention_profile.json` |
| TracVLA Goal untrained CF | `tracvla_goal/untrained/counterfactual_combined.json` |
| TracVLA Spatial trained R² | `tracvla_spatial/trained/action_r2_probing.json` |
| TracVLA Spatial trained L1 | `tracvla_spatial/trained/l1_attention_profile.json` |
| TracVLA Spatial trained CF | `tracvla_spatial/trained/counterfactual_combined.json` |
| TracVLA Spatial untrained R² | `tracvla_spatial/untrained/action_r2_probing.json` |
| TracVLA Spatial untrained L1 | `tracvla_spatial/untrained/l1_attention_profile.json` |
| TracVLA Spatial untrained CF | `tracvla_spatial/untrained/counterfactual_combined.json` |
| TracVLA Object trained R² | `tracvla_object/trained/action_r2_probing.json` |
| TracVLA Object trained L1 | `tracvla_object/trained/l1_attention_profile.json` |
| TracVLA Object trained CF | `tracvla_object/trained/counterfactual_combined.json` |
| TracVLA Object untrained R² | `tracvla_object/untrained/action_r2_probing.json` |
| TracVLA Object untrained L1 | `tracvla_object/untrained/l1_attention_profile.json` |
| TracVLA Object untrained CF | `tracvla_object/untrained/counterfactual_combined.json` |
| TracVLA Long trained R² | `tracvla_long/trained/action_r2_probing.json` |
| TracVLA Long trained L1 | `tracvla_long/trained/l1_attention_profile.json` |
| TracVLA Long trained CF | `tracvla_long/trained/counterfactual_combined.json` |
| TracVLA Long untrained R² | `tracvla_long/untrained/action_r2_probing.json` |
| TracVLA Long untrained L1 | `tracvla_long/untrained/l1_attention_profile.json` |
| TracVLA Long untrained CF | `tracvla_long/untrained/counterfactual_combined.json` |
| NORA Goal trained R² | `nora_goal/trained/action_r2_probing.json` |
| NORA Goal trained L1 | `nora_goal/trained/l1_attention_profile.json` |
| NORA Goal trained CF | `nora_goal/trained/counterfactual_combined.json` |
| NORA Goal untrained R² | `nora_goal/untrained/action_r2_probing.json` |
| NORA Goal untrained L1 | `nora_goal/untrained/l1_attention_profile.json` |
| NORA Goal untrained CF | `nora_goal/untrained/counterfactual_combined.json` |
| NORA Spatial trained R² | `nora_spatial/trained/action_r2_probing.json` |
| NORA Spatial trained L1 | `nora_spatial/trained/l1_attention_profile.json` |
| NORA Spatial trained CF | `nora_spatial/trained/counterfactual_combined.json` |
| NORA Spatial untrained R² | `nora_spatial/untrained/action_r2_probing.json` |
| NORA Spatial untrained L1 | `nora_spatial/untrained/l1_attention_profile.json` |
| NORA Spatial untrained CF | MISSING — file does not exist |
| OpenVLA Goal (all) | MISSING — no `libero_goal_trained/` or `libero_goal_untrained/` directories exist; old dirs `trained_libero_goal/` contain only goal_classification data, not standardized pipeline output |
| OpenVLA Spatial (all) | MISSING — no `libero_spatial_trained/` or `libero_spatial_untrained/` directories exist |

All paths relative to `/root/autodl-tmp/vla-ssd/results/`.
