# paper writing related work d097

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_d097_20260522T060541_result.json`
- **Structured JSON:** [`af57744033ac89058be5.json`](../../sessions/af/af57744033ac89058be5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D097 compliance check:
- "architecture-independent": absent
- "7-10×": absent
- L1 attention = base-model prior (line 12: "reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training")
- "significantly" without stats: absent
- NORA `\cite{TODO_nora}`, TracVLA `\cite{zheng2024tracevla}`: correct (line 4)
- No em-dashes: confirmed
- No -ing phrase endings: confirmed

All 5 paragraphs updated:
1. **VLA models**: added TracVLA/NORA, cross-architecture positioning, replaced "redistributes rather than distorts" with "exit collapse and counterfactual sensitivity while L1 attention reflects inherited base-model priors"
2. **Mechanistic interp**: D097-corrected L1 claim (24/32 is base-model prior, not training effect)
3. **Behavioral/mechanistic VLA**: cross-architecture matrix positioning, explicit training-induced vs inherited decomposition
4. **Token-level**: cross-architecture confirmation of instruction-blindness and readout integration
5. **RSA/probing**: added metric limitations (RSA/CKA divergence + Cohen's d/cosine incomparability)

---
