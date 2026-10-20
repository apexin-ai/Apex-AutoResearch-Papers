# code mlp probe controls

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mlp_probe_controls_20260517T045344_result.json`
- **Structured JSON:** [`9e3db9560238bfbf1599.json`](../../sessions/9e/9e3db9560238bfbf1599.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results:

| Experiment | Accuracy | F1 |
|---|---|---|
| MLP image_mean L8 | 0.1000 | 0.0269 |
| MLP last_preaction L8 | 1.0000 | 1.0000 |
| Random features (PCA+LogReg) | 0.1030 | 0.1028 |
| Instr. embedding (PCA+LogReg) | 1.0000 | 1.0000 |

**Interpretations:**

1. **MLP confirms LogReg finding**: Even a nonlinear MLP gets exactly chance (10%) on image_mean at L8. The instruction signal genuinely isn't there, not a probe capacity issue.

2. **Random baseline**: 10.3% confirms the probe isn't memorizing from label structure alone.

3. **Instruction embedding**: 100% trivially, with pairwise cosine similarity min=0.22 (well separated). This confirms instruction identity IS encodable at embedding level. The non-trivial finding: this information reaches last_preaction through attention (100% at L8) but never image tokens (10% at L8).

Script: `/root/vla-ssd/scripts/cross_instruction_mlp_controls.py`
Results: `/root/autodl-tmp/vla-ssd/results/cross_instruction/control_probes.json`

---
