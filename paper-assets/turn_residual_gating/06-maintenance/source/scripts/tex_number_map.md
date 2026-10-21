# Eval Results → Paper Number Mapping

Maps eval JSON fields to specific numbers in the paper `.tex` files.
Run `python scripts/compute_bootstrap_ci.py <json>` on the server to get updated values.

---

## Abstract (`paper/sections/abstract.tex`, line 2)

| Paper text | Current value | Source JSON / field | Notes |
|---|---|---|---|
| "GAR declines by 70.8%" | 70.8% | `results/phase1_gar_results.json` → `relative_drop` | Phase 1 diagnostic |
| "20--33$\times$ gap" | 20–33× | Multi-seed AR vs TF GAR-ours ratio | Range across 5-way configs |
| "0.015--0.025" (AR GAR range) | 0.015–0.025 | `runs/eval_v7_tg_s123/ar_*/epoch_2_gar.json` → `mid_turns_avg_gar` | AR eval across configs |
| "0.064 to 0.727" (steering) | 0.064→0.727 | `runs/attention_steering/attention_steering_gen_n50_fixed.json` → `results.beta_0.0.mid_turns_avg_gar`, `results.beta_5.0.mid_turns_avg_gar` | β=0 vs β=5 |
| "1.57$\times$" (SS gap) | 1.57× | SS eval: TF mid_turns_avg_gar / AR mid_turns_avg_gar | Single seed s42 |
| "27$\times$ by median" (Llama) | 27× | `runs/eval_llama_ar_n20/` → median GAR-ours TF/AR ratio | Llama cross-model |

## Introduction (`paper/sections/introduction.tex`)

| Paper text | Line | Current value | Source |
|---|---|---|---|
| "27--48% between early and mid-conversation" | 3 | 27–48% | Dongre et al. (literature) |
| "70.8% relative decline" | 3 | 70.8% | `results/phase1_gar_results.json` → `relative_drop` |
| "0.0418 at turn~1 to 0.0122" | 3 | 0.0418→0.0122 | `results/phase1_gar_results.json` → `avg_gar_per_turn[0]`, `mid_turns_avg_gar` |
| "AUC=0.98" | 5 | 0.98 | Dongre et al. (literature) |
| "GAR-ours reaches 0.50" (TF) | 10, 16 | 0.50 | `runs/4way_eval/tg_v7_ours/` → mean of gar_curves |
| "0.015--0.025" (AR GAR) | 10, 16 | 0.015–0.025 | AR eval across 5-way configs |
| "20--33$\times$ gap" | 10, 16 | 20–33× | TF/AR ratio range |
| "0.75 pp spread" | 16 | 0.75 | Max–min of TF GAR-ours across 4 fine-tuned variants |
| "PPL at 2.78" | 16 | 2.78 | Table 1 PPL column |
| "0.016 to 0.318 (20×)" (SS) | 16 | 0.016→0.318 | SS s42 AR eval: base AR GAR vs SS AR GAR |
| "31× gap to 1.57×" (SS) | 16, 18 | 31×→1.57× | TF/AR ratio before and after SS |
| "0.064 to 0.727" (steering) | 18 | 0.064→0.727 | Steering β=0 vs β=5 |
| "27× gap" (Llama) | 18 | 27× | Llama TF/AR median ratio |

## Experiments (`paper/sections/experiments.tex`)

### Table 1 (line 23–36): Five-way comparison

| Cell | Value | Source eval dir |
|---|---|---|
| Base / IID GAR-O | 0.01 | `runs/4way_eval/base_ours/` |
| Base / IID GAR-D | 0.00 | `runs/4way_eval/base_dongre/` |
| Base / IID PPL | 4.23 | `runs/4way_eval/base_ours/` → `avg_ppl` |
| Base / Held-out GAR-O | 0.01 | `runs/phase2_4way_eval_heldout/base_ours/` |
| Base / Held-out PPL | 4.34 | `runs/phase2_4way_eval_heldout/base_ours/` → `avg_ppl` |
| Base / AR GAR-O | 0.012 | `results/phase1_gar_results.json` → `mid_turns_avg_gar` |
| TG / IID GAR-O | 0.50 | `runs/4way_eval/tg_v7_ours/` |
| TG / IID PPL | 2.78 | `runs/4way_eval/tg_v7_ours/` → `avg_ppl` |
| TG / Held-out GAR-O | 0.50 | `runs/phase2_4way_eval_heldout/tg_v7_ours/` |
| TG / AR GAR-O | 0.016 | AR eval TG s42 → `mid_turns_avg_gar` |
| +PCGrad / AR GAR-O | 0.015 | `runs/eval_v9_pcgrad_heldout/` → `mid_turns_avg_gar` |
| UG / AR GAR-O | 0.015 | AR eval UG s42 → `mid_turns_avg_gar` |
| LoRA-only / AR GAR-O | 0.025 | AR eval LO s42 → `mid_turns_avg_gar` |

### §5.2 Main Results (line 12–16)

