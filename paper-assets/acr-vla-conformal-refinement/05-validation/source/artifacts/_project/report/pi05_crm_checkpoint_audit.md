# π0.5 CRM Checkpoint Usage Audit

**Date**: 2026-05-26
**Trigger**: Reviewer concern that π0.5 Goal CRM evaluations may have used the SmolVLA CRM checkpoint by mistake.
**Verdict**: **No misuse detected.** Every π0.5 CRM evaluation (completed and currently running) uses `crm_pi05_unified_3suite/crm_best.pt`. Every SmolVLA CRM evaluation uses `crm_smolvla_3suite_v1/crm_best.pt`. The two are not interchangeable — they have incompatible input dimensions.

---

## 1. Checkpoint inventory (per server)

| Server | Path | Size (bytes) | md5 |
|---|---|---:|---|
| cqa1-32758 | `crm_pi05_unified_3suite/crm_best.pt` | 2,484,379 | `25093621fd5158951b2297ca406472f4` |
| cqa1-32758 | `crm_smolvla_3suite_v1/crm_best.pt` | 1,320,219 | `4161c6403b8eb268864b99dd986be784` |
| bjb1-32546 | `crm_pi05_unified_3suite/crm_best.pt` | 2,484,379 | `25093621fd5158951b2297ca406472f4` |
| bjb1-32546 | `crm_smolvla_3suite_v1/crm_best.pt` | 1,320,219 | `4161c6403b8eb268864b99dd986be784` |
| bjb1-32546 | `crm_pi05_full/{object,spatial}/crm_best.pt` | 2,484,379 | distinct (per-suite) |
| bjb2-28827 | `crm_pi05_unified_3suite/crm_best.pt` | 2,484,379 | `25093621fd5158951b2297ca406472f4` |
| bjb2-28827 | `crm_smolvla_3suite_v1/crm_best.pt` | 1,320,219 | `4161c6403b8eb268864b99dd986be784` |
| bjb1-18228 | **UNREACHABLE** (port 18228 timing out — AutoDL restart likely changed the SSH port; user should refresh from console) | — | — |

The md5 of `crm_pi05_unified_3suite/crm_best.pt` matches across all three reachable servers; same for the SmolVLA file. So a single, consistent π0.5 CRM artifact is in use.

## 2. Checkpoint contents (model dimensionality)

Inspected with `torch.load(..., weights_only=False)` on bjb1-32546:

| Checkpoint | `input_mean` shape | `net.0.weight` shape | Total params (reported by eval log) |
|---|---|---|---:|
| `crm_pi05_unified_3suite/crm_best.pt` | (2118,) | (256, 2118) | 615,966 |
| `crm_smolvla_3suite_v1/crm_best.pt`   | (990,)  | (256, 990)  | 327,198 |

The input layer widths (2118 vs 990) are different — loading a SmolVLA CRM into the π0.5 pipeline (or vice versa) would raise a shape-mismatch error on the first linear layer, so a silent misuse is not possible. The param counts printed by `[eval] CRM loaded from ...` in every eval log are an additional integrity tag.

## 3. Audit of completed eval logs

Script: scan every `*.log` under `/root/acr-vla-conformal-refinement/logs/`, extract each `[evaluate] args: {...}` block, and pair `'model'` against the basename of `'crm_checkpoint'`.

| Server | pi05 + π0.5 CRM | **pi05 + SmolVLA CRM** | smolvla + SmolVLA CRM | **smolvla + π0.5 CRM** | other (smolvla + Long `crm_unified_4suite_r4`) |
|---|---:|---:|---:|---:|---:|
| cqa1-32758 | 5 | **0** | 11 | **0** | 5 |
| bjb1-32546 | 0 | **0** | 48 | **0** | 4 |
| bjb2-28827 | 3 | **0** | 40 | **0** | 0 |

The "other" rows are legitimate: SmolVLA Long-suite evals use `crm_unified_4suite_r4/crm_best.pt` (SmolVLA-trained, 4-suite-unified), which is also a SmolVLA-side checkpoint. Files: `eval-supp-long-adapt-tau025-s44.log`, `eval-supp-long-crm-norm005-s{44,46-r2}.log`, `eval-supp-obj-{crm,adapt}-tau025-s47-r2.log`, etc.

**Zero suspect logs across all three reachable servers.** No completed π0.5 CRM eval loaded a SmolVLA checkpoint.

## 4. Currently running π0.5 CRM experiments

Note: the task description said the running π0.5 CRM Long experiments live on `bjb1-18228`, but that server is currently unreachable. The actually-running π0.5 CRM jobs are on **cqa1-32758** (tmux session `pi05-tau050`), launched 10:54 today:

| GPU | benchmark | mode | τ | `--crm_checkpoint` |
|---|---|---|---|---|
| 0 | goal | adaptive_conformal_crm | 0.50 | `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` ✓ |
| 1 | goal | adaptive_conformal_crm | 0.70 | `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` ✓ |
| 2 | goal | adaptive_conformal_crm | 0.90 | `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` ✓ |
| 3 | goal | vla_only (k2mean) | —   | (no CRM) |
| 4 | object | adaptive_conformal_crm | 0.25 | `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` ✓ |
| 5 | long | adaptive_conformal_crm | 0.25 | `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` ✓ |

Other servers' running jobs are all `--model smolvla` paired with `crm_smolvla_3suite_v1/crm_best.pt` — also correct (bjb1-32546 tmux `tau025_spatial_s42`, bjb2-28827 tmux `goal_vla_s49`).

## 5. Conclusion

- **All π0.5 CRM experiments — completed and in-flight — load `crm_pi05_unified_3suite/crm_best.pt`.** The reviewer's concern is not borne out by the logs or the live process list.
- **All SmolVLA CRM experiments load a SmolVLA-side checkpoint** (`crm_smolvla_3suite_v1` for 3-suite, `crm_unified_4suite_r4` for Long).
- Accidental swap is structurally impossible: the input dimensions differ (2118 vs 990), so a wrong-checkpoint run would crash at `load_state_dict` rather than silently report bad numbers. The `[eval] CRM loaded from ... (N params)` line in every log provides a second, independent check.
- **Not verified**: `bjb1-18228` was unreachable during this audit (likely AutoDL restart-induced SSH port change). All other π0.5 CRM artifacts and the active π0.5 CRM eval are accounted for on the three reachable servers, but if any π0.5 logs live exclusively on bjb1-18228, re-check after the SSH port is refreshed.

## Suspect-experiment list

**None.** Every (model, crm_checkpoint) pair across all scanned logs and live processes is consistent.
