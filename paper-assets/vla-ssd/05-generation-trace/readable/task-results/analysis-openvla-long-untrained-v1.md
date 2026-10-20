# analysis openvla long untrained v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_openvla_long_untrained_v1_20260521T225356_result.json`
- **Structured JSON:** [`983f9fb2e554be44ae32.json`](../../sessions/98/983f9fb2e554be44ae32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the analysis summary:

**Conclusion: negative** — hypothesis falsified.

The OXE-pretrained base (openvla-7b untrained) on LIBERO-Long does NOT lack the convergent routing pattern. Key findings:

1. **R² probing**: No exit collapse (L31 img=0.839, last_pre=0.810 vs peaks 0.848/0.826), but trained also shows no clear collapse — this feature doesn't differentiate conditions. Untrained has lower absolute R² (~0.03-0.04 below trained) and peaks later (L12-L23 vs L8-L11).

2. **L1 attention**: Untrained has 25/32 instruction-dominant heads vs trained 14/32. The base model is MORE instruction-polarized; fine-tuning creates more mixed heads (17 vs 7), suggesting fine-tuning diversifies rather than concentrates routing.

3. **Counterfactual**: Untrained is 1.5-2x MORE sensitive than trained (empty d=1.05 vs 0.51, wrong d=0.83 vs 0.55). Ordering also differs: untrained empty > wrong > shuffled > para, trained shuffled > wrong > empty > para.

The OXE pretraining (970K+ trajectories) already instills strong instruction-grounded routing. LIBERO fine-tuning reshapes it — increasing R², creating mixed L1 heads, and reducing (not increasing) counterfactual sensitivity.

---
