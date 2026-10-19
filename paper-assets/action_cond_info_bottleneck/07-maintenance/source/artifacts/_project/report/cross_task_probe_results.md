# Cross-Task Probe Results — acib_v5_div_reg / seed1 / checkpoint-5000

**Date**: 2026-05-16
**Server**: westb-13953
**Checkpoint**: `/root/acib/outputs/acib_v5_div_reg/checkpoint-5000`
**Script**: `/root/acib/scripts/cross_task_probe.py`
**Run command**: `CUDA_VISIBLE_DEVICES=0 python3 scripts/cross_task_probe.py --checkpoint_dir /root/acib/outputs/acib_v5_div_reg/checkpoint-5000 --output_dir /root/acib/outputs/cross_task_probe --device cuda`

---

## 1. Tested Language Instruction Set (3 LIBERO tasks)

| idx | instruction |
| --- | --- |
| 0 | pick up the bbq sauce and place it in the basket |
| 1 | pick up the black bowl next to the cookie box and place it on the plate |
| 2 | pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate |

---

## 2. Probe A — Fixed Image, Swap Instruction (counter-factual)

Holds the visual observation fixed and only swaps the language instruction. If the scorer is action-conditioned on language, its importance weights should differ across instructions.

### Per-instruction logits / weights (identical across all three)

| instruction | logits mean | logits std | weight mean | weight std |
| --- | --- | --- | --- | --- |
| inst 0 | 1.44928 | 4.03057 | 0.54225 | 0.45254 |
| inst 1 | 1.44928 | 4.03057 | 0.54225 | 0.45254 |
| inst 2 | 1.44928 | 4.03057 | 0.54225 | 0.45254 |

### Pairwise similarity

| pair | cosine | L2 | bit-identical |
| --- | --- | --- | --- |
| 0 vs 1 | 1.000000 | 0.000000 | ✅ True |
| 0 vs 2 | 1.000000 | 0.000000 | ✅ True |
| 1 vs 2 | 1.000000 | 0.000000 | ✅ True |

**Verdict A**: `bit_identical_for_all_pairs=True`, cos ∈ [1.0000, 1.0000].
→ **The scorer's output is invariant to the language instruction — architecturally AND empirically, the language tokens have zero influence on the importance map.**

---

## 3. Probe B — Natural Cross-Task Observations

Uses different (image, instruction) pairs drawn from each task's actual trajectories.

### Per-task weight stats

| task | weight mean | weight std |
| --- | --- | --- |
| task 0 | 0.5423 | 0.4525 |
| task 1 | 0.5518 | 0.4423 |
| task 2 | 0.5564 | 0.4393 |

### Pairwise similarity of importance maps

| pair | cosine | L2 |
| --- | --- | --- |
| 0 vs 1 | 0.993844 | 0.885834 |
| 0 vs 2 | 0.994162 | 0.864232 |
| 1 vs 2 | 0.997806 | 0.530175 |

**Verdict B**: cos ∈ [0.9938, 0.9978], all above 0.99.
→ **Cross-task importance maps are highly similar regardless of task — the scorer is selecting the same hot zones across visually distinct scenes. This is a SPATIAL POSITION PRIOR, not a task-dependent selector.**

---

## 4. Conclusion — "Action-Conditioned" Framing Does NOT Hold

The empirical evidence is strongly negative for the action-conditioned information-bottleneck framing:

1. **Probe A (bit-identical instruction swap)**: the scorer is structurally insensitive to language. Whether the prompt says "pick up the bbq sauce" or "pick up the black bowl in the top drawer", the model produces exactly the same per-token importance logits — there is no path from language tokens to the scorer's output.
2. **Probe B (natural cross-task obs)**: even when both image and instruction vary across tasks, the resulting importance maps are nearly indistinguishable (cos > 0.99). The model has learned a fixed spatial prior — likely a centered/grid-positional pattern from camera1/camera2 — rather than task-specific attention.

**Implication for the paper / framing**:
- The current scorer is *not* action-conditioned. Calling the method "action-conditioned information bottleneck" is empirically unsupported with the v5_div_reg architecture as-is.
- Two reasonable paths forward:
  - **(a) Reframe as "spatial information bottleneck"** — own the position-prior result, study why a position prior alone helps (regularization / capacity / induction bias) and compare against learned-position baselines.
  - **(b) Fix the conditioning architecturally** — route language (and optionally state/action history) into the scorer (e.g., FiLM, cross-attention from text-encoder outputs to vision tokens) and re-run the probes. The Probe-A bit-identity result tells us the current architecture has no such pathway, which explains the failure cleanly.

---

## 5. Local Artifacts Pulled to `artifacts/`

### Cross-task probe (this run)
- `probe_A_fixed_image_swap_instruction.png` — 3-row heatmap, identical per-token importance across 3 instructions on a single image
- `probe_B_cross_task_heatmaps.png` — 3-row heatmap, importance over different task images (visually similar hot zones)
- `cross_task_probe_summary.json` — full numerical results

### Seed1 scorer analysis (step 5000, previously generated)
- `seed1_token_importance_heatmap.png` — per-token heatmap, camera1 vs camera2
- `seed1_avg_importance_per_camera.png` — bar chart, average importance per camera
- `seed1_scorer_weight_histogram.png` — distribution of scorer weights

### This summary
- `cross_task_probe_results.md` — this document