| Paper text | Line | Value | Source |
|---|---|---|---|
| "0.75 percentage points" | 12 | 0.75 pp | max(TG,PCGrad,UG,LO TF GAR) - min |
| "PPL is 2.78 for all four" | 12 | 2.78 | 4way_eval PPLs |
| "GAR-ours jumps from 0.01 to ~0.50" | 14 | 0.01→0.50 | Base vs fine-tuned TF GAR |
| "PPL improves from 4.23 to 2.78" | 14 | 4.23→2.78 | Base vs fine-tuned PPL |
| "TF GAR-ours 0.504±0.001" (seed 123) | 16 | 0.504±0.001 | `runs/eval_v7_tg_s123/tf_tg_ours/` |
| "AR GAR-ours 0.016±0.001" (seed 123) | 16 | 0.016±0.001 | `runs/eval_v7_tg_s123/ar_tg_ours/` |
| "gap ~31× (range 30.5--32.1×)" | 16 | 30.5–32.1× | TF/AR ratio per seed |

### §5.3 Steering (line 45–53)

| Paper text | Line | Value | Source |
|---|---|---|---|
| "0.062→0.6795±0.020" (N=5 β=2→5) | 49 | 0.062→0.680 | N=5 steering pilot |
| "PPL rises 35% (1.41→1.91)" | 49 | 1.41→1.91 | N=5 steering pilot |
| "β=10: GAR 0.959, PPL 4.22" | 49 | 0.959, 4.22 | N=5 steering pilot |
| "0.128±0.110 (β=2)" | 51 | 0.128±0.110 | `steering_n50_fixed` → `results.beta_2.0` |
| "0.556±0.060 (β=3)" | 51 | 0.556±0.060 | `steering_n50_fixed` → `results.beta_3.0` |
| "1.43→1.56 (9% PPL)" | 51 | 1.43→1.56 | `steering_n50_fixed` → `results.beta_0.0.avg_ppl`, `beta_3.0.avg_ppl` |
| "mean 0.064, median 0.031, std 0.081" | 51 | 0.064/0.031/0.081 | `steering_n50_fixed` → `results.beta_0.0` |
| "0.727±0.061, PPL 1.77±0.27" (β=5) | 51 | 0.727±0.061 | `steering_n50_fixed` → `results.beta_5.0` |

## Analysis (`paper/sections/analysis.tex`)

| Paper text | Line | Value | Source |
|---|---|---|---|
| "Wilcoxon p=3.73e-8, r=0.975" | 9 | p, r | `scripts/gate_wilcoxon_test.py` output |
| "L23: 0.769→0.979; L14: 0.747→0.928" | 9 | gate values | `*_gar.json` → `gate_dynamic_range` |
| "0.93 to 0.98 (2–7% attenuation)" | 11 | 0.93–0.98 | gate_dynamic_range late-turn values |
| "68–79% of layers" (conflict) | 22 | 68–79% | `runs/analysis/gradient_conflict/` |
| "cosine -0.089 to -0.042" | 22 | -0.089→-0.042 | gradient_conflict epoch JSONs |
| "NTP 7.5–14.7× magnitude" | 22 | 7.5–14.7× | gradient_conflict epoch JSONs |
| "TF/AR TRC: TG 0.334/0.332, LO 0.349/0.411" | 41 | TRC values | TRC eval output |
| "Llama AR/TF Dongre ratio 1.002×" | 43 | 1.002× | Llama eval Dongre files |
| "27× and 26×" (Llama TF-AR gap) | 47 | 27×, 26× | `runs/eval_llama_ar_n20/` median ratios |

## Discussion (`paper/sections/discussion.tex`)

| Paper text | Line | Value | Source |
|---|---|---|---|
| "NTP 7.5–14.7× GAR magnitude" | 1 | 7.5–14.7× | gradient_conflict |
| "2–7% attenuation" | 1 | 2–7% | gate_dynamic_range |
| "0.064 to 0.727" (steering) | 1 | 0.064→0.727 | steering_n50_fixed β=0,5 |
| "0.016 to 0.318 (20×)" (SS AR) | 5 | 0.016→0.318 | SS s42 AR eval |
| "~31× gap to 1.57×" (SS) | 5 | 31×→1.57× | SS TF/AR ratio |
| "PPL 1.38 vs 1.36" (SS) | 5 | 1.38/1.36 | SS s42 PPL |
| "Dongre 0.019→0.353" (SS) | 5 | 0.019→0.353 | SS s42 Dongre eval |
| "β=5: 24% PPL cost (1.43→1.77)" | 5 | 1.43→1.77 | steering_n50_fixed |
| "β=3: +9%" | 5 | +9% | steering_n50_fixed |
| "seed 2: AR GAR=0.418, gap 1.20×" | 5 | 0.418, 1.20× | SS s123 eval |
| "+23.8 pp, McNemar p=0.077" (IR) | 7 | 23.8pp, 0.077 | `results/instruction_retention.json` |

## Conclusion (`paper/sections/conclusion.tex`, line 3)

All numbers are repeated from above sections — no unique values.
