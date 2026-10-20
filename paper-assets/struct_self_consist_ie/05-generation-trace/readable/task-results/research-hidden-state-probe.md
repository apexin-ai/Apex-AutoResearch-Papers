# research hidden state probe

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_hidden_state_probe_20260521T013621_result.json`
- **Structured JSON:** [`b35e6122e912525f58e2.json`](../../sessions/b3/b35e6122e912525f58e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts registered. Summary:

## P0-1 Hidden State Probe — Complete (2/3 datasets)

### Results

| Method | AUROC | |
|---|---|---|
| Random | 0.50 | — |
| ESJ (prompt-based) | 0.51 | prompting fails |
| **Hidden Probe — LODO** | **0.62** | cross-dataset transfer |
| **MV Agreement** | **0.87** | multi-sample behavioral |
| **Hidden Probe — FewNERD (within-CV)** | **0.920** | single-sample representation |
| **Hidden Probe — CoNLL (within-CV)** | **0.957** | single-sample representation |

### Interpretation

**The model knows which entities are correct.** Within-dataset probe AUROC (0.92–0.96) far exceeds both MV agreement (0.87) and ESJ prompting (0.51). This confirms:

1. Entity quality information is **strongly encoded** in the model's last-layer hidden states at entity span positions
2. **Prompting cannot access it** (ESJ = 0.51, essentially random)
3. **Multi-sample aggregation partially recovers it** (MV = 0.87), but a supervised linear probe from a single sample does even better
4. Cross-dataset transfer is weaker (LODO = 0.62), suggesting the encoding is partly domain-specific

This is the strongest evidence for the paper's core argument: the model has latent knowledge about output quality that is behaviorally inaccessible — motivating structured self-consistency as an extraction mechanism.

### Remaining

- **SciERC** not yet extracted (merged checkpoint not available on autodl-5090-c). Can be added when the checkpoint is copied over or a GPU frees up on autodl-5090.

---
