# ops fitd dd fix and analysis

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fitd-dd-fix-and-analysis_20260517T204347_result.json`
- **Structured JSON:** [`2f41996d68e3e37a7426.json`](../../sessions/2f/2f41996d68e3e37a7426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Tasks Complete ===

1. FITD/DD Strategy Mapping: 0-based → 1-based ✓
   FITD (80 convs): strategies now in {1,2,4,6}
   DD (80 convs): strategies now in {1,3,4,5,6,7}

2. plan_007 TF-IDF Sanity:
   FITD+DD vs v4c Benign: F1=1.0000 ± 0.0000
   FITD only: F1=1.0000 ± 0.0000
   DD only: F1=1.0000 ± 0.0000
   Top jailbreak features: "of", "that", "how", "we", "have you"
   Top benign features: "like", "it", "what if", "do", "how do"
   → Trivially separable by surface lexical features (different generation styles)

3. plan_008 Strategy Transitions:
   Crescendo: 1818 transitions
     - Dominant: role_assignment→role_assignment (545), obfuscation→obfuscation (173)
     - Clear escalation: mean strategy index rises 0.86→2.49→2.98→3.49→5.02→5.64 over turns
   FITD: 541 transitions
     - Fixed pattern: rapport(1)→rapport(1)→escalation(6)→escalation(6)→authority(2)→reframing(4)→escalation(6)
   DD: 565 transitions
     - Fixed pattern: rapport(1)→rapport(1)→obfuscation(7)→obfuscation(7)→reframing(4)→escalation(6)→reframing(4)
   Escalation: Crescendo shows gradual increase; FITD/DD show rigid scripted sequences
   Saved to: results/strategy_transition_matrices.json
```

---
